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
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Protocol, Sequence

from main.designers.entity_checks import (
    SOFT_JUDGE_FLAGS,
    normalize_inline_entity_tags,
)
from main.designers.persona_tag_patch import (
    apply_persona_tag_patch,
    locked_surrogates,
    persona_flags_present,
)
from main.designers.repair import (
    clear_upstream_soft_fail_fields,
    issues_from_judge_flags,
    load_repair_settings_from_generation,
    merge_repair_issues,
    repair_document,
    RepairIssue,
    RepairSettings,
)
from main.designers.translator import (
    TranslationSettings,
    translate_english_once,
)
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
    "judge_repair_attempts",
    "judge_repaired",
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
    max_workers: int = 24
    must_work_languages: tuple[str, ...] = ()
    rare_script_languages: tuple[str, ...] = ()


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

    max_workers = int(block.get("max_workers", 24))
    if max_workers < 1:
        raise ValueError("max_workers must be >= 1")

    def _lang_tuple(key: str) -> tuple[str, ...]:
        raw = block.get(key) or []
        if not isinstance(raw, list):
            raise ValueError(f"{key} must be a list when set")
        return tuple(str(x).strip() for x in raw if str(x).strip())

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
        max_workers=max_workers,
        must_work_languages=_lang_tuple("must_work_languages"),
        rare_script_languages=_lang_tuple("rare_script_languages"),
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
        "(e.g. male maternal delivery; age 70 paediatric; extreme-age routine "
        "mid-trimester pregnancy — unsafe / not age-plausible).\n"
        "- invented_entity_type is SOFT for billing/admin extras: do NOT fail "
        "solely for EMAIL/CONTACT_EMAIL/ADDRESS_NUMBER/RECEIPT_NUMBER/STATE/"
        "money-amount invents when required allow-list tags + script/domain are fine. "
        "You may list invented_entity_type as an advisory flag; map aliases mentally "
        "to EMAIL_ADDRESS / RESIDENTIAL_ADDRESS; receipt/state/money belong in prose. "
        "Still fail for invent storms that replace required types, or missing required tags.\n"
        "- Flag invented_entity_type ONLY for TYPE names outside the allow-list "
        "(e.g. DATE, TIME, APPOINTMENT_DATE, POLICY_NUMBER) — and treat billing "
        "near-misses as soft as above. "
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

    # Soft: invented_entity_type alone must not fail an otherwise-OK doc.
    hard_flags = [f for f in flags_t if f not in SOFT_JUDGE_FLAGS]
    if (
        verdict == "fail"
        and score >= pass_threshold
        and flags_t
        and not hard_flags
    ):
        verdict = "pass"

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



def _judge_one_row(
    index: int,
    row: Mapping[str, Any],
    *,
    client: _ChatClient,
    settings: JudgeSettings,
    allow_list: Sequence[str],
    repair_client: SarvamClient | None,
    repair_settings: RepairSettings | None,
    translation_settings: TranslationSettings | None,
    max_quality_repairs: int,
    multi_constraint: bool,
    via_english_pivot: bool,
    attempts_per_row: int,
    total_rows: int,
) -> tuple[dict[str, Any], str, dict[str, Any] | None, bool, int]:
    """Judge + optional repair for one row. Thread-safe (no shared mutables)."""
    working = dict(row)
    text0 = str(working.get("generated_text") or "")
    normalized, norm_notes = normalize_inline_entity_tags(text0)
    if norm_notes:
        working["generated_text"] = normalized
        working["entity_tag_normalize_notes"] = norm_notes
    result: ChatResult | None = None
    parsed: dict[str, Any] | None = None
    last_error: Exception | None = None
    repair_attempts = 0
    repaired = False
    en_pivot_delta = 0
    accumulated_issues: list[RepairIssue] = []
    accumulated_flags: list[str] = []
    rare_dedicated_tried = False
    print(
        f"[s5] judging {index + 1}/{total_rows} "
        f"uuid={working.get('uuid')} lang={working.get('document_language_code')} "
        f"doc_type={working.get('doc_type_id')}",
        file=sys.stderr,
        flush=True,
    )

    for quality_round in range(max_quality_repairs + 1):
        result = None
        parsed = None
        last_error = None
        for attempt in range(attempts_per_row):
            try:
                result = _call_judge(
                    client,
                    settings=settings,
                    messages=build_judge_messages(working, allow_list=allow_list),
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
                        f"uuid={working.get('uuid')} after {delay:.0f}s: {exc}",
                        file=sys.stderr,
                        flush=True,
                    )
                    time.sleep(delay)
                    continue
                if _is_retryable_judge_error(exc):
                    break
                raise JudgeError(
                    f"Judge failed at row {index} uuid={working.get('uuid')!r}: {exc}"
                ) from exc

        if parsed is None:
            break

        if parsed["judge_verdict"] == "pass":
            if quality_round > 0:
                repaired = True
                print(
                    f"[s5] REPAIRED-THEN-PASS uuid={working.get('uuid')} "
                    f"rounds={repair_attempts} score={parsed['judge_score']}",
                    file=sys.stderr,
                    flush=True,
                )
            break

        flags = [str(f) for f in (parsed.get("judge_flags") or [])]
        repair_flags = [f for f in flags if f not in SOFT_JUDGE_FLAGS]
        issues = issues_from_judge_flags(
            repair_flags,
            reasoning=str(parsed.get("judge_reasoning") or ""),
            row=working,
        )
        if multi_constraint:
            accumulated_issues = merge_repair_issues(accumulated_issues, issues)
            issues = accumulated_issues
            accumulated_flags = sorted(set(accumulated_flags) | set(flags))
        else:
            accumulated_flags = list(flags)

        if not issues or repair_client is None or repair_settings is None:
            break

        required = [str(x) for x in (working.get("required_entities") or [])]
        if str(working.get("doc_type_id") or "") == "lab_report":
            required = [t for t in required if t != "STUDENT_ID"]
        lang = str(working.get("document_language_code") or "")
        rare_langs = set(settings.rare_script_languages or ())
        is_rare = lang in rare_langs
        # Persona path: tag-only patch then at most one LLM (2 repairs total).
        # Other flags keep configured max; rare still capped at 2.
        has_persona = persona_flags_present(accumulated_flags or flags)
        if has_persona and not any(
            f
            in {
                "dialect_script_impurity",
                "cross_language_entity_shift",
                "instruction_drift",
                "invented_entity_type",
                "length_violation",
            }
            for f in (accumulated_flags or flags)
        ):
            row_max_repairs = min(2, max_quality_repairs)
        else:
            row_max_repairs = (
                min(2, max_quality_repairs) if is_rare else max_quality_repairs
            )

        # First persona fail → tag-only patch (no LLM), then re-judge.
        if (
            has_persona
            and not working.get("_persona_tag_patched")
            and quality_round < row_max_repairs
        ):
            patched, notes = apply_persona_tag_patch(
                str(working.get("generated_text") or ""),
                working,
            )
            working["_persona_tag_patched"] = True
            repair_attempts += 1
            if notes:
                working["generated_text"] = patched
                working["persona_tag_patch_notes"] = notes
                # Also patch EN pivot so later translate stays consistent.
                en_src = str(working.get("generated_text_en") or "")
                if en_src.strip():
                    en_patched, en_notes = apply_persona_tag_patch(en_src, working)
                    if en_notes:
                        working["generated_text_en"] = en_patched
                clear_upstream_soft_fail_fields(working)
                print(
                    f"[s5] persona tag-only patch "
                    f"uuid={working.get('uuid')} changes={notes[:6]}",
                    file=sys.stderr,
                    flush=True,
                )
                continue
            # No tag changes possible — fall through to LLM with locked values.

        if quality_round >= row_max_repairs:
            if (
                is_rare
                and not rare_dedicated_tried
                and translation_settings is not None
                and any(
                    f in {"dialect_script_impurity", "cross_language_entity_shift"}
                    for f in accumulated_flags
                )
            ):
                from main.designers.translator import try_dedicated_translate_fallback

                rare_dedicated_tried = True
                en_draft = str(
                    working.get("generated_text_en")
                    or working.get("generated_text")
                    or ""
                )
                ded_text, ded_err, ded_ok = try_dedicated_translate_fallback(
                    client=repair_client,
                    english_text=en_draft,
                    row=working,
                    settings=translation_settings,
                )
                if ded_text:
                    working["generated_text"] = ded_text
                    if ded_ok:
                        print(
                            f"[s5] rare dedicated /translate "
                            f"uuid={working.get('uuid')} lang={lang}",
                            file=sys.stderr,
                            flush=True,
                        )
                    else:
                        print(
                            f"[s5] rare dedicated soft "
                            f"uuid={working.get('uuid')} err={ded_err}",
                            file=sys.stderr,
                            flush=True,
                        )
                    continue
            break

        use_en_pivot = (
            via_english_pivot
            and lang not in {"en", "en_IN", ""}
            and translation_settings is not None
        )
        script_related = any(
            f in {"dialect_script_impurity", "cross_language_entity_shift"}
            for f in accumulated_flags
        )
        check_script = (not use_en_pivot) and (
            script_related or (multi_constraint and lang not in {"en", "en_IN", ""})
        )
        print(
            f"[s5] repair {quality_round + 1}/{max_quality_repairs} "
            f"uuid={working.get('uuid')} flags={flags}"
            + (
                f" accumulated={accumulated_flags}"
                if multi_constraint and accumulated_flags != flags
                else ""
            )
            + (" via=en_pivot+translate" if use_en_pivot else "")
            + (" persona_llm" if has_persona else ""),
            file=sys.stderr,
            flush=True,
        )
        one_shot = RepairSettings(
            model=repair_settings.model,
            temperature=repair_settings.temperature,
            max_tokens=repair_settings.max_tokens,
            reasoning_effort=repair_settings.reasoning_effort,
            timeout_s=repair_settings.timeout_s,
            max_repairs=1,
            multi_constraint=repair_settings.multi_constraint,
            via_english_pivot=repair_settings.via_english_pivot,
        )
        locks = locked_surrogates(working) if has_persona else None
        if use_en_pivot:
            en_draft = str(
                working.get("generated_text_en")
                or working.get("generated_text")
                or ""
            )
            fix = repair_document(
                repair_client,
                draft=en_draft,
                row=working,
                required=required,
                issues=issues,
                settings=one_shot,
                check_script=False,
                locked_surrogates=locks,
            )
            repair_attempts += 1
            if fix.text.strip():
                working["generated_text_en"] = fix.text
                translated, tr_err = translate_english_once(
                    repair_client,
                    english_text=fix.text,
                    row=working,
                    settings=translation_settings,
                    retry_harder=True,
                )
                if translated:
                    working["generated_text"] = translated
                    en_pivot_delta += 1
                    if tr_err:
                        print(
                            f"[s5] en_pivot translate soft "
                            f"uuid={working.get('uuid')} err={tr_err}",
                            file=sys.stderr,
                            flush=True,
                        )
                else:
                    working["generated_text"] = fix.text
                    print(
                        f"[s5] en_pivot translate failed "
                        f"uuid={working.get('uuid')} err={tr_err}",
                        file=sys.stderr,
                        flush=True,
                    )
                clear_upstream_soft_fail_fields(working)
        else:
            fix = repair_document(
                repair_client,
                draft=str(working.get("generated_text") or ""),
                row=working,
                required=required,
                issues=issues,
                settings=one_shot,
                check_script=check_script,
                locked_surrogates=locks,
            )
            repair_attempts += 1
            if fix.text.strip():
                working["generated_text"] = fix.text
                clear_upstream_soft_fail_fields(working)

        fixed_text = str(working.get("generated_text") or "")
        fixed_norm, fixed_notes = normalize_inline_entity_tags(fixed_text)
        if fixed_notes:
            working["generated_text"] = fixed_norm
            prev = list(working.get("entity_tag_normalize_notes") or [])
            working["entity_tag_normalize_notes"] = list(
                dict.fromkeys([*prev, *fixed_notes])
            )

    out = dict(working)
    out.pop("_persona_tag_patched", None)
    status = "ok"
    soft_entry: dict[str, Any] | None = None
    if parsed is not None and result is not None:
        out.update(parsed)
        out.update(
            {
                "judge_provider": settings.provider,
                "judge_model": result.model,
                "judge_soft_fail": False,
                "judge_error": None,
                "judge_repair_attempts": repair_attempts,
                "judge_repaired": repaired,
                "stage": "s5_linguistic_judge",
            }
        )
        print(
            f"[s5] done {index + 1}/{total_rows} "
            f"verdict={out.get('judge_verdict')} score={out.get('judge_score')} "
            f"repairs={repair_attempts}",
            file=sys.stderr,
            flush=True,
        )
    else:
        assert last_error is not None
        err = str(last_error)
        print(
            f"[s5] SOFT-FAIL uuid={working.get('uuid')} "
            f"doc_type={working.get('doc_type_id')} error={err}",
            file=sys.stderr,
            flush=True,
        )
        soft_entry = {
            "uuid": working.get("uuid"),
            "document_id": working.get("document_id"),
            "doc_type_id": working.get("doc_type_id"),
            "document_language_code": working.get("document_language_code"),
            "judge_error": err,
        }
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
                "judge_repair_attempts": repair_attempts,
                "judge_repaired": False,
                "stage": "s5_linguistic_judge",
            }
        )
        # Transport blips must not stick — resume retries (same policy as S4b).
        status = (
            "hard_fail"
            if _is_retryable_judge_error(last_error)
            else "soft_fail"
        )
    return out, status, soft_entry, repaired, en_pivot_delta


def judge_documents(
    rows: Sequence[Mapping[str, Any]],
    *,
    client: _ChatClient,
    settings: JudgeSettings,
    checkpoint: CheckpointStore | None = None,
    repair_client: SarvamClient | None = None,
    repair_settings: RepairSettings | None = None,
    translation_settings: TranslationSettings | None = None,
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
    repaired_count = 0
    en_pivot_repair_count = 0
    max_quality_repairs = (
        repair_settings.max_repairs
        if repair_settings is not None and repair_client is not None
        else 0
    )
    multi_constraint = bool(
        repair_settings is not None and repair_settings.multi_constraint
    )
    via_english_pivot = bool(
        repair_settings is not None and repair_settings.via_english_pivot
    )


    results_by_index: dict[int, dict[str, Any]] = {}
    pending: list[tuple[int, Mapping[str, Any], str, str]] = []
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
                results_by_index[index] = out
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
        pending.append((index, row, key, req))

    workers = min(settings.max_workers, max(1, len(pending))) if pending else 1
    print(
        f"[s5] start rows={len(selected)} pending={len(pending)} "
        f"resumed={resumed} workers={workers} "
        f"timeout_s={settings.timeout_s} model={settings.model}",
        file=sys.stderr,
        flush=True,
    )
    done_count = 0
    if pending:
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(
                    _judge_one_row,
                    index,
                    row,
                    client=client,
                    settings=settings,
                    allow_list=allow_list,
                    repair_client=repair_client,
                    repair_settings=repair_settings,
                    translation_settings=translation_settings,
                    max_quality_repairs=max_quality_repairs,
                    multi_constraint=multi_constraint,
                    via_english_pivot=via_english_pivot,
                    attempts_per_row=attempts_per_row,
                    total_rows=len(selected),
                ): (index, key, req)
                for index, row, key, req in pending
            }
            for future in as_completed(futures):
                index, key, req = futures[future]
                row = selected[index]
                try:
                    out, status, soft_entry, repaired, en_pivot_delta = future.result()
                except Exception as exc:  # noqa: BLE001 — one row must not kill stage
                    err = str(exc)
                    print(
                        f"[s5] SOFT-FAIL uuid={row.get('uuid')} "
                        f"lang={row.get('document_language_code')} "
                        f"doc_type={row.get('doc_type_id')} error=row_exception:{err}",
                        file=sys.stderr,
                        flush=True,
                    )
                    soft_entry = {
                        "uuid": row.get("uuid"),
                        "document_id": row.get("document_id"),
                        "doc_type_id": row.get("doc_type_id"),
                        "document_language_code": row.get("document_language_code"),
                        "judge_error": err,
                    }
                    out = dict(row)
                    out.update(
                        {
                            "judge_verdict": "fail",
                            "judge_score": 0.0,
                            "judge_flags": ["judge_network_error"],
                            "judge_reasoning": (
                                f"Soft-fail after worker exception. "
                                f"Logged — not silent. error={err}"
                            ),
                            "judge_provider": settings.provider,
                            "judge_model": settings.model,
                            "judge_soft_fail": True,
                            "judge_error": err,
                            "judge_repair_attempts": 0,
                            "judge_repaired": False,
                            "stage": "s5_linguistic_judge",
                        }
                    )
                    status = (
                        "hard_fail"
                        if _is_retryable_judge_error(exc)
                        else "soft_fail"
                    )
                    repaired = False
                    en_pivot_delta = 0
                results_by_index[index] = out
                if soft_entry is not None:
                    soft_failures.append(soft_entry)
                if repaired:
                    repaired_count += 1
                en_pivot_repair_count += en_pivot_delta
                if checkpoint is not None:
                    checkpoint.append(
                        row_key=key,
                        status=status,
                        request_hash=req,
                        payload=out,
                        error=out.get("judge_error"),
                    )
                done_count += 1
                if done_count == 1 or done_count % 5 == 0 or done_count == len(pending):
                    print(
                        f"[s5] progress {done_count}/{len(pending)} "
                        f"uuid={out.get('uuid')} lang={out.get('document_language_code')} "
                        f"verdict={out.get('judge_verdict')} soft={bool(out.get('judge_soft_fail'))}",
                        file=sys.stderr,
                        flush=True,
                    )

    outputs = [results_by_index[i] for i in range(len(selected))]
    network_fail_n = sum(
        1
        for row in outputs
        if "judge_network_error" in (row.get("judge_flags") or [])
        and row.get("judge_soft_fail")
    )
    if pending and network_fail_n >= max(1, len(pending) // 2):
        raise JudgeError(
            f"S5 transport failures on {network_fail_n}/{len(selected)} rows "
            "(timeout/connection). Checkpointed as hard_fail for resume."
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
            "judge_repair_attempts": row.get("judge_repair_attempts"),
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
        "max_workers": settings.max_workers,
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
        "judge_repaired_count": repaired_count,
        "en_pivot_repair_count": en_pivot_repair_count,
        "quality_repair_max": max_quality_repairs,
        "repair_multi_constraint": multi_constraint,
        "repair_via_english_pivot": via_english_pivot,
        "must_work_languages": list(settings.must_work_languages),
        "rare_script_languages": list(settings.rare_script_languages),
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
            f"[s5] WARNING: {len(failures)} judge fail(s) after repair logged "
            "— see failed.jsonl and audit failures",
            file=sys.stderr,
        )
        must = set(settings.must_work_languages)
        rare = set(settings.rare_script_languages)
        if must:
            must_fails = [
                f
                for f in failures
                if str(f.get("document_language_code") or "") in must
            ]
            if must_fails:
                print(
                    f"[s5] MUST-WORK language fail(s): {len(must_fails)} "
                    f"(treat as system bug) langs="
                    f"{sorted({f.get('document_language_code') for f in must_fails})}",
                    file=sys.stderr,
                    flush=True,
                )
        if rare:
            rare_fails = [
                f
                for f in failures
                if str(f.get("document_language_code") or "") in rare
            ]
            if rare_fails:
                print(
                    f"[s5] rare-script fail(s): {len(rare_fails)} "
                    f"(expected capacity loss) langs="
                    f"{sorted({f.get('document_language_code') for f in rare_fails})}",
                    file=sys.stderr,
                    flush=True,
                )
    if repaired_count:
        print(
            f"[s5] quality-repaired-to-pass: {repaired_count}",
            file=sys.stderr,
            flush=True,
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
        f"- judge_repaired_count: **{audit.get('judge_repaired_count', 0)}**\n"
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
    root = load_yaml(pipeline_config)
    gen = root.get("generation") if isinstance(root.get("generation"), dict) else {}
    repair_settings = (
        load_repair_settings_from_generation(gen) if gen.get("model") else None
    )
    repair_client: SarvamClient | None = None
    if repair_settings is not None and repair_settings.max_repairs > 0:
        gen_key = require_env(str(gen.get("api_key_env") or "SARVAM_API_KEY"))
        rpm = gen.get("requests_per_minute")
        limiter = RateLimiter(float(rpm)) if rpm is not None and float(rpm) > 0 else None
        repair_client = SarvamClient(
            api_key=gen_key,
            base_url=str(gen.get("base_url") or "https://api.sarvam.ai/v1"),
            rate_limiter=limiter,
        )
    translation_settings: TranslationSettings | None = None
    need_translate = bool(
        repair_settings is not None
        and (
            repair_settings.via_english_pivot
            or settings.rare_script_languages
        )
    )
    if need_translate:
        from main.designers.translator import load_settings as load_translation_settings

        translation_settings = load_translation_settings(pipeline_config)
    rows = read_jsonl(settings.input_jsonl)
    checkpoint = CheckpointStore(settings.output_dir / "checkpoint.jsonl")
    judged, audit = judge_documents(
        rows,
        client=client,
        settings=settings,
        checkpoint=checkpoint,
        repair_client=repair_client,
        repair_settings=repair_settings,
        translation_settings=translation_settings,
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
