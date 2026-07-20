"""Targeted generator repair for known soft failures (S4 / S4b / S5 / S6).

Philosophy: machine-checkable and judge-flagged defects are sent back to the
generator with *clear* fix instructions (3–5 attempts), then re-checked.
Prefer deterministic checksum/phone fixes when possible (no LLM cost).
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from main.designers.entity_checks import (
    MAX_OCCURRENCES_PER_TYPE,
    coverage_and_stuffing,
    invalid_type_tags,
    tag_issues,
)
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.validators.checksums import verhoeff_validate
from main.validators.script_purity import evaluate_script_purity

_TAG_VALUE_RE = re.compile(r"\[\[([A-Z][A-Z0-9_]*)\|([^\]]*)\]\]")

# Judge flags we know how to repair with clear instructions.
REPAIRABLE_JUDGE_FLAGS: frozenset[str] = frozenset(
    {
        "dialect_script_impurity",
        "instruction_drift",
        "surrogate_plausibility_collapse",
        "domain_persona_mismatch",
        "cross_language_entity_shift",
        "invented_entity_type",
        "length_violation",
    }
)


@dataclass(frozen=True)
class RepairSettings:
    model: str
    temperature: float
    max_tokens: int
    reasoning_effort: str | None
    timeout_s: float
    max_repairs: int


@dataclass(frozen=True)
class RepairIssue:
    kind: str
    detail: str


@dataclass
class RepairResult:
    text: str
    attempts: int
    repaired: bool
    issues_remaining: list[RepairIssue]
    model: str | None = None
    finish_reason: str | None = None
    error: str | None = None
    deterministic_fixes: list[str] | None = None


def issues_from_coverage(
    missing: Sequence[str],
    stuffed: Sequence[str],
    invalid_types: Sequence[str] | None = None,
) -> list[RepairIssue]:
    issues: list[RepairIssue] = []
    if invalid_types:
        issues.append(
            RepairIssue(kind="invalid_type_tags", detail=",".join(invalid_types))
        )
    if missing:
        issues.append(RepairIssue(kind="missing_entities", detail=",".join(missing)))
    if stuffed:
        issues.append(RepairIssue(kind="entity_stuffing", detail=",".join(stuffed)))
    return issues


def issues_from_text(text: str, required: Sequence[str]) -> list[RepairIssue]:
    missing, stuffed, invalid = tag_issues(text, required)
    return issues_from_coverage(missing, stuffed, invalid)


def script_issue(
    *,
    language_name: str,
    language_code: str,
    script: str,
    purity_detail: str,
) -> RepairIssue:
    return RepairIssue(
        kind="wrong_language_script",
        detail=f"target={language_name}/{language_code}/{script}; {purity_detail}",
    )


def issues_from_judge_flags(
    flags: Sequence[str],
    *,
    reasoning: str = "",
    row: Mapping[str, Any] | None = None,
) -> list[RepairIssue]:
    """Map S5 judge flags → repair issues (only known recoverable flags)."""
    row = row or {}
    issues: list[RepairIssue] = []
    seen: set[str] = set()
    for flag in flags:
        flag = str(flag).strip()
        if flag not in REPAIRABLE_JUDGE_FLAGS or flag in seen:
            continue
        seen.add(flag)
        if flag == "dialect_script_impurity":
            issues.append(
                script_issue(
                    language_name=str(row.get("document_language_name") or ""),
                    language_code=str(row.get("document_language_code") or ""),
                    script=str(row.get("document_script") or ""),
                    purity_detail=reasoning or flag,
                )
            )
        else:
            issues.append(RepairIssue(kind=flag, detail=reasoning or flag))
    return issues


def issues_from_auditor_errors(
    errors: Sequence[str],
    *,
    row: Mapping[str, Any] | None = None,
) -> list[RepairIssue]:
    """Map S6 auditor errors → repair issues (skip pure judge_failed)."""
    row = row or {}
    issues: list[RepairIssue] = []
    missing: list[str] = []
    stuffed: list[str] = []
    for err in errors:
        err = str(err)
        if err.startswith("missing_required:"):
            missing.extend(err.split(":", 1)[1].split(","))
        elif err.startswith("upstream_missing_required:"):
            missing.extend(err.split(":", 1)[1].split(","))
        elif err.startswith("entity_stuffing:") and "total_tags" not in err:
            stuffed.extend(err.split(":", 1)[1].split(","))
        elif "entity_stuffing_total_tags" in err or err.startswith(
            "upstream_entity_stuffing"
        ):
            stuffed.append(err)
        elif err.startswith("format:AADHAAR_NUMBER:"):
            issues.append(RepairIssue(kind="format_aadhaar", detail=err))
        elif err.startswith("format:PHONE_NUMBER:"):
            issues.append(RepairIssue(kind="format_phone", detail=err))
        elif err.startswith("format:"):
            issues.append(RepairIssue(kind="format_other", detail=err))
        elif err.startswith("phi_residue:"):
            issues.append(RepairIssue(kind="phi_residue", detail=err))
        elif "translation_soft_fail" in err or "script_purity" in err:
            issues.append(
                script_issue(
                    language_name=str(row.get("document_language_name") or ""),
                    language_code=str(row.get("document_language_code") or ""),
                    script=str(row.get("document_script") or ""),
                    purity_detail=err,
                )
            )
        elif err.startswith("upstream_generation_soft_fail:missing_required"):
            # parse embedded types if present
            if "missing_required_entities:" in err:
                part = err.split("missing_required_entities:", 1)[1]
                missing.extend(part.split(",")[:20])
            else:
                issues.append(RepairIssue(kind="missing_entities", detail=err))
        # judge_failed / span / dics — not repaired here
    missing = [m for m in dict.fromkeys(missing) if m]
    stuffed = [s for s in dict.fromkeys(stuffed) if s]
    issues.extend(issues_from_coverage(missing, stuffed))
    return issues


def _verhoeff_check_digit(body11: str) -> str:
    for digit in "0123456789":
        cand = body11 + digit
        if verhoeff_validate(cand):
            return digit
    raise RuntimeError("Verhoeff check digit search failed")


def make_valid_aadhaar(seed: str) -> str:
    """12-digit Verhoeff-valid Aadhaar starting with 2–9 (synthetic)."""
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    body = "2" + "".join(str(int(digest[i], 16) % 10) for i in range(10))
    return body + _verhoeff_check_digit(body)


def make_valid_phone(seed: str) -> str:
    digest = hashlib.sha256(("phone:" + seed).encode("utf-8")).hexdigest()
    # Indian mobile: starts 6–9
    lead = str(6 + (int(digest[0], 16) % 4))
    rest = "".join(str(int(digest[i], 16) % 10) for i in range(1, 10))
    return lead + rest


def apply_deterministic_format_fixes(text: str) -> tuple[str, list[str]]:
    """Fix invalid Aadhaar Verhoeff / phone tags in-place without an LLM call."""
    from main.validators.checksums import validate_aadhaar, validate_phone

    fixes: list[str] = []

    def replacer(match: re.Match[str]) -> str:
        entity_type, value = match.group(1), match.group(2)
        if entity_type == "AADHAAR_NUMBER":
            ok, _code = validate_aadhaar(value)
            if ok:
                return match.group(0)
            new_val = make_valid_aadhaar(value)
            fixes.append(f"aadhaar:{value}->{new_val}")
            return f"[[AADHAAR_NUMBER|{new_val}]]"
        if entity_type == "PHONE_NUMBER":
            ok, _code = validate_phone(value)
            if ok:
                return match.group(0)
            digits = re.sub(r"\D", "", value)
            if digits.startswith("91") and len(digits) == 12:
                digits = digits[2:]
            if len(digits) == 10 and digits[0] in "6789":
                new_val = digits
            else:
                new_val = make_valid_phone(value)
            fixes.append(f"phone:{value}->{new_val}")
            return f"[[PHONE_NUMBER|{new_val}]]"
        return match.group(0)

    return _TAG_VALUE_RE.sub(replacer, text), fixes


def _repair_instructions(issues: Sequence[RepairIssue]) -> str:
    bits: list[str] = []
    for issue in issues:
        if issue.kind == "missing_entities":
            bits.append(
                "MISSING TAGS — omit none of: "
                f"{issue.detail}. Each MUST appear ≥ once as [[TYPE|value]] with "
                "the EXACT English uppercase TYPE from the allow-list "
                "(e.g. [[PATIENT_NAME|…]], [[MRN|…]]). "
                "Tag HOSPITAL_NAME for the facility name (HOSPITAL_ID alone is not enough). "
                "Tag DOCTOR_NAME even if the name appears in prose."
            )
        elif issue.kind == "invalid_type_tags":
            bits.append(
                "INVALID / LOCALIZED TYPE NAMES — you used illegal TYPE spellings: "
                f"{issue.detail}. TYPE must be EXACT ASCII uppercase from the "
                "allow-list (PATIENT_NAME, AGE, GENDER, MRN, DOCTOR_NAME, …). "
                "NEVER translate or localize the TYPE itself "
                "(forbidden: [[রোগীর_নাম|…]], [[एज|…]], [[PatientName|…]]). "
                "Rewrite as an English-pivot document with correct [[TYPE|value]] tags; "
                "a later stage translates prose — not TYPE names."
            )
        elif issue.kind == "entity_stuffing":
            bits.append(
                "STUFFING — reduce repeats for: "
                f"{issue.detail}. Each non-speaker TYPE ≤ "
                f"{MAX_OCCURRENCES_PER_TYPE} times; no dump lists."
            )
        elif issue.kind == "wrong_language_script":
            bits.append(
                "WRONG LANGUAGE/SCRIPT — "
                f"({issue.detail}). Rewrite ALL clinical prose/headings into the "
                "target language AND exact target script (not Devanagari unless that "
                "is the target; not English). Keep [[TYPE|…]] tags. Translate "
                "name/place VALUES into the target script when natural; keep "
                "ID/number/email/URL values Latin/digits."
            )
        elif issue.kind == "dialect_script_impurity":
            bits.append(
                "SCRIPT IMPURITY — clinical narrative is wrong language/script. "
                f"Detail: {issue.detail}. Rewrite the WHOLE body into the target "
                "script. Latin inside ID tags is fine; prose must not stay English."
            )
        elif issue.kind == "instruction_drift":
            bits.append(
                "INSTRUCTION DRIFT — content drifted from assigned clinical domain. "
                f"Detail: {issue.detail}. Rewrite so chief complaint, findings, and "
                "plan clearly match the assigned DOMAIN — not a generic TB/default story."
            )
        elif issue.kind == "surrogate_plausibility_collapse":
            bits.append(
                "PLAUSIBILITY — geography/names/IDs contradict persona anchors. "
                f"Detail: {issue.detail}. DISTRICT/VILLAGE/HOSPITAL must sit in the "
                "persona state+district. PATIENT_NAME and ABHA local-part must align. "
                "Do not invent distant districts."
            )
        elif issue.kind == "domain_persona_mismatch":
            bits.append(
                "DOMAIN×PERSONA MISMATCH — clinical content conflicts with sex/age. "
                f"Detail: {issue.detail}. Match persona sex and age exactly "
                "(no male maternal delivery; no paediatric content for adults)."
            )
        elif issue.kind == "cross_language_entity_shift":
            bits.append(
                "ENTITY SCRIPT SHIFT — person/place tag values wrong script. "
                f"Detail: {issue.detail}. Put PATIENT_NAME/DOCTOR_NAME/HOSPITAL_NAME/"
                "DISTRICT values into the target script when natural."
            )
        elif issue.kind == "invented_entity_type":
            bits.append(
                "INVENTED TYPE — remove or rewrite illegal TYPE names. "
                f"Detail: {issue.detail}. Never use DATE/TIME/APPOINTMENT_DATE/"
                "POLICY_NUMBER. Put dates/money in plain prose."
            )
        elif issue.kind == "length_violation":
            bits.append(
                "LENGTH — SMS/note is far too long. "
                f"Detail: {issue.detail}. Compress to ≤ ~400 characters / 2–4 "
                "sentences while keeping every mandatory tag once."
            )
        elif issue.kind == "format_aadhaar":
            bits.append(
                "AADHAAR FORMAT — replace [[AADHAAR_NUMBER|…]] with a plausible "
                "12-digit Verhoeff-valid synthetic Aadhaar (leading digit 2–9)."
            )
        elif issue.kind == "format_phone":
            bits.append(
                "PHONE FORMAT — replace [[PHONE_NUMBER|…]] with a 10-digit Indian "
                "mobile starting with 6–9 (optional +91 ok)."
            )
        elif issue.kind == "format_other":
            bits.append(f"FORMAT — fix invalid tagged value: {issue.detail}.")
        elif issue.kind == "phi_residue":
            bits.append(
                "PHI RESIDUE — bare ID-like numbers appear outside tags. "
                f"Detail: {issue.detail}. Wrap them as [[TYPE|value]] or remove."
            )
        else:
            bits.append(f"Fix issue {issue.kind}: {issue.detail}")
    return " ".join(bits)


def build_repair_messages(
    *,
    draft: str,
    row: Mapping[str, Any],
    issues: Sequence[RepairIssue],
    required: Sequence[str],
    english_pivot: bool = False,
) -> list[dict[str, str]]:
    lang_name = str(row.get("document_language_name") or "")
    lang_code = str(row.get("document_language_code") or "")
    script = str(row.get("document_script") or "")
    doc_type = str(row.get("doc_type_name") or row.get("doc_type_id") or "")
    domain = str(row.get("domain_name") or row.get("domain_id") or "")

    system = (
        "You repair synthetic Indian clinical documents for a PHI NER pipeline.\n"
        "Rules:\n"
        "1) Output ONLY the full repaired document text — no markdown fences.\n"
        "2) TYPE names inside [[TYPE|value]] MUST be EXACT English uppercase "
        "allow-list ids (PATIENT_NAME, MRN, …). Never translate/localize TYPE.\n"
        "3) Do not invent TYPE names (no DATE/TIME/POLICY_NUMBER).\n"
        "4) Clinical content MUST match assigned domain AND persona sex/age/"
        "state/district.\n"
        "5) When fixing missing/invalid tags at generation time, rewrite as an "
        "English (Latin) pivot document with correct tags — a later stage "
        "translates prose to the target language.\n"
        "6) When fixing language/script after translation, rewrite the whole "
        "body into the exact target script — keep TYPE names English."
    )
    mandatory = ", ".join(required) if required else "(none listed)"
    anchors = (
        f"sex={row.get('sex')}, age={row.get('age')}, "
        f"state={row.get('state')}, district={row.get('district')}, "
        f"zone={row.get('zone')}"
    )
    if english_pivot:
        lang_block = (
            f"OUTPUT LANGUAGE FOR THIS REPAIR: English (Latin script) ONLY.\n"
            f"Target Indic language ({lang_name}/{script}) is for a LATER "
            "pipeline stage — do NOT write the body in that language now.\n"
            "Replace any localized TYPE spellings "
            "(e.g. রোগীর_নাম, বয়স, এম.আর.এন) with ASCII allow-list TYPE names.\n"
        )
    else:
        lang_block = (
            f"Target language: {lang_name} (code={lang_code}, script={script})\n"
            "Rewrite clinical prose into that exact script; keep TYPE names ASCII.\n"
        )
    user = (
        f"Document type: {doc_type}\n"
        f"Clinical domain: {domain}\n"
        f"{lang_block}"
        f"Persona anchors (MUST stay consistent): {anchors}\n"
        f"Mandatory TYPEs (each ≥ once): {mandatory}\n\n"
        f"REPAIR INSTRUCTIONS (follow ALL):\n{_repair_instructions(issues)}\n\n"
        f"Previous draft to repair:\n{draft}"
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _evaluate(
    text: str,
    *,
    required: Sequence[str],
    row: Mapping[str, Any],
    check_script: bool,
) -> list[RepairIssue]:
    missing, stuffed, invalid = tag_issues(text, required)
    issues = issues_from_coverage(missing, stuffed, invalid)
    if check_script:
        lang = str(row.get("document_language_code") or "")
        script = str(row.get("document_script") or "")
        if lang and lang not in {"en", "en_IN"}:
            ok, reason = evaluate_script_purity(
                text, language_code=lang, script=script
            )
            if not ok:
                issues.append(
                    script_issue(
                        language_name=str(row.get("document_language_name") or ""),
                        language_code=lang,
                        script=script,
                        purity_detail=reason or "script_purity_failed",
                    )
                )
    return issues


def repair_document(
    client: SarvamClient,
    *,
    draft: str,
    row: Mapping[str, Any],
    required: Sequence[str],
    issues: Sequence[RepairIssue],
    settings: RepairSettings,
    check_script: bool = False,
) -> RepairResult:
    """Call generator up to ``max_repairs`` times until checks pass or exhausted.

    Deterministic Aadhaar/phone fixes are applied first (no LLM). Remaining
    issues go to the generator with clear instructions.
    """
    text = draft
    deterministic_fixes: list[str] = []
    text, deterministic_fixes = apply_deterministic_format_fixes(text)

    # Drop format_* issues after deterministic pass — re-evaluate coverage/script.
    llm_issues = [i for i in issues if i.kind not in {"format_aadhaar", "format_phone"}]
    if check_script or llm_issues:
        remaining = _evaluate(
            text, required=required, row=row, check_script=check_script
        )
        # Keep non-coverage judge/auditor semantic issues for LLM
        semantic_kinds = {
            "instruction_drift",
            "surrogate_plausibility_collapse",
            "domain_persona_mismatch",
            "cross_language_entity_shift",
            "invented_entity_type",
            "length_violation",
            "phi_residue",
            "format_other",
            "wrong_language_script",
            "dialect_script_impurity",
        }
        for issue in llm_issues:
            if issue.kind in semantic_kinds and all(
                i.kind != issue.kind for i in remaining
            ):
                remaining.append(issue)
    else:
        remaining = list(llm_issues)

    if not remaining:
        return RepairResult(
            text=text,
            attempts=0,
            repaired=bool(deterministic_fixes) or text != draft,
            issues_remaining=[],
            deterministic_fixes=deterministic_fixes or None,
        )

    if settings.max_repairs < 1:
        return RepairResult(
            text=text,
            attempts=0,
            repaired=bool(deterministic_fixes),
            issues_remaining=remaining,
            deterministic_fixes=deterministic_fixes or None,
        )

    last_model: str | None = None
    last_finish: str | None = None
    last_error: str | None = None
    attempts = 0

    for _ in range(settings.max_repairs):
        attempts += 1
        try:
            result = client.chat_completion(
                model=settings.model,
                messages=build_repair_messages(
                    draft=text,
                    row=row,
                    issues=remaining,
                    required=required,
                    english_pivot=not check_script,
                ),
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
                reasoning_effort=settings.reasoning_effort,
                timeout_s=settings.timeout_s,
            )
        except SarvamClientError as exc:
            last_error = str(exc)
            break

        candidate = (result.content or "").strip()
        last_model = result.model
        last_finish = result.finish_reason
        if not candidate:
            last_error = "empty repair content"
            continue

        text = candidate
        text, more_fixes = apply_deterministic_format_fixes(text)
        deterministic_fixes.extend(more_fixes)

        remaining = _evaluate(
            text, required=required, row=row, check_script=check_script
        )
        if not remaining:
            return RepairResult(
                text=text,
                attempts=attempts,
                repaired=True,
                issues_remaining=[],
                model=last_model,
                finish_reason=last_finish,
                deterministic_fixes=deterministic_fixes or None,
            )
        # Semantic judge/auditor flags are re-validated by the caller (re-judge /
        # re-audit). After an LLM rewrite, keep only coverage/script remainder.
        remaining = [
            i
            for i in remaining
            if i.kind
            in {
                "missing_entities",
                "invalid_type_tags",
                "entity_stuffing",
                "wrong_language_script",
                "dialect_script_impurity",
            }
        ]
        if not remaining:
            return RepairResult(
                text=text,
                attempts=attempts,
                repaired=True,
                issues_remaining=[],
                model=last_model,
                finish_reason=last_finish,
                deterministic_fixes=deterministic_fixes or None,
            )

    return RepairResult(
        text=text,
        attempts=attempts,
        repaired=False,
        issues_remaining=remaining,
        model=last_model,
        finish_reason=last_finish,
        error=last_error,
        deterministic_fixes=deterministic_fixes or None,
    )


def clear_upstream_soft_fail_fields(row: dict[str, Any]) -> None:
    """After a successful content repair, stop S6 from re-failing on upstream flags."""
    row["generation_soft_fail"] = False
    row["generation_soft_fail_reasons"] = []
    row["entity_coverage_complete"] = True
    row["missing_required_entities"] = []
    row["entity_stuffing"] = False
    row["stuffed_entity_types"] = []
    row["translation_soft_fail"] = False
    row["translation_script_ok"] = True
    row["translation_error"] = None


def load_repair_settings_from_generation(block: Mapping[str, Any]) -> RepairSettings:
    """Build repair settings from the pipeline ``generation`` YAML block."""
    reasoning = block.get("reasoning_effort", None)
    if reasoning is not None:
        reasoning = str(reasoning)
    # Default 5 attempts — recover known soft fails before giving up.
    max_repairs = int(block.get("repair_retries", 5))
    if max_repairs < 0:
        max_repairs = 0
    return RepairSettings(
        model=str(block.get("model", "sarvam-105b")),
        temperature=float(block.get("temperature", 0.3)),
        max_tokens=int(block.get("max_tokens", 8192)),
        reasoning_effort=reasoning,
        timeout_s=float(block.get("timeout_s", 180)),
        max_repairs=max_repairs,
    )
