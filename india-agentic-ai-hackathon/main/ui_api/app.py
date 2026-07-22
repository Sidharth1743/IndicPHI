"""FastAPI app for the HackGrid pipeline demo UI."""

from __future__ import annotations

import asyncio
import json
import threading
import traceback
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

from main.pipeline.config_io import REPO_ROOT
from main.pipeline.run_layout import new_run_id, run_dir
from main.ui_api.constants import MODELS_BLURB
from main.ui_api.overlay import write_smoke_overlay
from main.ui_api.progress import build_snapshot, list_runs, load_languages
from main.ui_api.replay import build_replay_timeline, events_from_live_delta

# In-memory live-run bookkeeping (single-user demo).
_LIVE: dict[str, dict[str, Any]] = {}
_LIVE_LOCK = threading.Lock()


class StartRunBody(BaseModel):
    num_docs: int = Field(default=10, ge=1, le=200)
    language_codes: list[str] = Field(default_factory=lambda: ["hi", "bn", "en"])
    config: str = "configs/synthetic-data/pipeline.smoke.yaml"


def create_app() -> FastAPI:
    app = FastAPI(title="HackGrid Pipeline Demo API", version="0.1.0")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://127.0.0.1:5173",
            "http://localhost:5173",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/api/meta")
    def meta() -> dict[str, Any]:
        return {
            "languages": load_languages(),
            "models": dict(MODELS_BLURB),
            "runs": list_runs(),
        }

    @app.post("/api/runs")
    def start_run(body: StartRunBody) -> dict[str, str]:
        if not body.language_codes:
            raise HTTPException(status_code=400, detail="language_codes required")
        try:
            overlay = write_smoke_overlay(
                num_docs=body.num_docs,
                language_codes=body.language_codes,
                base_config=body.config,
            )
        except FileNotFoundError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc

        run_id = new_run_id()
        # Avoid colliding with an existing folder in the same second.
        while run_dir(run_id).exists():
            run_id = new_run_id()

        with _LIVE_LOCK:
            _LIVE[run_id] = {
                "status": "starting",
                "overlay": str(overlay),
                "error": None,
            }

        def _worker() -> None:
            from main.pipeline.run_pipeline import run_pipeline

            with _LIVE_LOCK:
                _LIVE[run_id]["status"] = "running"
            try:
                code = run_pipeline(
                    base_config=overlay.resolve(),
                    run_id=run_id,
                )
                with _LIVE_LOCK:
                    _LIVE[run_id]["status"] = "ok" if code == 0 else "failed"
                    _LIVE[run_id]["exit_code"] = code
            except Exception as exc:  # noqa: BLE001
                with _LIVE_LOCK:
                    _LIVE[run_id]["status"] = "failed"
                    _LIVE[run_id]["error"] = str(exc)
                    _LIVE[run_id]["traceback"] = traceback.format_exc()

        thread = threading.Thread(
            target=_worker, name=f"pipeline-{run_id}", daemon=True
        )
        thread.start()
        with _LIVE_LOCK:
            _LIVE[run_id]["thread"] = thread

        return {"run_id": run_id, "mode": "live"}

    @app.get("/api/runs/{run_id}")
    def get_run(run_id: str) -> dict[str, Any]:
        root = run_dir(run_id)
        if not root.is_dir() and run_id not in _LIVE:
            raise HTTPException(status_code=404, detail=f"Run not found: {run_id}")
        # Wait briefly for materialize if just started.
        if not (root / "run_results.json").is_file() and run_id in _LIVE:
            return {
                "run_id": run_id,
                "status": "running",
                "path": str(root),
                "models": dict(MODELS_BLURB),
                "stages": [],
                "active_stage": "seed",
                "repair_active": False,
                "repair_nodes": [],
                "summary": {},
                "inspector": {
                    "node_id": "seed",
                    "status": "running",
                    "model": MODELS_BLURB["personas"],
                    "counts": {},
                    "sample": [],
                    "fail_reason": None,
                },
                "raw_stages": [],
            }
        try:
            snap = build_snapshot(run_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        with _LIVE_LOCK:
            live = _LIVE.get(run_id)
        if live and live.get("error") and snap.get("status") != "failed":
            snap["status"] = "failed"
            snap["error"] = live["error"]
        return snap

    @app.post("/api/runs/{run_id}/stop")
    def stop_run(run_id: str) -> dict[str, str]:
        root = run_dir(run_id)
        if not root.is_dir() and run_id not in _LIVE:
            raise HTTPException(status_code=404, detail=f"Run not found: {run_id}")
        (root / ".cancel").write_text("1\n", encoding="utf-8")
        with _LIVE_LOCK:
            if run_id in _LIVE:
                _LIVE[run_id]["status"] = "stopping"
        return {"run_id": run_id, "status": "stopping"}

    @app.get("/api/runs/{run_id}/stream")
    async def stream_run(run_id: str) -> StreamingResponse:
        async def event_gen():
            prev: dict[str, Any] | None = None
            while True:
                try:
                    if (run_dir(run_id) / "run_results.json").is_file():
                        curr = build_snapshot(run_id)
                    elif run_id in _LIVE:
                        curr = {
                            "run_id": run_id,
                            "status": "running",
                            "stages": [],
                            "summary": {},
                            "repair_active": False,
                            "repair_nodes": [],
                        }
                    else:
                        payload = {
                            "type": "error",
                            "message": f"Run not found: {run_id}",
                        }
                        yield f"event: error\ndata: {json.dumps(payload)}\n\n"
                        return
                except FileNotFoundError as exc:
                    payload = {"type": "error", "message": str(exc)}
                    yield f"event: error\ndata: {json.dumps(payload)}\n\n"
                    return

                deltas = events_from_live_delta(prev, curr)
                for ev in deltas:
                    etype = str(ev.get("type") or "message")
                    yield f"event: {etype}\ndata: {json.dumps(ev)}\n\n"
                    if etype in {"done", "error"}:
                        return

                if curr.get("status") == "running" and not deltas:
                    active = curr.get("active_stage") or "seed"
                    heartbeat = {
                        "type": "progress",
                        "node_id": active,
                        "stage": active,
                        "message": curr.get("activity"),
                        "counts": next(
                            (
                                s.get("counts")
                                for s in (curr.get("stages") or [])
                                if s.get("id") == active
                            ),
                            {},
                        ),
                        "inspector": curr.get("inspector"),
                        "repair_path": curr.get("repair_path") or [],
                    }
                    yield f"event: progress\ndata: {json.dumps(heartbeat)}\n\n"

                if curr.get("status") in {"ok", "failed", "cancelled"} and not deltas:
                    # Attached after completion with no status flip vs prev.
                    if curr.get("status") == "ok":
                        done = {"type": "done", "status": "ok", "run_id": run_id}
                        yield f"event: done\ndata: {json.dumps(done)}\n\n"
                    elif curr.get("status") == "cancelled":
                        done = {
                            "type": "done",
                            "status": "cancelled",
                            "run_id": run_id,
                            "message": "Run stopped by user",
                        }
                        yield f"event: done\ndata: {json.dumps(done)}\n\n"
                    else:
                        snap = build_snapshot(run_id)
                        failure = snap.get("failure")
                        node = failure.get("node_id") if failure else None
                        msg = (
                            f"{node} failed: {failure.get('error')}"
                            if failure and node
                            else "Pipeline failed"
                        )
                        done = {
                            "type": "done",
                            "status": "failed",
                            "run_id": run_id,
                            "message": msg,
                            "stage": node,
                            "node_id": node,
                            "fail_reason": failure.get("error") if failure else None,
                            "summary": snap.get("summary") or {},
                        }
                        yield f"event: done\ndata: {json.dumps(done)}\n\n"
                    return

                prev = curr
                await asyncio.sleep(0.35)

        return StreamingResponse(
            event_gen(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    @app.post("/api/replay/{run_id}")
    def replay(run_id: str) -> dict[str, Any]:
        try:
            return build_replay_timeline(run_id)
        except FileNotFoundError as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.get("/api/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "repo": str(REPO_ROOT)}

    return app


app = create_app()
