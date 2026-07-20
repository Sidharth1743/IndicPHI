"""Stage 10 — Persona-held-out train/eval split.

All documents belonging to a persona ``uuid`` go entirely to train OR eval
(never both). Assignment is stratified by language with a target eval fraction.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.io import read_jsonl, write_json, write_jsonl

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"


@dataclass(frozen=True)
class SplitSettings:
    input_jsonl: Path
    output_dir: Path
    eval_fraction: float
    seed: int
    persona_id_field: str
    language_field: str
    max_docs: int | None


class SplitError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> SplitSettings:
    root = load_yaml(pipeline_config)
    block = root.get("split")
    if not isinstance(block, dict):
        raise ValueError(f"'split' mapping required in {pipeline_config}")

    for key in ("input_jsonl", "output_dir"):
        if key not in block:
            raise ValueError(f"Missing split.{key}")

    eval_fraction = float(block.get("eval_fraction", 0.15))
    if not 0.0 < eval_fraction < 1.0:
        raise ValueError("split.eval_fraction must be in (0, 1)")

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    return SplitSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        eval_fraction=eval_fraction,
        seed=int(block.get("seed", 42)),
        persona_id_field=str(block.get("persona_id_field", "uuid")),
        language_field=str(block.get("language_field", "document_language_code")),
        max_docs=max_docs,
    )


def _persona_language(
    docs: Sequence[Mapping[str, Any]],
    *,
    language_field: str,
) -> str:
    counts = Counter(
        str(doc.get(language_field) or "") for doc in docs if doc.get(language_field)
    )
    if not counts:
        return ""
    return counts.most_common(1)[0][0]


def _to_gliner_record(row: Mapping[str, Any]) -> dict[str, Any] | None:
    tokenized = row.get("tokenized_text")
    ner = row.get("ner")
    if isinstance(tokenized, list) and isinstance(ner, list):
        return {"tokenized_text": tokenized, "ner": ner}
    return None


def split_by_persona(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: SplitSettings,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise SplitError("No rows selected for split")

    by_persona: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in selected:
        persona_id = str(row.get(settings.persona_id_field) or "")
        if not persona_id:
            raise SplitError(
                f"Missing {settings.persona_id_field} on row "
                f"{row.get('document_id')!r}"
            )
        by_persona[persona_id].append(dict(row))

    personas_by_stratum: dict[str, list[str]] = defaultdict(list)
    for persona_id, docs in by_persona.items():
        lang = _persona_language(docs, language_field=settings.language_field)
        doc_types = Counter(str(d.get("doc_type_id") or "") for d in docs)
        domains = Counter(str(d.get("domain_id") or "") for d in docs)
        rare = Counter()
        for d in docs:
            for ent in d.get("entity_types") or []:
                rare[str(ent)] += 1
            for span in d.get("ner") or []:
                if isinstance(span, (list, tuple)) and len(span) >= 3:
                    rare[str(span[2])] += 1
        primary_doc = doc_types.most_common(1)[0][0] if doc_types else ""
        primary_dom = domains.most_common(1)[0][0] if domains else ""
        # Stratum: language first (hard constraint), then doc_type/domain for balance.
        stratum = f"{lang}|{primary_doc}|{primary_dom}"
        personas_by_stratum[stratum].append(persona_id)

    rng = random.Random(settings.seed)
    eval_personas: set[str] = set()
    per_language_assignment: dict[str, dict[str, int]] = defaultdict(
        lambda: {"personas": 0, "eval_personas": 0, "train_personas": 0, "docs": 0}
    )
    per_stratum: dict[str, dict[str, int]] = {}

    for stratum in sorted(personas_by_stratum):
        persona_ids = list(personas_by_stratum[stratum])
        rng.shuffle(persona_ids)
        n_eval = int(round(len(persona_ids) * settings.eval_fraction))
        if settings.eval_fraction > 0 and len(persona_ids) >= 2:
            n_eval = max(1, min(n_eval, len(persona_ids) - 1))
        elif len(persona_ids) == 1:
            n_eval = 0
        chosen = set(persona_ids[:n_eval])
        eval_personas.update(chosen)
        lang = stratum.split("|", 1)[0] or "_missing"
        docs_n = sum(len(by_persona[pid]) for pid in persona_ids)
        per_stratum[stratum] = {
            "personas": len(persona_ids),
            "eval_personas": len(chosen),
            "train_personas": len(persona_ids) - len(chosen),
            "docs": docs_n,
        }
        bucket = per_language_assignment[lang]
        bucket["personas"] += len(persona_ids)
        bucket["eval_personas"] += len(chosen)
        bucket["train_personas"] += len(persona_ids) - len(chosen)
        bucket["docs"] += docs_n

    train_rows: list[dict[str, Any]] = []
    eval_rows: list[dict[str, Any]] = []
    for persona_id, docs in by_persona.items():
        bucket = eval_rows if persona_id in eval_personas else train_rows
        for doc in docs:
            out = dict(doc)
            out["split"] = "eval" if persona_id in eval_personas else "train"
            out["stage"] = "s10_split"
            bucket.append(out)

    audit = {
        "stage": "s10_split",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_jsonl": str(settings.input_jsonl),
        "rows_in": len(selected),
        "personas_in": len(by_persona),
        "eval_fraction_target": settings.eval_fraction,
        "seed": settings.seed,
        "persona_id_field": settings.persona_id_field,
        "language_field": settings.language_field,
        "stratify_by": ["language", "doc_type_id", "domain_id"],
        "train_rows": len(train_rows),
        "eval_rows": len(eval_rows),
        "eval_personas": len(eval_personas),
        "train_personas": len(by_persona) - len(eval_personas),
        "eval_fraction_actual_docs": (
            round(len(eval_rows) / len(selected), 4) if selected else 0.0
        ),
        "per_language": dict(per_language_assignment),
        "per_stratum": per_stratum,
        "train_language_counts": dict(
            Counter(str(r.get(settings.language_field, "")) for r in train_rows)
        ),
        "eval_language_counts": dict(
            Counter(str(r.get(settings.language_field, "")) for r in eval_rows)
        ),
    }
    return train_rows, eval_rows, audit


def write_outputs(
    train_rows: Sequence[Mapping[str, Any]],
    eval_rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    train_jsonl = output_dir / "train.jsonl"
    eval_jsonl = output_dir / "eval.jsonl"
    write_jsonl(train_jsonl, train_rows)
    write_jsonl(eval_jsonl, eval_rows)

    gliner_train = [
        rec
        for row in train_rows
        if (rec := _to_gliner_record(row)) is not None
    ]
    gliner_eval = [
        rec
        for row in eval_rows
        if (rec := _to_gliner_record(row)) is not None
    ]

    gliner_train_path = output_dir / "gliner_train.json"
    gliner_eval_path = output_dir / "gliner_eval.json"
    gliner_train_path.write_text(
        json.dumps(gliner_train, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    gliner_eval_path.write_text(
        json.dumps(gliner_eval, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    audit_out = dict(audit)
    audit_out["gliner_train_records"] = len(gliner_train)
    audit_out["gliner_eval_records"] = len(gliner_eval)
    if len(gliner_train) + len(gliner_eval) == 0:
        audit_out["gliner_note"] = (
            "No tokenized_text/ner fields on input rows; wrote empty GLiNER JSONs. "
            "Pass s9 gliner_docs.jsonl (or curated rows that already carry tokenized fields)."
        )

    audit_json = output_dir / "audit.json"
    write_json(audit_json, audit_out)
    audit_md = output_dir / "audit.md"
    audit_md.write_text(
        "# Stage 10 — Train/Eval Split\n\n"
        f"- rows_in: **{audit_out['rows_in']}**\n"
        f"- train_rows: **{audit_out['train_rows']}**\n"
        f"- eval_rows: **{audit_out['eval_rows']}**\n"
        f"- eval_fraction_actual_docs: `{audit_out['eval_fraction_actual_docs']}`\n"
        f"- personas train/eval: "
        f"`{audit_out['train_personas']}` / `{audit_out['eval_personas']}`\n"
        f"- gliner_train/eval records: "
        f"`{audit_out['gliner_train_records']}` / `{audit_out['gliner_eval_records']}`\n",
        encoding="utf-8",
    )

    return {
        "train_jsonl": train_jsonl,
        "eval_jsonl": eval_jsonl,
        "gliner_train": gliner_train_path,
        "gliner_eval": gliner_eval_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
    }


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    rows = read_jsonl(settings.input_jsonl, allow_empty=True)
    if not rows:
        audit = {
            "stage": "s10_split",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "input_jsonl": str(settings.input_jsonl),
            "rows_in": 0,
            "train_rows": 0,
            "eval_rows": 0,
            "note": "No input rows; wrote empty split outputs.",
        }
        return write_outputs([], [], audit, settings.output_dir)
    train_rows, eval_rows, audit = split_by_persona(rows, settings=settings)
    return write_outputs(train_rows, eval_rows, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 10: persona-held-out train/eval split")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (SplitError, ValueError, FileNotFoundError) as exc:
        print(f"[s10] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s10] Split complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
