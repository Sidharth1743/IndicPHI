"""Stage 4b — Tag-preserving translation of English pivot clinical docs.

S4 generates annotated clinical text in English. For non-English document
languages, this stage translates prose into the target language/script while
keeping ID/number entity values byte-stable and allowing name/place values to
translate into the target script when natural.
"""

from __future__ import annotations

import argparse
import re
import sys
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
from main.validators.script_purity import evaluate_script_purity

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

_TAG_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|([^\]]*)\]\]")
_ID_PLACEHOLDER_RE = re.compile(r"⟦ID(\d+)⟧")
_NM_PLACEHOLDER_RE = re.compile(r"⟦NM(\d+)⟧")
_ANY_PLACEHOLDER_RE = re.compile(r"⟦(?:ID|NM)\d+⟧")

# Byte-stable ID / number / code entity types — protect full [[TYPE|value]].
ID_ENTITY_TYPES: frozenset[str] = frozenset(
    {
        "AADHAAR_NUMBER",
        "PAN_NUMBER",
        "IFSC_CODE",
        "PHONE_NUMBER",
        "EMAIL_ADDRESS",
        "IP_ADDRESS",
        "URL",
        "IMEI_NUMBER",
        "MAC_ADDRESS",
        "CREDIT_CARD_NUMBER",
        "CVV",
        "PIN",
        "PIN_CODE",
        "BANK_ACCOUNT_NUMBER",
        "BANK_ROUTING_NUMBER",
        "MRN",
        "PATIENT_ID",
        "HOSPITAL_ID",
        "ABHA_ID",
        "ABHA_ADDRESS",
        "ADMISSION_NUMBER",
        "ENCOUNTER_ID",
        "APPOINTMENT_ID",
        "REFERRAL_ID",
        "INSURANCE_POLICY_NUMBER",
        "BED_NUMBER",
        "WARD_NUMBER",
        "TAX_ID",
        "DOB",
        "AGE",
        "GENDER",
        "EMPLOYEE_ID",
        "STUDENT_ID",
        "DRIVING_LICENCE",
        "PASSPORT_NUMBER",
        "VOTER_ID",
        "BPL_RATION_CARD",
        "VEHICLE_REGISTRATION",
        "TELEPHONE_LANDLINE",
    }
)

# Person / place / address types — keep TYPE fixed; value may translate.
NAME_PLACE_ENTITY_TYPES: frozenset[str] = frozenset(
    {
        "PATIENT_NAME",
        "DOCTOR_NAME",
        "RELATIVE_NAME",
        "ASHA_WORKER_NAME",
        "HOSPITAL_NAME",
        "RESIDENTIAL_ADDRESS",
        "DISTRICT",
        "VILLAGE",
        "OCCUPATION",
        "CASTE",
        "RELIGION",
    }
)

# Alias used in audits / soft-fail reasons.
LATIN_OK_ENTITY_TYPES = ID_ENTITY_TYPES

TRANSLATION_COLUMNS: tuple[str, ...] = (
    "generated_text_en",
    "generated_text",
    "translation_applied",
    "translation_script_ok",
    "translator_model",
    "translator_finish_reason",
    "translation_attempts",
    "translation_error",
    "translation_soft_fail",
    "stage",
)


@dataclass(frozen=True)
class TranslationSettings:
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
    skip_language_codes: tuple[str, ...]


@dataclass(frozen=True)
class TagProtection:
    text: str
    id_mapping: dict[str, str]
    name_mapping: dict[str, str]
    name_types: dict[str, str]


class TranslationError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> TranslationSettings:
    root = load_yaml(pipeline_config)
    block = root.get("translation")
    if not isinstance(block, dict):
        raise ValueError(f"'translation' mapping required in {pipeline_config}")

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
        raise ValueError(f"Missing translation keys {missing}")

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

    skip = block.get("skip_language_codes") or ["en"]
    if not isinstance(skip, list) or not all(isinstance(x, str) for x in skip):
        raise ValueError("skip_language_codes must be a list of strings")

    return TranslationSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        model=str(block["model"]),
        base_url=str(block["base_url"]),
        api_key_env=str(block["api_key_env"]),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        reasoning_effort=reasoning_effort,
        timeout_s=float(block.get("timeout_s", 300)),
        max_docs=max_docs,
        requests_per_minute=rpm,
        max_workers=max_workers,
        skip_language_codes=tuple(skip),
    )


def protect_tags(text: str) -> TagProtection:
    """Protect entity tags for translation.

    - ID/number types: full ``[[TYPE|value]]`` → ``⟦IDn⟧``
    - Name/place types: ``[[TYPE|value]]`` → ``[[TYPE|⟦NMn⟧]]`` (TYPE stays visible)
    - Unknown types: full-tag protect (safe default)
    """
    id_mapping: dict[str, str] = {}
    name_mapping: dict[str, str] = {}
    name_types: dict[str, str] = {}

    def _repl(match: re.Match[str]) -> str:
        entity_type = match.group(1)
        value = match.group(2)
        full = match.group(0)
        if entity_type in NAME_PLACE_ENTITY_TYPES:
            key = f"⟦NM{len(name_mapping)}⟧"
            name_mapping[key] = value
            name_types[key] = entity_type
            return f"[[{entity_type}|{key}]]"
        # ID types and unknown → full protect
        key = f"⟦ID{len(id_mapping)}⟧"
        id_mapping[key] = full
        return key

    protected = _TAG_RE.sub(_repl, text)
    return TagProtection(
        text=protected,
        id_mapping=id_mapping,
        name_mapping=name_mapping,
        name_types=name_types,
    )


def restore_tags(text: str, protection: TagProtection) -> str:
    """Restore ID tags byte-stably; restore or accept translated name values."""
    restored = text

    def _restore_id(match: re.Match[str]) -> str:
        key = f"⟦ID{match.group(1)}⟧"
        if key not in protection.id_mapping:
            raise TranslationError(f"Missing ID placeholder restore for {key}")
        return protection.id_mapping[key]

    restored = _ID_PLACEHOLDER_RE.sub(_restore_id, restored)
    for key, value in protection.id_mapping.items():
        if key in restored:
            restored = restored.replace(key, value)

    # Name placeholders still present → restore original source value.
    def _restore_nm(match: re.Match[str]) -> str:
        key = f"⟦NM{match.group(1)}⟧"
        if key not in protection.name_mapping:
            raise TranslationError(f"Missing NM placeholder restore for {key}")
        return protection.name_mapping[key]

    restored = _NM_PLACEHOLDER_RE.sub(_restore_nm, restored)
    for key, value in protection.name_mapping.items():
        if key in restored:
            restored = restored.replace(key, value)

    leftover = _ANY_PLACEHOLDER_RE.findall(restored)
    if leftover:
        raise TranslationError(
            f"Translation dropped/kept placeholders unrestored: {leftover[:5]}"
        )

    for original in protection.id_mapping.values():
        if original not in restored:
            raise TranslationError(f"Translation lost protected ID tag {original!r}")

    # Name/place: TYPE must remain; value may be original or model-translated.
    for key, entity_type in protection.name_types.items():
        type_prefix = f"[[{entity_type}|"
        if type_prefix not in restored:
            raise TranslationError(
                f"Translation lost or altered name/place TYPE {entity_type!r} "
                f"(placeholder {key})"
            )

    # Count [[TYPE|…]] occurrences must be >= expected for each name type.
    expected_counts: dict[str, int] = {}
    for entity_type in protection.name_types.values():
        expected_counts[entity_type] = expected_counts.get(entity_type, 0) + 1
    for entity_type, expected in expected_counts.items():
        found = len(re.findall(rf"\[\[{re.escape(entity_type)}\|[^\]]*\]\]", restored))
        if found < expected:
            raise TranslationError(
                f"Translation under-counted [[{entity_type}|…]] "
                f"tags: found={found} expected>={expected}"
            )

    return restored


def optional_langid_score(
    text: str,
    *,
    language_code: str,
) -> str | None:
    """Optional language-ID check. Returns a soft-fail reason fragment or None.

    Skips silently when ``langid`` is not installed (no heavy dependency).
    Script purity remains the primary gate.
    """
    try:
        import langid  # type: ignore[import-untyped]
    except ImportError:
        return None

    try:
        prose = _TAG_RE.sub(" ", text)
        predicted, _confidence = langid.classify(prose)
    except Exception:  # noqa: BLE001 — optional hook must never abort
        return None

    # langid uses ISO 639-1; our codes are mostly the same for Indic.
    if predicted and predicted != language_code and language_code != "en":
        return f"langid_mismatch:predicted={predicted}:expected={language_code}"
    return None


def build_translate_messages(
    *,
    protected_text: str,
    language_name: str,
    language_code: str,
    script: str,
    doc_type_name: str,
    retry_harder: bool = False,
) -> list[dict[str, str]]:
    system = (
        "You translate synthetic Indian clinical documents into the requested "
        "Indic language/script.\n"
        "CRITICAL RULES:\n"
        "1) Preserve every placeholder like ⟦ID0⟧ exactly — do not translate, "
        "alter, or remove them.\n"
        "2) Keep entity TYPE names inside [[TYPE|…]] tags exactly unchanged.\n"
        "3) Translate person names, place names, hospital names, and addresses "
        "into the target script when natural. Placeholders like ⟦NM0⟧ inside "
        "[[TYPE|⟦NM0⟧]] may be replaced with the translated value, but TYPE "
        "must stay exact.\n"
        "4) Keep ID/number/email/URL entity VALUES unchanged (they appear as "
        "⟦IDn⟧ placeholders).\n"
        "5) Translate ALL clinical prose and headings into the target language/"
        "script. Do NOT leave the body in English.\n"
        "6) Keep drug names, lab analyte names, and Latin abbreviations as Latin.\n"
        "7) Output ONLY the translated document text."
    )
    if retry_harder:
        system += (
            "\nRETRY: Previous output was still mostly English. You MUST rewrite "
            f"the prose in {language_name} ({script} script). ID placeholders stay. "
            "Translate name/place values into the target script when natural."
        )
    user = (
        f"Target language: {language_name} (code={language_code}, script={script}).\n"
        f"Document type: {doc_type_name}.\n\n"
        f"English source with protected entity placeholders:\n{protected_text}"
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _translate_one(
    index: int,
    row: Mapping[str, Any],
    *,
    client: SarvamClient,
    settings: TranslationSettings,
) -> dict[str, Any]:
    source = str(row.get("generated_text", ""))
    if not source.strip():
        raise TranslationError(f"Empty generated_text at row {index}")

    lang = str(row.get("document_language_code", ""))
    script = str(row.get("document_script", ""))
    out = dict(row)
    out["generated_text_en"] = source

    if lang in settings.skip_language_codes:
        out.update(
            {
                "generated_text": source,
                "translation_applied": False,
                "translation_script_ok": True,
                "translator_model": None,
                "translator_finish_reason": "skipped_english",
                "translation_attempts": 0,
                "translation_error": None,
                "translation_soft_fail": False,
                "stage": "s4b_translation",
            }
        )
        return out

    protection = protect_tags(source)
    if not protection.id_mapping and not protection.name_mapping:
        raise TranslationError(
            f"No [[TYPE|value]] tags found to protect at row {index} "
            f"uuid={row.get('uuid')!r}"
        )

    last_error: Exception | None = None
    last_restored: str | None = None
    last_model: str | None = None
    last_finish: str | None = None
    for attempt, harder in enumerate((False, True)):
        try:
            result = client.chat_completion(
                model=settings.model,
                messages=build_translate_messages(
                    protected_text=protection.text,
                    language_name=str(row.get("document_language_name", "")),
                    language_code=lang,
                    script=script,
                    doc_type_name=str(row.get("doc_type_name", "")),
                    retry_harder=harder,
                ),
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                reasoning_effort=settings.reasoning_effort,
                timeout_s=settings.timeout_s,
            )
            restored = restore_tags(result.content.strip(), protection)
            last_restored = restored
            last_model = result.model
            last_finish = result.finish_reason
            ok, reason = evaluate_script_purity(
                restored, language_code=lang, script=script
            )
            if not ok:
                # Script purity already encodes Latin-ratio failures; optional
                # langid may add a secondary soft-fail hint when available.
                langid_hint = optional_langid_score(restored, language_code=lang)
                detail = reason
                if langid_hint:
                    detail = f"{reason};{langid_hint}"
                last_error = TranslationError(
                    f"script_purity_failed:{detail} attempt={attempt}"
                )
                continue
            out.update(
                {
                    "generated_text": restored,
                    "translation_applied": True,
                    "translation_script_ok": True,
                    "translator_model": result.model,
                    "translator_finish_reason": result.finish_reason,
                    "translation_attempts": attempt + 1,
                    "translation_error": None,
                    "translation_soft_fail": False,
                    "stage": "s4b_translation",
                }
            )
            return out
        except (SarvamClientError, TranslationError) as exc:
            last_error = exc
            continue

    if last_restored is None:
        raise TranslationError(
            f"Translation failed at row {index} uuid={row.get('uuid')!r}: {last_error}"
        ) from last_error

    # Soft-fail: keep best attempt for judge/auditor (do not abort the run).
    # Always log — never silent. Script purity / Latin-ratio is the primary gate;
    # langid is optional and only appended when importable.
    error_msg = str(last_error)
    langid_hint = optional_langid_score(last_restored, language_code=lang)
    if langid_hint and langid_hint not in error_msg:
        error_msg = f"{error_msg};{langid_hint}"
    print(
        f"[s4b] SOFT-FAIL uuid={row.get('uuid')} lang={lang} "
        f"doc_type={row.get('doc_type_id')} error={error_msg}",
        file=sys.stderr,
    )
    out.update(
        {
            "generated_text": last_restored,
            "translation_applied": True,
            "translation_script_ok": False,
            "translator_model": last_model,
            "translator_finish_reason": last_finish,
            "translation_attempts": 2,
            "translation_error": error_msg,
            "translation_soft_fail": True,
            "stage": "s4b_translation",
        }
    )
    return out


def translate_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    client: SarvamClient,
    settings: TranslationSettings,
    checkpoint: CheckpointStore | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise TranslationError("No rows selected for translation")

    results: dict[int, dict[str, Any]] = {}
    pending: list[tuple[int, Mapping[str, Any], str]] = []
    resumed = 0
    for index, row in enumerate(selected):
        key = row_key_from_prompt(row)
        req = request_hash(
            [
                row.get("generated_text"),
                row.get("document_language_code"),
                settings.model,
                settings.temperature,
                settings.max_tokens,
            ]
        )
        if checkpoint is not None:
            existing = checkpoint.get(key)
            if (
                existing
                and existing.status in {"ok", "soft_fail", "skipped"}
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
                    _translate_one, index, row, client=client, settings=settings
                ): (index, req)
                for index, row, req in pending
            }
            for future in as_completed(futures):
                index, req = futures[future]
                try:
                    out = future.result()
                except TranslationError:
                    for pending_fut in futures:
                        pending_fut.cancel()
                    raise
                results[index] = out
                if checkpoint is not None:
                    if out.get("translation_soft_fail"):
                        status = "soft_fail"
                    elif not out.get("translation_applied"):
                        status = "skipped"
                    else:
                        status = "ok"
                    checkpoint.append(
                        row_key=row_key_from_prompt(selected[index]),
                        status=status,
                        request_hash=req,
                        payload=out,
                        error=out.get("translation_error"),
                    )

    outputs = [results[i] for i in range(len(selected))]
    translated = sum(1 for row in outputs if row.get("translation_applied"))
    soft_failures = [
        {
            "uuid": row.get("uuid"),
            "document_id": row.get("document_id"),
            "doc_type_id": row.get("doc_type_id"),
            "document_language_code": row.get("document_language_code"),
            "translation_error": row.get("translation_error"),
            "translation_script_ok": row.get("translation_script_ok"),
        }
        for row in outputs
        if row.get("translation_soft_fail")
        or (
            row.get("translation_applied")
            and row.get("translation_script_ok") is False
        )
    ]
    audit = {
        "stage": "s4b_translation",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "model": settings.model,
        "rows_in": len(selected),
        "rows_out": len(outputs),
        "rows_translated": translated,
        "rows_skipped": len(outputs) - translated,
        "rows_resumed_from_checkpoint": resumed,
        "rows_newly_translated": len(pending),
        "soft_failures": soft_failures,
        "soft_fail_count": len(soft_failures),
        "script_fail_count": sum(
            1
            for row in outputs
            if row.get("translation_applied") and not row.get("translation_script_ok")
        ),
        "max_workers": workers if pending else 0,
        "requests_per_minute": settings.requests_per_minute,
        "skip_language_codes": list(settings.skip_language_codes),
        "columns_added": list(TRANSLATION_COLUMNS),
        "tag_protection": {
            "id_entity_types": sorted(ID_ENTITY_TYPES),
            "name_place_entity_types": sorted(NAME_PLACE_ENTITY_TYPES),
            "langid_hook": "optional_if_installed",
            "primary_purity_gate": "script_purity_latin_ratio",
        },
    }
    if soft_failures:
        print(
            f"[s4b] WARNING: {len(soft_failures)} translation soft-fail(s) logged "
            "— see audit soft_failures",
            file=sys.stderr,
        )
    return outputs, audit


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = output_dir / "documents.jsonl"
    atomic_write_jsonl(jsonl_path, rows)
    parquet_path = output_dir / "documents.parquet"
    write_parquet(parquet_path, rows)
    audit_json = output_dir / "audit.json"
    write_json(audit_json, audit)
    soft_fail_path = output_dir / "soft_failures.jsonl"
    write_jsonl(soft_fail_path, audit.get("soft_failures") or [])
    audit_md = output_dir / "audit.md"
    lines = [
        "# Stage 4b — Translation Audit",
        "",
        f"- model: `{audit['model']}`",
        f"- rows_translated: **{audit['rows_translated']}**",
        f"- rows_skipped: `{audit['rows_skipped']}`",
        f"- soft_fail_count: **{audit.get('soft_fail_count', 0)}**",
        f"- script_fail_count: `{audit.get('script_fail_count', 0)}`",
        f"- max_workers: `{audit['max_workers']}`",
        "",
    ]
    soft_failures = audit.get("soft_failures") or []
    if soft_failures:
        lines.extend(["## Soft failures (audited — not silent)", ""])
        for item in soft_failures:
            lines.append(
                f"- `{item.get('uuid')}` · `{item.get('doc_type_id')}` · "
                f"`{item.get('document_language_code')}` · "
                f"error={item.get('translation_error')}"
            )
        lines.append("")
    audit_md.write_text("\n".join(lines), encoding="utf-8")
    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
        "soft_failures_jsonl": soft_fail_path,
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
    translated, audit = translate_rows(
        rows, client=client, settings=settings, checkpoint=checkpoint
    )
    return write_outputs(translated, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 4b: tag-preserving translation")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (TranslationError, ValueError, FileNotFoundError, SarvamClientError) as exc:
        print(f"[s4b] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s4b] Translation complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
