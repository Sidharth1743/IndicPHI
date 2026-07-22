"""Sarvam dedicated ``/translate`` API (sarvam-translate:v1).

Used as a rare-script fallback after chat-translate fails. Max 2000 chars
per call — callers must chunk longer clinical notes.
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from typing import Sequence

from main.llm.rate_limit import RateLimiter

# Our pipeline codes → Sarvam BCP-47 (Odia is od-IN, not or-IN).
_LANG_TO_BCP47: dict[str, str] = {
    "as": "as-IN",
    "bn": "bn-IN",
    "brx": "brx-IN",
    "doi": "doi-IN",
    "en": "en-IN",
    "gu": "gu-IN",
    "hi": "hi-IN",
    "kn": "kn-IN",
    "ks": "ks-IN",
    "kok": "kok-IN",
    "mai": "mai-IN",
    "ml": "ml-IN",
    "mni": "mni-IN",
    "mr": "mr-IN",
    "ne": "ne-IN",
    "or": "od-IN",
    "pa": "pa-IN",
    "sa": "sa-IN",
    "sat": "sat-IN",
    "sd": "sd-IN",
    "ta": "ta-IN",
    "te": "te-IN",
    "ur": "ur-IN",
}

_SENTENCE_SPLIT_RE = re.compile(r"(?<=[\n.!?।\|])\s+")


class SarvamTranslateError(RuntimeError):
    pass


def to_bcp47(language_code: str) -> str:
    code = str(language_code or "").strip().lower()
    if code in _LANG_TO_BCP47:
        return _LANG_TO_BCP47[code]
    if "-" in code:
        return code
    raise SarvamTranslateError(f"Unsupported language_code for /translate: {language_code!r}")


def chunk_text(text: str, *, max_chars: int = 1800) -> list[str]:
    """Split on sentence/newline boundaries under max_chars (sarvam-translate=2000)."""
    text = text.strip()
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]

    parts = _SENTENCE_SPLIT_RE.split(text)
    chunks: list[str] = []
    buf = ""
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) > max_chars:
            if buf:
                chunks.append(buf)
                buf = ""
            for i in range(0, len(part), max_chars):
                chunks.append(part[i : i + max_chars])
            continue
        candidate = f"{buf} {part}".strip() if buf else part
        if len(candidate) <= max_chars:
            buf = candidate
        else:
            chunks.append(buf)
            buf = part
    if buf:
        chunks.append(buf)
    return chunks


class SarvamTranslateClient:
    """HTTP client for ``POST https://api.sarvam.ai/translate``."""

    def __init__(
        self,
        *,
        api_key: str,
        rate_limiter: RateLimiter | None = None,
        endpoint: str = "https://api.sarvam.ai/translate",
    ) -> None:
        if not api_key:
            raise SarvamTranslateError("Sarvam api_key is empty")
        self.api_key = api_key
        self.rate_limiter = rate_limiter
        self.endpoint = endpoint.rstrip("/")

    def translate_chunk(
        self,
        text: str,
        *,
        source_language_code: str = "en-IN",
        target_language_code: str,
        model: str = "sarvam-translate:v1",
        numerals_format: str = "international",
        timeout_s: float = 120.0,
    ) -> str:
        if self.rate_limiter is not None:
            self.rate_limiter.acquire()

        payload = {
            "input": text,
            "source_language_code": source_language_code,
            "target_language_code": target_language_code,
            "model": model,
            "numerals_format": numerals_format,
        }
        request = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "api-subscription-key": self.api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout_s) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise SarvamTranslateError(
                f"Sarvam /translate HTTP {exc.code}: {detail[:800]}"
            ) from exc
        except urllib.error.URLError as exc:
            raise SarvamTranslateError(f"Sarvam /translate network error: {exc}") from exc
        except TimeoutError as exc:
            raise SarvamTranslateError(
                f"Sarvam /translate timeout after {timeout_s}s: {exc}"
            ) from exc
        except OSError as exc:
            raise SarvamTranslateError(
                f"Sarvam /translate OS/network error: {exc}"
            ) from exc

        out = body.get("translated_text")
        if not isinstance(out, str) or not out.strip():
            raise SarvamTranslateError(
                f"Sarvam /translate empty translated_text: {body!r}"
            )
        return out.strip()

    def translate_long(
        self,
        text: str,
        *,
        language_code: str,
        source_language_code: str = "en-IN",
        model: str = "sarvam-translate:v1",
        numerals_format: str = "international",
        max_chars: int = 1800,
        timeout_s: float = 120.0,
    ) -> str:
        target = to_bcp47(language_code)
        chunks = chunk_text(text, max_chars=max_chars)
        if not chunks:
            return ""
        translated: list[str] = []
        for chunk in chunks:
            translated.append(
                self.translate_chunk(
                    chunk,
                    source_language_code=source_language_code,
                    target_language_code=target,
                    model=model,
                    numerals_format=numerals_format,
                    timeout_s=timeout_s,
                )
            )
        return "\n".join(translated)
