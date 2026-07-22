"""Orchestrate a timestamped pipeline run (smoke or full).

Creates ``data/generated/runs/<timestamp>/`` with per-stage folders, writes a
resolved config, then executes stages in order. Each stage's outputs stay under
that run folder so every run is inspectable.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Sequence

from main.pipeline.config_io import REPO_ROOT
from main.pipeline.failures_report import write_failures_report
from main.pipeline.run_layout import STAGE_SPECS, materialize_run_config, run_dir

# (label, folder, callable importing lazily inside to keep startup light)
StageFn = Callable[[Path], dict[str, Path]]


def _load_stage_runners() -> list[tuple[str, str, StageFn]]:
    from main.designers import (
        deterministic_auditor,
        generator,
        linguistic_judge,
        persona_sampler,
        persona_summarizer,
        prompt_builder,
        taxonomy,
        translator,
    )
    from main.pipeline import curate, gliner_format, split

    return [
        ("s1_persona_sampling", "s1_persona_sampling", persona_sampler.run),
        ("s2_taxonomy", "s2_taxonomy", taxonomy.run),
        ("s2b_persona_summary", "s2b_persona_summary", persona_summarizer.run),
        ("s3_prompt_construction", "s3_prompts", prompt_builder.run),
        ("s4_generation", "s4_generation", generator.run),
        ("s4b_translation", "s4b_translation", translator.run),
        ("s5_linguistic_judge", "s5_linguistic_judge", linguistic_judge.run),
        ("s6_deterministic_auditor", "s6_deterministic_auditor", deterministic_auditor.run),
        ("s7_s8_curation", "s7_s8_curation", curate.run),
        ("s9_gliner_format", "s9_gliner_format", gliner_format.run),
        ("s10_split", "s10_split", split.run),
    ]


def _preview_file(folder: Path) -> Path | None:
    for name in (
        "audit.md",
        "audit.json",
        "personas.jsonl",
        "assignments.jsonl",
        "prompts.jsonl",
        "documents.jsonl",
        "judged.jsonl",
        "passed.jsonl",
        "audited.jsonl",
        "curated.jsonl",
        "gliner_docs.jsonl",
        "train.jsonl",
        "eval.jsonl",
    ):
        candidate = folder / name
        if candidate.is_file():
            return candidate
    return None


def _cancel_requested(root: Path) -> bool:
    return (root / ".cancel").is_file()


def _write_run_results(
    root: Path,
    *,
    run_id: str,
    status: str,
    stages: list[dict[str, object]],
    base_config: Path | None = None,
    resolved_config: Path | None = None,
) -> None:
    payload: dict[str, object] = {
        "run_id": run_id,
        "status": status,
        "stages": stages,
        "stage_specs": [
            {"block": b, "folder": f, "primary": p} for b, f, p in STAGE_SPECS
        ],
    }
    if base_config is not None:
        payload["base_config"] = str(base_config)
    if resolved_config is not None:
        payload["resolved_config"] = str(resolved_config)
    (root / "run_results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def run_pipeline(
    *,
    base_config: Path,
    run_id: str | None = None,
    stop_after: str | None = None,
    from_stage: str | None = None,
) -> int:
    if run_id and (run_dir(run_id) / "pipeline.resolved.yaml").is_file():
        resolved_config = run_dir(run_id) / "pipeline.resolved.yaml"
        print(f"[run] resuming run_id={run_id}")
    else:
        run_id, resolved_config, _root = materialize_run_config(
            base_config, run_id=run_id
        )
    root = run_dir(run_id)
    print(f"[run] run_id={run_id}")
    print(f"[run] folder={root}")
    print(f"[run] config={resolved_config}")

    results: list[dict[str, object]] = []
    runners = _load_stage_runners()
    started_resume = from_stage is None

    # Seed progress file so the demo UI can attach immediately.
    _write_run_results(
        root,
        run_id=run_id,
        status="running",
        stages=results,
        base_config=base_config,
        resolved_config=resolved_config,
    )

    for label, folder_name, runner in runners:
        if _cancel_requested(root):
            print("[run] cancelled by user", file=sys.stderr)
            _write_run_results(
                root,
                run_id=run_id,
                status="cancelled",
                stages=results,
                base_config=base_config,
                resolved_config=resolved_config,
            )
            return 2

        if not started_resume:
            if from_stage in {label, folder_name}:
                started_resume = True
            else:
                print(f"--- skip {label} (before --from-stage) ---")
                continue

        print(f"\n=== {label} ===")
        started_dt = datetime.now(timezone.utc)
        started = started_dt.isoformat()
        try:
            paths = runner(resolved_config)
        except Exception as exc:  # noqa: BLE001 — surface stage failure clearly
            finished_dt = datetime.now(timezone.utc)
            elapsed_s = (finished_dt - started_dt).total_seconds()
            print(
                f"[{label}] FAILED after {elapsed_s:.1f}s: {exc}",
                file=sys.stderr,
            )
            results.append(
                {
                    "stage": label,
                    "folder": folder_name,
                    "status": "failed",
                    "error": str(exc),
                    "started_utc": started,
                    "finished_utc": finished_dt.isoformat(),
                    "elapsed_s": round(elapsed_s, 2),
                }
            )
            _write_run_results(
                root,
                run_id=run_id,
                status="failed",
                stages=results,
                base_config=base_config,
                resolved_config=resolved_config,
            )
            try:
                failures_path = write_failures_report(root)
                print(f"[run] failures audit → {failures_path}")
            except Exception as report_exc:  # noqa: BLE001
                print(f"[run] failures.md write failed: {report_exc}", file=sys.stderr)
            return 1

        finished_dt = datetime.now(timezone.utc)
        elapsed_s = (finished_dt - started_dt).total_seconds()
        stage_folder = root / folder_name
        preview = _preview_file(stage_folder)
        entry = {
            "stage": label,
            "folder": folder_name,
            "status": "ok",
            "started_utc": started,
            "finished_utc": finished_dt.isoformat(),
            "elapsed_s": round(elapsed_s, 2),
            "outputs": {k: str(v) for k, v in paths.items()},
            "preview": str(preview) if preview else None,
        }
        results.append(entry)
        # Incremental write so the demo UI can light stages as they finish.
        _write_run_results(
            root,
            run_id=run_id,
            status="running",
            stages=results,
            base_config=base_config,
            resolved_config=resolved_config,
        )
        mins, secs = divmod(int(elapsed_s), 60)
        print(f"[{label}] OK in {mins}m{secs:02d}s ({elapsed_s:.1f}s) → {stage_folder}")
        for key, path in paths.items():
            print(f"  {key}: {path}")

        if stop_after and (stop_after == label or stop_after == folder_name):
            print(f"[run] stop_after={stop_after}")
            break

    total_s = sum(float(s.get("elapsed_s") or 0) for s in results)
    tm, ts = divmod(int(total_s), 60)
    print(f"\n[run] stage timings (sum={tm}m{ts:02d}s):")
    for s in results:
        es = float(s.get("elapsed_s") or 0)
        m, sec = divmod(int(es), 60)
        print(f"  {s.get('stage')}: {m}m{sec:02d}s ({es:.1f}s) [{s.get('status')}]")

    _write_run_results(
        root,
        run_id=run_id,
        status="ok",
        stages=results,
        base_config=base_config,
        resolved_config=resolved_config,
    )
    print(f"\n[run] complete → {root}")
    print(f"[run] latest symlink → {root.parent / 'latest'}")
    try:
        failures_path = write_failures_report(root)
        print(f"[run] failures audit → {failures_path}")
    except Exception as report_exc:  # noqa: BLE001
        print(f"[run] failures.md write failed: {report_exc}", file=sys.stderr)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Timestamped pipeline orchestrator")
    parser.add_argument(
        "--config",
        type=Path,
        default=REPO_ROOT / "configs" / "synthetic-data" / "pipeline.smoke.yaml",
        help="Base pipeline YAML (paths rewritten into runs/<timestamp>/)",
    )
    parser.add_argument("--run-id", type=str, default=None)
    parser.add_argument(
        "--from-stage",
        type=str,
        default=None,
        help="Resume at this stage label/folder (e.g. s4_generation)",
    )
    parser.add_argument(
        "--stop-after",
        type=str,
        default=None,
        help="Optional stage label/folder to stop after (e.g. s3_prompts)",
    )
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    return run_pipeline(
        base_config=config_path.resolve(),
        run_id=args.run_id,
        stop_after=args.stop_after,
        from_stage=args.from_stage,
    )


if __name__ == "__main__":
    raise SystemExit(main())
