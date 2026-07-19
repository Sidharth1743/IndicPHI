"""Intrinsic dataset metrics for Stage 9 (plan §10.2 / idea S9).

- ECR  — Entity Coverage Rate (per doc, vs required profile)
- ISED — Inter-Sample Entity Diversity (plan alias: IED)
- Span Precision / Recall / F1 vs gold (exact boundary + label)
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Mapping, Sequence


def compute_document_ecr(
    ner: Sequence[Sequence[Any]],
    expected_entity_types: Sequence[str],
) -> float:
    if not expected_entity_types:
        return 0.0
    present = {str(span[2]) for span in ner if len(span) >= 3}
    hit = sum(1 for entity_id in expected_entity_types if entity_id in present)
    return hit / len(expected_entity_types)


def compute_corpus_ecr(
    rows: Sequence[Mapping[str, Any]],
    *,
    expected_by_doc_type: Mapping[str, Sequence[str]],
    doc_type_key: str = "doc_type_id",
    ner_key: str = "ner",
) -> dict[str, Any]:
    scores: list[float] = []
    missing_profiles: list[str] = []
    for row in rows:
        doc_type = str(row.get(doc_type_key, ""))
        expected = expected_by_doc_type.get(doc_type)
        if expected is None:
            missing_profiles.append(doc_type)
            continue
        scores.append(compute_document_ecr(list(row.get(ner_key, [])), expected))

    if missing_profiles:
        unique = sorted(set(missing_profiles))
        raise ValueError(
            f"ECR: missing entity profiles for doc_type_id values {unique}"
        )
    if not scores:
        return {"mean_ecr": 0.0, "n": 0}

    return {
        "mean_ecr": sum(scores) / len(scores),
        "min_ecr": min(scores),
        "max_ecr": max(scores),
        "n": len(scores),
    }


def compute_ised(
    rows: Sequence[Mapping[str, Any]],
    *,
    ner_key: str = "ner",
    text_key: str = "tokenized_text",
) -> dict[str, Any]:
    """ISED / IED = unique surrogate values / total mentions, per entity type.

    Surrogate string is reconstructed from ``tokenized_text[start:end+1]``.
    """
    values_by_type: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        tokens = [str(tok) for tok in row.get(text_key, [])]
        for span in row.get(ner_key, []):
            if len(span) < 3:
                continue
            start, end, label = int(span[0]), int(span[1]), str(span[2])
            if start < 0 or end < start or end >= len(tokens):
                continue
            value = " ".join(tokens[start : end + 1])
            values_by_type[label].append(value)

    per_type: dict[str, float] = {}
    for label, values in sorted(values_by_type.items()):
        if not values:
            per_type[label] = 0.0
        else:
            per_type[label] = len(set(values)) / len(values)

    mean = sum(per_type.values()) / len(per_type) if per_type else 0.0
    return {
        "mean_ised": mean,
        "per_entity_type": per_type,
        "entity_types": len(per_type),
        "total_mentions": sum(len(v) for v in values_by_type.values()),
    }


def _span_key(span: Mapping[str, Any] | Sequence[Any]) -> tuple[int, int, str]:
    if isinstance(span, Mapping):
        return int(span["start"]), int(span["end"]), str(span["label"])
    return int(span[0]), int(span[1]), str(span[2])


def span_prf1(
    predicted: Sequence[Mapping[str, Any] | Sequence[Any]],
    gold: Sequence[Mapping[str, Any] | Sequence[Any]],
) -> dict[str, float]:
    """Exact match on (start, end, label). Char or token indices — caller decides."""
    pred_set = {_span_key(span) for span in predicted}
    gold_set = {_span_key(span) for span in gold}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        0.0
        if precision + recall == 0
        else 2 * precision * recall / (precision + recall)
    )
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": float(tp),
        "fp": float(fp),
        "fn": float(fn),
    }


def load_gold_records(path: Path) -> dict[str, dict[str, Any]]:
    """Load gold JSONL keyed by document_id.

    Each gold row must include ``document_id`` and either:
    - ``ner`` (token-indexed), or
    - ``spans`` (char-indexed ``{start,end,label}``).
    """
    if not path.is_file():
        raise FileNotFoundError(f"Gold JSONL not found: {path}")
    out: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            row = json.loads(text)
            if not isinstance(row, dict) or "document_id" not in row:
                raise ValueError(f"Gold row {line_no} needs document_id object")
            doc_id = str(row["document_id"])
            if doc_id in out:
                raise ValueError(f"Duplicate gold document_id={doc_id!r}")
            out[doc_id] = row
    if not out:
        raise ValueError(f"No gold rows in {path}")
    return out


def evaluate_spans_against_gold(
    predicted_rows: Sequence[Mapping[str, Any]],
    gold_by_id: Mapping[str, Mapping[str, Any]],
    *,
    id_key: str = "document_id",
) -> dict[str, Any]:
    """Micro-averaged exact span P/R/F1 over docs present in both sets."""
    matched = 0
    missing_pred: list[str] = []
    micro_tp = micro_fp = micro_fn = 0

    pred_by_id = {str(row[id_key]): row for row in predicted_rows}
    for doc_id, gold_row in gold_by_id.items():
        pred_row = pred_by_id.get(doc_id)
        if pred_row is None:
            missing_pred.append(doc_id)
            continue
        matched += 1

        if "ner" in gold_row and gold_row["ner"] is not None:
            gold_spans = list(gold_row["ner"])
            pred_spans = list(pred_row.get("ner", []))
        elif "spans" in gold_row and gold_row["spans"] is not None:
            gold_spans = list(gold_row["spans"])
            pred_spans = list(pred_row.get("spans", []))
        else:
            raise ValueError(
                f"Gold document {doc_id!r} needs 'ner' or 'spans' annotations"
            )

        stats = span_prf1(pred_spans, gold_spans)
        micro_tp += int(stats["tp"])
        micro_fp += int(stats["fp"])
        micro_fn += int(stats["fn"])

    precision = micro_tp / (micro_tp + micro_fp) if (micro_tp + micro_fp) else 0.0
    recall = micro_tp / (micro_tp + micro_fn) if (micro_tp + micro_fn) else 0.0
    f1 = (
        0.0
        if precision + recall == 0
        else 2 * precision * recall / (precision + recall)
    )
    return {
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": micro_tp,
        "fp": micro_fp,
        "fn": micro_fn,
        "docs_compared": matched,
        "gold_docs_missing_in_pred": missing_pred,
        "gold_docs_total": len(gold_by_id),
    }
