"""Stages 7–8 — Near-duplicate removal + language-stratified balancing."""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.io import read_jsonl, write_json, write_jsonl, write_parquet
from main.pipeline.minhash_lsh import MinHashLSHConfig, find_near_duplicate_ids
from main.pipeline.nemo_curator_fuzzy import NemoCuratorDedupError, run_fuzzy_dedup

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"


@dataclass(frozen=True)
class CurationSettings:
    input_jsonl: Path
    output_dir: Path
    text_field: str
    id_field: str
    language_field: str
    dedup_backend: str
    jaccard_threshold: float
    char_ngrams: int
    num_bands: int
    rows_per_band: int
    minhashes_per_band: int
    seed: int
    curator_work_dir: Path
    enable_balancing: bool
    target_docs_per_language: int | None
    max_docs: int | None


class CurationError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> CurationSettings:
    root = load_yaml(pipeline_config)
    block = root.get("curation")
    if not isinstance(block, dict):
        raise ValueError(f"'curation' mapping required in {pipeline_config}")

    dedup = block.get("dedup")
    balancing = block.get("balancing")
    if not isinstance(dedup, dict):
        raise ValueError("'curation.dedup' mapping required")
    if not isinstance(balancing, dict):
        raise ValueError("'curation.balancing' mapping required")

    for key in ("input_jsonl", "output_dir"):
        if key not in block:
            raise ValueError(f"Missing curation.{key}")

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    target = balancing.get("target_docs_per_language")
    if target is not None:
        target = int(target)
        if target < 1:
            raise ValueError("target_docs_per_language must be >= 1 when set")

    backend = str(dedup.get("backend", "cpu_minhash")).strip().lower()
    if backend not in {"cpu_minhash", "nemo_curator"}:
        raise CurationError(
            f"Unsupported curation.dedup.backend={backend!r}. "
            "Use cpu_minhash (portable) or nemo_curator (explicit GPU/Ray path)."
        )

    return CurationSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        text_field=str(block.get("text_field", "generated_text")),
        id_field=str(block.get("id_field", "document_id")),
        language_field=str(block.get("language_field", "document_language_code")),
        dedup_backend=backend,
        jaccard_threshold=float(dedup.get("jaccard_threshold", 0.8)),
        char_ngrams=int(dedup.get("char_ngrams", 24)),
        num_bands=int(dedup.get("num_bands", 20)),
        rows_per_band=int(dedup.get("rows_per_band", 5)),
        minhashes_per_band=int(dedup.get("minhashes_per_band", 13)),
        seed=int(dedup.get("seed", 42)),
        curator_work_dir=resolve_repo_path(
            str(dedup.get("curator_work_dir", "artifacts/nemo_curator_dedup"))
        ),
        enable_balancing=bool(balancing.get("enabled", True)),
        target_docs_per_language=target,
        max_docs=max_docs,
    )


def ensure_document_ids(
    rows: Sequence[Mapping[str, Any]],
    *,
    id_field: str,
) -> list[dict[str, Any]]:
    outputs: list[dict[str, Any]] = []
    for index, row in enumerate(rows):
        out = dict(row)
        if id_field not in out or not out[id_field]:
            uuid = out.get("uuid", "unknown")
            slot = out.get("doc_slot", index)
            out[id_field] = f"{uuid}__{slot}__{index}"
        outputs.append(out)
    return outputs


def deduplicate_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: CurationSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if settings.dedup_backend == "nemo_curator":
        try:
            return run_fuzzy_dedup(
                rows,
                work_dir=settings.curator_work_dir,
                id_field=settings.id_field,
                text_field=settings.text_field,
                seed=settings.seed,
                char_ngrams=settings.char_ngrams,
                num_bands=settings.num_bands,
                minhashes_per_band=settings.minhashes_per_band,
            )
        except NemoCuratorDedupError as exc:
            raise CurationError(str(exc)) from exc

    documents: list[tuple[str, str]] = []
    for row in rows:
        doc_id = str(row[settings.id_field])
        text = str(row.get(settings.text_field, ""))
        if not text.strip():
            raise CurationError(f"Empty {settings.text_field} for {doc_id}")
        documents.append((doc_id, text))

    config = MinHashLSHConfig(
        seed=settings.seed,
        char_ngrams=settings.char_ngrams,
        num_bands=settings.num_bands,
        rows_per_band=settings.rows_per_band,
        jaccard_threshold=settings.jaccard_threshold,
    )
    drop_ids = find_near_duplicate_ids(documents, config)
    kept = [row for row in rows if str(row[settings.id_field]) not in drop_ids]
    dropped = [row for row in rows if str(row[settings.id_field]) in drop_ids]

    report = {
        "backend": settings.dedup_backend,
        "jaccard_threshold": settings.jaccard_threshold,
        "rows_in": len(rows),
        "rows_kept": len(kept),
        "rows_dropped": len(dropped),
        "dropped_ids": sorted(drop_ids),
    }
    return kept, report


def balance_by_language(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: CurationSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if not settings.enable_balancing:
        return list(rows), {"enabled": False, "rows_out": len(rows)}

    by_lang: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        lang = str(row.get(settings.language_field, ""))
        if not lang:
            raise CurationError(f"Missing {settings.language_field} on row {row.get(settings.id_field)}")
        by_lang[lang].append(dict(row))

    if settings.target_docs_per_language is None:
        # Cap each language at the minimum language count (equalize down).
        if not by_lang:
            return [], {"enabled": True, "rows_out": 0}
        target = min(len(items) for items in by_lang.values())
    else:
        target = settings.target_docs_per_language

    balanced: list[dict[str, Any]] = []
    per_language: dict[str, int] = {}
    underfilled: dict[str, int] = {}
    for lang in sorted(by_lang):
        items = by_lang[lang]
        # Stable order: existing order already deterministic from upstream.
        chosen = items[:target]
        per_language[lang] = len(chosen)
        if len(chosen) < target:
            underfilled[lang] = len(chosen)
        balanced.extend(chosen)

    if underfilled and settings.target_docs_per_language is not None:
        raise CurationError(
            "Language balancing under-filled with explicit target_docs_per_language "
            f"(no silent pad). underfilled={underfilled} target={target}"
        )

    report = {
        "enabled": True,
        "target_docs_per_language": target,
        "per_language": per_language,
        "rows_out": len(balanced),
        "underfilled": underfilled,
    }
    return balanced, report


def curate(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: CurationSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    selected = ensure_document_ids(selected, id_field=settings.id_field)

    deduped, dedup_report = deduplicate_rows(selected, settings=settings)
    balanced, balance_report = balance_by_language(deduped, settings=settings)

    for row in balanced:
        row["stage"] = "s8_distribution_balancing"

    audit = {
        "stage": "s7_s8_curation",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "rows_in": len(selected),
        "dedup": dedup_report,
        "balancing": balance_report,
        "language_counts_out": dict(
            Counter(str(row[settings.language_field]) for row in balanced)
        ),
        "rows_out": len(balanced),
    }
    return balanced, audit


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "jsonl": output_dir / "curated.jsonl",
        "parquet": output_dir / "curated.parquet",
        "audit_json": output_dir / "audit.json",
        "audit_md": output_dir / "audit.md",
    }
    write_jsonl(paths["jsonl"], rows)
    if rows:
        write_parquet(paths["parquet"], rows)
    else:
        paths["parquet"].write_text("", encoding="utf-8")
    write_json(paths["audit_json"], audit)
    paths["audit_md"].write_text(
        "# Stages 7–8 — Curation Audit\n\n"
        f"- rows_in: **{audit['rows_in']}**\n"
        f"- rows_out: **{audit['rows_out']}**\n"
        f"- dedup_dropped: **{audit['dedup']['rows_dropped']}**\n"
        f"- language_counts_out: `{audit['language_counts_out']}`\n"
        f"- balancing: `{audit['balancing']}`\n",
        encoding="utf-8",
    )
    return paths


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    rows = read_jsonl(settings.input_jsonl, allow_empty=True)
    if not rows:
        audit = {
            "stage": "s7_s8_curation",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "rows_in": 0,
            "dedup": {"backend": settings.dedup_backend, "rows_in": 0, "rows_kept": 0, "rows_dropped": 0},
            "balancing": {"enabled": settings.enable_balancing, "rows_out": 0},
            "language_counts_out": {},
            "rows_out": 0,
            "note": "No auditor-passed rows; wrote empty curation outputs.",
        }
        return write_outputs([], audit, settings.output_dir)
    curated, audit = curate(rows, settings=settings)
    return write_outputs(curated, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stages 7-8: dedup + balancing")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (CurationError, ValueError, FileNotFoundError, NemoCuratorDedupError) as exc:
        print(f"[s7-s8] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s7-s8] Curation complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
