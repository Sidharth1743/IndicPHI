"""Scan generated text for unlabeled real-looking PHI/PII residue."""

from __future__ import annotations

import re

from main.entities.inline import INLINE_TAG_RE

# Patterns applied only to text *outside* inline tags.
_RESIDUE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("aadhaar_like", re.compile(r"(?<!\d)\d{4}\s?\d{4}\s?\d{4}(?!\d)")),
    ("pan_like", re.compile(r"\b[A-Z]{5}\d{4}[A-Z]\b")),
    ("ifsc_like", re.compile(r"\b[A-Z]{4}0[A-Z0-9]{6}\b")),
    ("phone_like", re.compile(r"(?<!\d)(?:\+91[\-\s]?)?[6-9]\d{9}(?!\d)")),
    ("email_like", re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")),
)


def _mask_tagged_regions(text: str) -> str:
    return INLINE_TAG_RE.sub(lambda match: " " * (match.end() - match.start()), text)


def scan_phi_residue(text: str) -> list[dict[str, str | int]]:
    masked = _mask_tagged_regions(text)
    hits: list[dict[str, str | int]] = []
    for label, pattern in _RESIDUE_PATTERNS:
        for match in pattern.finditer(masked):
            hits.append(
                {
                    "kind": label,
                    "value": match.group(0),
                    "start": match.start(),
                    "end": match.end(),
                }
            )
    return hits
