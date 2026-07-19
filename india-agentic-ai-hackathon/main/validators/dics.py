"""Document Internal Consistency Score (DICS)."""

from __future__ import annotations

from collections import defaultdict

from main.entities.inline import extract_inline_spans


def compute_dics(text: str) -> dict[str, object]:
    """DICS = consistent_coreferences / total_coreferences.

    For each entity type that appears more than once, all values must match.
    Hard target: 1.0
    """
    by_type: dict[str, list[str]] = defaultdict(list)
    for span in extract_inline_spans(text):
        by_type[span.entity_type].append(span.value.strip())

    total = 0
    consistent = 0
    conflicts: dict[str, list[str]] = {}

    for entity_type, values in by_type.items():
        if len(values) < 2:
            continue
        total += len(values)
        unique = sorted(set(values))
        if len(unique) == 1:
            consistent += len(values)
        else:
            conflicts[entity_type] = unique

    score = 1.0 if total == 0 else consistent / total
    return {
        "dics": score,
        "coreference_mentions": total,
        "consistent_mentions": consistent,
        "conflicts": conflicts,
        "ok": score == 1.0,
    }
