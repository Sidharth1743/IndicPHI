"""Stage 9 — Convert inline [[TYPE|value]] tags to GLiNER token-span JSON.

GLiNER training schema (token-indexed, inclusive ends)::

    {
      "tokenized_text": ["…", "…"],
      "ner": [[start_tok, end_tok, "LABEL"], …]
    }

Also retains plan fields ``text`` + character ``spans`` for auditability.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.entities.inline import INLINE_TAG_RE, extract_inline_spans
from main.entities.schema import load_entity_specs
from main.metrics.intrinsic import (
    compute_corpus_ecr,
    compute_ised,
    evaluate_spans_against_gold,
    load_gold_records,
)
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.io import read_jsonl, write_json, write_jsonl, write_parquet

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

# Whitespace-separated tokens; keep Indic letters attached to words.
# Punctuation becomes its own token so entity boundaries stay recoverable.
_TOKEN_RE = re.compile(
    r"[^\W\d_]+(?:['’][^\W\d_]+)*"  # alphabetic / Indic words
    r"|\d+(?:[.,]\d+)*"  # numbers
    r"|[^\s]",  # single punctuation / symbol
    re.UNICODE,
)


@dataclass(frozen=True)
class GlinerFormatSettings:
    input_jsonl: Path
    output_dir: Path
    entities_config: Path
    entity_profiles_config: Path
    text_field: str
    id_field: str
    gold_jsonl: Path | None
    max_docs: int | None
    fail_on_token_misalign: bool


class GlinerFormatError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> GlinerFormatSettings:
    root = load_yaml(pipeline_config)
    block = root.get("gliner_format")
    if not isinstance(block, dict):
        raise ValueError(f"'gliner_format' mapping required in {pipeline_config}")

    required = ("input_jsonl", "output_dir", "entities_config", "entity_profiles_config")
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing gliner_format keys {missing}")

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    gold_raw = block.get("gold_jsonl")
    gold_jsonl = resolve_repo_path(str(gold_raw)) if gold_raw else None

    return GlinerFormatSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        entities_config=resolve_repo_path(str(block["entities_config"])),
        entity_profiles_config=resolve_repo_path(str(block["entity_profiles_config"])),
        text_field=str(block.get("text_field", "generated_text")),
        id_field=str(block.get("id_field", "document_id")),
        gold_jsonl=gold_jsonl,
        max_docs=max_docs,
        fail_on_token_misalign=bool(block.get("fail_on_token_misalign", True)),
    )


def load_expected_entities(path: Path) -> dict[str, tuple[str, ...]]:
    root = load_yaml(path)
    raw = root.get("profiles")
    if not isinstance(raw, dict) or not raw:
        raise ValueError(f"'profiles' mapping required in {path}")
    out: dict[str, tuple[str, ...]] = {}
    for doc_type_id, entry in raw.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid profile for {doc_type_id!r}")
        required = entry.get("required")
        if not isinstance(required, list) or not required:
            raise ValueError(f"Profile {doc_type_id!r} needs non-empty required")
        out[str(doc_type_id)] = tuple(str(item) for item in required)
    return out


def tokenize(text: str) -> list[tuple[str, int, int]]:
    """Return (token, char_start, char_end) with end exclusive."""
    return [(m.group(0), m.start(), m.end()) for m in _TOKEN_RE.finditer(text)]


def inline_to_surface(tagged_text: str) -> tuple[str, list[dict[str, Any]]]:
    """Strip tags to surface text; return char-level spans over the surface string.

    Span offsets are character indices into the returned surface ``text``
    (start inclusive, end exclusive) covering the surrogate value only.
    """
    pieces: list[str] = []
    spans: list[dict[str, Any]] = []
    cursor = 0
    surface_pos = 0

    for match in INLINE_TAG_RE.finditer(tagged_text):
        prefix = tagged_text[cursor : match.start()]
        pieces.append(prefix)
        surface_pos += len(prefix)

        entity_type = match.group(1)
        value = match.group(2)
        start = surface_pos
        end = start + len(value)
        spans.append(
            {
                "start": start,
                "end": end,
                "label": entity_type,
                "text": value,
            }
        )
        pieces.append(value)
        surface_pos = end
        cursor = match.end()

    pieces.append(tagged_text[cursor:])
    return "".join(pieces), spans


def char_spans_to_token_ner(
    tokens: Sequence[tuple[str, int, int]],
    char_spans: Sequence[Mapping[str, Any]],
) -> tuple[list[list[Any]], list[str]]:
    """Map character spans to inclusive token indices ``[start, end, label]``."""
    ner: list[list[Any]] = []
    errors: list[str] = []

    for span in char_spans:
        c_start = int(span["start"])
        c_end = int(span["end"])
        label = str(span["label"])
        overlapping = [
            index
            for index, (_tok, t_start, t_end) in enumerate(tokens)
            if t_start < c_end and t_end > c_start
        ]
        if not overlapping:
            errors.append(f"no_token_overlap:{label}:{c_start}-{c_end}")
            continue

        tok_start = overlapping[0]
        tok_end = overlapping[-1]
        # Require exact cover of the entity characters by the selected tokens.
        cover_start = tokens[tok_start][1]
        cover_end = tokens[tok_end][2]
        if cover_start != c_start or cover_end != c_end:
            errors.append(
                f"token_boundary_misalign:{label}:{c_start}-{c_end}"
                f"->tok[{tok_start}:{tok_end}]chars[{cover_start}:{cover_end}]"
            )
            continue
        ner.append([tok_start, tok_end, label])

    return ner, errors


def convert_document(
    row: Mapping[str, Any],
    *,
    settings: GlinerFormatSettings,
    known_entities: Mapping[str, Any],
) -> dict[str, Any]:
    tagged = str(row.get(settings.text_field, ""))
    if not tagged.strip():
        raise GlinerFormatError(
            f"Empty {settings.text_field} for {row.get(settings.id_field)!r}"
        )

    surface, char_spans = inline_to_surface(tagged)
    unknown = sorted(
        {span["label"] for span in char_spans if span["label"] not in known_entities}
    )
    if unknown:
        raise GlinerFormatError(
            f"Unknown entity labels in {row.get(settings.id_field)!r}: {unknown}"
        )

    tokens_with_offsets = tokenize(surface)
    tokenized_text = [tok for tok, _s, _e in tokens_with_offsets]
    ner, align_errors = char_spans_to_token_ner(tokens_with_offsets, char_spans)
    if align_errors and settings.fail_on_token_misalign:
        raise GlinerFormatError(
            f"Token alignment failed for {row.get(settings.id_field)!r}: "
            f"{align_errors[:5]}"
        )

    inline_count = len(extract_inline_spans(tagged))
    if inline_count != len(char_spans):
        raise GlinerFormatError(
            f"Inline parse mismatch for {row.get(settings.id_field)!r}: "
            f"regex={inline_count} surface_spans={len(char_spans)}"
        )

    doc_id = str(row.get(settings.id_field) or row.get("uuid") or "")
    return {
        "document_id": doc_id,
        "text": surface,
        "tokenized_text": tokenized_text,
        "ner": ner,
        "spans": char_spans,
        "token_align_errors": align_errors,
        "document_language_code": row.get("document_language_code"),
        "doc_type_id": row.get("doc_type_id"),
        "domain_id": row.get("domain_id"),
        "uuid": row.get("uuid"),
        "stage": "s9_gliner_format",
    }


def format_corpus(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: GlinerFormatSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    known = load_entity_specs(settings.entities_config)
    expected_by_doc_type = load_expected_entities(settings.entity_profiles_config)

    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise GlinerFormatError("No rows selected for GLiNER formatting")

    outputs: list[dict[str, Any]] = []
    for row in selected:
        outputs.append(convert_document(row, settings=settings, known_entities=known))

    ecr_report = compute_corpus_ecr(
        outputs,
        expected_by_doc_type=expected_by_doc_type,
        doc_type_key="doc_type_id",
        ner_key="ner",
    )
    ised_report = compute_ised(outputs, ner_key="ner")

    gold_metrics: dict[str, Any] | None = None
    if settings.gold_jsonl is not None:
        if not settings.gold_jsonl.is_file():
            raise GlinerFormatError(f"Gold file not found: {settings.gold_jsonl}")
        gold = load_gold_records(settings.gold_jsonl)
        gold_metrics = evaluate_spans_against_gold(outputs, gold, id_key="document_id")

    audit = {
        "stage": "s9_gliner_format",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_jsonl": str(settings.input_jsonl),
        "rows_in": len(selected),
        "rows_out": len(outputs),
        "mean_tokens": (
            sum(len(row["tokenized_text"]) for row in outputs) / len(outputs)
        ),
        "mean_entities": (sum(len(row["ner"]) for row in outputs) / len(outputs)),
        "ecr": ecr_report,
        "ised": ised_report,
        "ied": ised_report,  # plan §10.2 alias (IED == ISED)
        "gold_span_metrics": gold_metrics,
        "gold_jsonl": str(settings.gold_jsonl) if settings.gold_jsonl else None,
        "fail_on_token_misalign": settings.fail_on_token_misalign,
    }
    return outputs, audit


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    # Lean GLiNER training JSON (list of dicts) — official schema.
    gliner_records = [
        {"tokenized_text": row["tokenized_text"], "ner": row["ner"]} for row in rows
    ]
    gliner_json = output_dir / "gliner_train.json"
    gliner_json.write_text(
        json.dumps(gliner_records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    paths = {
        "jsonl": output_dir / "gliner_docs.jsonl",
        "parquet": output_dir / "gliner_docs.parquet",
        "gliner_json": gliner_json,
        "audit_json": output_dir / "audit.json",
        "audit_md": output_dir / "audit.md",
    }
    write_jsonl(paths["jsonl"], rows)
    if rows:
        write_parquet(paths["parquet"], rows)
    else:
        paths["parquet"].write_text("", encoding="utf-8")
    write_json(paths["audit_json"], audit)

    gold_line = (
        f"- gold_span_f1: **{audit['gold_span_metrics']['f1']:.3f}**\n"
        if audit.get("gold_span_metrics")
        else "- gold_span_metrics: _(not computed — set gliner_format.gold_jsonl)_\n"
    )
    paths["audit_md"].write_text(
        "# Stage 9 — GLiNER Format & Intrinsic Metrics\n\n"
        f"- rows_out: **{audit['rows_out']}**\n"
        f"- mean_ecr: **{audit['ecr']['mean_ecr']:.3f}**\n"
        f"- mean_ised: **{audit['ised']['mean_ised']:.3f}**\n"
        f"{gold_line}",
        encoding="utf-8",
    )

    preview = REPO_ROOT / "data" / "samples" / "s9_gliner_preview.jsonl"
    preview.parent.mkdir(parents=True, exist_ok=True)
    with preview.open("w", encoding="utf-8") as handle:
        for row in rows[: min(3, len(rows))]:
            handle.write(
                json.dumps(
                    {
                        "document_id": row["document_id"],
                        "document_language_code": row.get("document_language_code"),
                        "tokenized_text": row["tokenized_text"][:40],
                        "ner": row["ner"][:10],
                        "text_preview": str(row["text"])[:400],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )
    paths["preview_jsonl"] = preview
    return paths


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    rows = read_jsonl(settings.input_jsonl, allow_empty=True)
    if not rows:
        audit = {
            "stage": "s9_gliner_format",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "input_jsonl": str(settings.input_jsonl),
            "rows_in": 0,
            "rows_out": 0,
            "mean_tokens": 0.0,
            "mean_entities": 0.0,
            "ecr": {"mean_ecr": 0.0, "n": 0},
            "ised": {"mean_ised": 0.0, "per_entity_type": {}, "entity_types": 0},
            "ied": {"mean_ised": 0.0, "per_entity_type": {}, "entity_types": 0},
            "gold_span_metrics": None,
            "gold_jsonl": None,
            "fail_on_token_misalign": settings.fail_on_token_misalign,
            "note": "No curated rows; wrote empty GLiNER outputs.",
        }
        return write_outputs([], audit, settings.output_dir)
    formatted, audit = format_corpus(rows, settings=settings)
    return write_outputs(formatted, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 9: GLiNER format + intrinsic metrics")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (GlinerFormatError, ValueError, FileNotFoundError) as exc:
        print(f"[s9] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s9] GLiNER format complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
