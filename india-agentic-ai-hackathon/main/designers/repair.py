"""Targeted generator repair for known, cheap-to-fix soft failures.

Rather than soft-failing immediately (or burning full re-generation batches),
send the draft back to the generator with a precise fix instruction, then
re-check. Known repairable classes:

- missing required [[TYPE|…]] tags
- entity stuffing / dump lists
- wrong language/script (e.g. Gujarati docs that stayed English after translate)

Used by S4 Data Designer post-pass and S4b after translation script failure.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from main.designers.entity_checks import (
    MAX_OCCURRENCES_PER_TYPE,
    coverage_and_stuffing,
)
from main.llm.sarvam import SarvamClient, SarvamClientError
from main.validators.script_purity import evaluate_script_purity


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
    kind: str  # missing_entities | entity_stuffing | wrong_language_script
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


def issues_from_coverage(
    missing: Sequence[str], stuffed: Sequence[str]
) -> list[RepairIssue]:
    issues: list[RepairIssue] = []
    if missing:
        issues.append(
            RepairIssue(
                kind="missing_entities",
                detail=",".join(missing),
            )
        )
    if stuffed:
        issues.append(
            RepairIssue(
                kind="entity_stuffing",
                detail=",".join(stuffed),
            )
        )
    return issues


def script_issue(
    *,
    language_name: str,
    language_code: str,
    script: str,
    purity_detail: str,
) -> RepairIssue:
    return RepairIssue(
        kind="wrong_language_script",
        detail=(
            f"target={language_name}/{language_code}/{script}; {purity_detail}"
        ),
    )


def _repair_instructions(issues: Sequence[RepairIssue]) -> str:
    bits: list[str] = []
    for issue in issues:
        if issue.kind == "missing_entities":
            bits.append(
                "MISSING TAGS — previous draft omitted mandatory entity types: "
                f"{issue.detail}. Include EVERY listed TYPE at least once as "
                "[[TYPE|surrogate_value]]. Do not invent new TYPE names. "
                "If HOSPITAL_NAME is missing, tag the facility name "
                "(not only HOSPITAL_ID)."
            )
        elif issue.kind == "entity_stuffing":
            bits.append(
                "STUFFING — previous draft repeated/dumped tags for: "
                f"{issue.detail}. Rewrite so each non-speaker TYPE appears at "
                f"most {MAX_OCCURRENCES_PER_TYPE} time(s), only where clinically "
                "natural. Put AGE/GENDER once in a header for chat docs."
            )
        elif issue.kind == "wrong_language_script":
            bits.append(
                "WRONG LANGUAGE/SCRIPT — previous output was mostly English or "
                f"wrong script ({issue.detail}). Rewrite ALL clinical prose and "
                "headings into the target language and script. Keep every "
                "[[TYPE|value]] tag. Translate name/place VALUES into the "
                "target script when natural; keep ID/number/email/URL values "
                "unchanged (Latin/digits)."
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
) -> list[dict[str, str]]:
    lang_name = str(row.get("document_language_name") or "")
    lang_code = str(row.get("document_language_code") or "")
    script = str(row.get("document_script") or "")
    doc_type = str(row.get("doc_type_name") or row.get("doc_type_id") or "")
    domain = str(row.get("domain_name") or row.get("domain_id") or "")

    system = (
        "You repair synthetic Indian clinical documents for a PHI NER pipeline.\n"
        "Rules:\n"
        "1) Output ONLY the full repaired document text — no markdown fences, "
        "no preamble.\n"
        "2) Preserve every required [[TYPE|value]] annotation; TYPE names stay "
        "exact uppercase.\n"
        "3) Do not invent TYPE names outside the mandatory list.\n"
        "4) Keep clinical content coherent with the assigned domain and persona.\n"
        "5) When asked to change language/script, rewrite the whole body — do "
        "not leave English paragraphs."
    )
    mandatory = ", ".join(required) if required else "(none listed)"
    user = (
        f"Document type: {doc_type}\n"
        f"Clinical domain: {domain}\n"
        f"Target language: {lang_name} (code={lang_code}, script={script})\n"
        f"Mandatory TYPEs (each ≥ once): {mandatory}\n\n"
        f"REPAIR INSTRUCTIONS:\n{_repair_instructions(issues)}\n\n"
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
    missing, stuffed = coverage_and_stuffing(text, required)
    issues = issues_from_coverage(missing, stuffed)
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
    """Call generator up to ``max_repairs`` times until checks pass or exhausted."""
    if settings.max_repairs < 1 or not issues:
        return RepairResult(
            text=draft,
            attempts=0,
            repaired=False,
            issues_remaining=list(issues),
        )

    text = draft
    remaining = list(issues)
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
            )

    return RepairResult(
        text=text,
        attempts=attempts,
        repaired=False,
        issues_remaining=remaining,
        model=last_model,
        finish_reason=last_finish,
        error=last_error,
    )


def load_repair_settings_from_generation(block: Mapping[str, Any]) -> RepairSettings:
    """Build repair settings from the pipeline ``generation`` YAML block."""
    reasoning = block.get("reasoning_effort", None)
    if reasoning is not None:
        reasoning = str(reasoning)
    max_repairs = int(
        block.get("repair_retries", block.get("empty_content_retries", 2))
    )
    if max_repairs < 0:
        max_repairs = 0
    return RepairSettings(
        model=str(block["model"]),
        temperature=float(block.get("temperature", 0.3)),
        max_tokens=int(block.get("max_tokens", 8192)),
        reasoning_effort=reasoning,
        timeout_s=float(block.get("timeout_s", 180)),
        max_repairs=max_repairs,
    )
