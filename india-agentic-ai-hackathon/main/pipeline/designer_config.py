"""NeMo Data Designer — **required** S4 generation engine.

Smoke and full pipelines must generate through Data Designer (batching,
parallelism, seed datasets). Direct Sarvam HTTP in ``generator.py`` is only
used as the OpenAI-compatible backend that Data Designer calls via a custom
provider — never as a silent alternate path around Data Designer.

Usage::

    from main.pipeline.designer_config import run_data_designer_generation
    paths = run_data_designer_generation(pipeline_config)
"""

from __future__ import annotations

import json
import os
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from main.designers.entity_checks import tag_issues
from main.designers.repair import (
    issues_from_coverage,
    load_repair_settings_from_generation,
    repair_document,
)
from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient
from main.pipeline.checkpoint import (
    CheckpointStore,
    atomic_write_jsonl,
    request_hash,
    row_key_from_prompt,
)
from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path
from main.pipeline.env import load_env_file, require_env
from main.pipeline.io import read_jsonl, write_json, write_parquet


@dataclass(frozen=True)
class DesignerBridgeSettings:
    seed_path: Path
    model_alias: str
    model_id: str
    provider: str
    temperature: float
    max_tokens: int
    # Sarvam: null → reasoning OFF; "low"|"medium"|"high" → ON.
    reasoning_effort: str | None
    system_prompt_column: str
    user_prompt_column: str
    output_column: str
    provider_endpoint: str
    provider_api_key_env: str
    # OpenAI-compatible auth header style: bearer | subscription_key
    auth_style: str
    required: bool


class DesignerConfigError(RuntimeError):
    pass


def load_designer_bridge_settings(pipeline_config: Path) -> DesignerBridgeSettings:
    root = load_yaml(pipeline_config)
    block = root.get("data_designer")
    if not isinstance(block, dict):
        raise DesignerConfigError(
            f"'data_designer' mapping is REQUIRED in {pipeline_config}. "
            "S4 must run through NeMo Data Designer — no silent HTTP fallback."
        )
    if block.get("required", True) is False:
        raise DesignerConfigError(
            "data_designer.required=false is not allowed. "
            "This pipeline strictly uses NeMo Data Designer for S4."
        )

    required = (
        "seed_path",
        "model_alias",
        "model_id",
        "provider",
        "temperature",
        "max_tokens",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise DesignerConfigError(f"Missing data_designer keys {missing}")

    gen = root.get("generation") if isinstance(root.get("generation"), dict) else {}
    endpoint = str(
        block.get("provider_endpoint")
        or gen.get("base_url")
        or "https://api.sarvam.ai/v1"
    )
    api_key_env = str(
        block.get("provider_api_key_env")
        or gen.get("api_key_env")
        or "SARVAM_API_KEY"
    )
    auth_style = str(block.get("auth_style", "subscription_key")).strip().lower()
    if auth_style not in {"bearer", "subscription_key"}:
        raise DesignerConfigError(
            f"Unsupported data_designer.auth_style={auth_style!r} "
            "(use bearer or subscription_key)"
        )

    # Prefer data_designer.reasoning_effort; fall back to generation.reasoning_effort.
    reasoning_raw = block.get("reasoning_effort", gen.get("reasoning_effort", None))
    if reasoning_raw is not None:
        reasoning_raw = str(reasoning_raw).strip().lower()
        if reasoning_raw not in {"low", "medium", "high"}:
            raise DesignerConfigError(
                f"Unsupported reasoning_effort={reasoning_raw!r} "
                "(use null|low|medium|high)"
            )

    return DesignerBridgeSettings(
        seed_path=resolve_repo_path(str(block["seed_path"])),
        model_alias=str(block["model_alias"]),
        model_id=str(block["model_id"]),
        provider=str(block["provider"]),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        reasoning_effort=reasoning_raw,
        system_prompt_column=str(block.get("system_prompt_column", "system_prompt")),
        user_prompt_column=str(block.get("user_prompt_column", "user_prompt")),
        output_column=str(block.get("output_column", "generated_text")),
        provider_endpoint=endpoint.rstrip("/"),
        provider_api_key_env=api_key_env,
        auth_style=auth_style,
        required=True,
    )


_SARVAM_STRING_CONTENT_PATCHED = False


def _flatten_text_only_content(content: Any) -> Any:
    """Sarvam rejects ChatML content-block lists; it needs ``content: str``."""
    if not isinstance(content, list):
        return content
    texts: list[str] = []
    for block in content:
        if isinstance(block, str):
            texts.append(block)
            continue
        if isinstance(block, dict) and block.get("type") == "text":
            texts.append(str(block.get("text") or ""))
            continue
        # Multimodal / non-text block — leave the list intact.
        return content
    return "\n".join(texts)


def _patch_data_designer_string_content() -> None:
    """Make Data Designer's OpenAI adapter emit string message content for Sarvam.

    Data Designer normalizes messages to::

        {"role": "...", "content": [{"type": "text", "text": "..."}]}

    Sarvam's chat API validates ``content`` as a plain string and returns::

        body.messages.0.system.content : Input should be a valid string
    """
    global _SARVAM_STRING_CONTENT_PATCHED
    if _SARVAM_STRING_CONTENT_PATCHED:
        return
    from data_designer.engine.models.clients.adapters import openai_compatible as oc

    original = oc.translate_openai_compatible_messages

    def _patched(
        messages: list[dict[str, Any]],
        *,
        provider_name: str,
        model_name: str,
    ) -> list[dict[str, Any]]:
        translated = original(
            messages, provider_name=provider_name, model_name=model_name
        )
        # Always flatten pure-text blocks: OpenAI accepts strings; Sarvam requires them.
        flattened: list[dict[str, Any]] = []
        for message in translated:
            item = dict(message)
            if "content" in item:
                item["content"] = _flatten_text_only_content(item.get("content"))
            flattened.append(item)
        return flattened

    oc.translate_openai_compatible_messages = _patched
    _SARVAM_STRING_CONTENT_PATCHED = True


def _import_data_designer():
    try:
        import data_designer.config as dd
        from data_designer.interface import DataDesigner
    except ImportError as exc:
        raise DesignerConfigError(
            "NeMo Data Designer is REQUIRED but not installed. "
            "Install with: `uv pip install 'data-designer>=0.7.0'` "
            "(or `uv sync` in india-agentic-ai-hackathon/)."
        ) from exc
    _patch_data_designer_string_content()
    return dd, DataDesigner


def _designer_home() -> Path:
    home = Path(
        os.environ.get(
            "DATA_DESIGNER_HOME",
            str(REPO_ROOT / "artifacts" / "data_designer_home"),
        )
    )
    home.mkdir(parents=True, exist_ok=True)
    os.environ["DATA_DESIGNER_HOME"] = str(home)
    return home


def build_model_provider(settings: DesignerBridgeSettings, api_key: str) -> Any:
    """Build an in-process ``ModelProvider`` for Sarvam / OpenAI-compatible APIs.

    Writing YAML under ``DATA_DESIGNER_HOME`` alone is not enough — ``DataDesigner``
    must receive ``model_providers=[...]`` or the named provider is unregistered.
    Sarvam auth uses ``api-subscription-key`` (not Bearer).
    """
    dd, _DataDesigner = _import_data_designer()
    os.environ[settings.provider_api_key_env] = api_key

    extra_body: dict[str, Any] = {"reasoning_effort": settings.reasoning_effort}
    if settings.auth_style == "subscription_key":
        # Avoid Bearer; Sarvam requires api-subscription-key.
        return dd.ModelProvider(
            name=settings.provider,
            endpoint=settings.provider_endpoint,
            provider_type="openai",
            api_key=None,
            extra_headers={"api-subscription-key": api_key},
            extra_body=extra_body,
        )
    return dd.ModelProvider(
        name=settings.provider,
        endpoint=settings.provider_endpoint,
        provider_type="openai",
        api_key=settings.provider_api_key_env,  # env var name resolved by DD
        extra_body=extra_body,
    )


def _ensure_provider_files(settings: DesignerBridgeSettings, api_key: str) -> Path:
    """Materialize DATA_DESIGNER_HOME YAML mirrors (audit/debug) + export API key."""
    home = _designer_home()
    providers_path = home / "model_providers.yaml"
    provider_entry: dict[str, Any] = {
        "name": settings.provider,
        "endpoint": settings.provider_endpoint,
        "provider_type": "openai",
    }
    if settings.auth_style == "subscription_key":
        provider_entry["api_key"] = None
        provider_entry["extra_headers"] = {"api-subscription-key": "${" + settings.provider_api_key_env + "}"}
        provider_entry["extra_body"] = {"reasoning_effort": settings.reasoning_effort}
    else:
        provider_entry["api_key"] = settings.provider_api_key_env
        provider_entry["extra_body"] = {"reasoning_effort": settings.reasoning_effort}

    providers_doc = {"providers": [provider_entry]}
    providers_path.write_text(
        __import__("yaml").safe_dump(providers_doc, sort_keys=False),
        encoding="utf-8",
    )

    models_path = home / "model_configs.yaml"
    models_doc = {
        "model_configs": [
            {
                "alias": settings.model_alias,
                "model": settings.model_id,
                "provider": settings.provider,
                "inference_parameters": {
                    "temperature": settings.temperature,
                    "max_tokens": settings.max_tokens,
                    "extra_body": {"reasoning_effort": settings.reasoning_effort},
                },
            }
        ]
    }
    models_path.write_text(
        __import__("yaml").safe_dump(models_doc, sort_keys=False),
        encoding="utf-8",
    )
    os.environ[settings.provider_api_key_env] = api_key
    return home


def _build_config_builder(
    dd: Any,
    settings: DesignerBridgeSettings,
    *,
    seed_path: Path,
    max_parallel_requests: int | None = None,
) -> Any:
    inference_kwargs: dict[str, Any] = {
        "temperature": settings.temperature,
        "max_tokens": settings.max_tokens,
        "extra_body": {"reasoning_effort": settings.reasoning_effort},
    }
    if max_parallel_requests is not None and max_parallel_requests > 0:
        inference_kwargs["max_parallel_requests"] = int(max_parallel_requests)

    builder = dd.DataDesignerConfigBuilder()
    builder.add_model_config(
        dd.ModelConfig(
            alias=settings.model_alias,
            model=settings.model_id,
            provider=settings.provider,
            inference_parameters=dd.ChatCompletionInferenceParams(**inference_kwargs),
        )
    )
    builder.with_seed_dataset(dd.LocalFileSeedSource(path=str(seed_path)))
    builder.add_column(
        dd.LLMTextColumnConfig(
            name=settings.output_column,
            model_alias=settings.model_alias,
            system_prompt=f"{{{{{settings.system_prompt_column}}}}}",
            prompt=f"{{{{{settings.user_prompt_column}}}}}",
        )
    )
    return builder


def load_config_builder(pipeline_config: Path | None = None):
    """Return a DataDesignerConfigBuilder seeded from S3 prompts parquet/jsonl."""
    dd, _DataDesigner = _import_data_designer()
    config_path = pipeline_config or (
        REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"
    )
    settings = load_designer_bridge_settings(config_path)
    if not settings.seed_path.is_file():
        raise DesignerConfigError(
            f"Data Designer seed not found: {settings.seed_path}. "
            "Run S3 prompt construction first (prompts.parquet preferred)."
        )
    return _build_config_builder(dd, settings, seed_path=settings.seed_path)


def _dataframe_to_rows(dataset: Any) -> list[dict[str, Any]]:
    if hasattr(dataset, "to_dict"):
        records = dataset.to_dict(orient="records")
        return [dict(row) for row in records]
    if isinstance(dataset, list):
        return [dict(row) for row in dataset]
    raise DesignerConfigError(f"Unsupported Data Designer dataset type: {type(dataset)}")


def _load_dd_rows_from_parquet_artifacts(
    artifact_path: Path,
    *,
    dataset_name: str,
    expected_rows: int,
    allow_partial: bool = False,
) -> list[dict[str, Any]] | None:
    """Salvage completed DD parquet when ``load_dataset()`` times out post-generate.

    NeMo Data Designer often finishes generation + writes parquet, then hangs on
    ``Measuring dataset column statistics`` / ``load_dataset``. Prefer on-disk
    batches over re-burning the full LLM batch.

    When the provider drops rows (rate-limit / timeout salvage), parquet may be
    shorter than ``expected_rows``. Pass ``allow_partial=True`` to keep those
    rows for key-aligned checkpointing + resume.
    """
    base = artifact_path / dataset_name / "parquet-files"
    if not base.is_dir():
        return None
    parts = sorted(base.glob("*.parquet"))
    if not parts:
        return None
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError:
        return None
    tables = [pq.read_table(p) for p in parts]
    if not tables:
        return None
    table = pa.concat_tables(tables) if len(tables) > 1 else tables[0]
    rows = table.to_pylist()
    if not rows:
        return None
    if expected_rows and len(rows) != expected_rows and not allow_partial:
        return None
    return [dict(row) for row in rows]


def _archive_data_designer_dataset(artifact_path: Path, dataset_name: str) -> Path | None:
    """Move a prior DD dataset aside so resume batches do not mix with old parquet."""
    src = artifact_path / dataset_name
    if not src.exists():
        return None
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    dest = artifact_path / f"{dataset_name}.prev_{stamp}"
    shutil.move(str(src), str(dest))
    print(f"[s4] archived prior Data Designer artifacts → {dest}", file=sys.stderr, flush=True)
    return dest


def _align_dd_rows_to_seeds(
    pending: Sequence[Mapping[str, Any]],
    dd_rows: Sequence[Mapping[str, Any]],
    *,
    output_column: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    """Match DD outputs to seeds by ``uuid__doc_slot`` (not positional zip).

    Returns ``(matched_seeds, matched_dd, unmatched_seeds)``.
    """
    by_key: dict[str, dict[str, Any]] = {}
    for raw in dd_rows:
        row = dict(raw)
        key = row_key_from_prompt(row)
        text = str(row.get(output_column) or row.get("generated_text") or "").strip()
        if not text:
            continue
        # First non-empty wins; duplicates should not happen for a single batch.
        by_key.setdefault(key, row)

    matched_seeds: list[dict[str, Any]] = []
    matched_dd: list[dict[str, Any]] = []
    unmatched: list[dict[str, Any]] = []
    for seed in pending:
        seed_row = dict(seed)
        key = row_key_from_prompt(seed_row)
        dd_row = by_key.get(key)
        if dd_row is None:
            unmatched.append(seed_row)
            continue
        matched_seeds.append(seed_row)
        matched_dd.append(dd_row)
    return matched_seeds, matched_dd, unmatched


def _load_data_designer_rows(
    results: Any,
    *,
    artifact_path: Path,
    dataset_name: str,
    expected_rows: int,
) -> list[dict[str, Any]]:
    """Load DD results; fall back to parquet if ``load_dataset`` times out."""
    try:
        dataset = results.load_dataset()
        return _dataframe_to_rows(dataset)
    except Exception as load_exc:  # noqa: BLE001 — salvage path
        salvaged = _load_dd_rows_from_parquet_artifacts(
            artifact_path,
            dataset_name=dataset_name,
            expected_rows=expected_rows,
            allow_partial=True,
        )
        if salvaged is not None:
            print(
                f"[s4] load_dataset failed ({load_exc}); "
                f"salvaged {len(salvaged)} rows from parquet artifacts",
                file=sys.stderr,
                flush=True,
            )
            return salvaged
        raise
def run_data_designer_generation(pipeline_config: Path) -> dict[str, Path]:
    """Execute S4 strictly via NeMo Data Designer with row-level checkpoints."""
    load_env_file()
    dd, DataDesigner = _import_data_designer()
    settings = load_designer_bridge_settings(pipeline_config)
    api_key = require_env(settings.provider_api_key_env)
    _ensure_provider_files(settings, api_key)

    root = load_yaml(pipeline_config)
    gen = root.get("generation") if isinstance(root.get("generation"), dict) else {}
    output_dir = resolve_repo_path(str(gen.get("output_dir", "data/generated/s4_generation")))
    output_dir.mkdir(parents=True, exist_ok=True)
    max_docs = gen.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)

    # Prefer parquet seed for Data Designer; fall back to converting JSONL.
    seed_path = settings.seed_path
    if seed_path.suffix == ".jsonl":
        parquet_seed = seed_path.with_suffix(".parquet")
        if not parquet_seed.is_file():
            rows = read_jsonl(seed_path)
            write_parquet(parquet_seed, rows)
        seed_path = parquet_seed
        # Rewrite settings seed for builder
        object.__setattr__  # placate linters — we pass path explicitly below

    prompts = read_jsonl(
        seed_path.with_suffix(".jsonl")
        if seed_path.with_suffix(".jsonl").is_file()
        else resolve_repo_path(str(gen["input_jsonl"]))
    )
    if max_docs is not None:
        prompts = prompts[:max_docs]
    if not prompts:
        raise DesignerConfigError("No prompt rows for Data Designer generation")

    checkpoint = CheckpointStore(output_dir / "checkpoint.jsonl")
    done = checkpoint.done_keys(accept_soft_fail=True)

    pending: list[dict[str, Any]] = []
    for row in prompts:
        key = row_key_from_prompt(row)
        req = request_hash(
            [
                row.get("system_prompt"),
                row.get("user_prompt"),
                settings.model_id,
                settings.temperature,
                settings.max_tokens,
            ]
        )
        existing = checkpoint.get(key)
        if existing and existing.status in {"ok", "soft_fail"} and existing.request_hash == req:
            continue
        pending.append(dict(row))

    soft_failures: list[dict[str, Any]] = []
    generated_new: list[dict[str, Any]] = []

    if pending:
        # Materialize pending seed shard for Data Designer (idempotent resume).
        pending_seed = output_dir / "pending_seed.parquet"
        write_parquet(pending_seed, pending)

        max_parallel = gen.get("max_workers")
        if max_parallel is not None:
            max_parallel = int(max_parallel)

        provider = build_model_provider(settings, api_key)
        builder = _build_config_builder(
            dd,
            settings,
            seed_path=pending_seed,
            max_parallel_requests=max_parallel,
        )

        artifact_path = output_dir / "data_designer_artifacts"
        artifact_path.mkdir(parents=True, exist_ok=True)
        # Prior underfilled batches must not mix into the next resume create/load.
        _archive_data_designer_dataset(artifact_path, "s4_generation")
        designer = DataDesigner(
            model_providers=[provider],
            artifact_path=str(artifact_path),
        )
        num_records = len(pending)
        try:
            # Health-check the named provider before spending the full batch.
            designer.check_models(builder)
            results = designer.create(
                builder,
                num_records=num_records,
                dataset_name="s4_generation",
                artifact_path=str(artifact_path),
            )
            dd_rows = _load_data_designer_rows(
                results,
                artifact_path=artifact_path,
                dataset_name="s4_generation",
                expected_rows=num_records,
            )
        except Exception as exc:  # noqa: BLE001
            # Last chance: create may have written parquet before load timed out.
            salvaged = _load_dd_rows_from_parquet_artifacts(
                artifact_path,
                dataset_name="s4_generation",
                expected_rows=num_records,
                allow_partial=True,
            )
            if salvaged is not None:
                print(
                    f"[s4] create/load failed ({exc}); "
                    f"salvaged {len(salvaged)} rows from parquet artifacts",
                    file=sys.stderr,
                    flush=True,
                )
                dd_rows = salvaged
            else:
                registered = []
                try:
                    # Never echo secrets from extra_headers / api_key into logs.
                    registered = [
                        {
                            "name": p.name,
                            "endpoint": p.endpoint,
                            "provider_type": p.provider_type,
                            "auth_style": settings.auth_style,
                            "has_extra_headers": bool(p.extra_headers),
                        }
                        for p in designer.model_provider_registry.providers
                    ]
                except Exception:  # noqa: BLE001
                    registered = []
                raise DesignerConfigError(
                    f"NeMo Data Designer generation failed: {exc}. "
                    f"Requested provider={settings.provider!r} endpoint={settings.provider_endpoint}. "
                    f"Registered providers={registered}. "
                    f"Auth style={settings.auth_style} (Sarvam needs subscription_key). "
                    f"Ensure {settings.provider_api_key_env} is set and "
                    "`data-designer` is installed (`uv sync`)."
                ) from exc

        matched_seeds, matched_dd, unmatched_seeds = _align_dd_rows_to_seeds(
            pending,
            dd_rows,
            output_column=settings.output_column,
        )
        if unmatched_seeds:
            print(
                f"[s4] Data Designer underfill: matched {len(matched_seeds)}/"
                f"{len(pending)} seeds by uuid__doc_slot; "
                f"will checkpoint matches then fail for resume "
                f"({len(unmatched_seeds)} remaining)",
                file=sys.stderr,
                flush=True,
            )

        # Targeted generator repair for known cheap issues (missing tags / stuffing)
        # instead of soft-failing immediately — cheaper than a full DD rebatch.
        repair_settings = load_repair_settings_from_generation(gen)
        repair_client: SarvamClient | None = None
        if repair_settings.max_repairs > 0 and matched_seeds:
            rpm = gen.get("requests_per_minute")
            limiter = (
                RateLimiter(float(rpm))
                if rpm is not None and float(rpm) > 0
                else None
            )
            repair_client = SarvamClient(
                api_key=api_key,
                base_url=str(gen.get("base_url") or settings.provider_endpoint),
                rate_limiter=limiter,
            )

        for seed_row, dd_row in zip(matched_seeds, matched_dd):
            text = str(dd_row.get(settings.output_column) or dd_row.get("generated_text") or "")
            key = row_key_from_prompt(seed_row)
            req = request_hash(
                [
                    seed_row.get("system_prompt"),
                    seed_row.get("user_prompt"),
                    settings.model_id,
                    settings.temperature,
                    settings.max_tokens,
                ]
            )
            required = [str(x) for x in (seed_row.get("required_entities") or [])]
            missing, stuffed, invalid = tag_issues(text, required)
            repair_attempts = 0
            repaired = False
            repair_model: str | None = None
            if (missing or stuffed or invalid) and repair_client is not None:
                result = repair_document(
                    repair_client,
                    draft=text,
                    row=seed_row,
                    required=required,
                    issues=issues_from_coverage(missing, stuffed, invalid),
                    settings=repair_settings,
                    check_script=False,
                )
                text = result.text
                repair_attempts = result.attempts
                repaired = result.repaired
                repair_model = result.model
                missing, stuffed, invalid = tag_issues(text, required)
            reasons: list[str] = []
            if invalid:
                reasons.append("invalid_type_tags:" + ",".join(invalid))
            if missing:
                reasons.append("missing_required_entities:" + ",".join(missing))
            if stuffed:
                reasons.append("entity_stuffing:" + ",".join(stuffed))
            soft = bool(reasons)
            uuid = str(seed_row["uuid"])
            doc_slot = seed_row.get("doc_slot", 0)
            out = dict(seed_row)
            out.update(
                {
                    "document_id": f"{uuid}__{doc_slot}",
                    "generated_text": text,
                    "generator_provider": (
                        "data_designer+repair" if repaired else "data_designer"
                    ),
                    "generator_model": repair_model or settings.model_id,
                    "generator_finish_reason": "data_designer",
                    "generator_prompt_tokens": None,
                    "generator_completion_tokens": None,
                    "entity_coverage_complete": len(missing) == 0 and len(invalid) == 0,
                    "missing_required_entities": missing,
                    "invalid_type_tags": invalid,
                    "entity_stuffing": len(stuffed) > 0,
                    "stuffed_entity_types": stuffed,
                    "generation_soft_fail": soft,
                    "generation_soft_fail_reasons": reasons,
                    "generation_repair_attempts": repair_attempts,
                    "generation_repaired": repaired,
                    "stage": "s4_generation",
                }
            )
            checkpoint.append(
                row_key=key,
                status="soft_fail" if soft else "ok",
                request_hash=req,
                payload=out,
                error=";".join(reasons) if reasons else None,
            )
            generated_new.append(out)
            if soft:
                soft_failures.append(
                    {
                        "uuid": out.get("uuid"),
                        "document_id": out.get("document_id"),
                        "doc_type_id": out.get("doc_type_id"),
                        "document_language_code": out.get("document_language_code"),
                        "missing_required_entities": missing,
                        "stuffed_entity_types": stuffed,
                        "reasons": reasons,
                    }
                )

        if unmatched_seeds:
            raise DesignerConfigError(
                f"Data Designer returned {len(dd_rows)} rows for {len(pending)} seeds "
                f"(checkpointed {len(matched_seeds)}; resume remaining {len(unmatched_seeds)})"
            )

    # Rebuild full ordered outputs from checkpoint (idempotent).
    by_key = {row_key_from_prompt(r): r for r in checkpoint.completed_payloads()}
    outputs: list[dict[str, Any]] = []
    for row in prompts:
        key = row_key_from_prompt(row)
        if key not in by_key:
            raise DesignerConfigError(f"Missing checkpoint payload for {key}")
        outputs.append(by_key[key])

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
        "engine": "nemo_data_designer",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider": settings.provider,
        "model": settings.model_id,
        "base_url": settings.provider_endpoint,
        "rows_requested": len(prompts),
        "rows_generated": len(outputs),
        "rows_from_checkpoint": len(done),
        "rows_newly_generated": len(generated_new),
        "soft_failures": soft_failures,
        "soft_fail_count": len(soft_failures),
        "generation_repaired_count": sum(
            1 for row in outputs if row.get("generation_repaired")
        ),
        "entity_coverage_complete_rate": (
            sum(1 for row in outputs if row.get("entity_coverage_complete")) / len(outputs)
            if outputs
            else 0.0
        ),
        "mean_chars": (
            sum(len(str(row.get("generated_text", ""))) for row in outputs) / len(outputs)
            if outputs
            else 0.0
        ),
        "checkpoint": str(output_dir / "checkpoint.jsonl"),
    }

    jsonl_path = output_dir / "documents.jsonl"
    atomic_write_jsonl(jsonl_path, outputs)
    parquet_path = output_dir / "documents.parquet"
    write_parquet(parquet_path, outputs)
    audit_json = output_dir / "audit.json"
    write_json(audit_json, audit)
    soft_path = output_dir / "soft_failures.jsonl"
    atomic_write_jsonl(soft_path, soft_failures)
    audit_md = output_dir / "audit.md"
    audit_md.write_text(
        "# Stage 4 — Generation Audit (NeMo Data Designer)\n\n"
        f"- engine: **nemo_data_designer** (required)\n"
        f"- model: `{audit['model']}`\n"
        f"- rows_generated: **{audit['rows_generated']}**\n"
        f"- rows_from_checkpoint: `{audit['rows_from_checkpoint']}`\n"
        f"- soft_fail_count: **{audit['soft_fail_count']}**\n"
        f"- generation_repaired_count: **{audit.get('generation_repaired_count', 0)}**\n"
        f"- entity_coverage_complete_rate: `{audit['entity_coverage_complete_rate']:.3f}`\n",
        encoding="utf-8",
    )
    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
        "soft_failures_jsonl": soft_path,
        "checkpoint_jsonl": output_dir / "checkpoint.jsonl",
    }


def describe_bridge() -> dict[str, Any]:
    return {
        "role": "REQUIRED S4 engine via NeMo Data Designer",
        "seed": "S3 prompts parquet (persona + taxonomy + annotation rules)",
        "curator": "REQUIRED S7 backend via NeMo Curator FuzzyDeduplicationWorkflow",
        "no_silent_fallback": True,
        "skills_aligned": [
            "data-designer (seed datasets + LLMTextColumnConfig + create())",
            "nemo-curator fuzzy dedup",
        ],
    }
