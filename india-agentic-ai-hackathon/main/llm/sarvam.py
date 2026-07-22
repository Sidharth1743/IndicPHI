"""Sarvam Chat Completions client (OpenAI-compatible HTTP API).

Auth header: ``api-subscription-key`` (not Bearer).
Model context window (sarvam-105b): 128000 tokens.
Pipeline generation uses a quality-safe ``max_tokens`` (e.g. 16384), not the
full context ceiling — larger caps encourage runaway dumps without better
clinical quality. Sarvam-105B Business: 120 req/min (ms-llm default is separate).

Reasoning control (verified against live API):
- Send ``"reasoning_effort": null`` in the JSON body → reasoning OFF.
- Omit the field entirely → Sarvam keeps default reasoning ON (burns tokens).
- ``"low"|"medium"|"high"`` → reasoning ON.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Sequence

from main.llm.rate_limit import RateLimiter
from main.llm.types import ChatResult

# Back-compat aliases used by older imports.
SarvamChatResult = ChatResult


class SarvamClientError(RuntimeError):
    pass


class SarvamClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        rate_limiter: RateLimiter | None = None,
    ) -> None:
        if not api_key:
            raise SarvamClientError("Sarvam api_key is empty")
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.rate_limiter = rate_limiter

    def chat_completion(
        self,
        *,
        model: str,
        messages: Sequence[dict[str, str]],
        temperature: float,
        max_tokens: int,
        reasoning_effort: str | None = None,
        timeout_s: float = 180.0,
    ) -> ChatResult:
        if self.rate_limiter is not None:
            self.rate_limiter.acquire()

        payload: dict[str, Any] = {
            "model": model,
            "messages": list(messages),
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": False,
            # CRITICAL: JSON null disables reasoning. Omitting this field leaves
            # Sarvam's default reasoning ON and often exhausts the output budget.
            "reasoning_effort": reasoning_effort,
        }

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
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
            raise SarvamClientError(
                f"Sarvam HTTP {exc.code}: {detail[:800]}"
            ) from exc
        except urllib.error.URLError as exc:
            raise SarvamClientError(f"Sarvam network error: {exc}") from exc
        except TimeoutError as exc:
            # urlopen raises bare TimeoutError on read timeout (not URLError).
            raise SarvamClientError(
                f"Sarvam timeout after {timeout_s}s: {exc}"
            ) from exc
        except OSError as exc:
            raise SarvamClientError(f"Sarvam OS/network error: {exc}") from exc

        try:
            choice = body["choices"][0]
            message = choice["message"]
            content = message.get("content")
            finish_reason = str(choice.get("finish_reason") or "")
            usage = body.get("usage") or {}
        except (KeyError, IndexError, TypeError) as exc:
            raise SarvamClientError(
                f"Unexpected Sarvam response shape: {body!r}"
            ) from exc

        if not isinstance(content, str) or not content.strip():
            raise SarvamClientError(
                "Sarvam returned empty content (reasoning may have exhausted "
                f"max_tokens). finish_reason={finish_reason!r} "
                f"reasoning_present={bool(message.get('reasoning_content'))} "
                "Send reasoning_effort=null and keep max_tokens within needs."
            )

        return ChatResult(
            content=content.strip(),
            model=str(body.get("model") or model),
            finish_reason=finish_reason,
            prompt_tokens=usage.get("prompt_tokens"),
            completion_tokens=usage.get("completion_tokens"),
            raw=body,
        )
