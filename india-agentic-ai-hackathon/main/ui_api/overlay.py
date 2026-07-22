"""Write a temporary smoke YAML overlay for demo UI runs."""

from __future__ import annotations

import math
import tempfile
from pathlib import Path
from typing import Any

import yaml

from main.pipeline.config_io import REPO_ROOT, load_yaml

_MAX_DOCS_BLOCKS = (
    "persona_summary",
    "prompt_construction",
    "generation",
    "translation",
    "linguistic_judge",
    "deterministic_auditor",
    "curation",
    "gliner_format",
)


def derive_persona_knobs(
    num_docs: int, language_codes: list[str]
) -> tuple[int, int, int]:
    """Return (personas_per_language, docs_per_persona, effective_docs).

    Prefer docs_per_persona=1 and personas_per_language = ceil(N / langs).
    """
    langs = max(1, len(language_codes))
    n = max(1, int(num_docs))
    docs_per_persona = 1
    personas_per_language = max(1, math.ceil(n / langs))
    effective = personas_per_language * docs_per_persona * langs
    return personas_per_language, docs_per_persona, effective


def write_smoke_overlay(
    *,
    num_docs: int,
    language_codes: list[str],
    base_config: Path | str,
) -> Path:
    """Clone base smoke YAML with UI overrides; return absolute temp path."""
    base_path = Path(base_config)
    if not base_path.is_absolute():
        base_path = (REPO_ROOT / base_path).resolve()
    root: dict[str, Any] = load_yaml(base_path)

    codes = [str(c).strip() for c in language_codes if str(c).strip()]
    if not codes:
        raise ValueError("language_codes must be non-empty")

    personas_per_language, docs_per_persona, effective = derive_persona_knobs(
        num_docs, codes
    )
    cap = max(int(num_docs), effective)

    root.setdefault("targets", {})
    root["targets"]["total_docs"] = effective
    root["targets"]["languages"] = len(codes)

    ps = root.setdefault("persona_sampling", {})
    ps["language_codes"] = codes
    ps["personas_per_language"] = personas_per_language
    ps["docs_per_persona"] = docs_per_persona

    for block in _MAX_DOCS_BLOCKS:
        section = root.setdefault(block, {})
        if isinstance(section, dict):
            section["max_docs"] = cap

    # Keep language filter on prompt construction when present.
    pc = root.setdefault("prompt_construction", {})
    if isinstance(pc, dict):
        pc["language_codes"] = codes

    out = Path(tempfile.mkstemp(prefix="hackgrid_ui_", suffix=".yaml")[1])
    out.write_text(
        yaml.safe_dump(root, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return out
