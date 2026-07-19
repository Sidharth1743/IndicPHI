"""OpenAI-compatible Chat Completions client (Azure Foundry / xAI / NIM).

Auth: ``Authorization: Bearer <api_key>``
Endpoint: ``{base_url}/chat/completions``

Proven for Grok-4.3 via Azure Foundry in IndicEvalHarness:
``…/openai/v1`` + model ``grok-4.3``.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any, Sequence

from main.llm.rate_limit import RateLimiter
from main.llm.types import ChatResult


class OpenAICompatibleClientError(RuntimeError):
    pass


class OpenAICompatibleClient:
    def __init__(
        self,
        *,
        api_key: str,
        base_url: str,
        rate_limiter: RateLimiter | None = None,
        max_tokens_field: str = "max_tokens",
    ) -> None:
        if not api_key:
            raise OpenAICompatibleClientError("api_key is empty")
        if max_tokens_field not in {"max_tokens", "max_completion_tokens"}:
            raise OpenAICompatibleClientError(
                f"Unsupported max_tokens_field={max_tokens_field!r}"
            )
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.rate_limiter = rate_limiter
        self.max_tokens_field = max_tokens_field

    def chat_completion(
        self,
        *,
        model: str,
        messages: Sequence[dict[str, str]],
        temperature: float,
        max_tokens: int,
        timeout_s: float = 180.0,
        extra_body: dict[str, Any] | None = None,
    ) -> ChatResult:
        if self.rate_limiter is not None:
            self.rate_limiter.acquire()

        payload: dict[str, Any] = {
            "model": model,
            "messages": list(messages),
            "temperature": temperature,
            self.max_tokens_field: max_tokens,
            "stream": False,
        }
        if extra_body:
            payload.update(extra_body)

        request = urllib.request.Request(
            f"{self.base_url}/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
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
            raise OpenAICompatibleClientError(
                f"OpenAI-compatible HTTP {exc.code}: {detail[:800]}"
            ) from exc
        except urllib.error.URLError as exc:
            raise OpenAICompatibleClientError(
                f"OpenAI-compatible network error: {exc}"
            ) from exc
        except TimeoutError as exc:
            # urlopen raises bare TimeoutError on read timeout (not URLError).
            raise OpenAICompatibleClientError(
                f"OpenAI-compatible timeout after {timeout_s}s: {exc}"
            ) from exc
        except OSError as exc:
            raise OpenAICompatibleClientError(
                f"OpenAI-compatible OS/network error: {exc}"
            ) from exc

        try:
            choice = body["choices"][0]
            message = choice["message"]
            content = message.get("content")
            finish_reason = str(choice.get("finish_reason") or "")
            usage = body.get("usage") or {}
        except (KeyError, IndexError, TypeError) as exc:
            raise OpenAICompatibleClientError(
                f"Unexpected response shape: {body!r}"
            ) from exc

        if not isinstance(content, str) or not content.strip():
            raise OpenAICompatibleClientError(
                "Provider returned empty content. "
                f"finish_reason={finish_reason!r} message_keys={list(message)}"
            )

        return ChatResult(
            content=content.strip(),
            model=str(body.get("model") or model),
            finish_reason=finish_reason,
            prompt_tokens=usage.get("prompt_tokens") or usage.get("input_tokens"),
            completion_tokens=usage.get("completion_tokens")
            or usage.get("output_tokens"),
            raw=body,
        )
