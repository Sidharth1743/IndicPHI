"""Inline [[TYPE|value]] annotation parsing."""

from __future__ import annotations

import re
from dataclasses import dataclass

INLINE_TAG_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|([^\]]+)\]\]")


@dataclass(frozen=True)
class InlineSpan:
    entity_type: str
    value: str
    start: int
    end: int


def extract_inline_spans(text: str) -> list[InlineSpan]:
    spans: list[InlineSpan] = []
    for match in INLINE_TAG_RE.finditer(text):
        spans.append(
            InlineSpan(
                entity_type=match.group(1),
                value=match.group(2),
                start=match.start(),
                end=match.end(),
            )
        )
    return spans


def strip_inline_tags(text: str) -> str:
    """Return surface text with tags removed but surrogate values retained."""
    return INLINE_TAG_RE.sub(lambda match: match.group(2), text)


def malformed_bracket_fragments(text: str) -> list[str]:
    """Detect likely broken annotation fragments (unbalanced / partial tags)."""
    issues: list[str] = []
    if text.count("[[") != text.count("]]"):
        issues.append("unbalanced_double_brackets")
    # Lone [[ without closing ]] within a reasonable window
    for match in re.finditer(r"\[\[(?![A-Z][A-Z0-9_]*\|[^\]]+\]\])", text):
        issues.append(f"malformed_open_at_{match.start()}")
    return issues
