"""Stages 7–8 — Near-duplicate removal + language-stratified balancing."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.entities.inline import strip_inline_tags
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.io import read_jsonl, write_json, write_jsonl, write_parquet
from main.pipeline.nemo_curator_fuzzy import NemoCuratorDedupError, run_fuzzy_dedup
from main.pipeline.semantic_dedup import find_semantic_near_duplicates

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

_TAG_VALUE_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|[^\]]*\]\]")
_WS_RE = re.compile(r"\s+")

DEDUP_TEXT_FIELD = "_dedup_text"
DEFAULT_DEDUP_TEXT_MODE = "english_pivot_or_masked"


@dataclass(frozen=True)
class CurationSettings:
    input_jsonl: Path
    output_dir: Path
    text_field: str
    id_field: str
    language_field: str
    dedup_backend: str
    dedup_text_mode: str
    jaccard_threshold: float
    char_ngrams: int
    num_bands: int
    rows_per_band: int
    minhashes_per_band: int
    seed: int
    curator_work_dir: Path
    enable_balancing: bool
    target_docs_per_language: int | None
    min_docs_per_language: int | None
    allow_underfill: bool
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

    min_docs = balancing.get("min_docs_per_language")
    if min_docs is not None:
        min_docs = int(min_docs)
        if min_docs < 1:
            raise ValueError("min_docs_per_language must be >= 1 when set")

    # Default: fail on underfill when an explicit target is set.
    if "allow_underfill" in balancing:
        allow_underfill = bool(balancing["allow_underfill"])
    else:
        allow_underfill = False

    backend = str(dedup.get("backend", "nemo_curator")).strip().lower()
    if backend != "nemo_curator":
        raise CurationError(
            f"Unsupported curation.dedup.backend={backend!r}. "
            "This pipeline STRICTLY requires backend=nemo_curator "
            "(NeMo Curator FuzzyDeduplicationWorkflow). "
            "cpu_minhash is disabled."
        )

    text_mode = str(dedup.get("text_mode", DEFAULT_DEDUP_TEXT_MODE)).strip().lower()
    if text_mode not in {"english_pivot_or_masked", "raw"}:
        raise CurationError(
            f"Unsupported curation.dedup.text_mode={text_mode!r}. "
            "Use english_pivot_or_masked (default) or raw."
        )

    return CurationSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        text_field=str(block.get("text_field", "generated_text")),
        id_field=str(block.get("id_field", "document_id")),
        language_field=str(block.get("language_field", "document_language_code")),
        dedup_backend=backend,
        dedup_text_mode=text_mode,
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
        min_docs_per_language=min_docs,
        allow_underfill=allow_underfill,
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


def template_fingerprint(text: str) -> str:
    """Normalize by replacing ``[[TYPE|value]]`` → ``[[TYPE]]`` and collapsing WS."""
    normalized = _TAG_VALUE_RE.sub(r"[[\1]]", text)
    return _WS_RE.sub(" ", normalized).strip()


def build_dedup_text(
    row: Mapping[str, Any],
    *,
    text_field: str,
    text_mode: str,
) -> str:
    """Build PHI-masked / English-pivot text for near-dup detection."""
    if text_mode == "raw":
        return str(row.get(text_field, ""))

    # english_pivot_or_masked (default)
    pivot = row.get("generated_text_en")
    if isinstance(pivot, str) and pivot.strip():
        return pivot
    raw = str(row.get(text_field, ""))
    return strip_inline_tags(raw)


def prepare_dedup_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: CurationSettings,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Attach ephemeral dedup text; return fingerprints keyed by document id."""
    prepared: list[dict[str, Any]] = []
    fingerprints: dict[str, str] = {}
    for row in rows:
        out = dict(row)
        doc_id = str(out[settings.id_field])
        source_for_fp = str(out.get(settings.text_field, ""))
        fingerprints[doc_id] = template_fingerprint(source_for_fp)
        out[DEDUP_TEXT_FIELD] = build_dedup_text(
            out,
            text_field=settings.text_field,
            text_mode=settings.dedup_text_mode,
        )
        prepared.append(out)
    return prepared, fingerprints


def _strip_dedup_field(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    cleaned: list[dict[str, Any]] = []
    for row in rows:
        out = dict(row)
        out.pop(DEDUP_TEXT_FIELD, None)
        cleaned.append(out)
    return cleaned


def deduplicate_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: CurationSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    prepared, fingerprints = prepare_dedup_rows(rows, settings=settings)

    if settings.dedup_backend != "nemo_curator":
        raise CurationError(
            f"Unsupported curation.dedup.backend={settings.dedup_backend!r}. "
            "Strict NeMo Curator path only."
        )

    try:
        kept_raw, curator_report = run_fuzzy_dedup(
            prepared,
            work_dir=settings.curator_work_dir,
            id_field=settings.id_field,
            text_field=DEDUP_TEXT_FIELD,
            seed=settings.seed,
            char_ngrams=settings.char_ngrams,
            num_bands=settings.num_bands,
            minhashes_per_band=settings.minhashes_per_band,
        )
    except NemoCuratorDedupError as exc:
        raise CurationError(str(exc)) from exc
    kept = _strip_dedup_field(kept_raw)

    # Second pass: semantic near-dup on the same pivot/masked text Curator used.
    # Rebuild ephemeral texts from prepared rows that survived Curator.
    kept_id_set = {str(row[settings.id_field]) for row in kept}
    semantic_docs: list[tuple[str, str]] = []
    prepared_by_id = {
        str(row[settings.id_field]): str(row.get(DEDUP_TEXT_FIELD, ""))
        for row in prepared
    }
    for row in kept:
        doc_id = str(row[settings.id_field])
        semantic_docs.append((doc_id, prepared_by_id.get(doc_id, "")))
    semantic_drop, semantic_report = find_semantic_near_duplicates(
        semantic_docs, threshold=0.92, seed=settings.seed
    )
    if semantic_drop:
        kept = [
            row for row in kept if str(row[settings.id_field]) not in semantic_drop
        ]

    kept_ids = {str(row[settings.id_field]) for row in kept}
    dropped_ids = sorted(
        doc_id for doc_id in fingerprints if doc_id not in kept_ids
    )
    report = {
        **curator_report,
        "backend": settings.dedup_backend,
        "text_mode": settings.dedup_text_mode,
        "template_fingerprints": {
            "unique": len(set(fingerprints.values())),
            "total": len(fingerprints),
        },
        "dropped_template_fingerprints": sorted(
            {fingerprints[doc_id] for doc_id in dropped_ids if doc_id in fingerprints}
        )[:50],
        "semantic_dedup": semantic_report,
        "curator_kept_before_semantic": len(kept_id_set),
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
            raise CurationError(
                f"Missing {settings.language_field} on row {row.get(settings.id_field)}"
            )
        by_lang[lang].append(dict(row))

    pre_balance_counts = {lang: len(items) for lang, items in sorted(by_lang.items())}

    if settings.min_docs_per_language is not None:
        below = {
            lang: count
            for lang, count in pre_balance_counts.items()
            if count < settings.min_docs_per_language
        }
        if below:
            raise CurationError(
                "Language count below balancing.min_docs_per_language after dedup "
                f"(before equalize). below={below} "
                f"min={settings.min_docs_per_language}"
            )

    equalize_mode = settings.target_docs_per_language is None
    if equalize_mode:
        # Cap each language at the minimum language count (equalize down).
        if not by_lang:
            return [], {
                "enabled": True,
                "equalize_mode": True,
                "target_docs_per_language": 0,
                "pre_balance_counts": pre_balance_counts,
                "discarded_by_balance": 0,
                "rows_out": 0,
            }
        target = min(len(items) for items in by_lang.values())
    else:
        target = settings.target_docs_per_language
        assert target is not None

    balanced: list[dict[str, Any]] = []
    per_language: dict[str, int] = {}
    underfilled: dict[str, int] = {}
    discarded_by_balance = 0
    for lang in sorted(by_lang):
        items = by_lang[lang]
        # Stable order: existing order already deterministic from upstream.
        chosen = items[:target]
        discarded_by_balance += len(items) - len(chosen)
        per_language[lang] = len(chosen)
        if len(chosen) < target:
            underfilled[lang] = len(chosen)
        balanced.extend(chosen)

    if underfilled and settings.target_docs_per_language is not None:
        if not settings.allow_underfill:
            raise CurationError(
                "Language balancing under-filled with explicit target_docs_per_language "
                f"(no silent pad). underfilled={underfilled} target={target} "
                f"(set balancing.allow_underfill: true to permit)"
            )

    rows_in = sum(pre_balance_counts.values())
    discard_ratio = (discarded_by_balance / rows_in) if rows_in else 0.0
    warning: str | None = None
    if equalize_mode and discard_ratio > 0.20:
        warning = (
            f"large_balance_discard: discarded {discarded_by_balance}/{rows_in} "
            f"rows ({discard_ratio:.1%}) while equalizing to {target} docs/language"
        )
        print(f"[s7-s8] WARNING: {warning}", file=sys.stderr)

    report: dict[str, Any] = {
        "enabled": True,
        "equalize_mode": equalize_mode,
        "target_docs_per_language": target,
        "min_docs_per_language": settings.min_docs_per_language,
        "allow_underfill": settings.allow_underfill,
        "pre_balance_counts": pre_balance_counts,
        "per_language": per_language,
        "discarded_by_balance": discarded_by_balance,
        "discard_ratio": round(discard_ratio, 4),
        "rows_out": len(balanced),
        "underfilled": underfilled,
    }
    if warning:
        report["warning"] = warning
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
    balancing = audit.get("balancing") or {}
    paths["audit_md"].write_text(
        "# Stages 7–8 — Curation Audit\n\n"
        f"- rows_in: **{audit['rows_in']}**\n"
        f"- rows_out: **{audit['rows_out']}**\n"
        f"- dedup_dropped: **{audit['dedup']['rows_dropped']}**\n"
        f"- dedup_text_mode: `{audit['dedup'].get('text_mode')}`\n"
        f"- discarded_by_balance: **{balancing.get('discarded_by_balance', 0)}**\n"
        f"- pre_balance_counts: `{balancing.get('pre_balance_counts', {})}`\n"
        f"- language_counts_out: `{audit['language_counts_out']}`\n"
        f"- balancing_warning: `{balancing.get('warning')}`\n"
        f"- balancing: `{balancing}`\n",
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
            "dedup": {
                "backend": settings.dedup_backend,
                "text_mode": settings.dedup_text_mode,
                "rows_in": 0,
                "rows_kept": 0,
                "rows_dropped": 0,
            },
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
