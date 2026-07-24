"""Post-judge persona tag-only patch (diversity-preserving).

First generation stays free. After S5 flags ``domain_persona_mismatch`` or
``surrogate_plausibility_collapse``, replace PATIENT_NAME / GENDER / DISTRICT
(and AGE when present) with locked persona-aligned values — no full rewrite.
"""

from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

from main.entities.surrogate import stable_bucket
from main.pipeline.config_io import REPO_ROOT, load_yaml

_TAG_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|([^\]]*)\]\]")

PERSONA_REPAIR_FLAGS: frozenset[str] = frozenset(
    {
        "domain_persona_mismatch",
        "surrogate_plausibility_collapse",
    }
)

DEFAULT_NAME_POOLS = REPO_ROOT / "configs" / "synthetic-data" / "persona_name_pools.yaml"


@lru_cache(maxsize=1)
def _load_pools(path_str: str) -> dict[str, tuple[str, ...]]:
    path = Path(path_str)
    if not path.is_file():
        return {
            "female": ("Anjali Sharma", "Priya Patel", "Sunita Devi"),
            "male": ("Ramesh Kumar", "Amit Sharma", "Suresh Patel"),
        }
    raw = load_yaml(path)
    female = tuple(str(x) for x in (raw.get("female") or []) if str(x).strip())
    male = tuple(str(x) for x in (raw.get("male") or []) if str(x).strip())
    return {
        "female": female or ("Anjali Sharma",),
        "male": male or ("Ramesh Kumar",),
    }


def _gender_label(sex: str) -> str:
    s = (sex or "").strip().lower()
    if s in {"f", "female", "woman", "girl"}:
        return "Female"
    if s in {"m", "male", "man", "boy"}:
        return "Male"
    return "Female" if "f" in s else "Male"


def locked_surrogates(
    row: Mapping[str, Any],
    *,
    pools_path: Path | None = None,
) -> dict[str, str]:
    """Deterministic locked PATIENT_NAME / GENDER / DISTRICT / AGE for a persona."""
    pools = _load_pools(str(pools_path or DEFAULT_NAME_POOLS))
    gender = _gender_label(str(row.get("sex") or ""))
    key = "female" if gender == "Female" else "male"
    names = pools[key]
    seed = (
        f"{row.get('uuid')}|{row.get('document_language_code')}|"
        f"{row.get('doc_type_id')}|{gender}"
    )
    name = names[stable_bucket(seed, len(names))]
    out: dict[str, str] = {
        "PATIENT_NAME": name,
        "GENDER": gender,
        "DISTRICT": str(row.get("district") or "").strip(),
    }
    age = row.get("age")
    if age is not None and str(age).strip():
        out["AGE"] = str(age).strip()
    return {k: v for k, v in out.items() if v}


def apply_persona_tag_patch(
    text: str,
    row: Mapping[str, Any],
    *,
    pools_path: Path | None = None,
) -> tuple[str, list[str]]:
    """Replace persona-critical tag values in place. Returns (text, change notes)."""
    locked = locked_surrogates(row, pools_path=pools_path)
    if not locked:
        return text, []

    notes: list[str] = []

    def _repl(match: re.Match[str]) -> str:
        etype, value = match.group(1), match.group(2)
        if etype not in locked:
            return match.group(0)
        new_val = locked[etype]
        if value.strip() == new_val:
            return match.group(0)
        notes.append(f"{etype}:{value}->{new_val}")
        return f"[[{etype}|{new_val}]]"

    patched = _TAG_RE.sub(_repl, text)

    # Ensure DISTRICT / GENDER / PATIENT_NAME exist at least once when locked.
    for etype, new_val in locked.items():
        if etype in {"PATIENT_NAME", "GENDER", "DISTRICT"} and not re.search(
            rf"\[\[{re.escape(etype)}\|", patched
        ):
            # Append a minimal tag line only if completely missing (rare).
            patched = patched.rstrip() + f"\n[[{etype}|{new_val}]]"
            notes.append(f"{etype}:inserted->{new_val}")

    return patched, notes


def persona_flags_present(flags: list[str] | tuple[str, ...]) -> bool:
    return bool(PERSONA_REPAIR_FLAGS.intersection(str(f) for f in flags))
