"""Stage 5 — Linguistic judge (Grok-4.3 via Azure OpenAI-compatible API).

Default: model=grok-4.3 on Azure Foundry chat/completions with Bearer auth.
Rate limits (account): 500 RPM / 500000 TPM — config enforces RPM spacing.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from main.llm.openai_compatible import (
    OpenAICompatibleClient,
    OpenAICompatibleClientError,
)
from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.llm.types import ChatResult
from main.metrics.judge_metrics import label_distribution, pass_rate, positional_length_bias
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

JUDGE_COLUMNS: tuple[str, ...] = (
    "judge_verdict",
    "judge_score",
    "judge_reasoning",
    "judge_flags",
    "judge_provider",
    "judge_model",
    "judge_soft_fail",
    "judge_error",
    "stage",
)

_JSON_BLOCK_RE = re.compile(r"\{.*\}", re.DOTALL)

# Explicit provider aliases — no silent remap beyond this set.
_OPENAI_COMPAT_PROVIDERS = frozenset(
    {"openai_compatible", "azure", "azure_foundry", "grok"}
)
_SARVAM_PROVIDERS = frozenset({"sarvam"})


class _ChatClient(Protocol):
    def chat_completion(self, **kwargs: Any) -> ChatResult: ...


@dataclass(frozen=True)
class JudgeSettings:
    provider: str
    input_jsonl: Path
    output_dir: Path
    model: str
    base_url: str
    api_key_env: str
    api_key_env_fallbacks: tuple[str, ...]
    temperature: float
    max_tokens: int
    max_tokens_field: str
    reasoning_effort: str | None
    timeout_s: float
    max_docs: int | None
    pass_threshold: float
    requests_per_minute: float | None
    entities_config: Path | None
    network_retries: int


class JudgeError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> JudgeSettings:
    root = load_yaml(pipeline_config)
    block = root.get("linguistic_judge")
    if not isinstance(block, dict):
        raise ValueError(f"'linguistic_judge' mapping required in {pipeline_config}")

    required = (
        "provider",
        "input_jsonl",
        "output_dir",
        "model",
        "base_url",
        "api_key_env",
        "temperature",
        "max_tokens",
        "pass_threshold",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing linguistic_judge keys {missing}")

    provider = str(block["provider"]).strip().lower()
    if provider not in _OPENAI_COMPAT_PROVIDERS | _SARVAM_PROVIDERS:
        raise JudgeError(
            f"Unsupported linguistic_judge.provider={provider!r}. "
            f"Use one of: {sorted(_OPENAI_COMPAT_PROVIDERS | _SARVAM_PROVIDERS)}"
        )

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    reasoning_effort = block.get("reasoning_effort")
    if reasoning_effort is not None:
        reasoning_effort = str(reasoning_effort)

    rpm = block.get("requests_per_minute")
    if rpm is not None:
        rpm = float(rpm)
        if rpm <= 0:
            raise ValueError("requests_per_minute must be > 0 when set")

    fallbacks_raw = block.get("api_key_env_fallbacks") or []
    if not isinstance(fallbacks_raw, list):
        raise ValueError("api_key_env_fallbacks must be a list when set")

    max_tokens_field = str(block.get("max_tokens_field", "max_tokens"))
    if max_tokens_field not in {"max_tokens", "max_completion_tokens"}:
        raise ValueError(f"Unsupported max_tokens_field={max_tokens_field!r}")

    entities_config = block.get("entities_config")
    entities_path = (
        resolve_repo_path(str(entities_config)) if entities_config is not None else None
    )

    return JudgeSettings(
        provider=provider,
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        model=str(block["model"]),
        base_url=str(block["base_url"]),
        api_key_env=str(block["api_key_env"]),
        api_key_env_fallbacks=tuple(str(item) for item in fallbacks_raw),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        max_tokens_field=max_tokens_field,
        reasoning_effort=reasoning_effort,
        timeout_s=float(block.get("timeout_s", 600)),
        max_docs=max_docs,
        pass_threshold=float(block["pass_threshold"]),
        requests_per_minute=rpm,
        entities_config=entities_path,
        network_retries=max(0, int(block.get("network_retries", 4))),
    )


def build_client(settings: JudgeSettings, api_key: str) -> _ChatClient:
    limiter = (
        RateLimiter(settings.requests_per_minute)
        if settings.requests_per_minute is not None
        else None
    )
    if settings.provider in _SARVAM_PROVIDERS:
        return SarvamClient(
            api_key=api_key, base_url=settings.base_url, rate_limiter=limiter
        )
    return OpenAICompatibleClient(
        api_key=api_key,
        base_url=settings.base_url,
        rate_limiter=limiter,
        max_tokens_field=settings.max_tokens_field,
    )


def load_entity_allow_list(path: Path | None) -> tuple[str, ...]:
    if path is None:
        return ()
    root = load_yaml(path)
    raw = root.get("entities")
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"'entities' list required in {path}")
    ids: list[str] = []
    for entry in raw:
        if not isinstance(entry, dict) or "id" not in entry:
            raise ValueError(f"Invalid entity entry in {path}: {entry!r}")
        ids.append(str(entry["id"]))
    return tuple(sorted(ids))


def build_judge_messages(
    row: Mapping[str, Any],
    *,
    allow_list: Sequence[str] = (),
) -> list[dict[str, str]]:
    allow_block = (
        "ENTITY TYPE ALLOW-LIST (ONLY these TYPE names are valid; do NOT flag them "
        "as invented_entity_type):\n"
        + ", ".join(allow_list)
        + "\n"
        if allow_list
        else ""
    )
    system = (
        "You are a strict linguistic auditor for synthetic Indic clinical text. "
        "Return ONLY a JSON object with keys: "
        "verdict (pass|fail), score (0-1 float), "
        "flags (array of strings from: instruction_drift, cross_language_entity_shift, "
        "surrogate_plausibility_collapse, dialect_script_impurity, "
        "domain_persona_mismatch, invented_entity_type, length_violation, other), "
        "reasoning (short string).\n\n"
        "Rubric (important):\n"
        "- Clinical PROSE should be in the expected language/script. "
        "Latin/digits inside [[TYPE|value]] for IDs (Aadhaar, PAN, phone, MRN, "
        "IFSC, email, policy/admission numbers, PIN, bed/ward) are EXPECTED — "
        "do NOT flag dialect_script_impurity for those.\n"
        "- Drug names, lab analyte names, and ICD-like codes may stay Latin; "
        "do not flag impurity for them.\n"
        "- Flag dialect_script_impurity only when clinical narrative prose is "
        "mostly wrong language/script (e.g. English body when Tamil was required).\n"
        "- Flag domain_persona_mismatch for sex/age vs clinical content "
        "(e.g. male maternal delivery; age 70 paediatric; geriatric maternal SMS).\n"
        "- Flag invented_entity_type ONLY for TYPE names outside the allow-list "
        "(e.g. DATE, TIME, APPOINTMENT_DATE, POLICY_NUMBER). "
        "PATIENT_NAME / HOSPITAL_NAME / DOCTOR_NAME / MRN etc. are valid if listed.\n"
        "- Flag length_violation if automated_sms is a long chart dump "
        "(>> ~400 chars / many paragraphs).\n"
        "- cross_language_entity_shift: only when PERSON/PLACE name tags are "
        "clearly wrong script for the document AND not culturally plausible.\n"
        f"{allow_block}"
    )
    user = (
        f"Document language expected: {row.get('document_language_name')} "
        f"({row.get('document_language_code')}, script={row.get('document_script')}).\n"
        f"Doc type: {row.get('doc_type_name')}\n"
        f"Domain: {row.get('domain_name')}\n"
        f"Persona anchors: sex={row.get('sex')}, age={row.get('age')}, "
        f"state={row.get('state')}, district={row.get('district')}.\n\n"
        f"Generated text:\n{row.get('generated_text')}\n\n"
        "Score instruction adherence, domain×persona fit, surrogate plausibility, "
        "and prose language/script — remembering Latin IDs inside tags are fine "
        "and allow-listed TYPE names are not invented."
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def parse_judge_response(content: str, *, pass_threshold: float) -> dict[str, Any]:
    match = _JSON_BLOCK_RE.search(content)
    if not match:
        raise JudgeError(f"Judge response missing JSON object: {content[:400]!r}")
    try:
        payload = json.loads(match.group(0))
    except json.JSONDecodeError as exc:
        raise JudgeError(f"Judge JSON parse failed: {exc}") from exc

    if "score" not in payload:
        raise JudgeError(f"Judge JSON missing score: {payload!r}")
    if "verdict" not in payload:
        raise JudgeError(f"Judge JSON missing verdict: {payload!r}")

    score = float(payload["score"])
    if score < 0.0 or score > 1.0:
        raise JudgeError(f"Judge score out of range: {score}")

    verdict = str(payload["verdict"]).strip().lower()
    if verdict not in {"pass", "fail"}:
        raise JudgeError(f"Judge verdict must be pass|fail, got {payload['verdict']!r}")

    if verdict == "pass" and score < pass_threshold:
        verdict = "fail"

    flags = payload.get("flags", [])
    if not isinstance(flags, list):
        raise JudgeError("Judge flags must be a list")
    flags_t = [str(item) for item in flags]
    reasoning = str(payload.get("reasoning", "")).strip()
    return {
        "judge_verdict": verdict,
        "judge_score": score,
        "judge_flags": flags_t,
        "judge_reasoning": reasoning,
    }


def _call_judge(
    client: _ChatClient,
    *,
    settings: JudgeSettings,
    messages: list[dict[str, str]],
) -> ChatResult:
    if settings.provider in _SARVAM_PROVIDERS:
        return client.chat_completion(
            model=settings.model,
            messages=messages,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            reasoning_effort=settings.reasoning_effort,
            timeout_s=settings.timeout_s,
        )
    return client.chat_completion(
        model=settings.model,
        messages=messages,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
        timeout_s=settings.timeout_s,
    )


def _is_retryable_judge_error(exc: BaseException) -> bool:
    message = str(exc).lower()
    needles = (
        "timed out",
        "timeout",
        "temporary failure",
        "name resolution",
        "connection reset",
        "connection refused",
        "network error",
        "os/network",
        "http 429",
        "rate limit",
        "http 502",
        "http 503",
        "http 504",
        "remote disconnected",
    )
    return any(item in message for item in needles)


def judge_documents(
    rows: Sequence[Mapping[str, Any]],
    *,
    client: _ChatClient,
    settings: JudgeSettings,
    checkpoint: CheckpointStore | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise JudgeError("No rows selected for linguistic judge")

    allow_list = load_entity_allow_list(settings.entities_config)
    outputs: list[dict[str, Any]] = []
    soft_failures: list[dict[str, Any]] = []
    attempts_per_row = settings.network_retries + 1
    resumed = 0

    for index, row in enumerate(selected):
        if "generated_text" not in row:
            raise JudgeError(f"Row {index} missing generated_text")

        key = row_key_from_prompt(row)
        req = request_hash(
            [
                row.get("generated_text"),
                row.get("document_language_code"),
                settings.model,
                settings.pass_threshold,
                sorted(allow_list),
            ]
        )
        if checkpoint is not None:
            existing = checkpoint.get(key)
            if (
                existing
                and existing.status in {"ok", "soft_fail"}
                and existing.request_hash == req
                and existing.payload
            ):
                out = dict(existing.payload)
                outputs.append(out)
                if out.get("judge_soft_fail"):
                    soft_failures.append(
                        {
                            "uuid": out.get("uuid"),
                            "document_id": out.get("document_id"),
                            "doc_type_id": out.get("doc_type_id"),
                            "document_language_code": out.get(
                                "document_language_code"
                            ),
                            "judge_error": out.get("judge_error"),
                        }
                    )
                resumed += 1
                continue

        result: ChatResult | None = None
        parsed: dict[str, Any] | None = None
        last_error: Exception | None = None
        for attempt in range(attempts_per_row):
            try:
                result = _call_judge(
                    client,
                    settings=settings,
                    messages=build_judge_messages(row, allow_list=allow_list),
                )
                parsed = parse_judge_response(
                    result.content, pass_threshold=settings.pass_threshold
                )
                last_error = None
                break
            except (
                SarvamClientError,
                OpenAICompatibleClientError,
                JudgeError,
                TimeoutError,
                OSError,
            ) as exc:
                last_error = exc
                if _is_retryable_judge_error(exc) and attempt < attempts_per_row - 1:
                    delay = min(30.0, 2.0 ** attempt)
                    print(
                        f"[s5] retry {attempt + 1}/{attempts_per_row - 1} "
                        f"uuid={row.get('uuid')} after {delay:.0f}s: {exc}",
                        file=sys.stderr,
                    )
                    time.sleep(delay)
                    continue
                if _is_retryable_judge_error(exc):
                    # Soft-fail this row so the rest of the corpus still judges.
                    break
                raise JudgeError(
                    f"Judge failed at row {index} uuid={row.get('uuid')!r}: {exc}"
                ) from exc

        out = dict(row)
        status = "ok"
        if parsed is not None and result is not None:
            out.update(parsed)
            out.update(
                {
                    "judge_provider": settings.provider,
                    "judge_model": result.model,
                    "judge_soft_fail": False,
                    "judge_error": None,
                    "stage": "s5_linguistic_judge",
                }
            )
        else:
            assert last_error is not None
            err = str(last_error)
            print(
                f"[s5] SOFT-FAIL uuid={row.get('uuid')} doc_type={row.get('doc_type_id')} "
                f"error={err}",
                file=sys.stderr,
            )
            soft_failures.append(
                {
                    "uuid": row.get("uuid"),
                    "document_id": row.get("document_id"),
                    "doc_type_id": row.get("doc_type_id"),
                    "document_language_code": row.get("document_language_code"),
                    "judge_error": err,
                }
            )
            out.update(
                {
                    "judge_verdict": "fail",
                    "judge_score": 0.0,
                    "judge_flags": ["judge_network_error"],
                    "judge_reasoning": (
                        f"Soft-fail after {attempts_per_row} attempts "
                        f"(timeout/network). Logged — not silent. error={err}"
                    ),
                    "judge_provider": settings.provider,
                    "judge_model": settings.model,
                    "judge_soft_fail": True,
                    "judge_error": err,
                    "stage": "s5_linguistic_judge",
                }
            )
            status = "soft_fail"
        outputs.append(out)
        if checkpoint is not None:
            checkpoint.append(
                row_key=key,
                status=status,
                request_hash=req,
                payload=out,
                error=out.get("judge_error"),
            )

    verdicts = [str(row["judge_verdict"]) for row in outputs]
    failures = [
        {
            "uuid": row.get("uuid"),
            "document_id": row.get("document_id"),
            "doc_type_id": row.get("doc_type_id"),
            "document_language_code": row.get("document_language_code"),
            "judge_verdict": row.get("judge_verdict"),
            "judge_score": row.get("judge_score"),
            "judge_flags": row.get("judge_flags"),
            "judge_rationale": row.get("judge_reasoning"),
            "judge_soft_fail": row.get("judge_soft_fail"),
            "judge_error": row.get("judge_error"),
        }
        for row in outputs
        if str(row.get("judge_verdict")) != "pass"
    ]
    audit = {
        "stage": "s5_linguistic_judge",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider": settings.provider,
        "model": settings.model,
        "base_url": settings.base_url,
        "requests_per_minute": settings.requests_per_minute,
        "timeout_s": settings.timeout_s,
        "network_retries": settings.network_retries,
        "rows_judged": len(outputs),
        "rows_resumed_from_checkpoint": resumed,
        "pass_rate": pass_rate(verdicts),
        "label_distribution": label_distribution(verdicts),
        "positional_length_bias": positional_length_bias(outputs),
        "failures": failures,
        "failure_count": len(failures),
        "soft_failures": soft_failures,
        "soft_fail_count": len(soft_failures),
        "columns_added": list(JUDGE_COLUMNS),
    }
    if soft_failures:
        print(
            f"[s5] WARNING: {len(soft_failures)} judge network soft-fail(s) logged "
            "— see audit soft_failures / failed.jsonl",
            file=sys.stderr,
        )
    if failures:
        print(
            f"[s5] WARNING: {len(failures)} judge fail(s) logged "
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
    passed = [row for row in rows if row["judge_verdict"] == "pass"]
    failed = [row for row in rows if row["judge_verdict"] != "pass"]

    paths = {
        "all_jsonl": output_dir / "judged.jsonl",
        "passed_jsonl": output_dir / "passed.jsonl",
        "failed_jsonl": output_dir / "failed.jsonl",
        "parquet": output_dir / "judged.parquet",
        "audit_json": output_dir / "audit.json",
        "audit_md": output_dir / "audit.md",
    }
    atomic_write_jsonl(paths["all_jsonl"], rows)
    atomic_write_jsonl(paths["passed_jsonl"], passed)
    atomic_write_jsonl(paths["failed_jsonl"], failed)
    write_parquet(paths["parquet"], rows)
    write_json(paths["audit_json"], audit)
    soft_fail_path = output_dir / "soft_failures.jsonl"
    write_jsonl(soft_fail_path, audit.get("soft_failures") or [])
    paths["soft_failures_jsonl"] = soft_fail_path
    failures = audit.get("failures") or []
    failure_block = ""
    if failures:
        failure_block = "\n## Failures (audited — not silent)\n\n" + "\n".join(
            f"- `{item.get('uuid')}` · `{item.get('doc_type_id')}` · "
            f"`{item.get('document_language_code')}` · "
            f"score={item.get('judge_score')} soft={item.get('judge_soft_fail')} · "
            f"{item.get('judge_rationale')}"
            for item in failures
        )
        failure_block += "\n"
    soft = audit.get("soft_failures") or []
    soft_block = ""
    if soft:
        soft_block = "\n## Network soft-fails\n\n" + "\n".join(
            f"- `{item.get('uuid')}` · `{item.get('doc_type_id')}` · "
            f"`{item.get('judge_error')}`"
            for item in soft
        )
        soft_block += "\n"
    paths["audit_md"].write_text(
        "# Stage 5 — Linguistic Judge Audit\n\n"
        f"- provider/model: `{audit['provider']}` / `{audit['model']}`\n"
        f"- requests_per_minute: `{audit['requests_per_minute']}`\n"
        f"- timeout_s: `{audit.get('timeout_s')}`\n"
        f"- network_retries: `{audit.get('network_retries')}`\n"
        f"- rows_judged: **{audit['rows_judged']}**\n"
        f"- soft_fail_count: **{audit.get('soft_fail_count', 0)}**\n"
        f"- failure_count: **{audit.get('failure_count', 0)}**\n"
        f"- pass_rate: **{audit['pass_rate']:.3f}**\n"
        f"- label_distribution: `{audit['label_distribution']}`\n"
        f"- positional_length_bias: `{audit['positional_length_bias']}`\n"
        f"{soft_block}{failure_block}",
        encoding="utf-8",
    )
    return paths


def run(pipeline_config: Path) -> dict[str, Path]:
    load_env_file()
    settings = load_settings(pipeline_config)
    api_key = require_env(
        settings.api_key_env, fallbacks=settings.api_key_env_fallbacks
    )
    client = build_client(settings, api_key)
    rows = read_jsonl(settings.input_jsonl)
    checkpoint = CheckpointStore(settings.output_dir / "checkpoint.jsonl")
    judged, audit = judge_documents(
        rows, client=client, settings=settings, checkpoint=checkpoint
    )
    return write_outputs(judged, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 5: linguistic judge")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (
        JudgeError,
        ValueError,
        FileNotFoundError,
        SarvamClientError,
        OpenAICompatibleClientError,
    ) as exc:
        print(f"[s5] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s5] Linguistic judge complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
