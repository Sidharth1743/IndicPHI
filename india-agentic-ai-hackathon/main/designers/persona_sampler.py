"""Stage 1 — Persona sampling from nvidia/Nemotron-Personas-India.

Samples personas stratified by the 23 document languages (22 Indic + English).
Each persona carries ``docs_per_persona`` for later document expansion (S2–S4).

Design rules for this stage:
- Keep every source column; only *add* pipeline provenance fields.
- Match ``first_language`` via exact configured aliases only (no fuzzy match,
  no geographic fallback, no reassignment to fill quotas).
- Fail hard if any language quota is under-filled after ``max_scan_rows``.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq
from huggingface_hub import HfApi, hf_hub_download

from main.pipeline.config_io import REPO_ROOT, load_yaml

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

SOURCE_COLUMNS: tuple[str, ...] = (
    "uuid",
    "professional_persona",
    "linguistic_persona",
    "sports_persona",
    "arts_persona",
    "travel_persona",
    "culinary_persona",
    "persona",
    "cultural_background",
    "linguistic_background",
    "skills_and_expertise",
    "skills_and_expertise_list",
    "hobbies_and_interests",
    "hobbies_and_interests_list",
    "career_goals_and_ambitions",
    "sex",
    "age",
    "marital_status",
    "education_level",
    "education_degree",
    "occupation",
    "first_language",
    "second_language",
    "third_language",
    "zone",
    "state",
    "district",
    "country",
)

PIPELINE_COLUMNS: tuple[str, ...] = (
    "document_language_code",
    "document_language_name",
    "document_script",
    "docs_per_persona",
    "persona_source_dataset",
    "persona_source_split",
    "persona_source_shard",
    "sample_seed",
    "stage",
)


@dataclass(frozen=True)
class LanguageSpec:
    code: str
    name: str
    script: str
    aliases: tuple[str, ...]


@dataclass(frozen=True)
class PersonaSamplingSettings:
    dataset_id: str
    split: str
    seed: int
    personas_per_language: int
    docs_per_persona: int
    max_scan_rows: int
    language_codes: tuple[str, ...] | None
    languages_config: Path
    output_dir: Path
    local_shard_path: Path | None


class PersonaSamplingError(RuntimeError):
    """Raised when Stage 1 cannot meet configured quotas without fallbacks."""


def load_settings(pipeline_config: Path) -> PersonaSamplingSettings:
    root = load_yaml(pipeline_config)
    block = root.get("persona_sampling")
    if not isinstance(block, dict):
        raise ValueError(f"'persona_sampling' mapping required in {pipeline_config}")

    required = (
        "dataset_id",
        "split",
        "seed",
        "personas_per_language",
        "docs_per_persona",
        "max_scan_rows",
        "languages_config",
        "output_dir",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing persona_sampling keys {missing} in {pipeline_config}")

    language_codes = block.get("language_codes")
    if language_codes is not None:
        if not isinstance(language_codes, list) or not all(
            isinstance(code, str) for code in language_codes
        ):
            raise ValueError("'language_codes' must be null or a list of strings")
        language_codes_tuple: tuple[str, ...] | None = tuple(language_codes)
    else:
        language_codes_tuple = None

    local_raw = block.get("local_shard_path")
    local_shard_path = None
    if local_raw is not None:
        local_shard_path = (REPO_ROOT / str(local_raw)).resolve()

    return PersonaSamplingSettings(
        dataset_id=str(block["dataset_id"]),
        split=str(block["split"]),
        seed=int(block["seed"]),
        personas_per_language=int(block["personas_per_language"]),
        docs_per_persona=int(block["docs_per_persona"]),
        max_scan_rows=int(block["max_scan_rows"]),
        language_codes=language_codes_tuple,
        languages_config=(REPO_ROOT / str(block["languages_config"])).resolve(),
        output_dir=(REPO_ROOT / str(block["output_dir"])).resolve(),
        local_shard_path=local_shard_path,
    )


def load_languages(
    languages_config: Path,
    language_codes: Sequence[str] | None,
) -> list[LanguageSpec]:
    root = load_yaml(languages_config)
    raw_languages = root.get("languages")
    if not isinstance(raw_languages, list) or not raw_languages:
        raise ValueError(f"'languages' list required in {languages_config}")

    specs: list[LanguageSpec] = []
    seen_codes: set[str] = set()
    alias_owner: dict[str, str] = {}

    for entry in raw_languages:
        if not isinstance(entry, dict):
            raise ValueError(f"Invalid language entry in {languages_config}: {entry!r}")
        for key in ("code", "name", "script", "hf_first_language_aliases"):
            if key not in entry:
                raise ValueError(f"Language entry missing '{key}': {entry!r}")
        code = str(entry["code"])
        if code in seen_codes:
            raise ValueError(f"Duplicate language code: {code}")
        aliases_raw = entry["hf_first_language_aliases"]
        if not isinstance(aliases_raw, list) or not aliases_raw:
            raise ValueError(f"Language '{code}' needs non-empty hf_first_language_aliases")
        aliases = tuple(str(alias) for alias in aliases_raw)
        for alias in aliases:
            if alias in alias_owner:
                raise ValueError(
                    f"Alias {alias!r} claimed by both '{alias_owner[alias]}' and '{code}'"
                )
            alias_owner[alias] = code
        seen_codes.add(code)
        specs.append(
            LanguageSpec(
                code=code,
                name=str(entry["name"]),
                script=str(entry["script"]),
                aliases=aliases,
            )
        )

    if language_codes is None:
        return specs

    wanted = list(language_codes)
    by_code = {spec.code: spec for spec in specs}
    missing = [code for code in wanted if code not in by_code]
    if missing:
        raise ValueError(
            f"language_codes not present in {languages_config}: {missing}"
        )
    return [by_code[code] for code in wanted]


def build_alias_index(languages: Sequence[LanguageSpec]) -> dict[str, LanguageSpec]:
    index: dict[str, LanguageSpec] = {}
    for spec in languages:
        for alias in spec.aliases:
            index[alias] = spec
    return index


def list_split_shards(dataset_id: str, split: str) -> list[str]:
    api = HfApi()
    files = api.list_repo_files(dataset_id, repo_type="dataset")
    prefix = f"data/{split}-"
    shards = sorted(name for name in files if name.startswith(prefix) and name.endswith(".parquet"))
    if not shards:
        raise PersonaSamplingError(
            f"No parquet shards found for dataset={dataset_id!r} split={split!r}"
        )
    return shards


def iter_source_rows(
    settings: PersonaSamplingSettings,
) -> Iterator[tuple[str, dict[str, Any]]]:
    """Yield (shard_name, row_dict) without dropping source fields."""
    if settings.local_shard_path is not None:
        path = settings.local_shard_path
        if not path.is_file():
            raise FileNotFoundError(f"local_shard_path not found: {path}")
        table = pq.read_table(path)
        _validate_source_columns(table.column_names, source=str(path))
        for batch in table.to_batches(max_chunksize=1024):
            rows = batch.to_pydict()
            n = len(next(iter(rows.values())))
            for i in range(n):
                yield path.name, {column: rows[column][i] for column in rows}
        return

    shards = list_split_shards(settings.dataset_id, settings.split)
    for shard_name in shards:
        local_path = hf_hub_download(
            repo_id=settings.dataset_id,
            repo_type="dataset",
            filename=shard_name,
        )
        table = pq.read_table(local_path)
        _validate_source_columns(table.column_names, source=shard_name)
        for batch in table.to_batches(max_chunksize=1024):
            rows = batch.to_pydict()
            n = len(next(iter(rows.values())))
            for i in range(n):
                yield shard_name, {column: rows[column][i] for column in rows}


def _validate_source_columns(columns: Sequence[str], *, source: str) -> None:
    present = set(columns)
    missing = [name for name in SOURCE_COLUMNS if name not in present]
    if missing:
        raise PersonaSamplingError(
            f"Source schema missing columns {missing} in {source}. "
            f"Present={sorted(present)}"
        )


def sample_personas(
    settings: PersonaSamplingSettings,
    languages: Sequence[LanguageSpec],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    if settings.personas_per_language < 1:
        raise ValueError("personas_per_language must be >= 1")
    if settings.docs_per_persona < 1:
        raise ValueError("docs_per_persona must be >= 1")
    if settings.max_scan_rows < 1:
        raise ValueError("max_scan_rows must be >= 1")

    alias_index = build_alias_index(languages)
    quotas = {spec.code: settings.personas_per_language for spec in languages}
    buckets: dict[str, list[dict[str, Any]]] = {spec.code: [] for spec in languages}

    observed_first_language: Counter[str] = Counter()
    matched_counts: Counter[str] = Counter()
    scanned = 0

    # Deterministic selection: fixed shard order, first N exact alias matches per language.
    # ``seed`` is recorded on every row for provenance / later stratified stages.
    for shard_name, source_row in iter_source_rows(settings):
        if scanned >= settings.max_scan_rows:
            break
        scanned += 1

        first_language = source_row["first_language"]
        if not isinstance(first_language, str):
            raise PersonaSamplingError(
                f"first_language must be str, got {type(first_language).__name__} "
                f"at scan_index={scanned} shard={shard_name}"
            )
        observed_first_language[first_language] += 1

        spec = alias_index.get(first_language)
        if spec is None:
            continue
        if len(buckets[spec.code]) >= quotas[spec.code]:
            continue

        row = dict(source_row)
        row.update(
            {
                "document_language_code": spec.code,
                "document_language_name": spec.name,
                "document_script": spec.script,
                "docs_per_persona": settings.docs_per_persona,
                "persona_source_dataset": settings.dataset_id,
                "persona_source_split": settings.split,
                "persona_source_shard": shard_name,
                "sample_seed": settings.seed,
                "stage": "s1_persona_sampling",
            }
        )
        buckets[spec.code].append(row)
        matched_counts[spec.code] += 1

        if all(len(buckets[code]) >= quotas[code] for code in quotas):
            break

    underfilled = {
        code: {"have": len(buckets[code]), "need": quotas[code]}
        for code in quotas
        if len(buckets[code]) < quotas[code]
    }
    if underfilled:
        raise PersonaSamplingError(
            "Language quotas under-filled with exact first_language alias matching "
            f"(no fallback). underfilled={underfilled} scanned={scanned} "
            f"max_scan_rows={settings.max_scan_rows} "
            f"observed_first_language_top={observed_first_language.most_common(30)}"
        )

    selected: list[dict[str, Any]] = []
    for spec in languages:
        selected.extend(buckets[spec.code][: quotas[spec.code]])
    selected.sort(key=lambda item: (item["document_language_code"], item["uuid"]))

    audit = {
        "stage": "s1_persona_sampling",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "dataset_id": settings.dataset_id,
        "split": settings.split,
        "seed": settings.seed,
        "personas_per_language": settings.personas_per_language,
        "docs_per_persona": settings.docs_per_persona,
        "languages_requested": [spec.code for spec in languages],
        "rows_scanned": scanned,
        "max_scan_rows": settings.max_scan_rows,
        "personas_selected": len(selected),
        "expected_documents_downstream": len(selected) * settings.docs_per_persona,
        "by_language": {
            spec.code: {
                "name": spec.name,
                "script": spec.script,
                "aliases": list(spec.aliases),
                "selected": sum(
                    1 for row in selected if row["document_language_code"] == spec.code
                ),
                "matched_during_scan": matched_counts[spec.code],
            }
            for spec in languages
        },
        "observed_first_language": dict(observed_first_language.most_common()),
        "demographics": _demographic_audit(selected),
        "source_columns_preserved": list(SOURCE_COLUMNS),
        "pipeline_columns_added": list(PIPELINE_COLUMNS),
    }
    return selected, audit


def _demographic_audit(rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    sex = Counter(str(row["sex"]) for row in rows)
    zone = Counter(str(row["zone"]) for row in rows)
    state = Counter(str(row["state"]) for row in rows)
    ages = [int(row["age"]) for row in rows]
    return {
        "sex": dict(sex),
        "zone": dict(zone),
        "state_top20": dict(state.most_common(20)),
        "age_min": min(ages) if ages else None,
        "age_max": max(ages) if ages else None,
        "age_mean": (sum(ages) / len(ages)) if ages else None,
    }


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = output_dir / "personas.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    column_order = list(SOURCE_COLUMNS) + list(PIPELINE_COLUMNS)
    table_dict: dict[str, list[Any]] = {name: [] for name in column_order}
    for row in rows:
        for name in column_order:
            table_dict[name].append(row[name])
    parquet_path = output_dir / "personas.parquet"
    pq.write_table(pa.table(table_dict), parquet_path)

    audit_json_path = output_dir / "audit.json"
    audit_json_path.write_text(
        json.dumps(dict(audit), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    audit_md_path = output_dir / "audit.md"
    audit_md_path.write_text(_render_audit_markdown(audit), encoding="utf-8")

    preview_dir = REPO_ROOT / "data" / "samples"
    preview_dir.mkdir(parents=True, exist_ok=True)
    preview_path = preview_dir / "s1_personas_preview.jsonl"
    with preview_path.open("w", encoding="utf-8") as handle:
        for row in list(rows)[: min(5, len(rows))]:
            handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    return {
        "jsonl": jsonl_path,
        "parquet": parquet_path,
        "audit_json": audit_json_path,
        "audit_md": audit_md_path,
        "preview_jsonl": preview_path,
    }


def _render_audit_markdown(audit: Mapping[str, Any]) -> str:
    lines = [
        "# Stage 1 — Persona Sampling Audit",
        "",
        f"- timestamp_utc: `{audit['timestamp_utc']}`",
        f"- dataset: `{audit['dataset_id']}` split=`{audit['split']}`",
        f"- seed: `{audit['seed']}`",
        f"- rows_scanned: **{audit['rows_scanned']}** / max `{audit['max_scan_rows']}`",
        f"- personas_selected: **{audit['personas_selected']}**",
        f"- docs_per_persona: `{audit['docs_per_persona']}`",
        f"- expected_documents_downstream: **{audit['expected_documents_downstream']}**",
        "",
        "## By language",
        "",
        "| code | name | script | selected | matched_during_scan |",
        "|------|------|--------|----------|---------------------|",
    ]
    by_language = audit["by_language"]
    assert isinstance(by_language, dict)
    for code, info in by_language.items():
        lines.append(
            f"| {code} | {info['name']} | {info['script']} | "
            f"{info['selected']} | {info['matched_during_scan']} |"
        )

    demographics = audit["demographics"]
    lines.extend(
        [
            "",
            "## Demographics (selected)",
            "",
            f"- sex: `{demographics['sex']}`",
            f"- zone: `{demographics['zone']}`",
            f"- age: min=`{demographics['age_min']}` max=`{demographics['age_max']}` "
            f"mean=`{demographics['age_mean']}`",
            f"- state_top20: `{demographics['state_top20']}`",
            "",
            "## Observed first_language in scan (all values)",
            "",
        ]
    )
    observed = audit["observed_first_language"]
    assert isinstance(observed, dict)
    for name, count in observed.items():
        lines.append(f"- {name}: {count}")
    lines.append("")
    return "\n".join(lines)


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    languages = load_languages(settings.languages_config, settings.language_codes)
    rows, audit = sample_personas(settings, languages)
    paths = write_outputs(rows, audit, settings.output_dir)
    return paths


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Stage 1: sample Nemotron-Personas-India stratified by language",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_PIPELINE_CONFIG,
        help="Path to configs/synthetic-data/pipeline.yaml",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)
    config_path = args.config if args.config.is_absolute() else (REPO_ROOT / args.config)
    try:
        paths = run(config_path.resolve())
    except (PersonaSamplingError, ValueError, FileNotFoundError) as exc:
        print(f"[s1] FAILED: {exc}", file=sys.stderr)
        return 1

    print("[s1] Persona sampling complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
