"""Build a timed replay timeline from an existing run folder."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from main.pipeline.run_layout import run_dir
from main.ui_api.constants import NODE_ORDER, NODE_STAGES, REPLAY_DURATION_S
from main.ui_api.progress import (
    _historical_repair_signals,
    _read_json,
    _repair_path,
    _repairing_nodes,
    _run_failure_detail,
    build_snapshot,
    build_summary,
)


def _parse_ts(value: object) -> datetime | None:
    if not value or not isinstance(value, str):
        return None
    text = value.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def _node_timings(results: dict[str, Any]) -> list[dict[str, Any]]:
    """Collapse orchestrator stages into presentation nodes with wall times."""
    by_label = {
        str(s["stage"]): s
        for s in (results.get("stages") or [])
        if isinstance(s, dict) and s.get("stage")
    }
    nodes: list[dict[str, Any]] = []
    for node_id in NODE_ORDER:
        labels = NODE_STAGES[node_id]
        present = [by_label[lab] for lab in labels if lab in by_label]
        if not present:
            continue
        starts = [_parse_ts(s.get("started_utc")) for s in present]
        ends = [_parse_ts(s.get("finished_utc")) for s in present]
        starts_f = [t for t in starts if t is not None]
        ends_f = [t for t in ends if t is not None]
        status = "failed" if any(s.get("status") == "failed" for s in present) else "ok"
        nodes.append(
            {
                "id": node_id,
                "status": status,
                "started": min(starts_f) if starts_f else None,
                "finished": max(ends_f) if ends_f else None,
                "error": next(
                    (s.get("error") for s in present if s.get("status") == "failed"),
                    None,
                ),
            }
        )
    return nodes


def build_replay_timeline(
    run_id: str, *, duration_s: float = REPLAY_DURATION_S
) -> dict[str, Any]:
    root = run_dir(run_id)
    if not root.is_dir():
        raise FileNotFoundError(f"Run not found: {run_id}")
    results = _read_json(root / "run_results.json")
    if not results:
        raise FileNotFoundError(f"run_results.json missing for {run_id}")

    nodes = _node_timings(results)
    stage_by_label = {
        str(s["stage"]): s
        for s in (results.get("stages") or [])
        if isinstance(s, dict) and s.get("stage")
    }
    repairing = _historical_repair_signals(root)
    summary = build_summary(root)
    snapshot = build_snapshot(run_id)

    # Proportional schedule from real stage durations, scaled to ~duration_s.
    real_spans: list[float] = []
    for node in nodes:
        started, finished = node["started"], node["finished"]
        if started and finished:
            real_spans.append(max(0.05, (finished - started).total_seconds()))
        else:
            real_spans.append(1.0)
    total_real = sum(real_spans) or 1.0
    scale = float(duration_s) * 0.85 / total_real  # leave room for summary/done

    events: list[dict[str, Any]] = []
    t = 0.0
    for i, node in enumerate(nodes):
        span = real_spans[i] * scale
        events.append(
            {
                "t": round(t, 3),
                "at": round(t * 1000),
                "type": "stage",
                "node_id": node["id"],
                "stage": node["id"],
                "status": "running",
                "message": f"{node['id']} started",
            }
        )
        # Mid-stage repair pulse when soft-fail/repair signals exist for arc nodes.
        if node["id"] in {"generate", "translate", "judge", "audit"} and repairing:
            mid = t + span * 0.45
            events.append(
                {
                    "t": round(mid, 3),
                    "at": round(mid * 1000),
                    "type": "repair",
                    "node_id": node["id"],
                    "stage": node["id"],
                    "status": "repairing",
                    "nodes": sorted(repairing) or [node["id"], "generate"],
                    "repair_path": _repair_path(repairing),
                    "message": "soft-fail / repair loop",
                }
            )
        events.append(
            {
                "t": round(t + span * 0.55, 3),
                "at": round((t + span * 0.55) * 1000),
                "type": "progress",
                "node_id": node["id"],
                "stage": node["id"],
                "counts": next(
                    (
                        s["counts"]
                        for s in snapshot["stages"]
                        if s["id"] == node["id"]
                    ),
                    {},
                ),
                "inspector": snapshot.get("inspector")
                if node["id"] == snapshot.get("active_stage")
                else None,
            }
        )
        end_status = "failed" if node["status"] == "failed" else "ok"
        events.append(
            {
                "t": round(t + span, 3),
                "at": round((t + span) * 1000),
                "type": "stage",
                "node_id": node["id"],
                "stage": node["id"],
                "status": end_status,
                "message": f"{node['id']} {end_status}",
                "error": node.get("error"),
            }
        )
        t += span
        if end_status == "failed":
            events.append(
                {
                    "t": round(t, 3),
                    "type": "error",
                    "node_id": node["id"],
                    "message": str(node.get("error") or "stage failed"),
                }
            )
            break

    events.append(
        {
            "t": round(t + 0.4, 3),
            "type": "summary",
            "summary": summary,
        }
    )
    events.append(
        {
            "t": round(min(float(duration_s), t + 1.0), 3),
            "type": "done",
            "status": str(results.get("status") or "ok"),
            "run_id": run_id,
        }
    )
    events.sort(key=lambda e: float(e["t"]))

    return {
        "run_id": run_id,
        "duration_s": float(duration_s),
        "duration_ms": int(float(duration_s) * 1000),
        "status": str(results.get("status") or "unknown"),
        "events": events,
        "summary": summary,
        "snapshot": snapshot,
    }


def _event_stage(node_id: str, **extra: Any) -> dict[str, Any]:
    """Normalize node_id → stage for frontend compatibility."""
    return {"node_id": node_id, "stage": node_id, **extra}


def events_from_live_delta(
    prev: dict[str, Any] | None, curr: dict[str, Any]
) -> list[dict[str, Any]]:
    """Diff two snapshots into SSE-friendly events (for live stream)."""
    out: list[dict[str, Any]] = []
    prev_stages = {
        s["id"]: s for s in ((prev or {}).get("stages") or []) if "id" in s
    }
    repair_path = curr.get("repair_path") or _repair_path(
        set(curr.get("repair_nodes") or [])
    )

    for stage in curr.get("stages") or []:
        node_id = stage["id"]
        prev_status = (prev_stages.get(node_id) or {}).get("status")
        status = stage.get("status")
        if status != prev_status:
            out.append(
                _event_stage(
                    node_id,
                    type="stage",
                    status=status,
                    counts=stage.get("counts") or {},
                    model=stage.get("model"),
                    message=curr.get("activity") if node_id == curr.get("active_stage") else None,
                )
            )
            if status == "repairing":
                out.append(
                    {
                        "type": "repair",
                        "node_id": node_id,
                        "stage": node_id,
                        "nodes": curr.get("repair_nodes") or [node_id],
                        "repair_path": repair_path,
                        "message": "soft-fail → repair loop",
                    }
                )
        elif status in {"running", "repairing"} and stage.get("counts") != (
            prev_stages.get(node_id) or {}
        ).get("counts"):
            out.append(
                _event_stage(
                    node_id,
                    type="progress",
                    status=status,
                    counts=stage.get("counts") or {},
                    message=curr.get("activity"),
                )
            )

    if curr.get("repair_active") and not (prev or {}).get("repair_active"):
        out.append(
            {
                "type": "repair",
                "nodes": curr.get("repair_nodes") or [],
                "repair_path": repair_path,
                "status": "repairing",
                "message": "repair loop active",
            }
        )

    # Heartbeat activity / inspector while running
    if curr.get("status") == "running":
        active = curr.get("active_stage")
        prev_activity = (prev or {}).get("activity")
        if active and curr.get("activity") and curr.get("activity") != prev_activity:
            out.append(
                {
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
                }
            )

    prev_status = (prev or {}).get("status")
    if curr.get("status") != prev_status and curr.get("status") in {
        "ok",
        "failed",
        "cancelled",
    }:
        out.append({"type": "summary", "summary": curr.get("summary") or {}})
        failure = curr.get("failure") or _run_failure_detail(
            {"stages": curr.get("raw_stages") or []}
        )
        if curr.get("status") == "ok":
            out.append(
                {"type": "done", "status": "ok", "run_id": curr.get("run_id")}
            )
        elif curr.get("status") == "cancelled":
            out.append(
                {
                    "type": "done",
                    "status": "cancelled",
                    "run_id": curr.get("run_id"),
                    "message": "Run stopped by user",
                }
            )
        else:
            node = failure.get("node_id") if failure else None
            msg = (
                f"{node} failed: {failure.get('error')}"
                if failure and node
                else "Pipeline failed"
            )
            out.append(
                {
                    "type": "done",
                    "status": "failed",
                    "run_id": curr.get("run_id"),
                    "message": msg,
                    "stage": node,
                    "node_id": node,
                    "fail_reason": failure.get("error") if failure else None,
                    "summary": curr.get("summary") or {},
                }
            )
    return out


# Re-export for callers.
__all__ = [
    "build_replay_timeline",
    "events_from_live_delta",
]
