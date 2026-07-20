"""Stage 3 — Prompt construction from persona + taxonomy + entity rules."""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq

from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

PROMPT_COLUMNS: tuple[str, ...] = (
    "system_prompt",
    "user_prompt",
    "required_entities",
    "optional_entities",
    "stage",
)


@dataclass(frozen=True)
class EntitySpec:
    id: str
    name: str
    category: str


@dataclass(frozen=True)
class EntityProfile:
    doc_type_id: str
    required: tuple[str, ...]
    optional: tuple[str, ...]


@dataclass(frozen=True)
class AnnotationRules:
    pattern: str
    description: str
    rules: tuple[str, ...]


@dataclass(frozen=True)
class PromptSettings:
    input_jsonl: Path
    entities_config: Path
    entity_profiles_config: Path
    annotation_rules_config: Path
    entity_format_examples_config: Path
    doc_format_examples_config: Path
    output_dir: Path
    max_docs: int | None
    language_codes: tuple[str, ...] | None
    # Keep Nemotron narrative columns in JSONL for provenance, but do NOT dump
    # long lifestyle text into the LLM user prompt (it distracts generation).
    include_persona_narrative_in_prompt: bool
    persona_narrative_max_chars: int
    # If true, required ∪ optional must all appear (≥1 each) in the generated doc.
    require_all_profile_entities: bool


class PromptBuildError(RuntimeError):
    pass


def load_settings(pipeline_config: Path) -> PromptSettings:
    root = load_yaml(pipeline_config)
    block = root.get("prompt_construction")
    if not isinstance(block, dict):
        raise ValueError(f"'prompt_construction' mapping required in {pipeline_config}")

    required = (
        "input_jsonl",
        "entities_config",
        "entity_profiles_config",
        "annotation_rules_config",
        "output_dir",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing prompt_construction keys {missing}")

    language_codes = block.get("language_codes")
    if language_codes is not None:
        if not isinstance(language_codes, list) or not all(
            isinstance(code, str) for code in language_codes
        ):
            raise ValueError("'language_codes' must be null or a list of strings")
        language_tuple: tuple[str, ...] | None = tuple(language_codes)
    else:
        language_tuple = None

    max_docs = block.get("max_docs")
    if max_docs is not None:
        max_docs = int(max_docs)
        if max_docs < 1:
            raise ValueError("max_docs must be >= 1 when set")

    entity_format = block.get(
        "entity_format_examples_config",
        "configs/synthetic-data/entity_format_examples.yaml",
    )
    doc_format = block.get(
        "doc_format_examples_config",
        "configs/synthetic-data/doc_format_examples.yaml",
    )

    return PromptSettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        entities_config=resolve_repo_path(str(block["entities_config"])),
        entity_profiles_config=resolve_repo_path(str(block["entity_profiles_config"])),
        annotation_rules_config=resolve_repo_path(str(block["annotation_rules_config"])),
        entity_format_examples_config=resolve_repo_path(str(entity_format)),
        doc_format_examples_config=resolve_repo_path(str(doc_format)),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        max_docs=max_docs,
        language_codes=language_tuple,
        include_persona_narrative_in_prompt=bool(
            block.get("include_persona_narrative_in_prompt", False)
        ),
        persona_narrative_max_chars=int(block.get("persona_narrative_max_chars", 180)),
        require_all_profile_entities=bool(
            block.get("require_all_profile_entities", True)
        ),
    )


def load_entities(path: Path) -> dict[str, EntitySpec]:
    root = load_yaml(path)
    raw = root.get("entities")
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"'entities' list required in {path}")
    out: dict[str, EntitySpec] = {}
    for entry in raw:
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid entity entry: {entry!r}")
        for key in ("id", "name", "category"):
            if key not in entry:
                raise ValueError(f"Entity missing '{key}': {entry!r}")
        entity_id = str(entry["id"])
        if entity_id in out:
            raise ValueError(f"Duplicate entity id: {entity_id}")
        out[entity_id] = EntitySpec(
            id=entity_id,
            name=str(entry["name"]),
            category=str(entry["category"]),
        )
    return out


def load_profiles(path: Path, known_entities: Mapping[str, EntitySpec]) -> dict[str, EntityProfile]:
    root = load_yaml(path)
    raw = root.get("profiles")
    if not isinstance(raw, dict) or not raw:
        raise ValueError(f"'profiles' mapping required in {path}")
    profiles: dict[str, EntityProfile] = {}
    for doc_type_id, entry in raw.items():
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid profile for {doc_type_id!r}")
        required = entry.get("required")
        optional = entry.get("optional", [])
        if not isinstance(required, list) or not required:
            raise ValueError(f"Profile {doc_type_id!r} needs non-empty required list")
        if not isinstance(optional, list):
            raise ValueError(f"Profile {doc_type_id!r} optional must be a list")
        req_t = tuple(str(item) for item in required)
        opt_t = tuple(str(item) for item in optional)
        for entity_id in (*req_t, *opt_t):
            if entity_id not in known_entities:
                raise ValueError(
                    f"Profile {doc_type_id!r} references unknown entity {entity_id!r}"
                )
        overlap = set(req_t) & set(opt_t)
        if overlap:
            raise ValueError(
                f"Profile {doc_type_id!r} has entities in both required and optional: {sorted(overlap)}"
            )
        profiles[str(doc_type_id)] = EntityProfile(
            doc_type_id=str(doc_type_id),
            required=req_t,
            optional=opt_t,
        )
    return profiles


def load_annotation_rules(path: Path) -> AnnotationRules:
    root = load_yaml(path)
    inline = root.get("inline_format")
    rules = root.get("rules")
    if not isinstance(inline, dict):
        raise ValueError(f"'inline_format' mapping required in {path}")
    if "pattern" not in inline or "description" not in inline:
        raise ValueError(f"'inline_format' needs pattern and description in {path}")
    if not isinstance(rules, list) or not rules:
        raise ValueError(f"'rules' list required in {path}")
    return AnnotationRules(
        pattern=str(inline["pattern"]),
        description=str(inline["description"]).strip(),
        rules=tuple(str(item) for item in rules),
    )


def load_assignments(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(f"S2 input not found: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError as exc:
                raise PromptBuildError(f"Invalid JSONL at {path}:{line_no}") from exc
            if not isinstance(row, dict):
                raise PromptBuildError(f"Row must be object at {path}:{line_no}")
            rows.append(row)
    if not rows:
        raise PromptBuildError(f"No rows in {path}")
    return rows


def _require_fields(row: Mapping[str, Any], fields: Sequence[str], *, index: int) -> None:
    missing = [name for name in fields if name not in row]
    if missing:
        raise PromptBuildError(
            f"Assignment row {index} missing {missing} (uuid={row.get('uuid')!r})"
        )


def load_entity_format_examples(path: Path) -> tuple[dict[str, str], tuple[str, ...]]:
    root = load_yaml(path)
    examples_raw = root.get("format_examples") or {}
    if not isinstance(examples_raw, dict):
        raise ValueError(f"'format_examples' mapping required in {path}")
    examples = {str(k): str(v) for k, v in examples_raw.items()}
    latin_ok = root.get("latin_ok_entity_types") or []
    if not isinstance(latin_ok, list):
        raise ValueError(f"'latin_ok_entity_types' must be a list in {path}")
    return examples, tuple(str(item) for item in latin_ok)


def load_doc_format_examples(path: Path) -> dict[str, str]:
    root = load_yaml(path)
    examples = root.get("examples")
    if not isinstance(examples, dict) or not examples:
        raise ValueError(f"'examples' mapping required in {path}")
    return {str(k): str(v).strip() for k, v in examples.items()}


def _truncate(text: str, max_chars: int) -> str:
    text = " ".join(text.split())
    if len(text) <= max_chars:
        return text
    return text[: max_chars - 1].rstrip() + "…"


def build_system_prompt(
    rules: AnnotationRules,
    *,
    entities: Mapping[str, EntitySpec],
    format_examples: Mapping[str, str],
    latin_ok_types: Sequence[str],
) -> str:
    bullet_rules = "\n".join(f"- {rule}" for rule in rules.rules)
    allow_list = ", ".join(sorted(entities))
    example_lines = []
    for entity_id in sorted(format_examples):
        if entity_id in entities:
            example_lines.append(f"  {format_examples[entity_id]}")
    examples_block = "\n".join(example_lines)
    latin_ok = ", ".join(latin_ok_types)
    return (
        "You generate synthetic Indian clinical documents with inline surrogate "
        "PHI/PII annotations for dataset creation under DPDP-safe research use.\n\n"
        f"Inline annotation format: {rules.pattern}\n"
        f"{rules.description.strip()}\n\n"
        f"Rules:\n{bullet_rules}\n\n"
        f"ENTITY TYPE ALLOW-LIST (use ONLY these TYPE names):\n{allow_list}\n\n"
        "Format examples (copy the bracket pattern; invent new synthetic values):\n"
        f"{examples_block}\n\n"
        "Latin/digits OK inside these entity values even for Indic documents: "
        f"{latin_ok}\n"
        "Do NOT invent types like DATE, TIME, APPOINTMENT_DATE, APPOINTMENT_TIME, "
        "POLICY_NUMBER, MEDICAL_RECORD_NUMBER. Put calendar dates/times in plain prose."
    )


def build_user_prompt(
    row: Mapping[str, Any],
    *,
    profile: EntityProfile,
    entities: Mapping[str, EntitySpec],
    format_examples: Mapping[str, str],
    doc_examples: Mapping[str, str],
    settings: PromptSettings,
) -> str:
    if settings.require_all_profile_entities:
        mandatory = tuple(dict.fromkeys((*profile.required, *profile.optional)))
        optional: tuple[str, ...] = ()
    else:
        mandatory = profile.required
        optional = profile.optional

    required_lines = "\n".join(
        f"- {entity_id} — {entities[entity_id].name}"
        + (
            f" e.g. {format_examples[entity_id]}"
            if entity_id in format_examples
            else ""
        )
        for entity_id in mandatory
    )
    optional_lines = (
        "\n".join(
            f"- {entity_id} — {entities[entity_id].name}"
            + (
                f" e.g. {format_examples[entity_id]}"
                if entity_id in format_examples
                else ""
            )
            for entity_id in optional
        )
        or "- (none)"
    )

    doc_type_id = str(row["doc_type_id"])
    format_example = doc_examples.get(doc_type_id, "").strip()
    format_block = (
        f"Document format guide for {row['doc_type_name']} "
        f"(English structure; a later stage translates to the target language):\n"
        f"{format_example}\n\n"
        if format_example
        else ""
    )

    summary = str(row.get("persona_clinical_summary", "")).strip()
    if not summary:
        raise PromptBuildError(
            f"Missing persona_clinical_summary for uuid={row.get('uuid')!r}. "
            "Run stage s2b_persona_summary first."
        )

    anchors = [
        f"- sex / gender: {row['sex']}",
        f"- age: {row['age']}",
        f"- marital_status: {row['marital_status']}",
        f"- occupation: {row['occupation']}",
        f"- education_level: {row['education_level']}",
        f"- zone: {row['zone']}",
        f"- state: {row['state']}",
        f"- district: {row['district']}",
        f"- first_language: {row['first_language']}",
        f"- clinical_persona_summary: {summary}",
    ]
    if settings.include_persona_narrative_in_prompt:
        persona = _truncate(
            str(row.get("persona", "")), settings.persona_narrative_max_chars
        )
        cultural = _truncate(
            str(row.get("cultural_background", "")),
            settings.persona_narrative_max_chars,
        )
        if persona:
            anchors.append(f"- persona_summary: {persona}")
        if cultural:
            anchors.append(f"- cultural_summary: {cultural}")

    length_hint = ""
    if doc_type_id == "automated_sms":
        length_hint = (
            "LENGTH HARD LIMIT: entire SMS ≤ ~500 characters, but you MUST still "
            "include every mandatory entity tag below at least once "
            "(compact tags OK).\n\n"
        )

    placement_hint = ""
    if doc_type_id == "opd_slip":
        placement_hint = (
            "PLACEMENT (OPD header): First line MUST include BOTH "
            "[[HOSPITAL_NAME|…]] (facility name) AND [[HOSPITAL_ID|…]] "
            "(facility code) — never substitute one for the other.\n"
            "Put [[EMPLOYEE_ID|…]] on the registrar/clerk line and "
            "[[RELATIVE_NAME|…]] on the attendant/relative line. "
            "Include [[DOB|YYYY-MM-DD]] and [[OCCUPATION|…]] with demographics.\n\n"
        )
    elif doc_type_id == "telemedicine_transcript":
        placement_hint = (
            "PLACEMENT (device/network): Put IP_ADDRESS, URL, IMEI_NUMBER, and "
            "MAC_ADDRESS exactly once each in a short session/metadata header. "
            "Do NOT repeat them in chat turns. Chat turns use patient/doctor/"
            "phone/email/appointment only.\n"
            "Also put AGE and GENDER exactly once in the session header "
            "(e.g. Patient [[PATIENT_NAME|...]] [[AGE|34]] [[GENDER|Female]]). "
            "Do NOT re-tag AGE/GENDER/PHONE/EMAIL/HOSPITAL_NAME in every turn.\n\n"
        )
    elif doc_type_id == "radiology_report":
        placement_hint = (
            "PLACEMENT: Include [[DOCTOR_NAME|…]] as the reporting radiologist "
            "(e.g. Reported by Dr [[DOCTOR_NAME|…]]) — do not leave the doctor "
            "name as untagged prose.\n\n"
        )
    elif doc_type_id == "er_triage_notes":
        placement_hint = (
            "PLACEMENT (vehicle): Put VEHICLE_REGISTRATION exactly once in the "
            "arrival/RTA/ambulance line. Do not dump or repeat it.\n\n"
        )
    elif doc_type_id in {"hospital_billing", "insurance_claim"}:
        placement_hint = (
            "PLACEMENT (vehicle): Put VEHICLE_REGISTRATION exactly once "
            "(parking/ambulance or motor claim line). Do not dump or repeat it.\n\n"
        )

    target_lang = (
        f"{row['document_language_name']} "
        f"(code={row['document_language_code']}, script={row['document_script']})"
    )

    mandatory_count = len(mandatory)
    return (
        f"Write one complete {row['doc_type_name']} for clinical domain "
        f"{row['domain_name']}.\n\n"
        "GENERATION LANGUAGE: English (Latin script) — this is an English pivot "
        "draft. A later pipeline stage will translate clinical prose into "
        f"{target_lang}. Keep [[TYPE|value]] tags intact and valid.\n"
        "ID-like tagged values stay Latin/digits. Drug names / labs stay untagged.\n"
        f"DOMAIN ANCHOR: chief complaint, findings, and plan MUST match "
        f"{row['domain_name']} — do not default to unrelated TB/generic content "
        "unless that is the assigned domain.\n\n"
        f"{length_hint}"
        f"{placement_hint}"
        "Persona anchors (must remain consistent; patient = this persona):\n"
        + "\n".join(anchors)
        + "\n\n"
        f"{format_block}"
        f"MANDATORY inline entities ({mandatory_count} types) — EACH must appear "
        "≥ once as [[TYPE|surrogate_value]]. Missing ANY is a hard failure:\n"
        f"{required_lines}\n\n"
        + (
            "Optional entities (include when natural):\n"
            f"{optional_lines}\n\n"
            if optional
            else ""
        )
        + "Before finishing, mentally checklist every mandatory TYPE above.\n"
        "Do NOT invent TYPE names (no DATE, TIME, APPOINTMENT_DATE, "
        "APPOINTMENT_TIME, POLICY_NUMBER, TOTAL_AMOUNT, GST_AMOUNT, GRAND_TOTAL). "
        "Put dates/times and money amounts in plain prose.\n"
        "Produce ONLY the clinical document text with inline annotations. "
        "No markdown fences, no preamble, no postscript."
    )


def build_prompts(
    rows: Sequence[Mapping[str, Any]],
    *,
    entities: Mapping[str, EntitySpec],
    profiles: Mapping[str, EntityProfile],
    rules: AnnotationRules,
    format_examples: Mapping[str, str],
    latin_ok_types: Sequence[str],
    doc_examples: Mapping[str, str],
    settings: PromptSettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    system_prompt = build_system_prompt(
        rules,
        entities=entities,
        format_examples=format_examples,
        latin_ok_types=latin_ok_types,
    )
    selected: list[dict[str, Any]] = []

    for index, row in enumerate(rows):
        _require_fields(
            row,
            (
                "uuid",
                "doc_type_id",
                "doc_type_name",
                "domain_id",
                "domain_name",
                "document_language_code",
                "document_language_name",
                "document_script",
                "sex",
                "age",
                "state",
                "district",
                "zone",
                "occupation",
                "marital_status",
                "education_level",
                "first_language",
                "persona_clinical_summary",
            ),
            index=index,
        )
        lang = str(row["document_language_code"])
        if settings.language_codes is not None and lang not in settings.language_codes:
            continue

        doc_type_id = str(row["doc_type_id"])
        if doc_type_id not in profiles:
            raise PromptBuildError(
                f"No entity profile for doc_type_id={doc_type_id!r} "
                "(every doc type must be configured; no default profile)"
            )
        profile = profiles[doc_type_id]
        if settings.require_all_profile_entities:
            mandatory = list(dict.fromkeys((*profile.required, *profile.optional)))
            optional_out: list[str] = []
        else:
            mandatory = list(profile.required)
            optional_out = list(profile.optional)
        out = dict(row)
        out.update(
            {
                "system_prompt": system_prompt,
                "user_prompt": build_user_prompt(
                    row,
                    profile=profile,
                    entities=entities,
                    format_examples=format_examples,
                    doc_examples=doc_examples,
                    settings=settings,
                ),
                "required_entities": mandatory,
                "optional_entities": optional_out,
                "stage": "s3_prompt_construction",
            }
        )
        selected.append(out)
        if settings.max_docs is not None and len(selected) >= settings.max_docs:
            break

    if not selected:
        raise PromptBuildError(
            "No prompt rows produced. Check language_codes / max_docs filters "
            f"against input {settings.input_jsonl}"
        )

    audit = {
        "stage": "s3_prompt_construction",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_jsonl": str(settings.input_jsonl),
        "rows_in": len(rows),
        "rows_out": len(selected),
        "max_docs": settings.max_docs,
        "language_codes": list(settings.language_codes) if settings.language_codes else None,
        "include_persona_narrative_in_prompt": settings.include_persona_narrative_in_prompt,
        "doc_type_counts": _count(selected, "doc_type_id"),
        "language_counts": _count(selected, "document_language_code"),
        "mean_user_prompt_chars": (
            sum(len(str(row["user_prompt"])) for row in selected) / len(selected)
        ),
        "mean_system_prompt_chars": len(system_prompt),
        "columns_added": list(PROMPT_COLUMNS),
    }
    return selected, audit


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
    jsonl_path = output_dir / "prompts.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    columns = list(rows[0].keys())
    table = {name: [row[name] for row in rows] for name in columns}
    parquet_path = output_dir / "prompts.parquet"
    pq.write_table(pa.table(table), parquet_path)

    audit_json = output_dir / "audit.json"
    audit_json.write_text(json.dumps(dict(audit), indent=2, ensure_ascii=False) + "\n")
    audit_md = output_dir / "audit.md"
    audit_md.write_text(
        "# Stage 3 — Prompt Construction Audit\n\n"
        f"- rows_in: **{audit['rows_in']}**\n"
        f"- rows_out: **{audit['rows_out']}**\n"
        f"- max_docs: `{audit['max_docs']}`\n"
        f"- languages: `{audit['language_counts']}`\n"
        f"- doc_types: `{audit['doc_type_counts']}`\n",
        encoding="utf-8",
    )

    preview = REPO_ROOT / "data" / "samples" / "s3_prompts_preview.jsonl"
    preview.parent.mkdir(parents=True, exist_ok=True)
    with preview.open("w", encoding="utf-8") as handle:
        for row in list(rows)[: min(3, len(rows))]:
            slim = {
                "uuid": row["uuid"],
                "doc_type_id": row["doc_type_id"],
                "domain_id": row["domain_id"],
                "document_language_code": row["document_language_code"],
                "required_entities": row["required_entities"],
                "user_prompt_preview": row["user_prompt"][:500],
            }
            handle.write(json.dumps(slim, ensure_ascii=False) + "\n")

    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json,
        "audit_md": audit_md,
        "preview_jsonl": preview,
    }


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    entities = load_entities(settings.entities_config)
    profiles = load_profiles(settings.entity_profiles_config, entities)
    rules = load_annotation_rules(settings.annotation_rules_config)
    format_examples, latin_ok = load_entity_format_examples(
        settings.entity_format_examples_config
    )
    doc_examples = load_doc_format_examples(settings.doc_format_examples_config)
    rows = load_assignments(settings.input_jsonl)
    prompts, audit = build_prompts(
        rows,
        entities=entities,
        profiles=profiles,
        rules=rules,
        format_examples=format_examples,
        latin_ok_types=latin_ok,
        doc_examples=doc_examples,
        settings=settings,
    )
    return write_outputs(prompts, audit, settings.output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Stage 3: build generation prompts")
    parser.add_argument("--config", type=Path, default=DEFAULT_PIPELINE_CONFIG)
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (PromptBuildError, ValueError, FileNotFoundError) as exc:
        print(f"[s3] FAILED: {exc}", file=sys.stderr)
        return 1
    print("[s3] Prompt construction complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
