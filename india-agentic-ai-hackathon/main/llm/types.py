"""Shared chat-completion result type."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ChatResult:
    content: str
    model: str
    finish_reason: str
    prompt_tokens: int | None
    completion_tokens: int | None
    raw: dict[str, Any]
