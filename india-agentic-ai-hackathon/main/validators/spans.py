"""Span / annotation boundary checks."""

from __future__ import annotations

from main.entities.inline import InlineSpan, extract_inline_spans, malformed_bracket_fragments


def validate_annotation_spans(text: str) -> dict[str, object]:
    spans = extract_inline_spans(text)
    malformed = malformed_bracket_fragments(text)
    empty_values = [span.entity_type for span in spans if not span.value.strip()]
    overlapping = _overlapping_spans(spans)
    return {
        "span_count": len(spans),
        "malformed": malformed,
        "empty_values": empty_values,
        "overlapping": overlapping,
        "ok": not malformed and not empty_values and not overlapping,
    }


def _overlapping_spans(spans: list[InlineSpan]) -> list[tuple[int, int]]:
    overlaps: list[tuple[int, int]] = []
    ordered = sorted(spans, key=lambda span: span.start)
    for left, right in zip(ordered, ordered[1:]):
        if right.start < left.end:
            overlaps.append((left.start, right.end))
    return overlaps
