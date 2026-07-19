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

_TAG_RE = re.compile(r"\[\[[^\]]+\]\]")
_LATIN_LETTER_RE = re.compile(r"[A-Za-z]")


def strip_inline_tags(text: str) -> str:
    return _TAG_RE.sub(" ", text)


def _count_script_chars(text: str, script: str) -> int:
    ranges = _SCRIPT_RANGES.get(script)
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
    """
    if language_code == "en" or script == "Latin":
        return True, "ok"

    prose = strip_inline_tags(text)
    target = _count_script_chars(prose, script)
    latin = len(_LATIN_LETTER_RE.findall(prose))
    denom = target + latin
    if denom == 0:
        return False, "no_letter_chars"
    ratio = target / denom
    if ratio < min_target_ratio:
        return False, f"target_script_ratio:{ratio:.3f}<{min_target_ratio}"
    return True, "ok"
