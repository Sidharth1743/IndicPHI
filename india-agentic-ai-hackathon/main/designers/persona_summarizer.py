"""Stage 2b — Clinical persona summary via Sarvam-30B.

Compresses long Nemotron-Personas-India lifestyle fields into a short
clinical-relevant English summary used by S3 (EN pivot generation).
Downstream S4b translates the English annotated document into the target
Indic language — we never ask the generator to invent Indic prose from a
noisy full persona dump.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.pipeline.checkpoint import (
    CheckpointStore,
    atomic_write_jsonl,
    request_hash,
    row_key_from_prompt,
)
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.env import load_env_file, require_env
from main.pipeline.io import read_jsonl, write_json, write_jsonl, write_parquet

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

SUMMARY_COLUMNS: tuple[str, ...] = (
    "persona_clinical_summary",
    "persona_summary_model",
    "stage",
)

_NARRATIVE_KEYS: tuple[str, ...] = (
    "persona",
    "cultural_background",
    "linguistic_background",
    "professional_persona",
    "sports_persona",
    "arts_persona",
    "travel_persona",
    "culinary_persona",
)


@dataclass(frozen=True)
class SummarySettings:
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
    requests_per_minute: float | None
    max_workers: int
    narrative_max_chars: int
    empty_content_retries: int = 3


class SummaryError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> SummarySettings:
    root = load_yaml(pipeline_config)
    block = root.get("persona_summary")
    if not isinstance(block, dict):
        raise ValueError(f"'persona_summary' mapping required in {pipeline_config}")

    required = (
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
        raise ValueError(f"Missing persona_summary keys {missing}")

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    rpm = block.get("requests_per_minute")
    if rpm is not None:
        rpm = float(rpm)
        if rpm <= 0:
            raise ValueError("requests_per_minute must be > 0 when set")

    reasoning_effort = block.get("reasoning_effort")
    if reasoning_effort is not None:
        reasoning_effort = str(reasoning_effort)

    max_workers = int(block.get("max_workers", 16))
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")

    empty_retries = int(block.get("empty_content_retries", 3))
    if empty_retries < 0:
        raise ValueError("empty_content_retries must be >= 0")

    return SummarySettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        model=str(block["model"]),
        base_url=str(block["base_url"]),
        api_key_env=str(block["api_key_env"]),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        reasoning_effort=reasoning_effort,
        timeout_s=float(block.get("timeout_s", 120)),
        max_docs=max_docs,
        requests_per_minute=rpm,
        max_workers=max_workers,
        narrative_max_chars=int(block.get("narrative_max_chars", 240)),
        empty_content_retries=empty_retries,
    )


def _clip(text: str, max_chars: int) -> str:
    text = " ".join(str(text).split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def build_summary_messages(
    row: Mapping[str, Any], *, narrative_max_chars: int
) -> list[dict[str, str]]:
    system = (
        "You compress Indian demographic personas into a short clinical-relevant "
        "English summary for synthetic medical document generation.\n"
        "Return ONLY 2–4 plain sentences. No markdown. No bullet lists. No tags.\n"
        "Include: age, sex/gender, occupation, education, marital status, "
        "geography (state/district/zone), first language, and any clinically "
        "useful lifestyle cues. Drop sports/travel/culinary fluff."
    )
    facts = [
        f"sex={row.get('sex')}",
        f"age={row.get('age')}",
        f"marital_status={row.get('marital_status')}",
        f"occupation={row.get('occupation')}",
        f"education_level={row.get('education_level')}",
        f"zone={row.get('zone')}",
        f"state={row.get('state')}",
        f"district={row.get('district')}",
        f"first_language={row.get('first_language')}",
    ]
    narratives = []
    for key in _NARRATIVE_KEYS:
        value = row.get(key)
        if value:
            narratives.append(f"{key}: {_clip(str(value), narrative_max_chars)}")
    user = (
        "Structured fields:\n"
        + "\n".join(f"- {item}" for item in facts)
        + "\n\nOptional Nemotron narrative snippets:\n"
        + ("\n".join(narratives) if narratives else "(none)")
        + "\n\nWrite the clinical persona summary now."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _summarize_one(
    index: int,
    row: Mapping[str, Any],
    *,
    client: SarvamClient,
    settings: SummarySettings,
) -> dict[str, Any]:
    messages = build_summary_messages(
        row, narrative_max_chars=settings.narrative_max_chars
    )
    attempts = settings.empty_content_retries + 1
    last_exc: Exception | None = None
    result = None
    for attempt in range(attempts):
        try:
            result = client.chat_completion(
                model=settings.model,
                messages=messages,
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                reasoning_effort=settings.reasoning_effort,
                timeout_s=settings.timeout_s,
            )
            summary = result.content.strip()
            if len(summary) < 20:
                raise SummaryError(
                    f"Persona summary too short at row {index} "
                    f"uuid={row.get('uuid')!r}"
                )
            out = dict(row)
            out.update(
                {
                    "persona_clinical_summary": summary,
                    "persona_summary_model": result.model,
                    "stage": "s2b_persona_summary",
                }
            )
            return out
        except (SarvamClientError, SummaryError, TimeoutError, OSError) as exc:
            last_exc = exc
            msg = str(exc).lower()
            retryable = (
                "empty content" in msg
                or "too short" in msg
                or "timed out" in msg
                or "timeout" in msg
                or "connection reset" in msg
                or "connection aborted" in msg
                or "temporarily unavailable" in msg
                or "network error" in msg
                or isinstance(exc, (TimeoutError, OSError))
            )
            if retryable and attempt < attempts - 1:
                delay = min(20.0, 2.0 ** attempt)
                print(
                    f"[s2b] retry {attempt + 1}/{attempts - 1} "
                    f"uuid={row.get('uuid')} after {delay:.0f}s: {exc}",
                    file=sys.stderr,
                    flush=True,
                )
                time.sleep(delay)
                continue
            raise SummaryError(
                f"Persona summary failed at row {index} uuid={row.get('uuid')!r}: {exc}"
            ) from exc
    raise SummaryError(
        f"Persona summary failed at row {index} uuid={row.get('uuid')!r}: {last_exc}"
    )


def summarize_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    client: SarvamClient,
    settings: SummarySettings,
    checkpoint: CheckpointStore | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise SummaryError("No rows selected for persona summary")

    results: dict[int, dict[str, Any]] = {}
    pending: list[tuple[int, Mapping[str, Any], str]] = []
    resumed = 0
    for index, row in enumerate(selected):
        key = row_key_from_prompt(row)
        req = request_hash(
            [
                row.get("uuid"),
                row.get("persona"),
                row.get("cultural_background"),
                settings.model,
                settings.temperature,
                settings.max_tokens,
            ]
        )
        if checkpoint is not None:
            existing = checkpoint.get(key)
            if (
                existing
                and existing.status == "ok"
                and existing.request_hash == req
                and existing.payload
            ):
                results[index] = dict(existing.payload)
                resumed += 1
                continue
        pending.append((index, row, req))

    workers = min(settings.max_workers, max(1, len(pending))) if pending else 1
    if pending:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(
                    _summarize_one, index, row, client=client, settings=settings
                ): (index, req)
                for index, row, req in pending
            }
            for future in as_completed(futures):
                index, req = futures[future]
                try:
                    out = future.result()
                except SummaryError:
                    for pending_fut in futures:
                        pending_fut.cancel()
                    raise
                results[index] = out
                if checkpoint is not None:
                    checkpoint.append(
                        row_key=row_key_from_prompt(selected[index]),
                        status="ok",
                        request_hash=req,
                        payload=out,
                    )

    outputs = [results[i] for i in range(len(selected))]
    audit = {
        "stage": "s2b_persona_summary",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "model": settings.model,
        "rows_in": len(selected),
        "rows_out": len(outputs),
        "rows_resumed_from_checkpoint": resumed,
        "rows_newly_summarized": len(pending),
        "max_workers": workers if pending else 0,
        "requests_per_minute": settings.requests_per_minute,
        "mean_summary_chars": (
            sum(len(row["persona_clinical_summary"]) for row in outputs) / len(outputs)
        ),
        "columns_added": list(SUMMARY_COLUMNS),
    }
    return outputs, audit


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = output_dir / "assignments_summarized.jsonl"
    atomic_write_jsonl(jsonl_path, rows)
    parquet_path = output_dir / "assignments_summarized.parquet"
    write_parquet(parquet_path, rows)
    audit_json = output_dir / "audit.json"
    write_json(audit_json, audit)
    audit_md = output_dir / "audit.md"
    lines = [
        "# Stage 2b — Persona Summary Audit",
        "",
        f"- model: `{audit['model']}`",
        f"- rows_out: **{audit['rows_out']}**",
        f"- mean_summary_chars: `{audit['mean_summary_chars']:.1f}`",
        f"- max_workers: `{audit['max_workers']}`",
        "",
        "## Preview",
        "",
    ]
    for row in rows[: min(3, len(rows))]:
        lines.append(
            f"### {row.get('document_language_code')} · {row.get('uuid')}"
        )
        lines.append("")
        lines.append(str(row.get("persona_clinical_summary", "")))
        lines.append("")
    audit_md.write_text("\n".join(lines), encoding="utf-8")
    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
    }


def run(pipeline_config: Path) -> dict[str, Path]:
    load_env_file()
    settings = load_settings(pipeline_config)
    api_key = require_env(settings.api_key_env)
    limiter = (
        RateLimiter(settings.requests_per_minute)
        if settings.requests_per_minute is not None
        else None
    )
    client = SarvamClient(
        api_key=api_key, base_url=settings.base_url, rate_limiter=limiter
    )
    rows = read_jsonl(settings.input_jsonl)
    checkpoint = CheckpointStore(settings.output_dir / "checkpoint.jsonl")
    summarized, audit = summarize_rows(
        rows, client=client, settings=settings, checkpoint=checkpoint
    )
    return write_outputs(summarized, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 2b: persona clinical summary")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (SummaryError, ValueError, FileNotFoundError, SarvamClientError) as exc:
        print(f"[s2b] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s2b] Persona summary complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
