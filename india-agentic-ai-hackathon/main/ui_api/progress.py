"""Build run snapshots, summaries, and inspector payloads from disk."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from main.pipeline.failures_report import collect_failure_entries
from main.pipeline.run_layout import RUNS_ROOT, run_dir
from main.ui_api.constants import (
    MODELS_BLURB,
    NODE_MODELS,
    NODE_ORDER,
    NODE_STAGES,
    STAGE_FOLDER,
    STAGE_TO_NODE,
)


def _read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def _count_jsonl(path: Path) -> int:
    if not path.is_file() or path.stat().st_size == 0:
        return 0
    n = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                n += 1
    return n


def _clip(text: str | None, n: int = 280) -> str:
    if not text:
        return ""
    text = str(text).replace("\r\n", "\n").strip()
    if len(text) <= n:
        return text
    return text[: n - 1] + "…"


def _preview_lines(path: Path, *, max_lines: int = 3) -> list[str]:
    if not path.is_file():
        return []
    lines: list[str] = []
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    for line in raw.splitlines():
        text = line.strip()
        if not text:
            continue
        if path.suffix == ".jsonl":
            try:
                row = json.loads(text)
            except json.JSONDecodeError:
                lines.append(_clip(text))
            else:
                preview = (
                    row.get("generated_text")
                    or row.get("generated_text_en")
                    or row.get("user_prompt")
                    or row.get("persona_summary")
                    or row.get("first_language")
                    or text
                )
                lines.append(_clip(str(preview)))
        else:
            lines.append(_clip(text, 200))
        if len(lines) >= max_lines:
            break
    return lines


def list_runs() -> list[dict[str, str]]:
    """Past runs with run_results.json, newest first."""
    if not RUNS_ROOT.is_dir():
        return []
    items: list[tuple[str, dict[str, str]]] = []
    for child in RUNS_ROOT.iterdir():
        if not child.is_dir() or child.name == "latest":
            continue
        results_path = child / "run_results.json"
        if not results_path.is_file():
            continue
        data = _read_json(results_path)
        items.append(
            (
                child.name,
                {
                    "run_id": child.name,
                    "status": str(data.get("status") or "unknown"),
                    "path": str(child),
                },
            )
        )
    items.sort(key=lambda x: x[0], reverse=True)
    return [row for _, row in items]


def load_languages() -> list[dict[str, str]]:
    from main.pipeline.config_io import REPO_ROOT, load_yaml

    data = load_yaml(REPO_ROOT / "configs" / "synthetic-data" / "languages.yaml")
    out: list[dict[str, str]] = []
    for row in data.get("languages") or []:
        if not isinstance(row, dict):
            continue
        code = row.get("code")
        if not code:
            continue
        out.append(
            {
                "code": str(code),
                "name": str(row.get("name") or code),
                "script": str(row.get("script") or ""),
            }
        )
    return out


def _stage_index(results: dict[str, Any]) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for stage in results.get("stages") or []:
        if isinstance(stage, dict) and stage.get("stage"):
            out[str(stage["stage"])] = stage
    return out


def _prior_nodes_ok(node_id: str, stage_by_label: dict[str, dict[str, Any]]) -> bool:
    for other in NODE_ORDER:
        if other == node_id:
            return True
        labels = NODE_STAGES[other]
        if not all(
            str(stage_by_label.get(lab, {}).get("status") or "") == "ok"
            for lab in labels
        ):
            return False
    return True


def _node_status(
    node_id: str,
    stage_by_label: dict[str, dict[str, Any]],
    run_status: str,
) -> str:
    labels = NODE_STAGES[node_id]
    statuses = [str(stage_by_label.get(lab, {}).get("status") or "") for lab in labels]
    if any(s == "failed" for s in statuses):
        return "failed"
    if all(s == "ok" for s in statuses):
        return "ok"
    if any(s == "ok" for s in statuses):
        return "running"
    if run_status == "running" and _prior_nodes_ok(node_id, stage_by_label):
        return "running"
    return "idle"


def _repairing_nodes(
    root: Path,
    stage_by_label: dict[str, dict[str, Any]],
    *,
    run_status: str,
    active_node: str | None,
) -> set[str]:
    """Detect in-flight repair activity for the dashed arc (not historical soft-fails)."""
    if run_status != "running":
        return set()
    if active_node not in {"generate", "translate", "judge", "audit"}:
        return set()

    repairing: set[str] = set()

    if active_node == "generate":
        gen = _read_json(root / "s4_generation" / "audit.json")
        if int(gen.get("generation_repaired_count") or 0) > 0:
            repairing.add("generate")
        if (root / "s4_generation" / "soft_failures.jsonl").is_file() and _count_jsonl(
            root / "s4_generation" / "soft_failures.jsonl"
        ):
            repairing.add("generate")

    if active_node == "translate":
        tr = _read_json(root / "s4b_translation" / "audit.json")
        if int(tr.get("generator_repaired_count") or 0) > 0:
            repairing.add("translate")
        if (root / "s4b_translation" / "soft_failures.jsonl").is_file() and _count_jsonl(
            root / "s4b_translation" / "soft_failures.jsonl"
        ):
            repairing.add("translate")

    if active_node == "judge":
        judge = _read_json(root / "s5_linguistic_judge" / "audit.json")
        for fail in judge.get("failures") or []:
            if isinstance(fail, dict) and int(fail.get("judge_repair_attempts") or 0) > 0:
                repairing.update({"judge", "generate", "translate"})
                break
        # Checkpoint growing during judge = rows being repaired/re-judged
        cp = _checkpoint_progress(root, "judge")
        if cp.get("rows_done", 0) > 0 and not stage_by_label.get(
            "s5_linguistic_judge", {}
        ).get("status") == "ok":
            repairing.add("judge")

    if active_node == "audit":
        aud = _read_json(root / "s6_deterministic_auditor" / "audit.json")
        for fail in aud.get("failures") or []:
            if isinstance(fail, dict) and int(fail.get("auditor_repair_attempts") or 0) > 0:
                repairing.update({"audit", "generate", "translate", "judge"})
                break

    return repairing


def _historical_repair_signals(root: Path) -> set[str]:
    """Soft-fail / repair signals for replay animation (not live arc)."""
    repairing: set[str] = set()
    gen = _read_json(root / "s4_generation" / "audit.json")
    if int(gen.get("generation_repaired_count") or 0) > 0 or int(
        gen.get("soft_fail_count") or 0
    ) > 0:
        repairing.add("generate")
    tr = _read_json(root / "s4b_translation" / "audit.json")
    if int(tr.get("generator_repaired_count") or 0) > 0 or int(
        tr.get("soft_fail_count") or 0
    ) > 0:
        repairing.add("translate")
    judge = _read_json(root / "s5_linguistic_judge" / "audit.json")
    for fail in judge.get("failures") or []:
        if isinstance(fail, dict) and int(fail.get("judge_repair_attempts") or 0) > 0:
            repairing.update({"judge", "generate", "translate"})
            break
    return repairing


def _run_failure_detail(results: dict[str, Any]) -> dict[str, Any] | None:
    for stage in reversed(results.get("stages") or []):
        if not isinstance(stage, dict) or stage.get("status") != "failed":
            continue
        label = str(stage.get("stage") or "")
        node = STAGE_TO_NODE.get(label, label)
        return {
            "stage_label": label,
            "node_id": node,
            "error": str(stage.get("error") or "stage failed"),
        }
    return None


def build_summary(root: Path) -> dict[str, Any]:
    gen = _read_json(root / "s4_generation" / "audit.json")
    tr = _read_json(root / "s4b_translation" / "audit.json")
    judged = _read_json(root / "s5_linguistic_judge" / "audit.json")
    audited = _read_json(root / "s6_deterministic_auditor" / "audit.json")
    curated_n = _count_jsonl(root / "s7_s8_curation" / "curated.jsonl")
    entries = collect_failure_entries(root)

    recovered = int(gen.get("generation_repaired_count") or 0) + int(
        tr.get("generator_repaired_count") or 0
    )
    soft_fails = (
        len(entries["generation_soft_failures"])
        + len(entries["translation_soft_failures"])
    )
    hard_fails = len(entries["stage_hard_failures"])
    judge_fails = len(entries["judge_failures"])
    auditor_fails = len(entries["auditor_failures"])

    return {
        "generated": int(gen.get("rows_generated") or 0),
        "translated": int(tr.get("rows_translated") or tr.get("rows_out") or 0),
        "judge_passed": int(
            round(
                float(judged.get("pass_rate") or 0)
                * float(judged.get("rows_judged") or 0)
            )
        )
        if judged
        else 0,
        "auditor_passed": int(audited.get("rows_passed") or 0),
        "curated": curated_n,
        "soft_fails": soft_fails,
        "hard_fails": hard_fails,
        "judge_fails": judge_fails,
        "auditor_fails": auditor_fails,
        "recovered": recovered,
        "s4_entity_coverage": gen.get("entity_coverage_complete_rate"),
        "s5_pass_rate": judged.get("pass_rate"),
        "s6_pass_rate": audited.get("pass_rate"),
    }


def _checkpoint_progress(root: Path, node_id: str) -> dict[str, Any]:
    """Row-level progress from checkpoint.jsonl while a stage is running."""
    folder_map = {
        "generate": "s4_generation",
        "translate": "s4b_translation",
        "judge": "s5_linguistic_judge",
        "audit": "s6_deterministic_auditor",
        "seed": "s2b_persona_summary",
    }
    folder = folder_map.get(node_id)
    if not folder:
        return {}
    stage_dir = root / folder
    checkpoint = stage_dir / "checkpoint.jsonl"
    if not checkpoint.is_file():
        return {}

    done = _count_jsonl(checkpoint)
    total = 0
    if node_id == "generate":
        total = _count_jsonl(root / "s3_prompts" / "prompts.jsonl")
    elif node_id == "translate":
        total = _count_jsonl(root / "s4_generation" / "documents.jsonl")
    elif node_id == "judge":
        total = _count_jsonl(root / "s4b_translation" / "documents.jsonl")
    elif node_id == "audit":
        total = _count_jsonl(root / "s5_linguistic_judge" / "passed.jsonl")
    elif node_id == "seed":
        total = _count_jsonl(root / "s2_taxonomy" / "assignments.jsonl")

    out: dict[str, Any] = {"rows_done": done}
    if total > 0:
        out["rows_total"] = total
        out["pct"] = round(min(1.0, done / total) * 100, 1)
    return out


def _repair_path(repairing: set[str]) -> list[str]:
    """Visual repair loop: judge/audit fail → regenerate → retranslate → re-judge."""
    if not repairing:
        return []
    if "audit" in repairing:
        return ["audit", "generate", "translate", "judge"]
    if "judge" in repairing:
        return ["judge", "generate", "translate", "judge"]
    if "translate" in repairing:
        return ["translate", "generate", "translate"]
    if "generate" in repairing:
        return ["generate", "generate"]
    return sorted(repairing)


def _activity_message(
    root: Path,
    node_id: str,
    status: str,
    counts: dict[str, Any],
    *,
    repairing: bool,
) -> str:
    cp = _checkpoint_progress(root, node_id)
    if cp.get("rows_total"):
        return (
            f"{node_id}: {cp.get('rows_done', 0)}/{cp['rows_total']} rows"
            f" ({cp.get('pct', 0)}%)"
        )
    if repairing and node_id in {"generate", "translate", "judge", "audit"}:
        return f"{node_id}: repair loop — regenerating / retranslating failed docs"
    if status == "running":
        return f"{node_id}: running…"
    if status == "ok":
        parts = [f"{k}={v}" for k, v in counts.items() if v not in (None, "", 0)]
        return f"{node_id}: done" + (f" ({', '.join(parts[:3])})" if parts else "")
    if status == "failed":
        return f"{node_id}: failed"
    return f"{node_id}: {status}"


def _node_counts(root: Path, node_id: str) -> dict[str, Any]:
    if node_id == "seed":
        return {
            "personas": _count_jsonl(root / "s1_persona_sampling" / "personas.jsonl"),
            "prompts": _count_jsonl(root / "s3_prompts" / "prompts.jsonl"),
        }
    if node_id == "generate":
        audit = _read_json(root / "s4_generation" / "audit.json")
        return {
            "generated": int(audit.get("rows_generated") or 0),
            "repaired": int(audit.get("generation_repaired_count") or 0),
            "soft_fails": int(audit.get("soft_fail_count") or 0),
            "entity_coverage": audit.get("entity_coverage_complete_rate"),
        }
    if node_id == "translate":
        audit = _read_json(root / "s4b_translation" / "audit.json")
        return {
            "translated": int(audit.get("rows_translated") or audit.get("rows_out") or 0),
            "repaired": int(audit.get("generator_repaired_count") or 0),
            "soft_fails": int(audit.get("soft_fail_count") or 0),
            "script_fails": int(audit.get("script_fail_count") or 0),
        }
    if node_id == "judge":
        audit = _read_json(root / "s5_linguistic_judge" / "audit.json")
        return {
            "judged": int(audit.get("rows_judged") or 0),
            "pass_rate": audit.get("pass_rate"),
            "failed": _count_jsonl(root / "s5_linguistic_judge" / "failed.jsonl"),
        }
    if node_id == "audit":
        audit = _read_json(root / "s6_deterministic_auditor" / "audit.json")
        return {
            "audited": int(audit.get("rows_audited") or 0),
            "passed": int(audit.get("rows_passed") or 0),
            "failed": int(audit.get("rows_failed") or 0),
            "pass_rate": audit.get("pass_rate"),
        }
    if node_id == "curate":
        return {"curated": _count_jsonl(root / "s7_s8_curation" / "curated.jsonl")}
    if node_id == "export":
        return {
            "gliner": _count_jsonl(root / "s9_gliner_format" / "gliner_docs.jsonl"),
            "train": _count_jsonl(root / "s10_split" / "train.jsonl"),
            "eval": _count_jsonl(root / "s10_split" / "eval.jsonl"),
        }
    return {}


def _inspector_for_node(root: Path, node_id: str, status: str) -> dict[str, Any]:
    folder_candidates = {
        "seed": [
            root / "s3_prompts" / "prompts.jsonl",
            root / "s1_persona_sampling" / "personas.jsonl",
            root / "s3_prompts" / "audit.md",
        ],
        "generate": [
            root / "s4_generation" / "documents.jsonl",
            root / "s4_generation" / "audit.md",
        ],
        "translate": [
            root / "s4b_translation" / "documents.jsonl",
            root / "s4b_translation" / "audit.md",
        ],
        "judge": [
            root / "s5_linguistic_judge" / "judged.jsonl",
            root / "s5_linguistic_judge" / "failed.jsonl",
            root / "s5_linguistic_judge" / "audit.md",
        ],
        "audit": [
            root / "s6_deterministic_auditor" / "audited.jsonl",
            root / "s6_deterministic_auditor" / "failed.jsonl",
            root / "s6_deterministic_auditor" / "audit.md",
        ],
        "curate": [
            root / "s7_s8_curation" / "curated.jsonl",
            root / "s7_s8_curation" / "audit.md",
        ],
        "export": [
            root / "s10_split" / "train.jsonl",
            root / "s9_gliner_format" / "gliner_docs.jsonl",
            root / "s10_split" / "audit.md",
        ],
    }
    sample: list[str] = []
    for path in folder_candidates.get(node_id, []):
        sample = _preview_lines(path)
        if sample:
            break

    fail_reason = None
    if node_id == "generate":
        soft = root / "s4_generation" / "soft_failures.jsonl"
        if soft.is_file() and soft.stat().st_size:
            rows = soft.read_text(encoding="utf-8").splitlines()
            if rows:
                try:
                    fail_reason = _clip(str(json.loads(rows[0]).get("reasons")))
                except json.JSONDecodeError:
                    fail_reason = _clip(rows[0])
    elif node_id == "judge":
        failed = root / "s5_linguistic_judge" / "failed.jsonl"
        if failed.is_file() and failed.stat().st_size:
            rows = failed.read_text(encoding="utf-8").splitlines()
            if rows:
                try:
                    row = json.loads(rows[0])
                    fail_reason = _clip(
                        f"{row.get('judge_flags')}: {row.get('judge_rationale') or row.get('judge_reasoning')}"
                    )
                except json.JSONDecodeError:
                    fail_reason = _clip(rows[0])
    elif node_id == "audit":
        failed = root / "s6_deterministic_auditor" / "failed.jsonl"
        if not failed.is_file():
            failed = root / "s6_deterministic_auditor" / "failures.jsonl"
        if failed.is_file() and failed.stat().st_size:
            rows = failed.read_text(encoding="utf-8").splitlines()
            if rows:
                try:
                    row = json.loads(rows[0])
                    fail_reason = _clip(str(row.get("auditor_errors")))
                except json.JSONDecodeError:
                    fail_reason = _clip(rows[0])

    counts = _node_counts(root, node_id)
    counts.update(_checkpoint_progress(root, node_id))
    return {
        "node_id": node_id,
        "status": status,
        "model": NODE_MODELS.get(node_id, ""),
        "engine": NODE_MODELS.get(node_id, ""),
        "counts": counts,
        "sample": sample,
        "preview": "\n".join(sample) if sample else None,
        "fail_reason": fail_reason,
    }


def build_snapshot(run_id: str, *, active_node: str | None = None) -> dict[str, Any]:
    root = run_dir(run_id)
    if not root.is_dir():
        raise FileNotFoundError(f"Run not found: {run_id}")

    results = _read_json(root / "run_results.json")
    run_status = str(results.get("status") or "unknown")
    stage_by_label = _stage_index(results)

    stages: list[dict[str, Any]] = []
    active = active_node
    for node_id in NODE_ORDER:
        status = _node_status(node_id, stage_by_label, run_status)
        stages.append(
            {
                "id": node_id,
                "status": status,
                "model": NODE_MODELS.get(node_id, ""),
                "counts": _node_counts(root, node_id),
                "pipeline_stages": list(NODE_STAGES[node_id]),
            }
        )
        if active is None and status in {"running", "repairing"}:
            active = node_id

    if active is None:
        for node in reversed(stages):
            if node["status"] == "ok":
                active = node["id"]
                break
        active = active or "seed"

    repairing = _repairing_nodes(
        root, stage_by_label, run_status=run_status, active_node=active
    )
    if repairing:
        for node in stages:
            if node["id"] in repairing and node["status"] == "running":
                node["status"] = "repairing"

    summary = build_summary(root)
    failure = _run_failure_detail(results) if run_status == "failed" else None
    active_status = next((s["status"] for s in stages if s["id"] == active), "idle")
    active_counts = next((s["counts"] for s in stages if s["id"] == active), {})
    repair_path = _repair_path(repairing)
    return {
        "run_id": run_id,
        "status": run_status,
        "path": str(root),
        "models": dict(MODELS_BLURB),
        "stages": stages,
        "active_stage": active,
        "repair_active": bool(repairing),
        "repair_nodes": sorted(repairing),
        "repair_path": repair_path,
        "activity": _activity_message(
            root,
            active,
            active_status,
            active_counts or {},
            repairing=bool(repairing),
        ),
        "summary": summary,
        "inspector": _inspector_for_node(root, active, active_status),
        "raw_stages": results.get("stages") or [],
        "failure": failure,
    }


def stage_label_to_node(stage_label: str) -> str | None:
    return STAGE_TO_NODE.get(stage_label)


def folder_for_stage(stage_label: str) -> str | None:
    return STAGE_FOLDER.get(stage_label)
