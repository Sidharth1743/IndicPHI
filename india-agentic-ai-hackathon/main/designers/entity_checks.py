"""Shared S4 entity coverage / stuffing checks (Data Designer + direct + repair)."""

from __future__ import annotations

import re
from typing import Sequence

_TAG_TYPE_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|")

# Reject / retry when any TYPE appears more than this many times, or total tags
# exceed required_count * multiplier. Speaker names may repeat in chat.
MAX_OCCURRENCES_PER_TYPE = 2
MAX_TAG_MULTIPLIER = 2
STUFFING_EXEMPT_TYPES = frozenset({"PATIENT_NAME", "DOCTOR_NAME"})


def entity_type_counts(text: str) -> dict[str, int]:
    tallies: dict[str, int] = {}
    for entity_id in _TAG_TYPE_RE.findall(text):
        tallies[entity_id] = tallies.get(entity_id, 0) + 1
    return tallies


def missing_required_entities(text: str, required: Sequence[str]) -> list[str]:
    present = set(_TAG_TYPE_RE.findall(text))
    return [entity_id for entity_id in required if entity_id not in present]


def stuffing_violations(text: str, required: Sequence[str]) -> list[str]:
    """Return stuffed TYPE ids (or TOTAL_TAGS>N) when tags are dumped/repeated."""
    counts = entity_type_counts(text)
    stuffed = [
        entity_id
        for entity_id, count in counts.items()
        if entity_id not in STUFFING_EXEMPT_TYPES
        and count > MAX_OCCURRENCES_PER_TYPE
    ]
    countable = sum(
        count
        for entity_id, count in counts.items()
        if entity_id not in STUFFING_EXEMPT_TYPES
    )
    cap = max(len(required), 1) * MAX_TAG_MULTIPLIER
    if countable > cap:
        for entity_id, count in counts.items():
            if (
                entity_id not in STUFFING_EXEMPT_TYPES
                and count > 1
                and entity_id not in stuffed
            ):
                stuffed.append(entity_id)
        if not stuffed:
            stuffed.append(f"TOTAL_TAGS>{cap}")
    return sorted(stuffed)


def coverage_and_stuffing(
    text: str, required: Sequence[str]
) -> tuple[list[str], list[str]]:
    """Return (missing_required, stuffing_violations)."""
    return missing_required_entities(text, required), stuffing_violations(
        text, required
    )
