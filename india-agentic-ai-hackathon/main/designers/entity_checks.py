"""Shared S4 entity coverage / stuffing checks (Data Designer + direct + repair)."""

from __future__ import annotations

import re
from typing import Sequence

# Canonical tags: TYPE must be ASCII uppercase allow-list ids.
_TAG_TYPE_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|")
# Any bracket pair — catches localized / illegal TYPE spellings.
_ANY_TAG_RE = re.compile(r"\[\[([^\]|\n]+)\|([^\]]*)\]\]")
_VALID_TYPE_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")
_CANONICAL_TAG_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|([^\]]*)\]\]")

# Reject / retry when any TYPE appears more than this many times, or total tags
# exceed required_count * multiplier. Speaker names may repeat in chat.
MAX_OCCURRENCES_PER_TYPE = 2
MAX_TAG_MULTIPLIER = 2
STUFFING_EXEMPT_TYPES = frozenset({"PATIENT_NAME", "DOCTOR_NAME"})

# Billing / admin invents → allow-list optionals (or closest required type).
TYPE_ALIASES: dict[str, str] = {
    "EMAIL": "EMAIL_ADDRESS",
    "CONTACT_EMAIL": "EMAIL_ADDRESS",
    "ADDRESS_NUMBER": "RESIDENTIAL_ADDRESS",
    "HOME_ADDRESS": "RESIDENTIAL_ADDRESS",
    "ADDRESS": "RESIDENTIAL_ADDRESS",
}

# Not PHI labels — unwrap to plain prose (value kept, TYPE dropped).
PROSE_ONLY_INVENT_TYPES: frozenset[str] = frozenset(
    {
        "RECEIPT_NUMBER",
        "BILL_NUMBER",
        "INVOICE_NUMBER",
        "STATE",
        "TOTAL_AMOUNT",
        "GST_AMOUNT",
        "GRAND_TOTAL",
        "AMOUNT",
        "DATE",
        "TIME",
        "APPOINTMENT_DATE",
        "APPOINTMENT_TIME",
        "POLICY_NUMBER",
    }
)

# Judge flag alone must not burn repair budget / force fail when score is OK.
SOFT_JUDGE_FLAGS: frozenset[str] = frozenset({"invented_entity_type"})


def entity_type_counts(text: str) -> dict[str, int]:
    tallies: dict[str, int] = {}
    for entity_id in _TAG_TYPE_RE.findall(text):
        tallies[entity_id] = tallies.get(entity_id, 0) + 1
    return tallies


def has_valid_entity_tags(text: str) -> bool:
    return _TAG_TYPE_RE.search(text) is not None


def normalize_inline_entity_tags(
    text: str,
    *,
    known_types: Sequence[str] | None = None,
) -> tuple[str, list[str]]:
    """Rewrite known aliases and unwrap prose-only / unknown invents.

    Returns ``(normalized_text, change_notes)``. Safe no-op when nothing matches.
    When ``known_types`` is provided, any remaining ASCII TYPE not in that set
    is unwrapped to plain prose (billing invents → soft cleanup, not hard fail).
    """
    known = set(known_types) if known_types is not None else None
    notes: list[str] = []

    def _replace(match: re.Match[str]) -> str:
        typ = match.group(1)
        value = match.group(2)
        if typ in TYPE_ALIASES:
            mapped = TYPE_ALIASES[typ]
            notes.append(f"alias:{typ}->{mapped}")
            return f"[[{mapped}|{value}]]"
        if typ in PROSE_ONLY_INVENT_TYPES:
            notes.append(f"unwrap:{typ}")
            return value
        if known is not None and typ not in known:
            notes.append(f"unwrap_unknown:{typ}")
            return value
        return match.group(0)

    normalized = _CANONICAL_TAG_RE.sub(_replace, text)
    # Deduplicate notes while preserving order.
    seen: set[str] = set()
    ordered: list[str] = []
    for note in notes:
        if note not in seen:
            seen.add(note)
            ordered.append(note)
    return normalized, ordered


def invalid_type_tags(text: str) -> list[str]:
    """TYPE spellings that are not canonical ASCII allow-list ids.

    Example failure: ``[[রোগীর_নাম|…]]`` — model localized the TYPE. Pipeline
    only accepts ``[[PATIENT_NAME|…]]``.
    """
    bad: list[str] = []
    seen: set[str] = set()
    for typ, _value in _ANY_TAG_RE.findall(text):
        typ = typ.strip()
        if _VALID_TYPE_RE.match(typ):
            continue
        if typ not in seen:
            seen.add(typ)
            bad.append(typ)
    return bad


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


def tag_issues(
    text: str, required: Sequence[str]
) -> tuple[list[str], list[str], list[str]]:
    """Return (missing, stuffed, invalid_type_spellings)."""
    missing, stuffed = coverage_and_stuffing(text, required)
    return missing, stuffed, invalid_type_tags(text)
