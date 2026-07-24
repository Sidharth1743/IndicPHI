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

from main.designers.entity_checks import (
    coverage_and_stuffing,
    has_valid_entity_tags,
    invalid_type_tags,
)
from main.designers.repair import (
    RepairIssue,
    RepairSettings,
    issues_from_text,
    load_repair_settings_from_generation,
    repair_document,
    script_issue,
)
from main.llm.rate_limit import RateLimiter
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.llm.sarvam_translate import SarvamTranslateClient, SarvamTranslateError
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
    "translation_generator_repair_attempts",
    "translation_repaired_by_generator",
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
    # After this many chat-translate failures, try dedicated /translate (rare scripts).
    rare_script_languages: tuple[str, ...] = ()
    rare_script_max_chat_attempts: int = 2
    dedicated_translate_model: str = "sarvam-translate:v1"
    dedicated_translate_timeout_s: float = 180.0
    # Business Translate (ms-ts) = 1000 RPM — keep separate from 105B chat 120 RPM.
    dedicated_translate_requests_per_minute: float = 900.0
    enable_dedicated_translate_fallback: bool = True
    # Extra chat attempts on timeout (on top of rare/normal chat budget).
    # Set 0 to jump to dedicated on first chat timeout.
    timeout_chat_retries: int = 0
    # Retries for dedicated /translate when that call itself times out.
    dedicated_retries: int = 2
    # Rare langs: try dedicated /translate first (then chat recovery if needed).
    rare_script_dedicated_first: bool = True
    # Longer dedicated timeout for rare scripts (Ol Chiki / Meitei / etc.).
    rare_dedicated_translate_timeout_s: float = 300.0
    # Langs where dedicated empirically fails → chat+few-shot first, then dedicated.
    rare_prefer_chat_languages: tuple[str, ...] = ()
    # Short chat budget for rare recovery (avoid 300s×N burns after dedicated fail).
    rare_chat_timeout_s: float = 180.0
    # Chat attempts after dedicated fails (or when prefer-chat).
    rare_chat_recovery_attempts: int = 1
    # Optional YAML with per-lang gold few-shot lines for chat translate.
    fewshot_config: Path | None = None


def _is_timeout_error(exc: BaseException) -> bool:
    """True for bare TimeoutError or wrapped 'timed out' / timeout messages."""
    if isinstance(exc, TimeoutError):
        return True
    msg = str(exc).lower()
    return "timed out" in msg or "timeout after" in msg or "read operation timed out" in msg


_TRANSPORT_NEEDLES = (
    "timed out",
    "timeout after",
    "read operation timed out",
    "network error",
    "name or service not known",
    "temporary failure in name resolution",
    "connection reset",
    "connection refused",
    "connection aborted",
    "broken pipe",
    "remotely closed",
    "errno -2",
    "errno 104",
    "errno 111",
)

# Quality / ladder failures — not transport even if an earlier attempt timed out.
_QUALITY_NEEDLES = (
    "lost protected",
    "lost or altered",
    "missing id placeholder",
    "under-counted",
    "script_purity",
    "wrong_indic",
    "tag_restore",
    "empty translation",
    "dedicated_translate_failed:translation",
)


def _error_segments(msg: str) -> list[str]:
    return [part.strip() for part in str(msg).split(";") if part.strip()]


def _segment_is_transport(segment: str) -> bool:
    low = segment.lower()
    if any(n in low for n in _QUALITY_NEEDLES):
        return False
    return any(n in low for n in _TRANSPORT_NEEDLES)


def _is_retryable_transport_error(exc_or_msg: BaseException | str | None) -> bool:
    """True when the *final* failure cause is DNS/timeout/connection.

    Error trails are ``attempt1:...;attempt2:...;last:...``. A timeout mid-ladder
    followed by ``lost protected ID tag`` is a quality soft-fail, not transport.
    """
    if exc_or_msg is None:
        return False
    if isinstance(exc_or_msg, BaseException):
        # Bare exceptions have no multi-attempt trail — use full message.
        if _is_timeout_error(exc_or_msg):
            return True
        msg = str(exc_or_msg)
    else:
        msg = str(exc_or_msg)
    segments = _error_segments(msg)
    if not segments:
        return False
    return _segment_is_transport(segments[-1])


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

    rare = block.get("rare_script_languages")
    if rare is None:
        # Fall back to linguistic_judge SLA list when translation omits it.
        judge = root.get("linguistic_judge") if isinstance(root.get("linguistic_judge"), dict) else {}
        rare = judge.get("rare_script_languages") or [
            "brx", "mni", "sat", "ks", "sd", "doi", "sa"
        ]
    if not isinstance(rare, list) or not all(isinstance(x, str) for x in rare):
        raise ValueError("rare_script_languages must be a list of strings")

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
        rare_script_languages=tuple(str(x) for x in rare),
        rare_script_max_chat_attempts=int(block.get("rare_script_max_chat_attempts", 2)),
        dedicated_translate_model=str(
            block.get("dedicated_translate_model", "sarvam-translate:v1")
        ),
        dedicated_translate_timeout_s=float(
            block.get("dedicated_translate_timeout_s", 180)
        ),
        dedicated_translate_requests_per_minute=float(
            block.get("dedicated_translate_requests_per_minute", 900)
        ),
        enable_dedicated_translate_fallback=bool(
            block.get("enable_dedicated_translate_fallback", True)
        ),
        timeout_chat_retries=max(0, int(block.get("timeout_chat_retries", 0))),
        dedicated_retries=max(0, int(block.get("dedicated_retries", 2))),
        rare_script_dedicated_first=bool(
            block.get("rare_script_dedicated_first", True)
        ),
        rare_dedicated_translate_timeout_s=float(
            block.get("rare_dedicated_translate_timeout_s", 300)
        ),
        rare_prefer_chat_languages=tuple(
            str(x)
            for x in (
                block.get("rare_prefer_chat_languages")
                or ["doi", "ks", "sd"]
            )
        ),
        rare_chat_timeout_s=float(block.get("rare_chat_timeout_s", 180)),
        rare_chat_recovery_attempts=max(
            0, int(block.get("rare_chat_recovery_attempts", 1))
        ),
        fewshot_config=(
            resolve_repo_path(str(block["fewshot_config"]))
            if block.get("fewshot_config")
            else resolve_repo_path(
                "configs/synthetic-data/translation_fewshots.yaml"
            )
        ),
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


def try_dedicated_translate_fallback(
    *,
    client: SarvamClient,
    english_text: str,
    row: Mapping[str, Any],
    settings: TranslationSettings,
    force: bool = False,
    rate_limiter: RateLimiter | None = None,
) -> tuple[str | None, str | None, bool]:
    """Run dedicated /translate + script purity. Returns (text, err, script_ok).

    By default limited to ``rare_script_languages``. Pass ``force=True`` for
    timeout recovery on any language (Business Translate API is 1000 RPM).

    Pass a **shared** ``rate_limiter`` from the stage so workers do not each
    create their own limiter and stampede the Translate API (timeouts).
    """
    lang = str(row.get("document_language_code") or "")
    script = str(row.get("document_script") or "")
    if not settings.enable_dedicated_translate_fallback:
        return None, "dedicated_translate_disabled", False
    if not force and lang not in settings.rare_script_languages:
        return None, "not_rare_script", False

    print(
        f"[s4b] dedicated /translate fallback lang={lang} "
        f"uuid={row.get('uuid')} doc_type={row.get('doc_type_id')}"
        + (" force=timeout" if force else ""),
        file=sys.stderr,
        flush=True,
    )
    try:
        # Translate API has its own Business pool (1000 RPM) — do not share 105B chat limiter.
        tr_limiter = rate_limiter or RateLimiter(
            settings.dedicated_translate_requests_per_minute
        )
        tr = SarvamTranslateClient(api_key=client.api_key, rate_limiter=tr_limiter)
        protection = protect_tags(english_text)
        if not protection.id_mapping and not protection.name_mapping:
            return None, "no_valid_entity_tags_to_protect", False
        is_rare = lang in settings.rare_script_languages
        ded_timeout = (
            settings.rare_dedicated_translate_timeout_s
            if is_rare
            else settings.dedicated_translate_timeout_s
        )
        last_exc: Exception | None = None
        translated = ""
        for ded_round in range(1 + max(0, settings.dedicated_retries)):
            try:
                translated = tr.translate_long(
                    protection.text,
                    language_code=lang,
                    model=settings.dedicated_translate_model,
                    timeout_s=ded_timeout,
                )
                last_exc = None
                break
            except (SarvamTranslateError, TranslationError, TimeoutError, OSError) as exc:
                last_exc = exc
                if _is_timeout_error(exc) and ded_round < settings.dedicated_retries:
                    print(
                        f"[s4b] dedicated timeout retry {ded_round + 1}/"
                        f"{settings.dedicated_retries} lang={lang} "
                        f"uuid={row.get('uuid')}",
                        file=sys.stderr,
                        flush=True,
                    )
                    continue
                return None, f"dedicated_translate_failed:{exc}", False
        if last_exc is not None:
            return None, f"dedicated_translate_failed:{last_exc}", False
        restored = restore_tags(translated, protection)
    except (SarvamTranslateError, TranslationError) as exc:
        return None, f"dedicated_translate_failed:{exc}", False

    ok, reason = evaluate_script_purity(
        restored, language_code=lang, script=script
    )
    if not ok:
        return restored, f"dedicated_script_purity_failed:{reason}", False
    return restored, None, True


def _fewshot_block(language_code: str, settings: TranslationSettings) -> str:
    """Load 2–3 gold lines for rare-script chat translate (empty if missing)."""
    path = settings.fewshot_config
    if path is None or not Path(path).is_file():
        return ""
    try:
        raw = load_yaml(Path(path))
        shots = (raw.get("fewshots") or {}).get(language_code) or []
    except Exception:  # noqa: BLE001 — optional few-shots must not abort
        return ""
    lines = [str(x).strip() for x in shots if str(x).strip()][:4]
    if not lines:
        return ""
    joined = "\n".join(f"- {ln}" for ln in lines)
    return (
        f"\nGOLD FEW-SHOT lines in the target script (match this language/"
        f"script style; do NOT copy entity values verbatim):\n{joined}\n"
    )


def _is_mostly_english_pivot(text: str, *, language_code: str, script: str) -> bool:
    """True when purity fails for latin-heavy body (not merely wrong Indic script)."""
    ok, reason = evaluate_script_purity(
        text, language_code=language_code, script=script
    )
    if ok:
        return False
    r = (reason or "").lower()
    if "wrong_indic_script" in r:
        return False
    return "latin" in r or "english" in r or "ratio" in r


def _chat_translate_once(
    client: SarvamClient,
    *,
    protection: TagProtection,
    row: Mapping[str, Any],
    settings: TranslationSettings,
    fewshot_extra: str,
    retry_harder: bool,
    timeout_s: float,
    script_lock: bool = False,
) -> tuple[str | None, Exception | None, str | None, str | None]:
    """One protected chat translate. Returns (text, err, model, finish)."""
    lang = str(row.get("document_language_code") or "")
    script = str(row.get("document_script") or "")
    try:
        result = client.chat_completion(
            model=settings.model,
            messages=build_translate_messages(
                protected_text=protection.text,
                language_name=str(row.get("document_language_name", "")),
                language_code=lang,
                script=script,
                doc_type_name=str(row.get("doc_type_name", "")),
                retry_harder=retry_harder,
                fewshot_extra=fewshot_extra,
                script_lock=script_lock,
            ),
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            reasoning_effort=settings.reasoning_effort,
            timeout_s=timeout_s,
        )
        restored = restore_tags(result.content.strip(), protection)
        return restored, None, result.model, result.finish_reason
    except (SarvamClientError, TranslationError, TimeoutError, OSError) as exc:
        err = (
            exc
            if isinstance(exc, (SarvamClientError, TranslationError))
            else TranslationError(str(exc))
        )
        return None, err, None, None


def build_translate_messages(
    *,
    protected_text: str,
    language_name: str,
    language_code: str,
    script: str,
    doc_type_name: str,
    retry_harder: bool = False,
    fewshot_extra: str = "",
    script_lock: bool = False,
) -> list[dict[str, str]]:
    system = (
        "You translate synthetic Indian clinical documents into the requested "
        "Indic language/script.\n"
        "CRITICAL RULES:\n"
        "1) Preserve every placeholder like ⟦ID0⟧ exactly — do not translate, "
        "alter, or remove them.\n"
        "2) Keep entity TYPE names inside [[TYPE|…]] tags EXACT ASCII "
        "unchanged forever (PATIENT_NAME, HOSPITAL_NAME, MRN, …). "
        "NEVER translate/localize TYPE "
        "(forbidden: রোগীর_নাম, रोगी_नाम, PatientName).\n"
        "3) Translate person names, place names, hospital names, and addresses "
        "into the target script when natural. Placeholders like ⟦NM0⟧ inside "
        "[[TYPE|⟦NM0⟧]] may be replaced with the translated value, but TYPE "
        "must stay exact.\n"
        "4) Keep ID/number/email/URL entity VALUES unchanged (they appear as "
        "⟦IDn⟧ placeholders).\n"
        "5) Translate ALL clinical prose and headings into the target language/"
        "script. Do NOT leave the body in English. Do NOT substitute a neighbor "
        "language (no Hindi for Dogri/Bodo; no Urdu for Kashmiri; no Hindi "
        "Devanagari for Sindhi).\n"
        "6) Keep drug names, lab analyte names, and Latin abbreviations as Latin.\n"
        "7) Output ONLY the translated document text."
    )
    # Sindhi/Kashmiri use Arabic script — models often slip into Devanagari.
    if script.strip().lower() == "arabic" or language_code in {"sd", "ks"}:
        system += (
            f"\nSCRIPT: {language_name} MUST use Arabic/Perso-Arabic letters "
            "(Sindhi/Kashmiri orthography). NEVER write Devanagari "
            "(कखग / डिस्चार्ज). Neighbor Hindi in Devanagari is a hard fail."
        )
    if retry_harder:
        system += (
            "\nRETRY: Previous output was still mostly English or wrong language. "
            f"You MUST rewrite the prose in {language_name} ({script} script) only. "
            "ID placeholders stay. Translate name/place values into the target "
            "script when natural."
        )
    if script_lock:
        system += (
            "\nSCRIPT LOCK (mandatory): Previous draft used the WRONG script "
            f"(e.g. Devanagari). Rewrite the ENTIRE body in {language_name} using "
            f"ONLY {script} script. Do not mix scripts. Keep ⟦IDn⟧ / TYPE names."
        )
    user = (
        f"Target language: {language_name} (code={language_code}, script={script}).\n"
        f"Document type: {doc_type_name}.\n"
        f"{fewshot_extra}"
        f"\nEnglish source with protected entity placeholders:\n{protected_text}"
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def translate_english_once(
    client: SarvamClient,
    *,
    english_text: str,
    row: Mapping[str, Any],
    settings: TranslationSettings,
    retry_harder: bool = True,
) -> tuple[str | None, str | None]:
    """One protected translate pass for S5 EN-pivot repair.

    Returns ``(translated_text, error)``. On total failure ``translated_text``
    is None. On script-purity soft failure, returns the restored text plus error
    so the caller can still re-judge.
    """
    lang = str(row.get("document_language_code") or "")
    script = str(row.get("document_script") or "")
    if not english_text.strip():
        return None, "empty_english_text"
    if lang in settings.skip_language_codes or lang in {"en", "en_IN"}:
        return english_text, None

    protection = protect_tags(english_text)
    if not protection.id_mapping and not protection.name_mapping:
        return None, "no_valid_entity_tags_to_protect"

    fewshot_extra = (
        _fewshot_block(lang, settings)
        if lang in settings.rare_script_languages
        else ""
    )
    try:
        result = client.chat_completion(
            model=settings.model,
            messages=build_translate_messages(
                protected_text=protection.text,
                language_name=str(row.get("document_language_name") or ""),
                language_code=lang,
                script=script,
                doc_type_name=str(row.get("doc_type_name") or row.get("doc_type_id") or ""),
                retry_harder=retry_harder,
                fewshot_extra=fewshot_extra,
            ),
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            reasoning_effort=settings.reasoning_effort,
            timeout_s=settings.timeout_s,
        )
        restored = restore_tags(result.content.strip(), protection)
    except (SarvamClientError, TranslationError) as exc:
        return None, f"translate_failed:{exc}"

    ok, reason = evaluate_script_purity(
        restored, language_code=lang, script=script
    )
    if not ok:
        return restored, f"script_purity_failed:{reason}"
    return restored, None


def _translate_one(
    index: int,
    row: Mapping[str, Any],
    *,
    client: SarvamClient,
    settings: TranslationSettings,
    repair_settings: RepairSettings | None = None,
    dedicated_limiter: RateLimiter | None = None,
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
                "translation_generator_repair_attempts": 0,
                "translation_repaired_by_generator": False,
                "stage": "s4b_translation",
            }
        )
        return out

    protection = protect_tags(source)
    tag_repair_attempts = 0
    if not protection.id_mapping and not protection.name_mapping:
        # Often the model localized TYPE names (e.g. [[রোগীর_নাম|…]]) so the
        # ASCII tag regex finds nothing. Soft-fail + repair — never abort run.
        required = [str(x) for x in (row.get("required_entities") or [])]
        # lab_report no longer requires STUDENT_ID; drop if baked into older prompts.
        if str(row.get("doc_type_id") or "") == "lab_report":
            required = [t for t in required if t != "STUDENT_ID"]
        invalid = invalid_type_tags(source)
        if repair_settings is not None and repair_settings.max_repairs > 0:
            issues = issues_from_text(source, required)
            if not issues:
                issues = [
                    RepairIssue(
                        kind="invalid_type_tags",
                        detail="no_valid_ascii_TYPE_tags",
                    )
                ]
                if required:
                    issues.append(
                        RepairIssue(
                            kind="missing_entities",
                            detail=",".join(required),
                        )
                    )
            repair = repair_document(
                client,
                draft=source,
                row=row,
                required=required,
                issues=issues,
                settings=repair_settings,
                check_script=False,
            )
            tag_repair_attempts = repair.attempts
            if repair.repaired and has_valid_entity_tags(repair.text):
                print(
                    f"[s4b] REPAIRED-TAGS uuid={row.get('uuid')} lang={lang} "
                    f"doc_type={row.get('doc_type_id')} attempts={tag_repair_attempts} "
                    f"invalid_was={invalid[:5]!r}",
                    file=sys.stderr,
                    flush=True,
                )
                source = repair.text
                out["generated_text_en"] = source
                protection = protect_tags(source)

        if not protection.id_mapping and not protection.name_mapping:
            err = "no_valid_entity_tags_to_protect"
            if invalid:
                err = f"{err};invalid_type_tags:{','.join(invalid)}"
            print(
                f"[s4b] SOFT-FAIL uuid={row.get('uuid')} lang={lang} "
                f"doc_type={row.get('doc_type_id')} error={err}",
                file=sys.stderr,
                flush=True,
            )
            out.update(
                {
                    "generated_text": source,
                    "translation_applied": False,
                    "translation_script_ok": False,
                    "translator_model": None,
                    "translator_finish_reason": "no_valid_tags",
                    "translation_attempts": 0,
                    "translation_error": err,
                    "translation_soft_fail": True,
                    "translation_generator_repair_attempts": tag_repair_attempts,
                    "translation_repaired_by_generator": False,
                    "stage": "s4b_translation",
                }
            )
            return out

    last_error: Exception | None = None
    last_restored: str | None = None
    last_model: str | None = None
    last_finish: str | None = None
    is_rare = lang in settings.rare_script_languages
    fewshot_extra = _fewshot_block(lang, settings) if is_rare else ""
    prefer_chat = is_rare and lang in settings.rare_prefer_chat_languages
    dedicated_first = bool(
        is_rare and settings.rare_script_dedicated_first and not prefer_chat
    )
    attempt = 0
    timed_out = False
    err_trail: list[str] = []

    def _accept_ok(
        text: str,
        *,
        model: str | None,
        finish: str | None,
        attempts: int,
    ) -> dict[str, Any]:
        out.update(
            {
                "generated_text": text,
                "translation_applied": True,
                "translation_script_ok": True,
                "translator_model": model,
                "translator_finish_reason": finish,
                "translation_attempts": attempts,
                "translation_error": None,
                "translation_soft_fail": False,
                "translation_generator_repair_attempts": tag_repair_attempts,
                "translation_repaired_by_generator": tag_repair_attempts > 0,
                "stage": "s4b_translation",
            }
        )
        return out

    def _keep_candidate(
        text: str,
        *,
        model: str | None,
        finish: str | None,
        err: str,
    ) -> None:
        nonlocal last_restored, last_model, last_finish, last_error
        # Prefer non-English candidates over English pivot.
        if last_restored is None or (
            _is_mostly_english_pivot(last_restored, language_code=lang, script=script)
            and not _is_mostly_english_pivot(text, language_code=lang, script=script)
        ):
            last_restored = text
            last_model = model
            last_finish = finish
        last_error = TranslationError(err)
        err_trail.append(err)

    def _run_dedicated(finish_label: str) -> dict[str, Any] | None:
        nonlocal attempt, last_error
        ded_text, ded_err, ded_ok = try_dedicated_translate_fallback(
            client=client,
            english_text=source,
            row=row,
            settings=settings,
            force=True,
            rate_limiter=dedicated_limiter,
        )
        attempt += 1
        if ded_text and ded_ok:
            print(
                f"[s4b] dedicated OK lang={lang} uuid={row.get('uuid')} "
                f"via={finish_label}",
                file=sys.stderr,
                flush=True,
            )
            return _accept_ok(
                ded_text,
                model=settings.dedicated_translate_model,
                finish=finish_label,
                attempts=attempt,
            )
        if ded_text:
            _keep_candidate(
                ded_text,
                model=settings.dedicated_translate_model,
                finish=finish_label,
                err=ded_err or "dedicated_script_soft",
            )
            print(
                f"[s4b] dedicated soft lang={lang} uuid={row.get('uuid')} "
                f"err={ded_err}",
                file=sys.stderr,
                flush=True,
            )
        else:
            # Always record real error (was previously lost → ":None").
            detail = ded_err or "dedicated_empty"
            last_error = TranslationError(detail)
            err_trail.append(detail)
            print(
                f"[s4b] dedicated FAIL lang={lang} uuid={row.get('uuid')} "
                f"err={detail}",
                file=sys.stderr,
                flush=True,
            )
        return None

    def _run_chat_recovery(*, harder: bool, label: str) -> dict[str, Any] | None:
        nonlocal attempt, timed_out, last_error
        # Sindhi: chat is the working path; allow more wall time than generic rare.
        if lang == "sd":
            timeout_s = max(float(settings.rare_chat_timeout_s), 240.0)
        elif is_rare:
            timeout_s = settings.rare_chat_timeout_s
        else:
            timeout_s = settings.timeout_s
        text, err, model, finish = _chat_translate_once(
            client,
            protection=protection,
            row=row,
            settings=settings,
            fewshot_extra=fewshot_extra,
            retry_harder=harder,
            timeout_s=timeout_s,
        )
        attempt += 1
        if err is not None:
            if _is_timeout_error(err):
                timed_out = True
            last_error = err
            err_trail.append(f"{label}:{err}")
            print(
                f"[s4b] chat {label} fail lang={lang} uuid={row.get('uuid')} "
                f"err={err}",
                file=sys.stderr,
                flush=True,
            )
            return None
        assert text is not None
        ok, reason = evaluate_script_purity(
            text, language_code=lang, script=script
        )
        if ok:
            print(
                f"[s4b] chat {label} OK lang={lang} uuid={row.get('uuid')}",
                file=sys.stderr,
                flush=True,
            )
            return _accept_ok(
                text, model=model, finish=finish or label, attempts=attempt
            )
        # Arabic-script langs (sd/ks): one forced script-lock rewrite if Devanagari leaked.
        if (
            "wrong_indic_script" in (reason or "").lower()
            and script.strip().lower() == "arabic"
        ):
            print(
                f"[s4b] chat script-lock retry lang={lang} uuid={row.get('uuid')} "
                f"reason={reason}",
                file=sys.stderr,
                flush=True,
            )
            locked, lerr, lmodel, lfinish = _chat_translate_once(
                client,
                protection=protection,
                row=row,
                settings=settings,
                fewshot_extra=fewshot_extra,
                retry_harder=True,
                timeout_s=timeout_s,
                script_lock=True,
            )
            attempt += 1
            if lerr is None and locked is not None:
                lok, lreason = evaluate_script_purity(
                    locked, language_code=lang, script=script
                )
                if lok:
                    return _accept_ok(
                        locked,
                        model=lmodel,
                        finish=lfinish or f"{label}_script_lock",
                        attempts=attempt,
                    )
                _keep_candidate(
                    locked,
                    model=lmodel,
                    finish=lfinish or f"{label}_script_lock",
                    err=f"script_purity_failed:{lreason}",
                )
            elif lerr is not None:
                err_trail.append(f"{label}_script_lock:{lerr}")
        _keep_candidate(
            text,
            model=model,
            finish=finish or label,
            err=f"script_purity_failed:{reason}",
        )
        return None

    # ---- Rare ladder: fix language at S4b (cheap) so S5 does not burn repairs ----
    # Evidence: doi/ks/sd — dedicated often empty or drops ID tags; chat+few-shot
    # recovers. brx/mni — dedicated often OK. Wrong-script still beats English.
    if is_rare:
        if dedicated_first:
            hit = _run_dedicated("dedicated_first")
            if hit is not None:
                return hit
        # Prefer-chat langs get ≥2 attempts (sd timeouts / Devanagari slips).
        prefer_chat_rounds = max(2, settings.rare_chat_recovery_attempts)
        recovery_rounds = max(1, settings.rare_chat_recovery_attempts)
        chat_rounds = prefer_chat_rounds if prefer_chat else (
            recovery_rounds
            if (
                dedicated_first
                or not settings.rare_script_dedicated_first
            )
            else 0
        )
        if prefer_chat and not dedicated_first:
            for i in range(prefer_chat_rounds):
                hit = _run_chat_recovery(
                    harder=i > 0, label=f"prefer_chat_{i + 1}"
                )
                if hit is not None:
                    return hit
            # Dedicated last — may still help ks; sd often tag-fails (then ignored).
            hit = _run_dedicated("dedicated_after_prefer_chat")
            if hit is not None:
                return hit
        elif chat_rounds:
            for i in range(chat_rounds):
                hit = _run_chat_recovery(
                    harder=True, label=f"rare_recovery_{i + 1}"
                )
                if hit is not None:
                    return hit
            hit = _run_dedicated("dedicated_after_chat_recovery")
            if hit is not None:
                return hit
        # Keep best non-English candidate rather than English soft-fail.
        if last_restored and not _is_mostly_english_pivot(
            last_restored, language_code=lang, script=script
        ):
            print(
                f"[s4b] rare keep non-English soft lang={lang} "
                f"uuid={row.get('uuid')} finish={last_finish}",
                file=sys.stderr,
                flush=True,
            )
            out.update(
                {
                    "generated_text": last_restored,
                    "translation_applied": True,
                    "translation_script_ok": False,
                    "translator_model": last_model,
                    "translator_finish_reason": last_finish or "rare_soft_keep",
                    "translation_attempts": attempt,
                    "translation_error": ";".join(err_trail) or str(last_error),
                    "translation_soft_fail": True,
                    "translation_generator_repair_attempts": tag_repair_attempts,
                    "translation_repaired_by_generator": False,
                    "stage": "s4b_translation",
                }
            )
            return out
        # True rare failure — English left; do NOT burn generator repairs here.
        error_msg = ";".join(err_trail) or f"rare_translate_failed:{last_error}"
        print(
            f"[s4b] SOFT-FAIL rare uuid={row.get('uuid')} lang={lang} "
            f"error={error_msg}",
            file=sys.stderr,
            flush=True,
        )
        out.update(
            {
                "generated_text": source,
                "translation_applied": False,
                "translation_script_ok": False,
                "translator_model": last_model,
                "translator_finish_reason": "rare_unrecovered",
                "translation_attempts": attempt,
                "translation_error": error_msg,
                "translation_soft_fail": True,
                "translation_generator_repair_attempts": tag_repair_attempts,
                "translation_repaired_by_generator": False,
                "stage": "s4b_translation",
            }
        )
        return out

    # ---- Common langs: chat (≤2), first timeout → dedicated immediately ----
    remaining = 2
    timeout_streak = 0
    while remaining > 0:
        remaining -= 1
        harder = attempt > 0
        text, err, model, finish = _chat_translate_once(
            client,
            protection=protection,
            row=row,
            settings=settings,
            fewshot_extra="",
            retry_harder=harder,
            timeout_s=settings.timeout_s,
        )
        if err is not None:
            if _is_timeout_error(err):
                timeout_streak += 1
                timed_out = True
                last_error = TranslationError(
                    f"timed out:{err} attempt={attempt + 1}"
                )
                print(
                    f"[s4b] chat timeout → dedicated "
                    f"attempt={attempt + 1} uuid={row.get('uuid')} lang={lang}",
                    file=sys.stderr,
                    flush=True,
                )
                attempt += 1
                break
            last_error = err
            attempt += 1
            continue
        assert text is not None
        last_restored = text
        last_model = model
        last_finish = finish
        ok, reason = evaluate_script_purity(
            text, language_code=lang, script=script
        )
        if not ok:
            langid_hint = optional_langid_score(text, language_code=lang)
            detail = reason
            if langid_hint:
                detail = f"{reason};{langid_hint}"
            last_error = TranslationError(
                f"script_purity_failed:{detail} attempt={attempt}"
            )
            attempt += 1
            continue
        return _accept_ok(
            text, model=model, finish=finish, attempts=attempt + 1
        )

    max_chat = attempt
    timed_out = timed_out or (
        last_error is not None and _is_timeout_error(last_error)
    )
    if timed_out or timeout_streak > 0:
        ded_text, ded_err, ded_ok = try_dedicated_translate_fallback(
            client=client,
            english_text=source,
            row=row,
            settings=settings,
            force=True,
            rate_limiter=dedicated_limiter,
        )
        if ded_text and ded_ok:
            return _accept_ok(
                ded_text,
                model=settings.dedicated_translate_model,
                finish="dedicated_after_timeout",
                attempts=max_chat + 1,
            )
        if ded_text:
            last_restored = ded_text
            last_error = TranslationError(ded_err or "dedicated_translate_soft")
            last_model = settings.dedicated_translate_model
            last_finish = "dedicated_after_timeout"
        elif ded_err:
            last_error = TranslationError(ded_err)

    # Translate / restore failed both attempts (often: model dropped or
    # localized a name/place TYPE like PATIENT_NAME). Soft-fail + optional
    # generator rewrite — never abort the stage on one row.
    if last_restored is None:
        error_msg = f"tag_restore_or_translate_failed:{last_error}"
        repair_attempts = 0
        if (
            not is_rare
            and repair_settings is not None
            and repair_settings.max_repairs > 0
        ):
            required = [str(x) for x in (row.get("required_entities") or [])]
            if str(row.get("doc_type_id") or "") == "lab_report":
                required = [t for t in required if t != "STUDENT_ID"]
            repair = repair_document(
                client,
                draft=source,
                row=row,
                required=required,
                issues=[
                    RepairIssue(
                        kind="invalid_type_tags",
                        detail=(
                            "translation_dropped_or_altered_TYPE_tags; "
                            f"{last_error}"
                        ),
                    ),
                    *(
                        [
                            RepairIssue(
                                kind="missing_entities",
                                detail=",".join(required),
                            )
                        ]
                        if required
                        else []
                    ),
                ],
                settings=repair_settings,
                check_script=False,
            )
            repair_attempts = repair.attempts
            if repair.repaired and has_valid_entity_tags(repair.text):
                # Re-try one protected translate from the repaired English pivot.
                try:
                    protection2 = protect_tags(repair.text)
                    if protection2.id_mapping or protection2.name_mapping:
                        result = client.chat_completion(
                            model=settings.model,
                            messages=build_translate_messages(
                                protected_text=protection2.text,
                                language_name=str(
                                    row.get("document_language_name", "")
                                ),
                                language_code=lang,
                                script=script,
                                doc_type_name=str(row.get("doc_type_name", "")),
                                retry_harder=True,
                            ),
                            temperature=settings.temperature,
                            max_tokens=settings.max_tokens,
                            reasoning_effort=settings.reasoning_effort,
                            timeout_s=settings.timeout_s,
                        )
                        restored = restore_tags(
                            result.content.strip(), protection2
                        )
                        ok, reason = evaluate_script_purity(
                            restored, language_code=lang, script=script
                        )
                        if ok:
                            print(
                                f"[s4b] REPAIRED-TAGS+TRANSLATE "
                                f"uuid={row.get('uuid')} lang={lang} "
                                f"doc_type={row.get('doc_type_id')} "
                                f"attempts={repair_attempts}",
                                file=sys.stderr,
                                flush=True,
                            )
                            out.update(
                                {
                                    "generated_text": restored,
                                    "generated_text_en": repair.text,
                                    "translation_applied": True,
                                    "translation_script_ok": True,
                                    "translator_model": result.model,
                                    "translator_finish_reason": (
                                        "generator_tag_repair_then_translate"
                                    ),
                                    "translation_attempts": 3,
                                    "translation_error": None,
                                    "translation_soft_fail": False,
                                    "translation_generator_repair_attempts": (
                                        tag_repair_attempts + repair_attempts
                                    ),
                                    "translation_repaired_by_generator": True,
                                    "stage": "s4b_translation",
                                }
                            )
                            return out
                        error_msg = (
                            f"{error_msg};post_repair_script_purity:{reason}"
                        )
                        last_restored = restored
                except (SarvamClientError, TranslationError) as exc:
                    error_msg = f"{error_msg};post_repair_translate:{exc}"

        print(
            f"[s4b] SOFT-FAIL uuid={row.get('uuid')} lang={lang} "
            f"doc_type={row.get('doc_type_id')} error={error_msg}",
            file=sys.stderr,
            flush=True,
        )
        out.update(
            {
                "generated_text": last_restored or source,
                "translation_applied": bool(last_restored),
                "translation_script_ok": False,
                "translator_model": last_model,
                "translator_finish_reason": "tag_restore_failed",
                "translation_attempts": 2,
                "translation_error": error_msg,
                "translation_soft_fail": True,
                "translation_generator_repair_attempts": (
                    tag_repair_attempts + repair_attempts
                ),
                "translation_repaired_by_generator": False,
                "stage": "s4b_translation",
            }
        )
        return out

    # Known cheap fix: wrong language/script → send English pivot to generator
    # for a full rewrite, then re-check purity (+ tag coverage). Avoids another
    # doomed translate pass and is usually cheaper than dropping the doc.
    # Rare scripts already spent 2 chat tries + dedicated /translate — do NOT
    # burn up to 5 generator repairs (budget); soft-fail for evaluation.
    error_msg = str(last_error)
    langid_hint = optional_langid_score(last_restored, language_code=lang)
    if langid_hint and langid_hint not in error_msg:
        error_msg = f"{error_msg};{langid_hint}"

    repair_attempts = 0
    repaired = False
    if (
        not is_rare
        and repair_settings is not None
        and repair_settings.max_repairs > 0
    ):
        required = [str(x) for x in (row.get("required_entities") or [])]
        purity_detail = error_msg
        repair = repair_document(
            client,
            draft=source,  # English pivot — cleaner rewrite source
            row=row,
            required=required,
            issues=[
                script_issue(
                    language_name=str(row.get("document_language_name") or ""),
                    language_code=lang,
                    script=script,
                    purity_detail=purity_detail,
                )
            ],
            settings=repair_settings,
            check_script=True,
        )
        repair_attempts = repair.attempts
        if repair.repaired:
            missing, stuffed = coverage_and_stuffing(repair.text, required)
            if not missing and not stuffed:
                print(
                    f"[s4b] REPAIRED-BY-GENERATOR uuid={row.get('uuid')} "
                    f"lang={lang} doc_type={row.get('doc_type_id')} "
                    f"attempts={repair_attempts}",
                    file=sys.stderr,
                    flush=True,
                )
                out.update(
                    {
                        "generated_text": repair.text,
                        "translation_applied": True,
                        "translation_script_ok": True,
                        "translator_model": repair.model or last_model,
                        "translator_finish_reason": "generator_script_repair",
                        "translation_attempts": 2,
                        "translation_error": None,
                        "translation_soft_fail": False,
                        "translation_generator_repair_attempts": repair_attempts,
                        "translation_repaired_by_generator": True,
                        "stage": "s4b_translation",
                    }
                )
                return out
            repaired = False
            error_msg = (
                f"{error_msg};generator_repair_left_coverage:"
                f"missing={missing};stuffed={stuffed}"
            )
        elif repair.text and repair.text != source:
            # Keep best repair attempt for downstream audit if still impure.
            ok, reason = evaluate_script_purity(
                repair.text, language_code=lang, script=script
            )
            if ok:
                last_restored = repair.text
            error_msg = (
                f"{error_msg};generator_repair_failed:"
                f"{repair.error or reason or 'issues_remain'}"
            )

    print(
        f"[s4b] SOFT-FAIL uuid={row.get('uuid')} lang={lang} "
        f"doc_type={row.get('doc_type_id')} error={error_msg}",
        file=sys.stderr,
        flush=True,
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
            "translation_generator_repair_attempts": repair_attempts,
            "translation_repaired_by_generator": repaired,
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
    repair_settings: RepairSettings | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected = list(rows)
    if settings.max_docs is not None:
        selected = selected[: settings.max_docs]
    if not selected:
        raise TranslationError("No rows selected for translation")

    # Shared across workers — per-call limiters stampede /translate and cause timeouts.
    dedicated_limiter = RateLimiter(settings.dedicated_translate_requests_per_minute)

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
    print(
        f"[s4b] start rows={len(selected)} pending={len(pending)} "
        f"resumed={resumed} workers={workers} "
        f"timeout_s={settings.timeout_s} model={settings.model} "
        f"rare_prefer_chat={list(settings.rare_prefer_chat_languages)} "
        f"dedicated_rpm={settings.dedicated_translate_requests_per_minute}",
        file=sys.stderr,
        flush=True,
    )
    if pending:
        done_count = 0
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {
                pool.submit(
                    _translate_one,
                    index,
                    row,
                    client=client,
                    settings=settings,
                    repair_settings=repair_settings,
                    dedicated_limiter=dedicated_limiter,
                ): (index, req)
                for index, row, req in pending
            }
            for future in as_completed(futures):
                index, req = futures[future]
                try:
                    out = future.result()
                except Exception as exc:  # noqa: BLE001 — one row must not kill stage
                    row = selected[index]
                    err = f"row_exception:{exc}"
                    lang = str(row.get("document_language_code") or "")
                    recovered = False
                    # Last-ditch: re-run _translate_one once (has chat+dedicated retries),
                    # then dedicated alone if that still raises.
                    if (
                        settings.enable_dedicated_translate_fallback
                        and _is_timeout_error(exc)
                    ):
                        print(
                            f"[s4b] row timeout → retranslate+dedicated "
                            f"uuid={row.get('uuid')} lang={lang}",
                            file=sys.stderr,
                            flush=True,
                        )
                        try:
                            out = _translate_one(
                                index,
                                row,
                                client=client,
                                settings=settings,
                                repair_settings=repair_settings,
                                dedicated_limiter=dedicated_limiter,
                            )
                            if out.get("translation_applied") and not out.get(
                                "translation_soft_fail"
                            ):
                                recovered = True
                        except Exception as retry_exc:  # noqa: BLE001
                            err = f"{err};retry:{retry_exc}"
                        if not recovered:
                            ded_text, ded_err, ded_ok = try_dedicated_translate_fallback(
                                client=client,
                                english_text=str(row.get("generated_text") or ""),
                                row=row,
                                settings=settings,
                                force=True,
                                rate_limiter=dedicated_limiter,
                            )
                            if ded_text and ded_ok:
                                out = dict(row)
                                out.update(
                                    {
                                        "generated_text": ded_text,
                                        "generated_text_en": row.get("generated_text"),
                                        "translation_applied": True,
                                        "translation_script_ok": True,
                                        "translator_model": (
                                            settings.dedicated_translate_model
                                        ),
                                        "translator_finish_reason": (
                                            "dedicated_after_timeout"
                                        ),
                                        "translation_attempts": 1,
                                        "translation_error": None,
                                        "translation_soft_fail": False,
                                        "translation_generator_repair_attempts": 0,
                                        "translation_repaired_by_generator": False,
                                        "stage": "s4b_translation",
                                    }
                                )
                                recovered = True
                            else:
                                err = (
                                    f"{err};"
                                    f"{ded_err or 'dedicated_after_timeout_failed'}"
                                )
                    if recovered:
                        results[index] = out
                        if checkpoint is not None:
                            checkpoint.append(
                                row_key=row_key_from_prompt(selected[index]),
                                status="ok",
                                request_hash=req,
                                payload=out,
                                error=None,
                            )
                        done_count += 1
                        print(
                            f"[s4b] progress {done_count}/{len(pending)} "
                            f"uuid={row.get('uuid')} lang={lang} "
                            f"ok=recovered_after_timeout",
                            file=sys.stderr,
                            flush=True,
                        )
                        continue
                    print(
                        f"[s4b] SOFT-FAIL uuid={row.get('uuid')} "
                        f"lang={row.get('document_language_code')} "
                        f"doc_type={row.get('doc_type_id')} error={err}",
                        file=sys.stderr,
                        flush=True,
                    )
                    out = dict(row)
                    out.update(
                        {
                            "generated_text": row.get("generated_text"),
                            "generated_text_en": row.get("generated_text"),
                            "translation_applied": False,
                            "translation_script_ok": False,
                            "translator_model": None,
                            "translator_finish_reason": "row_exception",
                            "translation_attempts": 0,
                            "translation_error": err,
                            "translation_soft_fail": True,
                            "translation_generator_repair_attempts": 0,
                            "translation_repaired_by_generator": False,
                            "stage": "s4b_translation",
                        }
                    )
                results[index] = out
                if checkpoint is not None:
                    err_msg = out.get("translation_error")
                    if _is_retryable_transport_error(
                        err_msg if isinstance(err_msg, str) else None
                    ):
                        # Transient DNS/timeout/connection — resume must retry.
                        status = "hard_fail"
                    elif out.get("translation_soft_fail"):
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
                done_count += 1
                if done_count == 1 or done_count % 5 == 0 or done_count == len(pending):
                    print(
                        f"[s4b] progress {done_count}/{len(pending)} "
                        f"uuid={out.get('uuid')} lang={out.get('document_language_code')} "
                        f"soft={bool(out.get('translation_soft_fail'))} "
                        f"applied={bool(out.get('translation_applied'))}",
                        file=sys.stderr,
                        flush=True,
                    )
    outputs = [results[i] for i in range(len(selected))]
    transport_fails = [
        row
        for row in outputs
        if _is_retryable_transport_error(
            row.get("translation_error")
            if isinstance(row.get("translation_error"), str)
            else None
        )
    ]
    if transport_fails:
        # Fail closed so operators resume S4b after DNS/API recovers (docs: checkpoint resume).
        # Do not write a poisoned documents.jsonl of English soft-fails.
        raise TranslationError(
            f"S4b transport failures on {len(transport_fails)}/{len(outputs)} rows "
            f"(DNS/timeout/connection). Checkpointed as hard_fail for resume. "
            f"Example: {transport_fails[0].get('translation_error')}"
        )
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
        "generator_repaired_count": sum(
            1 for row in outputs if row.get("translation_repaired_by_generator")
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
        f"- generator_repaired_count: `{audit.get('generator_repaired_count', 0)}`",
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
    print("[s4b] boot: load env + settings", file=sys.stderr, flush=True)
    load_env_file()
    settings = load_settings(pipeline_config)
    print(
        f"[s4b] boot: input={settings.input_jsonl} "
        f"workers={settings.max_workers} rare={list(settings.rare_script_languages)}",
        file=sys.stderr,
        flush=True,
    )
    api_key = require_env(settings.api_key_env)
    limiter = (
        RateLimiter(settings.requests_per_minute)
        if settings.requests_per_minute is not None
        else None
    )
    client = SarvamClient(
        api_key=api_key, base_url=settings.base_url, rate_limiter=limiter
    )
    root = load_yaml(pipeline_config)
    gen = root.get("generation") if isinstance(root.get("generation"), dict) else {}
    repair_settings = (
        load_repair_settings_from_generation(gen) if gen.get("model") else None
    )
    print("[s4b] boot: reading input jsonl", file=sys.stderr, flush=True)
    rows = read_jsonl(settings.input_jsonl)
    print(f"[s4b] boot: rows_loaded={len(rows)}", file=sys.stderr, flush=True)
    checkpoint = CheckpointStore(settings.output_dir / "checkpoint.jsonl")
    translated, audit = translate_rows(
        rows,
        client=client,
        settings=settings,
        checkpoint=checkpoint,
        repair_settings=repair_settings,
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
