"""HackGrid pipeline demo UI API (FastAPI)."""

from __future__ import annotations

__all__ = ["app", "create_app"]


def __getattr__(name: str):
    if name in {"app", "create_app"}:
        from main.ui_api.app import app, create_app

        return app if name == "app" else create_app
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
