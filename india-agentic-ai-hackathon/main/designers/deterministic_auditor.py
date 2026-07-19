"""Stage 6 — Deterministic annotation & format auditor."""

from __future__ import annotations

import argparse
import math
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.entities.inline import extract_inline_spans
from main.entities.schema import load_entity_specs
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.io import read_jsonl, write_json, write_jsonl, write_parquet
from main.validators.checksums import validate_entity_value
from main.validators.dics import compute_dics
from main.validators.phi_residue import scan_phi_residue
from main.validators.script_purity import evaluate_script_purity
from main.validators.spans import validate_annotation_spans

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

_MAX_OCCURRENCES_PER_TYPE = 2
_MAX_TAG_MULTIPLIER = 2
_STUFFING_EXEMPT_TYPES = frozenset({"PATIENT_NAME", "DOCTOR_NAME"})


@dataclass(frozen=True)
class AuditorSettings:
    input_jsonl: Path
    entities_config: Path
    entity_profiles_config: Path
    output_dir: Path
    require_judge_pass: bool
    max_docs: int | None
    min_dics: float
    max_boundary_corruption_rate: float
    require_all_profile_entities: bool


class AuditorError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> AuditorSettings:
    root = load_yaml(pipeline_config)
    block = root.get("deterministic_auditor")
    if not isinstance(block, dict):
        raise ValueError(f"'deterministic_auditor' mapping required in {pipeline_config}")

    required = (
        "input_jsonl",
        "entities_config",
        "entity_profiles_config",
        "output_dir",
        "min_dics",
        "max_boundary_corruption_rate",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing deterministic_auditor keys {missing}")

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    return AuditorSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        entities_config=resolve_repo_path(str(block["entities_config"])),
        entity_profiles_config=resolve_repo_path(str(block["entity_profiles_config"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        require_judge_pass=bool(block.get("require_judge_pass", True)),
        max_docs=max_docs,
        min_dics=float(block["min_dics"]),
        max_boundary_corruption_rate=float(block["max_boundary_corruption_rate"]),
        require_all_profile_entities=bool(
            block.get("require_all_profile_entities", True)
        ),
    )


def load_profiles(path: Path) -> dict[str, dict[str, tuple[str, ...]]]:
    root = load_yaml(path)
    raw = root.get("profiles")
    if not isinstance(raw, dict) or not raw:
        raise ValueError(f"'profiles' mapping required in {path}")
    profiles: dict[str, dict[str, tuple[str, ...]]] = {}
    for doc_type_id, entry in raw.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid profile for {doc_type_id!r}")
        required = entry.get("required")
        optional = entry.get("optional", [])
        if not isinstance(required, list) or not required:
            raise ValueError(f"Profile {doc_type_id!r} needs non-empty required")
        if not isinstance(optional, list):
            raise ValueError(f"Profile {doc_type_id!r} optional must be a list")
        profiles[str(doc_type_id)] = {
            "required": tuple(str(item) for item in required),
            "optional": tuple(str(item) for item in optional),
        }
    return profiles


def _label_entropy(entity_types: Sequence[str]) -> float:
    if not entity_types:
        return 0.0
    counts = Counter(entity_types)
    total = len(entity_types)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log(p, 2)
    return entropy


def audit_document(
    row: Mapping[str, Any],
    *,
    known_entities: Mapping[str, Any],
    profiles: Mapping[str, Mapping[str, tuple[str, ...]]],
    settings: AuditorSettings,
) -> dict[str, Any]:
    text = str(row.get("generated_text", ""))
    if not text.strip():
        return {
            "auditor_pass": False,
            "auditor_errors": ["empty_generated_text"],
            "dics": 0.0,
            "entity_coverage_rate": 0.0,
            "label_entropy": 0.0,
            "boundary_corruption_rate": 1.0,
            "phi_residue_count": 0,
        }

    spans = extract_inline_spans(text)
    span_report = validate_annotation_spans(text)
    dics_report = compute_dics(text)
    residue = scan_phi_residue(text)

    errors: list[str] = []
    if settings.require_judge_pass:
        verdict = row.get("judge_verdict")
        if verdict is None:
            errors.append("missing_judge_verdict")
        elif verdict != "pass":
            errors.append("judge_failed")

    doc_type_id = str(row.get("doc_type_id", ""))
    if doc_type_id not in profiles:
        errors.append(f"missing_entity_profile:{doc_type_id}")
        required: tuple[str, ...] = ()
        optional: tuple[str, ...] = ()
    else:
        required = profiles[doc_type_id]["required"]
        optional = profiles[doc_type_id]["optional"]

    expected = (
        tuple(dict.fromkeys((*required, *optional)))
        if settings.require_all_profile_entities
        else required
    )

    present_types = {span.entity_type for span in spans}
    unknown_types = sorted(present_types - set(known_entities))
    if unknown_types:
        errors.append(f"unknown_entity_types:{','.join(unknown_types)}")

    missing_required = [entity_id for entity_id in expected if entity_id not in present_types]
    if missing_required:
        errors.append(f"missing_required:{','.join(missing_required)}")

    type_counts = Counter(span.entity_type for span in spans)
    stuffed = [
        entity_id
        for entity_id, count in type_counts.items()
        if entity_id not in _STUFFING_EXEMPT_TYPES
        and count > _MAX_OCCURRENCES_PER_TYPE
    ]
    countable_tags = sum(
        count
        for entity_id, count in type_counts.items()
        if entity_id not in _STUFFING_EXEMPT_TYPES
    )
    tag_cap = max(len(expected), 1) * _MAX_TAG_MULTIPLIER
    if countable_tags > tag_cap:
        errors.append(f"entity_stuffing_total_tags:{countable_tags}>{tag_cap}")
    if stuffed:
        errors.append(f"entity_stuffing:{','.join(sorted(stuffed))}")

    # Upstream soft-fails must never be silent — surface them as auditor errors.
    if row.get("generation_soft_fail"):
        reasons = row.get("generation_soft_fail_reasons") or []
        errors.append(
            "upstream_generation_soft_fail:"
            + (";".join(str(r) for r in reasons) if reasons else "true")
        )
    if row.get("translation_soft_fail") or (
        row.get("translation_applied") and row.get("translation_script_ok") is False
    ):
        errors.append(
            "upstream_translation_soft_fail:"
            + str(row.get("translation_error") or "script_purity_failed")
        )
    if row.get("entity_coverage_complete") is False:
        missing_up = row.get("missing_required_entities") or []
        if missing_up and not missing_required:
            errors.append(f"upstream_missing_required:{','.join(missing_up)}")
    if row.get("entity_stuffing") and not stuffed:
        stuffed_up = row.get("stuffed_entity_types") or []
        errors.append(
            "upstream_entity_stuffing:"
            + (",".join(str(x) for x in stuffed_up) if stuffed_up else "true")
        )

    coverage = (
        0.0
        if not expected
        else (len(expected) - len(missing_required)) / len(expected)
    )

    format_failures = 0
    checked = 0
    for span in spans:
        ok, code = validate_entity_value(span.entity_type, span.value)
        checked += 1
        if not ok:
            format_failures += 1
            errors.append(f"format:{span.entity_type}:{code}")

    if not span_report["ok"]:
        errors.append("span_alignment_failure")
    if residue:
        errors.append(f"phi_residue:{len(residue)}")
    if float(dics_report["dics"]) < settings.min_dics:
        errors.append(f"dics_below_threshold:{dics_report['dics']}")

    script_ok, script_reason = evaluate_script_purity(
        text,
        language_code=str(row.get("document_language_code", "")),
        script=str(row.get("document_script", "")),
    )
    if not script_ok:
        errors.append(f"script_purity:{script_reason}")

    malformed_count = len(span_report["malformed"]) + len(span_report["empty_values"])
    bcr = 0.0 if not spans else malformed_count / len(spans)
    if bcr > settings.max_boundary_corruption_rate:
        errors.append(f"boundary_corruption_rate:{bcr}")

    persona_age = str(row.get("age", "")).strip()
    age_values = {
        span.value.strip() for span in spans if span.entity_type == "AGE" and span.value.strip()
    }
    if persona_age and age_values and persona_age not in age_values:
        errors.append("persona_age_mismatch")

    entropy = _label_entropy([span.entity_type for span in spans])
    # Low entropy with many spans suggests entity-type collapse
    if len(spans) >= 4 and entropy < 1.0:
        errors.append(f"entity_type_collapse_entropy:{entropy:.3f}")

    return {
        "auditor_pass": len(errors) == 0,
        "auditor_errors": errors,
        "dics": float(dics_report["dics"]),
        "dics_conflicts": dics_report["conflicts"],
        "entity_coverage_rate": coverage,
        "label_entropy": entropy,
        "boundary_corruption_rate": bcr,
        "phi_residue_count": len(residue),
        "format_checks": checked,
        "format_failures": format_failures,
        "inline_span_count": len(spans),
        "stage": "s6_deterministic_auditor",
    }


def audit_corpus(
    rows: Sequence[Mapping[str, Any]],
    *,
    settings: AuditorSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    known = load_entity_specs(settings.entities_config)
    profiles = load_profiles(settings.entity_profiles_config)

    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise AuditorError("No rows selected for deterministic auditor")

    outputs: list[dict[str, Any]] = []
    for row in selected:
        report = audit_document(
            row, known_entities=known, profiles=profiles, settings=settings
        )
        out = dict(row)
        out.update(report)
        outputs.append(out)

    passed = sum(1 for row in outputs if row["auditor_pass"])
    failed_rows = [
        {
            "uuid": row.get("uuid"),
            "document_id": row.get("document_id"),
            "doc_type_id": row.get("doc_type_id"),
            "document_language_code": row.get("document_language_code"),
            "auditor_errors": row.get("auditor_errors"),
        }
        for row in outputs
        if not row["auditor_pass"]
    ]
    audit = {
        "stage": "s6_deterministic_auditor",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "rows_audited": len(outputs),
        "rows_passed": passed,
        "rows_failed": len(failed_rows),
        "pass_rate": passed / len(outputs),
        "mean_dics": sum(float(row["dics"]) for row in outputs) / len(outputs),
        "mean_ecr": sum(float(row["entity_coverage_rate"]) for row in outputs)
        / len(outputs),
        "mean_bcr": sum(float(row["boundary_corruption_rate"]) for row in outputs)
        / len(outputs),
        "failures": failed_rows,
        "failure_count": len(failed_rows),
    }
    if failed_rows:
        print(
            f"[s6] WARNING: {len(failed_rows)} auditor failure(s) logged "
            "— see failed.jsonl and audit failures",
            file=sys.stderr,
        )
    return outputs, audit


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    passed = [row for row in rows if row.get("auditor_pass")]
    failed = [row for row in rows if not row.get("auditor_pass")]
    paths = {
        "all_jsonl": output_dir / "audited.jsonl",
        "passed_jsonl": output_dir / "passed.jsonl",
        "failed_jsonl": output_dir / "failed.jsonl",
        "parquet": output_dir / "audited.parquet",
        "audit_json": output_dir / "audit.json",
        "audit_md": output_dir / "audit.md",
    }
    write_jsonl(paths["all_jsonl"], rows)
    write_jsonl(paths["passed_jsonl"], passed)
    write_jsonl(paths["failed_jsonl"], failed)
    if rows:
        write_parquet(paths["parquet"], rows)
    else:
        paths["parquet"].write_text("", encoding="utf-8")
    write_json(paths["audit_json"], audit)
    soft_fail_path = output_dir / "failures.jsonl"
    write_jsonl(soft_fail_path, audit.get("failures") or [])
    paths["failures_jsonl"] = soft_fail_path
    failure_lines = ""
    failures = audit.get("failures") or []
    if failures:
        failure_lines = "\n## Failures (audited — not silent)\n\n" + "\n".join(
            f"- `{item.get('uuid')}` · `{item.get('doc_type_id')}` · "
            f"`{item.get('document_language_code')}` · {item.get('auditor_errors')}"
            for item in failures
        )
        failure_lines += "\n"
    paths["audit_md"].write_text(
        "# Stage 6 — Deterministic Auditor\n\n"
        f"- rows_audited: **{audit['rows_audited']}**\n"
        f"- rows_failed: **{audit.get('rows_failed', 0)}**\n"
        f"- pass_rate: **{audit['pass_rate']:.3f}**\n"
        f"- mean_dics: **{audit['mean_dics']:.3f}**\n"
        f"- mean_ecr: **{audit['mean_ecr']:.3f}**\n"
        f"- mean_bcr: **{audit['mean_bcr']:.4f}**\n"
        f"{failure_lines}",
        encoding="utf-8",
    )
    return paths


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    rows = read_jsonl(settings.input_jsonl, allow_empty=True)
    if not rows:
        audit = {
            "stage": "s6_deterministic_auditor",
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "rows_audited": 0,
            "rows_passed": 0,
            "pass_rate": 0.0,
            "mean_dics": 0.0,
            "mean_ecr": 0.0,
            "mean_bcr": 0.0,
            "note": "No judge-passed rows; wrote empty auditor outputs.",
        }
        return write_outputs([], audit, settings.output_dir)
    audited, audit = audit_corpus(rows, settings=settings)
    return write_outputs(audited, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 6: deterministic auditor")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (AuditorError, ValueError, FileNotFoundError) as exc:
        print(f"[s6] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s6] Deterministic auditor complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
