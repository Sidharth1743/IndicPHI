"""Script / language purity helpers for Indic clinical text."""

from __future__ import annotations

import re
from typing import Mapping

# Target script Unicode ranges for document_script labels used in languages.yaml.
_SCRIPT_RANGES: Mapping[str, tuple[tuple[int, int], ...]] = {
    "Latin": ((0x0041, 0x007A),),
    "Devanagari": ((0x0900, 0x097F),),
    "Bengali": ((0x0980, 0x09FF),),
    "Gurmukhi": ((0x0A00, 0x0A7F),),
    "Gujarati": ((0x0A80, 0x0AFF),),
    "Oriya": ((0x0B00, 0x0B7F),),
    "Odia": ((0x0B00, 0x0B7F),),
    "Tamil": ((0x0B80, 0x0BFF),),
    "Telugu": ((0x0C00, 0x0C7F),),
    "Kannada": ((0x0C80, 0x0CFF),),
    "Malayalam": ((0x0D00, 0x0D7F),),
    "Arabic": ((0x0600, 0x06FF), (0x0750, 0x077F)),
    "Meitei": ((0xABC0, 0xABFF),),
    "Ol Chiki": ((0x1C50, 0x1C7F),),
}

_SCRIPT_ALIASES: Mapping[str, str] = {
    "Ol_Chiki": "Ol Chiki",
    "OlChiki": "Ol Chiki",
    "ol_chiki": "Ol Chiki",
}

_TAG_RE = re.compile(r"\[\[[^\]]+\]\]")
_LATIN_LETTER_RE = re.compile(r"[A-Za-z]")


def normalize_script_name(script: str) -> str:
    """Map known aliases (e.g. Ol_Chiki) to canonical ``_SCRIPT_RANGES`` keys."""
    return _SCRIPT_ALIASES.get(script, script)


def strip_inline_tags(text: str) -> str:
    return _TAG_RE.sub(" ", text)


def _count_script_chars(text: str, script: str) -> int:
    ranges = _SCRIPT_RANGES.get(normalize_script_name(script))
    if not ranges:
        return 0
    total = 0
    for char in text:
        code = ord(char)
        for start, end in ranges:
            if start <= code <= end:
                total += 1
                break
    return total


def evaluate_script_purity(
    text: str,
    *,
    language_code: str,
    script: str,
    min_target_ratio: float = 0.35,
) -> tuple[bool, str]:
    """Return (ok, reason). English / Latin docs always pass.

    For Indic scripts, require enough target-script letters in non-tag prose.
    Also fail when another known Indic script has more letters than the target
    (e.g. Devanagari body for a Gujarati document).
    """
    if language_code == "en" or script == "Latin":
        return True, "ok"

    script = normalize_script_name(script)
    prose = strip_inline_tags(text)
    target = _count_script_chars(prose, script)

    # Fail when a non-target Indic/Arabic script dominates the body
    # (e.g. Devanagari prose for a Gujarati document).
    target_ranges = _SCRIPT_RANGES.get(script)
    for other_name, other_ranges in _SCRIPT_RANGES.items():
        if other_name == "Latin" or other_name == script:
            continue
        if target_ranges is not None and other_ranges == target_ranges:
            continue
        other_count = _count_script_chars(prose, other_name)
        if other_count > target:
            return False, f"wrong_indic_script:{other_name}>{script}"

    latin = len(_LATIN_LETTER_RE.findall(prose))
    denom = target + latin
    if denom == 0:
        return False, "no_letter_chars"
    ratio = target / denom
    if ratio < min_target_ratio:
        return False, f"target_script_ratio:{ratio:.3f}<{min_target_ratio}"
    return True, "ok"
