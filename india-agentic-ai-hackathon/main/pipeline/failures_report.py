"""Build a run-level ``failures.md`` that audits every soft-fail / reject.

Called at the end of ``run_pipeline`` (success or stage failure) so each
``data/generated/runs/<id>/failures.md`` is the single place to inspect what
went wrong — no silent drops.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping, Sequence


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.is_file() or path.stat().st_size == 0:
        return []
    rows: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        text = line.strip()
        if not text:
            continue
        row = json.loads(text)
        if not isinstance(row, dict):
            raise ValueError(f"{path}:{line_no} expected object")
        rows.append(row)
    return rows


def _read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def _clip(text: str | None, n: int = 500) -> str:
    if not text:
        return ""
    text = str(text).replace("\r\n", "\n").strip()
    if len(text) <= n:
        return text
    return text[: n - 1] + "…"


def _section(title: str, body_lines: Sequence[str]) -> list[str]:
    if not body_lines:
        return [f"## {title}", "", "_None._", ""]
    return [f"## {title}", "", *body_lines, ""]


def collect_failure_entries(run_root: Path) -> dict[str, list[dict[str, Any]]]:
    """Gather failure-like rows from stage artifacts."""
    out: dict[str, list[dict[str, Any]]] = {
        "stage_hard_failures": [],
        "generation_soft_failures": [],
        "translation_soft_failures": [],
        "judge_failures": [],
        "auditor_failures": [],
    }

    run_results = _read_json(run_root / "run_results.json")
    for stage in run_results.get("stages") or []:
        if stage.get("status") == "failed":
            out["stage_hard_failures"].append(dict(stage))

    out["generation_soft_failures"] = _read_jsonl(
        run_root / "s4_generation" / "soft_failures.jsonl"
    )
    # Prefer dedicated soft_failures; fall back to audit.json list.
    if not out["generation_soft_failures"]:
        audit = _read_json(run_root / "s4_generation" / "audit.json")
        out["generation_soft_failures"] = list(audit.get("soft_failures") or [])

    out["translation_soft_failures"] = _read_jsonl(
        run_root / "s4b_translation" / "soft_failures.jsonl"
    )
    if not out["translation_soft_failures"]:
        audit = _read_json(run_root / "s4b_translation" / "audit.json")
        out["translation_soft_failures"] = list(audit.get("soft_failures") or [])

    out["judge_failures"] = _read_jsonl(
        run_root / "s5_linguistic_judge" / "failed.jsonl"
    )
    out["auditor_failures"] = _read_jsonl(
        run_root / "s6_deterministic_auditor" / "failed.jsonl"
    )
    if not out["auditor_failures"]:
        out["auditor_failures"] = _read_jsonl(
            run_root / "s6_deterministic_auditor" / "failures.jsonl"
        )
    return out


def _lookup_doc(run_root: Path, uuid: str | None) -> dict[str, Any] | None:
    if not uuid:
        return None
    for rel in (
        "s4b_translation/documents.jsonl",
        "s4_generation/documents.jsonl",
        "s5_linguistic_judge/judged.jsonl",
        "s6_deterministic_auditor/audited.jsonl",
    ):
        for row in _read_jsonl(run_root / rel):
            if str(row.get("uuid")) == str(uuid):
                return row
    return None


def _diagnosis_generation(row: Mapping[str, Any], doc: Mapping[str, Any] | None) -> str:
    missing = row.get("missing_required_entities") or []
    stuffed = row.get("stuffed_entity_types") or []
    reasons = row.get("reasons") or row.get("generation_soft_fail_reasons") or []
    bits = [
        f"- **What:** generation soft-fail on `{row.get('doc_type_id')}` "
        f"(`{row.get('document_language_code')}`).",
        f"- **Missing required tags:** `{missing or '—'}`",
        f"- **Stuffing flags:** `{stuffed or '—'}`",
        f"- **Raw reasons:** `{reasons}`",
    ]
    if doc and missing:
        bits.append(
            "- **Why likely:** model wrote clinical chat/prose without wrapping "
            "every mandatory TYPE (common on telemedicine when AGE/GENDER stay "
            "in narrative only)."
        )
    if stuffed:
        bits.append(
            "- **Note:** repeated speaker names in multi-turn chat can look like "
            "stuffing; device/vehicle IDs should still appear once only."
        )
    if doc:
        bits.append(f"- **Preview:**\n\n```\n{_clip(str(doc.get('generated_text')), 600)}\n```")
    return "\n".join(bits)


def _diagnosis_translation(row: Mapping[str, Any], doc: Mapping[str, Any] | None) -> str:
    err = row.get("translation_error") or ""
    bits = [
        f"- **What:** translation soft-fail on `{row.get('doc_type_id')}` "
        f"(`{row.get('document_language_code')}`).",
        f"- **Error:** `{err}`",
        f"- **script_ok:** `{row.get('translation_script_ok')}`",
    ]
    if "script_purity" in str(err):
        bits.append(
            "- **Why:** output stayed Latin / Romanized instead of the target "
            "Indic script (ratio below threshold). Judge usually fails this too."
        )
    if doc:
        bits.append(
            f"- **EN pivot preview:**\n\n```\n{_clip(str(doc.get('generated_text_en')), 400)}\n```"
        )
        bits.append(
            f"- **Translated preview:**\n\n```\n{_clip(str(doc.get('generated_text')), 400)}\n```"
        )
    return "\n".join(bits)


def _diagnosis_judge(row: Mapping[str, Any]) -> str:
    bits = [
        f"- **What:** linguistic judge **fail** on `{row.get('doc_type_id')}` "
        f"(`{row.get('document_language_code')}`).",
        f"- **Score / verdict:** `{row.get('judge_score')}` / `{row.get('judge_verdict')}`",
        f"- **Flags:** `{row.get('judge_flags')}`",
        f"- **Reasoning:** {_clip(str(row.get('judge_reasoning') or ''), 700) or '—'}",
        f"- **Preview:**\n\n```\n{_clip(str(row.get('generated_text')), 500)}\n```",
    ]
    return "\n".join(bits)


def _diagnosis_auditor(row: Mapping[str, Any]) -> str:
    errors = row.get("auditor_errors") or []
    bits = [
        f"- **What:** deterministic auditor **fail** on `{row.get('doc_type_id')}` "
        f"(`{row.get('document_language_code')}`).",
        f"- **Errors:** `{errors}`",
    ]
    joined = " ".join(str(e) for e in errors)
    if "upstream_generation_soft_fail" in joined:
        bits.append("- **Cause chain:** inherited S4 generation soft-fail (not silent).")
    if "upstream_translation_soft_fail" in joined or "script_purity" in joined:
        bits.append("- **Cause chain:** translation/script purity issue.")
    if "entity_stuffing" in joined:
        bits.append("- **Cause:** tag dump / over-repetition of entity TYPEs.")
    if "missing_required" in joined:
        bits.append("- **Cause:** profile-required entity TYPE(s) absent from text.")
    bits.append(
        f"- **Preview:**\n\n```\n{_clip(str(row.get('generated_text')), 500)}\n```"
    )
    return "\n".join(bits)


def build_failures_markdown(run_root: Path) -> str:
    run_id = run_root.name
    run_results = _read_json(run_root / "run_results.json")
    status = run_results.get("status", "unknown")
    entries = collect_failure_entries(run_root)

    # Throughput snapshot
    curated_n = len(_read_jsonl(run_root / "s7_s8_curation" / "curated.jsonl"))
    judged = _read_json(run_root / "s5_linguistic_judge" / "audit.json")
    audited = _read_json(run_root / "s6_deterministic_auditor" / "audit.json")
    gen = _read_json(run_root / "s4_generation" / "audit.json")
    tr = _read_json(run_root / "s4b_translation" / "audit.json")

    total_issues = sum(len(v) for v in entries.values())
    lines: list[str] = [
        f"# Failures audit — `{run_id}`",
        "",
        f"- **run status:** `{status}`",
        f"- **resolved config:** `{run_results.get('resolved_config', '—')}`",
        f"- **issue count:** **{total_issues}** "
        f"(hard={len(entries['stage_hard_failures'])}, "
        f"gen_soft={len(entries['generation_soft_failures'])}, "
        f"tr_soft={len(entries['translation_soft_failures'])}, "
        f"judge={len(entries['judge_failures'])}, "
        f"auditor={len(entries['auditor_failures'])})",
        f"- **S4 entity_coverage_complete_rate:** "
        f"`{gen.get('entity_coverage_complete_rate', '—')}`",
        f"- **S4b script_fail_count:** `{tr.get('script_fail_count', '—')}`",
        f"- **S5 pass_rate:** `{judged.get('pass_rate', '—')}`",
        f"- **S6 pass_rate / passed:** "
        f"`{audited.get('pass_rate', '—')}` / `{audited.get('rows_passed', '—')}`",
        f"- **curated docs:** `{curated_n}`",
        "",
        "## Summary",
        "",
    ]

    if total_issues == 0 and status == "ok":
        lines.append("No soft-fails or rejects recorded. Pipeline completed cleanly.")
        lines.append("")
    else:
        lines.append("| Stage | UUID | Lang | Doc type | Symptom |")
        lines.append("| --- | --- | --- | --- | --- |")
        for row in entries["stage_hard_failures"]:
            lines.append(
                f"| hard `{row.get('stage')}` | — | — | — | "
                f"{_clip(str(row.get('error')), 120)} |"
            )
        for row in entries["generation_soft_failures"]:
            lines.append(
                f"| S4 soft | `{row.get('uuid')}` | `{row.get('document_language_code')}` | "
                f"`{row.get('doc_type_id')}` | `{_clip(str(row.get('reasons')), 100)}` |"
            )
        for row in entries["translation_soft_failures"]:
            lines.append(
                f"| S4b soft | `{row.get('uuid')}` | `{row.get('document_language_code')}` | "
                f"`{row.get('doc_type_id')}` | `{_clip(str(row.get('translation_error')), 100)}` |"
            )
        for row in entries["judge_failures"]:
            lines.append(
                f"| S5 fail | `{row.get('uuid')}` | `{row.get('document_language_code')}` | "
                f"`{row.get('doc_type_id')}` | score={row.get('judge_score')} "
                f"flags={row.get('judge_flags')} |"
            )
        for row in entries["auditor_failures"]:
            lines.append(
                f"| S6 fail | `{row.get('uuid')}` | `{row.get('document_language_code')}` | "
                f"`{row.get('doc_type_id')}` | `{_clip(str(row.get('auditor_errors')), 100)}` |"
            )
        lines.append("")

    detail_blocks: list[str] = []
    for i, row in enumerate(entries["stage_hard_failures"], 1):
        detail_blocks.extend(
            [
                f"### Hard stage failure {i}: `{row.get('stage')}`",
                "",
                f"- **error:** `{row.get('error')}`",
                f"- **started:** `{row.get('started_utc')}`",
                f"- **finished:** `{row.get('finished_utc')}`",
                "",
            ]
        )
    for i, row in enumerate(entries["generation_soft_failures"], 1):
        doc = _lookup_doc(run_root, row.get("uuid"))
        detail_blocks.extend(
            [
                f"### S4 generation soft-fail {i}",
                "",
                _diagnosis_generation(row, doc),
                "",
            ]
        )
    for i, row in enumerate(entries["translation_soft_failures"], 1):
        doc = _lookup_doc(run_root, row.get("uuid"))
        detail_blocks.extend(
            [
                f"### S4b translation soft-fail {i}",
                "",
                _diagnosis_translation(row, doc),
                "",
            ]
        )
    for i, row in enumerate(entries["judge_failures"], 1):
        detail_blocks.extend(
            [
                f"### S5 judge fail {i}",
                "",
                _diagnosis_judge(row),
                "",
            ]
        )
    for i, row in enumerate(entries["auditor_failures"], 1):
        detail_blocks.extend(
            [
                f"### S6 auditor fail {i}",
                "",
                _diagnosis_auditor(row),
                "",
            ]
        )

    lines.extend(_section("Per-failure audit", detail_blocks))

    # Curated language mix
    curated = _read_jsonl(run_root / "s7_s8_curation" / "curated.jsonl")
    if curated:
        by_lang = Counter(str(r.get("document_language_code")) for r in curated)
        by_doc = Counter(str(r.get("doc_type_id")) for r in curated)
        lines.extend(
            [
                "## Surviving curated set",
                "",
                f"- languages: `{dict(sorted(by_lang.items()))}`",
                f"- doc_types: `{dict(sorted(by_doc.items()))}`",
                "",
            ]
        )

    lines.append(
        "_Generated by `main.pipeline.failures_report`. Re-run: "
        "`python -m main.pipeline.failures_report --run-id <id>`._\n"
    )
    return "\n".join(lines)


def write_failures_report(run_root: Path) -> Path:
    run_root = Path(run_root)
    path = run_root / "failures.md"
    path.write_text(build_failures_markdown(run_root), encoding="utf-8")
    return path


def main(argv: Sequence[str] | None = None) -> int:
    import argparse
    import sys

    from main.pipeline.run_layout import RUNS_ROOT, run_dir

    parser = argparse.ArgumentParser(description="Write run-level failures.md")
    parser.add_argument("--run-id", type=str, default=None)
    parser.add_argument(
        "--run-dir",
        type=Path,
        default=None,
        help="Explicit run folder (overrides --run-id)",
    )
    args = parser.parse_args(argv)
    if args.run_dir is not None:
        root = args.run_dir
    elif args.run_id:
        root = run_dir(args.run_id)
    else:
        latest = RUNS_ROOT / "latest"
        root = latest.resolve() if latest.exists() else None
        if root is None:
            print("No --run-id / --run-dir and no runs/latest", file=sys.stderr)
            return 1
    if not root.is_dir():
        print(f"Run folder missing: {root}", file=sys.stderr)
        return 1
    path = write_failures_report(root)
    print(f"[failures] wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
