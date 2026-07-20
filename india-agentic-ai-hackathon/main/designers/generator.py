"""Stage 4 — Generate clinical text via **NeMo Data Designer** (required).

Data Designer owns batching/parallelism over S3 seed prompts. The underlying
model is configured in ``data_designer`` (typically Sarvam-105B through an
OpenAI-compatible provider). Direct Sarvam HTTP is not a silent alternate path.

Row-level checkpoints live under the stage output dir (``checkpoint.jsonl``).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq

from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.env import load_env_file, require_env

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

_TAG_TYPE_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|")

GENERATION_COLUMNS: tuple[str, ...] = (
    "document_id",
    "generated_text",
    "generator_provider",
    "generator_model",
    "generator_finish_reason",
    "generator_prompt_tokens",
    "generator_completion_tokens",
    "entity_coverage_complete",
    "missing_required_entities",
    "entity_stuffing",
    "stuffed_entity_types",
    "generation_soft_fail",
    "generation_soft_fail_reasons",
    "stage",
)

# Reject / retry when any TYPE appears more than this many times, or total tags
# exceed required_count * this multiplier (prevents dump-style completeness retries).
# Speaker names may repeat naturally in multi-turn telemedicine chat — exclude them
# from per-type stuffing (device/vehicle IDs and other PHI still capped).
_MAX_OCCURRENCES_PER_TYPE = 2
_MAX_TAG_MULTIPLIER = 2
_STUFFING_EXEMPT_TYPES = frozenset({"PATIENT_NAME", "DOCTOR_NAME"})


@dataclass(frozen=True)
class GenerationSettings:
    provider: str
    input_jsonl: Path
    output_dir: Path
    model: str
    base_url: str
    api_key_env: str
    temperature: float
    max_tokens: int
    reasoning_effort: str | None
    timeout_s: float
    max_docs: int | None
    empty_content_retries: int
    requests_per_minute: float | None
    reject_truncated: bool
    max_workers: int


class GenerationError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> GenerationSettings:
    root = load_yaml(pipeline_config)
    block = root.get("generation")
    if not isinstance(block, dict):
        raise ValueError(f"'generation' mapping required in {pipeline_config}")

    required = (
        "provider",
        "input_jsonl",
        "output_dir",
        "model",
        "base_url",
        "api_key_env",
        "temperature",
        "max_tokens",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing generation keys {missing}")

    provider = str(block["provider"]).strip().lower()
    if provider != "sarvam":
        raise GenerationError(
            f"Unsupported generation.provider={provider!r}. "
            "Use provider=sarvam (Sarvam API). NIM/Data Designer are separate."
        )

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    # null / missing → reasoning OFF (field omitted from request body).
    reasoning_effort = block.get("reasoning_effort", None)
    if reasoning_effort is not None:
        reasoning_effort = str(reasoning_effort)

    empty_content_retries = int(block.get("empty_content_retries", 2))
    if empty_content_retries < 0:
        raise ValueError("empty_content_retries must be >= 0")

    rpm = block.get("requests_per_minute")
    if rpm is not None:
        rpm = float(rpm)
        if rpm <= 0:
            raise ValueError("requests_per_minute must be > 0 when set")

    max_workers = int(block.get("max_workers", 24))
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")

    return GenerationSettings(
        provider=provider,
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        model=str(block["model"]),
        base_url=str(block["base_url"]),
        api_key_env=str(block["api_key_env"]),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        reasoning_effort=reasoning_effort,
        timeout_s=float(block.get("timeout_s", 180)),
        max_docs=max_docs,
        empty_content_retries=empty_content_retries,
        requests_per_minute=rpm,
        reject_truncated=bool(block.get("reject_truncated", True)),
        max_workers=max_workers,
    )


def load_prompts(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(f"S3 input not found: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            row = json.loads(text)
            if not isinstance(row, dict):
                raise GenerationError(f"Prompt row must be object at line {line_no}")
            rows.append(row)
    if not rows:
        raise GenerationError(f"No prompt rows in {path}")
    return rows


def _missing_required_entities(text: str, required: Sequence[str]) -> list[str]:
    present = set(_TAG_TYPE_RE.findall(text))
    return [entity_id for entity_id in required if entity_id not in present]


def _entity_type_counts(text: str) -> dict[str, int]:
    tallies: dict[str, int] = {}
    for entity_id in _TAG_TYPE_RE.findall(text):
        tallies[entity_id] = tallies.get(entity_id, 0) + 1
    return tallies


def _stuffing_violations(
    text: str, required: Sequence[str]
) -> list[str]:
    """Return stuffed TYPE ids when tags are dumped/repeated unnaturally."""
    counts = _entity_type_counts(text)
    stuffed = [
        entity_id
        for entity_id, count in counts.items()
        if entity_id not in _STUFFING_EXEMPT_TYPES
        and count > _MAX_OCCURRENCES_PER_TYPE
    ]
    # Total-tag cap ignores exempt speaker repeats so chat docs are not punished.
    countable = sum(
        count
        for entity_id, count in counts.items()
        if entity_id not in _STUFFING_EXEMPT_TYPES
    )
    cap = max(len(required), 1) * _MAX_TAG_MULTIPLIER
    if countable > cap:
        for entity_id, count in counts.items():
            if (
                entity_id not in _STUFFING_EXEMPT_TYPES
                and count > 1
                and entity_id not in stuffed
            ):
                stuffed.append(entity_id)
        if not stuffed:
            stuffed.append(f"TOTAL_TAGS>{cap}")
    return sorted(stuffed)


def _generate_one(
    index: int,
    row: Mapping[str, Any],
    *,
    client: SarvamClient,
    settings: GenerationSettings,
) -> dict[str, Any]:
    for field in ("system_prompt", "user_prompt", "uuid", "doc_type_id"):
        if field not in row:
            raise GenerationError(f"Prompt row {index} missing {field}")

    required = [str(item) for item in (row.get("required_entities") or [])]
    result = None
    last_error: Exception | None = None
    soft_fail_reasons: list[str] = []
    attempts = settings.empty_content_retries + 1
    for attempt in range(attempts):
        try:
            user_content = str(row["user_prompt"])
            if attempt > 0:
                prev = result.content if result is not None else ""
                missing_hint = _missing_required_entities(prev, required)
                stuffed_hint = _stuffing_violations(prev, required) if prev else []
                retry_bits: list[str] = []
                if missing_hint:
                    retry_bits.append(
                        "Previous draft omitted mandatory entity types: "
                        f"{', '.join(missing_hint)}. Include EVERY mandatory "
                        "[[TYPE|value]] at least once."
                    )
                if stuffed_hint:
                    retry_bits.append(
                        "Previous draft STUFFED / repeated tags for: "
                        f"{', '.join(stuffed_hint)}. Rewrite so each TYPE "
                        f"appears at most {_MAX_OCCURRENCES_PER_TYPE} time(s), "
                        "placed only where clinically natural (no dump lists)."
                    )
                if retry_bits:
                    user_content += "\n\nRETRY: " + " ".join(retry_bits)
            result = client.chat_completion(
                model=settings.model,
                messages=[
                    {"role": "system", "content": str(row["system_prompt"])},
                    {"role": "user", "content": user_content},
                ],
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                reasoning_effort=settings.reasoning_effort,
                timeout_s=settings.timeout_s,
            )
            if (
                settings.reject_truncated
                and str(result.finish_reason).lower() == "length"
            ):
                raise SarvamClientError(
                    "truncated generation (finish_reason=length); "
                    f"completion_tokens={result.completion_tokens} "
                    f"max_tokens={settings.max_tokens}. "
                    "Raise max_tokens or tighten doc-type length rules."
                )
            missing = _missing_required_entities(result.content, required)
            if missing:
                raise SarvamClientError(
                    "missing_required_entities:" + ",".join(missing)
                )
            stuffed = _stuffing_violations(result.content, required)
            if stuffed:
                raise SarvamClientError(
                    "entity_stuffing:" + ",".join(stuffed)
                )
            break
        except SarvamClientError as exc:
            last_error = exc
            message = str(exc).lower()
            retryable = (
                "empty content" in message
                or "truncated generation" in message
                or "missing_required_entities" in message
                or "entity_stuffing" in message
                or "connection reset" in message
                or "timed out" in message
                or "temporary" in message
                or "network error" in message
                or "http 429" in message
                or "rate limit" in message
            )
            # Soft-fail incomplete coverage / stuffing after retries so the run
            # continues — but reasons are always recorded on the row + audit.
            if attempt >= attempts - 1 and result is not None and (
                "missing_required_entities" in message
                or "entity_stuffing" in message
            ):
                soft_fail_reasons.append(str(exc))
                break
            if (not retryable) or attempt >= attempts - 1:
                raise GenerationError(
                    f"Generation failed at row {index} uuid={row.get('uuid')!r}: {exc}"
                ) from exc
            continue

    if result is None:
        assert last_error is not None
        raise GenerationError(
            f"Generation failed at row {index} uuid={row.get('uuid')!r}: {last_error}"
        ) from last_error

    missing_final = _missing_required_entities(result.content, required)
    stuffed_final = _stuffing_violations(result.content, required)
    if missing_final and "missing_required_entities:" + ",".join(missing_final) not in soft_fail_reasons:
        soft_fail_reasons.append(
            "missing_required_entities:" + ",".join(missing_final)
        )
    if stuffed_final and "entity_stuffing:" + ",".join(stuffed_final) not in soft_fail_reasons:
        soft_fail_reasons.append("entity_stuffing:" + ",".join(stuffed_final))

    uuid = str(row["uuid"])
    doc_slot = row.get("doc_slot", index)
    soft_fail = bool(soft_fail_reasons)
    out = dict(row)
    out.update(
        {
            "document_id": f"{uuid}__{doc_slot}",
            "generated_text": result.content,
            "generator_provider": settings.provider,
            "generator_model": result.model,
            "generator_finish_reason": result.finish_reason,
            "generator_prompt_tokens": result.prompt_tokens,
            "generator_completion_tokens": result.completion_tokens,
            "entity_coverage_complete": len(missing_final) == 0,
            "missing_required_entities": missing_final,
            "entity_stuffing": len(stuffed_final) > 0,
            "stuffed_entity_types": stuffed_final,
            "generation_soft_fail": soft_fail,
            "generation_soft_fail_reasons": soft_fail_reasons,
            "stage": "s4_generation",
        }
    )
    if soft_fail:
        print(
            f"[s4] SOFT-FAIL uuid={uuid} doc_type={row.get('doc_type_id')} "
            f"reasons={soft_fail_reasons}",
            file=sys.stderr,
        )
    return out


def generate_documents(
    rows: Sequence[Mapping[str, Any]],
    *,
    client: SarvamClient,
    settings: GenerationSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise GenerationError("No rows selected for generation")

    workers = min(settings.max_workers, len(selected))
    failures: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {
            pool.submit(
                _generate_one, index, row, client=client, settings=settings
            ): index
            for index, row in enumerate(selected)
        }
        results: dict[int, dict[str, Any]] = {}
        for future in as_completed(futures):
            index = futures[future]
            try:
                results[index] = future.result()
            except GenerationError as exc:
                row = selected[index]
                failures.append(
                    {
                        "index": index,
                        "uuid": row.get("uuid"),
                        "doc_type_id": row.get("doc_type_id"),
                        "error": str(exc),
                    }
                )
                # Cancel remaining work; first hard failure still aborts the stage.
                for pending in futures:
                    pending.cancel()
                raise

    outputs = [results[i] for i in range(len(selected))]

    soft_failures = [
        {
            "uuid": row.get("uuid"),
            "document_id": row.get("document_id"),
            "doc_type_id": row.get("doc_type_id"),
            "document_language_code": row.get("document_language_code"),
            "missing_required_entities": row.get("missing_required_entities") or [],
            "stuffed_entity_types": row.get("stuffed_entity_types") or [],
            "reasons": row.get("generation_soft_fail_reasons") or [],
        }
        for row in outputs
        if row.get("generation_soft_fail")
    ]

    audit = {
        "stage": "s4_generation",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider": settings.provider,
        "model": settings.model,
        "base_url": settings.base_url,
        "reasoning_effort": settings.reasoning_effort,
        "requests_per_minute": settings.requests_per_minute,
        "max_workers": workers,
        "max_tokens": settings.max_tokens,
        "reject_truncated": settings.reject_truncated,
        "input_jsonl": str(settings.input_jsonl),
        "rows_requested": len(selected),
        "rows_generated": len(outputs),
        "failures": failures,
        "soft_failures": soft_failures,
        "soft_fail_count": len(soft_failures),
        "entity_coverage_incomplete_count": sum(
            1 for row in outputs if not row.get("entity_coverage_complete")
        ),
        "entity_stuffing_count": sum(
            1 for row in outputs if row.get("entity_stuffing")
        ),
        "doc_type_counts": _count(outputs, "doc_type_id"),
        "language_counts": _count(outputs, "document_language_code"),
        "mean_chars": (
            sum(len(row["generated_text"]) for row in outputs) / len(outputs)
            if outputs
            else 0
        ),
        "entity_coverage_complete_rate": (
            sum(1 for row in outputs if row.get("entity_coverage_complete"))
            / len(outputs)
            if outputs
            else 0
        ),
        "columns_added": list(GENERATION_COLUMNS),
    }
    if soft_failures:
        print(
            f"[s4] WARNING: {len(soft_failures)} soft-fail(s) logged "
            "(incomplete coverage and/or stuffing) — see audit soft_failures",
            file=sys.stderr,
        )
    return outputs, audit


def _count(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    tallies: dict[str, int] = {}
    for row in rows:
        value = str(row[key])
        tallies[value] = tallies.get(value, 0) + 1
    return dict(sorted(tallies.items()))


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = output_dir / "documents.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    columns = list(rows[0].keys())
    table = {name: [row[name] for row in rows] for name in columns}
    parquet_path = output_dir / "documents.parquet"
    pq.write_table(pa.table(table), parquet_path)

    audit_json = output_dir / "audit.json"
    audit_json.write_text(json.dumps(dict(audit), indent=2, ensure_ascii=False) + "\n")

    soft_fail_path = output_dir / "soft_failures.jsonl"
    with soft_fail_path.open("w", encoding="utf-8") as handle:
        for item in audit.get("soft_failures") or []:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")

    audit_md = output_dir / "audit.md"
    lines = [
        "# Stage 4 — Generation Audit",
        "",
        f"- provider: `{audit['provider']}`",
        f"- model: `{audit['model']}`",
        f"- reasoning_effort: `{audit['reasoning_effort']}` (null = OFF)",
        f"- requests_per_minute: `{audit['requests_per_minute']}`",
        f"- max_workers: `{audit.get('max_workers')}`",
        f"- max_tokens: `{audit['max_tokens']}`",
        f"- reject_truncated: `{audit.get('reject_truncated')}`",
        f"- rows_generated: **{audit['rows_generated']}**",
        f"- soft_fail_count: **{audit.get('soft_fail_count', 0)}**",
        f"- entity_coverage_incomplete_count: `{audit.get('entity_coverage_incomplete_count', 0)}`",
        f"- entity_stuffing_count: `{audit.get('entity_stuffing_count', 0)}`",
        f"- entity_coverage_complete_rate: `{audit.get('entity_coverage_complete_rate', 0):.3f}`",
        f"- mean_chars: `{audit['mean_chars']:.1f}`",
        f"- languages: `{audit['language_counts']}`",
        f"- doc_types: `{audit['doc_type_counts']}`",
        "",
    ]
    soft_failures = audit.get("soft_failures") or []
    if soft_failures:
        lines.extend(["## Soft failures (audited — not silent)", ""])
        for item in soft_failures:
            lines.append(
                f"- `{item.get('uuid')}` · `{item.get('doc_type_id')}` · "
                f"`{item.get('document_language_code')}` · reasons={item.get('reasons')}"
            )
        lines.append("")
    lines.extend(
        [
            "## Preview",
            "",
        ]
    )
    for row in rows[: min(3, len(rows))]:
        lines.append(
            f"### {row['document_language_code']} · {row['doc_type_id']} · {row['domain_id']}"
        )
        lines.append("")
        lines.append("```")
        lines.append(str(row["generated_text"])[:1200])
        lines.append("```")
        lines.append("")
    audit_md.write_text("\n".join(lines), encoding="utf-8")

    preview = REPO_ROOT / "data" / "samples" / "s4_documents_preview.jsonl"
    preview.parent.mkdir(parents=True, exist_ok=True)
    with preview.open("w", encoding="utf-8") as handle:
        for row in rows[: min(3, len(rows))]:
            handle.write(
                json.dumps(
                    {
                        "uuid": row["uuid"],
                        "document_language_code": row["document_language_code"],
                        "doc_type_id": row["doc_type_id"],
                        "domain_id": row["domain_id"],
                        "generator_model": row["generator_model"],
                        "generated_text": row["generated_text"][:1500],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
        "soft_failures_jsonl": soft_fail_path,
        "preview_jsonl": preview,
    }


def run(pipeline_config: Path) -> dict[str, Path]:
    """Strict Data Designer path — raises if the package/config is missing."""
    from main.pipeline.designer_config import (
        DesignerConfigError,
        run_data_designer_generation,
    )

    root = load_yaml(pipeline_config)
    engine = str(
        (root.get("generation") or {}).get("engine")
        or (root.get("data_designer") or {}).get("engine")
        or "data_designer"
    ).strip().lower()
    if engine not in {"data_designer", "nemo_data_designer"}:
        raise GenerationError(
            f"Unsupported generation.engine={engine!r}. "
            "This pipeline requires engine=data_designer (NeMo Data Designer)."
        )
    try:
        return run_data_designer_generation(pipeline_config)
    except DesignerConfigError as exc:
        raise GenerationError(str(exc)) from exc


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 4: Sarvam generation")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (GenerationError, ValueError, FileNotFoundError, SarvamClientError) as exc:
        print(f"[s4] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s4] Generation complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
