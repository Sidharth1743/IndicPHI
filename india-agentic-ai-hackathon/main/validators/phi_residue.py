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
    # ABHA: 14 consecutive digits, or XX-XXXX-XXXX-XXXX
    (
        "abha_like",
        re.compile(
            r"(?<!\d)\d{14}(?!\d)|(?<![A-Za-z0-9])[A-Za-z0-9]{2}-\d{4}-\d{4}-\d{4}(?![A-Za-z0-9])"
        ),
    ),
    ("mrn_like", re.compile(r"\b(?:MRN|OPD|RX)[- ]?\d{3,}\b", re.IGNORECASE)),
    ("passport_like", re.compile(r"\b[A-Z]\d{7,8}\b")),
    # 9–18 digit runs excluding exact 12-digit aadhaar-length blocks
    ("bank_account_like", re.compile(r"(?<!\d)(?:\d{9,11}|\d{13,18})(?!\d)")),
    (
        "credit_card_like",
        re.compile(r"(?<!\d)(?:\d{4}[\s\-]?){3}\d{4}(?!\d)"),
    ),
    (
        "ipv4_like",
        re.compile(
            r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}"
            r"(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\b"
        ),
    ),
    ("mac_like", re.compile(r"\b(?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\b")),
    ("url_like", re.compile(r"https?://[^\s<>\"']+")),
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
