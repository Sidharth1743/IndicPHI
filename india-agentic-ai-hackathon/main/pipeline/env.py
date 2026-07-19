"""Environment loading for pipeline stages."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Sequence

from main.pipeline.config_io import REPO_ROOT


def load_env_file(path: Path | None = None) -> None:
    """Load KEY=VALUE pairs from `.env` without overriding existing exports."""
    env_path = path or (REPO_ROOT / ".env")
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        if key and key not in os.environ:
            os.environ[key] = value


def require_env(name: str, *, fallbacks: Sequence[str] | None = None) -> str:
    """Return the first non-empty env var among ``name`` and optional fallbacks.

    Fallbacks must be listed explicitly in config (no silent guess of secrets).
    """
    candidates = (name, *(fallbacks or ()))
    for key in candidates:
        value = os.environ.get(key, "").strip()
        if value:
            return value
    joined = ", ".join(candidates)
    raise RuntimeError(
        f"Missing required environment variable(s): {joined}. "
        f"Set one in the shell or in {REPO_ROOT / '.env'}."
    )
