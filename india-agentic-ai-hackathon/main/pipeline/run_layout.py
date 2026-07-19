"""Timestamped run layout for pipeline stages.

Every pipeline invocation writes under::

    data/generated/runs/<YYYYMMDDTHHMMSS>/
      pipeline.resolved.yaml
      manifest.json
      s1_persona_sampling/
      s2_taxonomy/
      ...
      s9_gliner_format/

Stages never overwrite a previous run; a new timestamp folder is created.
"""

from __future__ import annotations

import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from main.pipeline.config_io import REPO_ROOT, load_yaml

RUNS_ROOT = REPO_ROOT / "data" / "generated" / "runs"

# (config_block, folder_name, primary_output_filename)
STAGE_SPECS: tuple[tuple[str, str, str], ...] = (
    ("persona_sampling", "s1_persona_sampling", "personas.jsonl"),
    ("taxonomy", "s2_taxonomy", "assignments.jsonl"),
    ("persona_summary", "s2b_persona_summary", "assignments_summarized.jsonl"),
    ("prompt_construction", "s3_prompts", "prompts.jsonl"),
    ("generation", "s4_generation", "documents.jsonl"),
    ("translation", "s4b_translation", "documents.jsonl"),
    ("linguistic_judge", "s5_linguistic_judge", "judged.jsonl"),
    ("deterministic_auditor", "s6_deterministic_auditor", "audited.jsonl"),
    ("curation", "s7_s8_curation", "curated.jsonl"),
    ("gliner_format", "s9_gliner_format", "gliner_docs.jsonl"),
)


def new_run_id() -> str:
    return datetime.now().strftime("%Y%m%dT%H%M%S")


def run_dir(run_id: str) -> Path:
    return RUNS_ROOT / run_id


def stage_dir(run_id: str, folder_name: str) -> Path:
    return run_dir(run_id) / folder_name


def materialize_run_config(
    base_config_path: Path,
    *,
    run_id: str | None = None,
) -> tuple[str, Path, dict[str, Any]]:
    """Clone base YAML with all stage I/O paths under ``runs/<run_id>/``.

    Returns ``(run_id, resolved_config_path, resolved_root_dict)``.
    """
    run_id = run_id or new_run_id()
    root = deepcopy(load_yaml(base_config_path))
    base = run_dir(run_id)
    base.mkdir(parents=True, exist_ok=True)

    # Wire sequential I/O under the run folder.
    root.setdefault("persona_sampling", {})
    root["persona_sampling"]["output_dir"] = str(
        (base / "s1_persona_sampling").relative_to(REPO_ROOT)
    )

    root.setdefault("taxonomy", {})
    root["taxonomy"]["input_jsonl"] = str(
        (base / "s1_persona_sampling" / "personas.jsonl").relative_to(REPO_ROOT)
    )
    root["taxonomy"]["output_dir"] = str((base / "s2_taxonomy").relative_to(REPO_ROOT))

    root.setdefault("persona_summary", {})
    root["persona_summary"]["input_jsonl"] = str(
        (base / "s2_taxonomy" / "assignments.jsonl").relative_to(REPO_ROOT)
    )
    root["persona_summary"]["output_dir"] = str(
        (base / "s2b_persona_summary").relative_to(REPO_ROOT)
    )

    root.setdefault("prompt_construction", {})
    root["prompt_construction"]["input_jsonl"] = str(
        (base / "s2b_persona_summary" / "assignments_summarized.jsonl").relative_to(
            REPO_ROOT
        )
    )
    root["prompt_construction"]["output_dir"] = str(
        (base / "s3_prompts").relative_to(REPO_ROOT)
    )

    root.setdefault("generation", {})
    root["generation"]["input_jsonl"] = str(
        (base / "s3_prompts" / "prompts.jsonl").relative_to(REPO_ROOT)
    )
    root["generation"]["output_dir"] = str(
        (base / "s4_generation").relative_to(REPO_ROOT)
    )

    root.setdefault("translation", {})
    root["translation"]["input_jsonl"] = str(
        (base / "s4_generation" / "documents.jsonl").relative_to(REPO_ROOT)
    )
    root["translation"]["output_dir"] = str(
        (base / "s4b_translation").relative_to(REPO_ROOT)
    )

    root.setdefault("linguistic_judge", {})
    root["linguistic_judge"]["input_jsonl"] = str(
        (base / "s4b_translation" / "documents.jsonl").relative_to(REPO_ROOT)
    )
    root["linguistic_judge"]["output_dir"] = str(
        (base / "s5_linguistic_judge").relative_to(REPO_ROOT)
    )

    root.setdefault("deterministic_auditor", {})
    root["deterministic_auditor"]["input_jsonl"] = str(
        (base / "s5_linguistic_judge" / "passed.jsonl").relative_to(REPO_ROOT)
    )
    root["deterministic_auditor"]["output_dir"] = str(
        (base / "s6_deterministic_auditor").relative_to(REPO_ROOT)
    )

    root.setdefault("curation", {})
    root["curation"]["input_jsonl"] = str(
        (base / "s6_deterministic_auditor" / "passed.jsonl").relative_to(REPO_ROOT)
    )
    root["curation"]["output_dir"] = str(
        (base / "s7_s8_curation").relative_to(REPO_ROOT)
    )
    dedup = root["curation"].setdefault("dedup", {})
    dedup["curator_work_dir"] = str(
        (base / "artifacts" / "nemo_curator_dedup").relative_to(REPO_ROOT)
    )

    root.setdefault("gliner_format", {})
    root["gliner_format"]["input_jsonl"] = str(
        (base / "s7_s8_curation" / "curated.jsonl").relative_to(REPO_ROOT)
    )
    root["gliner_format"]["output_dir"] = str(
        (base / "s9_gliner_format").relative_to(REPO_ROOT)
    )

    if "data_designer" in root and isinstance(root["data_designer"], dict):
        root["data_designer"]["seed_path"] = str(
            (base / "s3_prompts" / "prompts.parquet").relative_to(REPO_ROOT)
        )

    root["run"] = {
        "run_id": run_id,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "base_config": str(base_config_path),
        "runs_root": str(RUNS_ROOT.relative_to(REPO_ROOT)),
    }

    resolved_path = base / "pipeline.resolved.yaml"
    resolved_path.write_text(
        yaml.safe_dump(root, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    manifest = {
        "run_id": run_id,
        "created_utc": root["run"]["created_utc"],
        "base_config": str(base_config_path),
        "resolved_config": str(resolved_path.relative_to(REPO_ROOT)),
        "stages": [
            {
                "block": block,
                "folder": folder,
                "primary_output": primary,
                "path": str((base / folder).relative_to(REPO_ROOT)),
            }
            for block, folder, primary in STAGE_SPECS
        ],
    }
    (base / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    # Point data/generated/runs/latest → this run (replace symlink).
    latest = RUNS_ROOT / "latest"
    if latest.is_symlink() or latest.exists():
        latest.unlink()
    latest.symlink_to(base.name)

    return run_id, resolved_path, root


def write_stage_summary(run_id: str, stage_folder: str, summary: dict[str, Any]) -> Path:
    path = stage_dir(run_id, stage_folder) / "stage_summary.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    return path
