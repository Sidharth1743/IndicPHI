"""Stage 2 — Document taxonomy assignment (14 doc types × 7 domains).

Reads S1 persona rows and expands each persona into ``docs_per_persona``
document slots. Assignment is stratified **per language** over the full
14×7 cell grid:

- Always pick the least-filled ``(doc_type, domain)`` cell for that language.
- Ties break deterministically (fixed cell order).
- Optionally prefer unused cells / doc types / domains *within* one persona
  so a single persona's 3 docs are not clones of the same cell.

Design rules:
- Keep every S1 column; only *add* taxonomy / slot fields.
- Doc type and domain IDs must come from config (no invented labels).
- No silent under-fill of required inputs; fail hard on bad S1 rows.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import pyarrow as pa
import pyarrow.parquet as pq

from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path

DEFAULT_PIPELINE_CONFIG = REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"

TAXONOMY_COLUMNS: tuple[str, ...] = (
    "doc_slot",
    "doc_type_id",
    "doc_type_name",
    "domain_id",
    "domain_name",
    "taxonomy_cell_id",
    "assignment_seed",
    "stage",
)


@dataclass(frozen=True)
class DocTypeSpec:
    id: str
    name: str


@dataclass(frozen=True)
class DomainSpec:
    id: str
    name: str
    require_sex: tuple[str, ...] = ()
    min_age: int | None = None
    max_age: int | None = None


@dataclass(frozen=True)
class TaxonomyCell:
    doc_type: DocTypeSpec
    domain: DomainSpec
    index: int

    @property
    def cell_id(self) -> str:
        return f"{self.doc_type.id}__{self.domain.id}"

    @property
    def key(self) -> tuple[str, str]:
        return (self.doc_type.id, self.domain.id)


@dataclass(frozen=True)
class TaxonomySettings:
    input_jsonl: Path
    doc_types_config: Path
    domains_config: Path
    output_dir: Path
    seed: int
    prefer_unique_cell_per_persona: bool
    prefer_unique_doc_type_per_persona: bool
    prefer_unique_domain_per_persona: bool


class TaxonomyError(RuntimeError):
    """Raised when Stage 2 cannot assign taxonomy without violating rules."""


def load_settings(pipeline_config: Path) -> TaxonomySettings:
    root = load_yaml(pipeline_config)
    block = root.get("taxonomy")
    if not isinstance(block, dict):
        raise ValueError(f"'taxonomy' mapping required in {pipeline_config}")

    required = (
        "input_jsonl",
        "doc_types_config",
        "domains_config",
        "output_dir",
        "seed",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise ValueError(f"Missing taxonomy keys {missing} in {pipeline_config}")

    return TaxonomySettings(
        input_jsonl=resolve_repo_path(str(block["input_jsonl"])),
        doc_types_config=resolve_repo_path(str(block["doc_types_config"])),
        domains_config=resolve_repo_path(str(block["domains_config"])),
        output_dir=resolve_repo_path(str(block["output_dir"])),
        seed=int(block["seed"]),
        prefer_unique_cell_per_persona=bool(
            block.get("prefer_unique_cell_per_persona", True)
        ),
        prefer_unique_doc_type_per_persona=bool(
            block.get("prefer_unique_doc_type_per_persona", True)
        ),
        prefer_unique_domain_per_persona=bool(
            block.get("prefer_unique_domain_per_persona", True)
        ),
    )


def load_doc_types(path: Path) -> list[DocTypeSpec]:
    root = load_yaml(path)
    raw = root.get("doc_types")
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"'doc_types' list required in {path}")
    specs: list[DocTypeSpec] = []
    seen: set[str] = set()
    for entry in raw:
        if not isinstance(entry, dict) or "id" not in entry or "name" not in entry:
            raise ValueError(f"Invalid doc_type entry in {path}: {entry!r}")
        doc_id = str(entry["id"])
        if doc_id in seen:
            raise ValueError(f"Duplicate doc_type id: {doc_id}")
        seen.add(doc_id)
        specs.append(DocTypeSpec(id=doc_id, name=str(entry["name"])))
    return specs


def load_domains(path: Path) -> list[DomainSpec]:
    root = load_yaml(path)
    raw = root.get("domains")
    if not isinstance(raw, list) or not raw:
        raise ValueError(f"'domains' list required in {path}")
    specs: list[DomainSpec] = []
    seen: set[str] = set()
    for entry in raw:
        if not isinstance(entry, dict) or "id" not in entry or "name" not in entry:
            raise ValueError(f"Invalid domain entry in {path}: {entry!r}")
        domain_id = str(entry["id"])
        if domain_id in seen:
            raise ValueError(f"Duplicate domain id: {domain_id}")
        seen.add(domain_id)
        require_sex_raw = entry.get("require_sex") or []
        if not isinstance(require_sex_raw, list):
            raise ValueError(f"domain {domain_id}: require_sex must be a list")
        min_age = entry.get("min_age")
        max_age = entry.get("max_age")
        if min_age is not None:
            min_age = int(min_age)
        if max_age is not None:
            max_age = int(max_age)
        specs.append(
            DomainSpec(
                id=domain_id,
                name=str(entry["name"]),
                require_sex=tuple(str(item) for item in require_sex_raw),
                min_age=min_age,
                max_age=max_age,
            )
        )
    return specs


def persona_matches_domain(persona: Mapping[str, Any], domain: DomainSpec) -> bool:
    """Return False when persona cannot be the patient for this clinical domain."""
    sex = str(persona.get("sex", "")).strip()
    try:
        age = int(persona["age"])
    except (KeyError, TypeError, ValueError) as exc:
        raise TaxonomyError(
            f"Persona {persona.get('uuid')!r} needs integer age for domain gates"
        ) from exc

    if domain.require_sex and sex not in domain.require_sex:
        return False
    if domain.min_age is not None and age < domain.min_age:
        return False
    if domain.max_age is not None and age > domain.max_age:
        return False
    return True


def eligible_cells_for_persona(
    persona: Mapping[str, Any],
    cells: Sequence[TaxonomyCell],
) -> list[TaxonomyCell]:
    eligible = [
        cell for cell in cells if persona_matches_domain(persona, cell.domain)
    ]
    if not eligible:
        raise TaxonomyError(
            f"No eligible taxonomy cells for persona uuid={persona.get('uuid')!r} "
            f"sex={persona.get('sex')!r} age={persona.get('age')!r}. "
            "Relax domain gates or resample personas."
        )
    return eligible


def build_cells(
    doc_types: Sequence[DocTypeSpec],
    domains: Sequence[DomainSpec],
) -> list[TaxonomyCell]:
    cells: list[TaxonomyCell] = []
    index = 0
    for doc_type in doc_types:
        for domain in domains:
            cells.append(TaxonomyCell(doc_type=doc_type, domain=domain, index=index))
            index += 1
    if not cells:
        raise TaxonomyError("Taxonomy grid is empty")
    return cells


def load_personas(path: Path) -> list[dict[str, Any]]:
    if not path.is_file():
        raise FileNotFoundError(f"S1 input not found: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, start=1):
            text = line.strip()
            if not text:
                continue
            try:
                row = json.loads(text)
            except json.JSONDecodeError as exc:
                raise TaxonomyError(
                    f"Invalid JSONL at {path}:{line_no}: {exc}"
                ) from exc
            if not isinstance(row, dict):
                raise TaxonomyError(f"JSONL row must be an object at {path}:{line_no}")
            rows.append(row)
    if not rows:
        raise TaxonomyError(f"No persona rows in {path}")
    return rows


def _validate_persona(row: Mapping[str, Any], *, index: int) -> None:
    required = ("uuid", "document_language_code", "docs_per_persona", "sex", "age")
    missing = [key for key in required if key not in row]
    if missing:
        raise TaxonomyError(
            f"Persona row {index} missing required fields {missing} (uuid={row.get('uuid')!r})"
        )
    docs = row["docs_per_persona"]
    if not isinstance(docs, int) or docs < 1:
        raise TaxonomyError(
            f"Persona {row['uuid']!r}: docs_per_persona must be int >= 1, got {docs!r}"
        )
    lang = row["document_language_code"]
    if not isinstance(lang, str) or not lang:
        raise TaxonomyError(
            f"Persona {row['uuid']!r}: document_language_code must be non-empty str"
        )
    try:
        int(row["age"])
    except (TypeError, ValueError) as exc:
        raise TaxonomyError(
            f"Persona {row['uuid']!r}: age must be int-compatible, got {row['age']!r}"
        ) from exc


def _language_offset(language_code: str, seed: int, n_cells: int) -> int:
    """Stable per-language rotation so languages explore different cells first."""
    digest = hashlib.blake2b(
        f"{seed}:{language_code}".encode("utf-8"),
        digest_size=8,
    ).digest()
    return int.from_bytes(digest, "big") % n_cells


def _pick_cell(
    *,
    cells: Sequence[TaxonomyCell],
    lang_counts: Counter[tuple[str, str]],
    used_cells: set[tuple[str, str]],
    used_doc_types: set[str],
    used_domains: set[str],
    settings: TaxonomySettings,
    language_offset: int,
) -> TaxonomyCell:
    n_cells = len(cells)

    def score(cell: TaxonomyCell) -> tuple[int, int, int, int, int]:
        key = cell.key
        rotated = (cell.index - language_offset) % n_cells
        return (
            lang_counts[key],
            int(
                settings.prefer_unique_cell_per_persona and key in used_cells
            ),
            int(
                settings.prefer_unique_doc_type_per_persona
                and cell.doc_type.id in used_doc_types
            ),
            int(
                settings.prefer_unique_domain_per_persona
                and cell.domain.id in used_domains
            ),
            rotated,
        )

    return min(cells, key=score)


def assign_taxonomy(
    personas: Sequence[Mapping[str, Any]],
    cells: Sequence[TaxonomyCell],
    settings: TaxonomySettings,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    for index, persona in enumerate(personas):
        _validate_persona(persona, index=index)

    ordered = sorted(
        personas,
        key=lambda row: (str(row["document_language_code"]), str(row["uuid"])),
    )

    lang_counts: dict[str, Counter[tuple[str, str]]] = defaultdict(Counter)
    assigned: list[dict[str, Any]] = []

    for persona in ordered:
        lang = str(persona["document_language_code"])
        docs_per_persona = int(persona["docs_per_persona"])
        used_cells: set[tuple[str, str]] = set()
        used_doc_types: set[str] = set()
        used_domains: set[str] = set()
        language_offset = _language_offset(lang, settings.seed, len(cells))

        for doc_slot in range(docs_per_persona):
            eligible = eligible_cells_for_persona(persona, cells)
            cell = _pick_cell(
                cells=eligible,
                lang_counts=lang_counts[lang],
                used_cells=used_cells,
                used_doc_types=used_doc_types,
                used_domains=used_domains,
                settings=settings,
                language_offset=language_offset,
            )
            lang_counts[lang][cell.key] += 1
            used_cells.add(cell.key)
            used_doc_types.add(cell.doc_type.id)
            used_domains.add(cell.domain.id)

            row = dict(persona)
            row.update(
                {
                    "doc_slot": doc_slot,
                    "doc_type_id": cell.doc_type.id,
                    "doc_type_name": cell.doc_type.name,
                    "domain_id": cell.domain.id,
                    "domain_name": cell.domain.name,
                    "taxonomy_cell_id": cell.cell_id,
                    "assignment_seed": settings.seed,
                    "stage": "s2_taxonomy",
                }
            )
            assigned.append(row)

    audit = _build_audit(
        personas=ordered,
        assigned=assigned,
        cells=cells,
        lang_counts=lang_counts,
        settings=settings,
    )
    return assigned, audit


def _build_audit(
    *,
    personas: Sequence[Mapping[str, Any]],
    assigned: Sequence[Mapping[str, Any]],
    cells: Sequence[TaxonomyCell],
    lang_counts: Mapping[str, Counter[tuple[str, str]]],
    settings: TaxonomySettings,
) -> dict[str, Any]:
    by_language: dict[str, Any] = {}
    for lang, counter in sorted(lang_counts.items()):
        fills = [counter[cell.key] for cell in cells]
        by_language[lang] = {
            "docs": sum(fills),
            "cells_touched": sum(1 for value in fills if value > 0),
            "cells_total": len(cells),
            "min_cell_fill": min(fills) if fills else 0,
            "max_cell_fill": max(fills) if fills else 0,
            "doc_type_counts": dict(
                Counter(row["doc_type_id"] for row in assigned if row["document_language_code"] == lang)
            ),
            "domain_counts": dict(
                Counter(row["domain_id"] for row in assigned if row["document_language_code"] == lang)
            ),
            "cell_counts": {
                cell.cell_id: counter[cell.key] for cell in cells if counter[cell.key] > 0
            },
        }

    persona_cell_sets = Counter()
    for persona in personas:
        uuid = persona["uuid"]
        slots = [row for row in assigned if row["uuid"] == uuid]
        unique_cells = len({row["taxonomy_cell_id"] for row in slots})
        persona_cell_sets[unique_cells] += 1

    return {
        "stage": "s2_taxonomy",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "input_jsonl": str(settings.input_jsonl),
        "seed": settings.seed,
        "personas_in": len(personas),
        "documents_out": len(assigned),
        "doc_types": len({cell.doc_type.id for cell in cells}),
        "domains": len({cell.domain.id for cell in cells}),
        "taxonomy_cells": len(cells),
        "prefer_unique_cell_per_persona": settings.prefer_unique_cell_per_persona,
        "prefer_unique_doc_type_per_persona": settings.prefer_unique_doc_type_per_persona,
        "prefer_unique_domain_per_persona": settings.prefer_unique_domain_per_persona,
        "by_language": by_language,
        "global_doc_type_counts": dict(Counter(row["doc_type_id"] for row in assigned)),
        "global_domain_counts": dict(Counter(row["domain_id"] for row in assigned)),
        "persona_unique_cells_histogram": dict(sorted(persona_cell_sets.items())),
        "columns_added": list(TAXONOMY_COLUMNS),
    }


def write_outputs(
    rows: Sequence[Mapping[str, Any]],
    audit: Mapping[str, Any],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = output_dir / "assignments.jsonl"
    with jsonl_path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(dict(row), ensure_ascii=False) + "\n")

    if rows:
        columns = list(rows[0].keys())
        table_dict: dict[str, list[Any]] = {name: [] for name in columns}
        for row in rows:
            for name in columns:
                table_dict[name].append(row[name])
        parquet_path = output_dir / "assignments.parquet"
        pq.write_table(pa.table(table_dict), parquet_path)
    else:
        parquet_path = output_dir / "assignments.parquet"
        pq.write_table(pa.table({}), parquet_path)

    audit_json_path = output_dir / "audit.json"
    audit_json_path.write_text(
        json.dumps(dict(audit), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    audit_md_path = output_dir / "audit.md"
    audit_md_path.write_text(_render_audit_markdown(audit), encoding="utf-8")

    preview_dir = REPO_ROOT / "data" / "samples"
    preview_dir.mkdir(parents=True, exist_ok=True)
    preview_path = preview_dir / "s2_taxonomy_preview.jsonl"
    with preview_path.open("w", encoding="utf-8") as handle:
        for row in list(rows)[: min(6, len(rows))]:
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
        "# Stage 2 — Taxonomy Assignment Audit",
        "",
        f"- timestamp_utc: `{audit['timestamp_utc']}`",
        f"- input: `{audit['input_jsonl']}`",
        f"- personas_in: **{audit['personas_in']}**",
        f"- documents_out: **{audit['documents_out']}**",
        f"- grid: `{audit['doc_types']} doc types × {audit['domains']} domains = "
        f"{audit['taxonomy_cells']} cells`",
        f"- seed: `{audit['seed']}`",
        "",
        "## Global doc_type counts",
        "",
    ]
    for doc_id, count in sorted(audit["global_doc_type_counts"].items()):
        lines.append(f"- `{doc_id}`: {count}")

    lines.extend(["", "## Global domain counts", ""])
    for domain_id, count in sorted(audit["global_domain_counts"].items()):
        lines.append(f"- `{domain_id}`: {count}")

    lines.extend(
        [
            "",
            "## Per-language fill",
            "",
            "| language | docs | cells_touched / total | min_cell | max_cell |",
            "|----------|------|-----------------------|----------|----------|",
        ]
    )
    by_language = audit["by_language"]
    assert isinstance(by_language, dict)
    for lang, info in by_language.items():
        lines.append(
            f"| {lang} | {info['docs']} | {info['cells_touched']} / {info['cells_total']} | "
            f"{info['min_cell_fill']} | {info['max_cell_fill']} |"
        )

    lines.extend(
        [
            "",
            "## Persona slot uniqueness",
            "",
            "How many distinct taxonomy cells each persona received across its slots:",
            "",
        ]
    )
    histogram = audit["persona_unique_cells_histogram"]
    assert isinstance(histogram, dict)
    for unique_cells, persona_count in histogram.items():
        lines.append(f"- {unique_cells} unique cell(s): {persona_count} persona(s)")
    lines.append("")
    return "\n".join(lines)


def run(pipeline_config: Path) -> dict[str, Path]:
    settings = load_settings(pipeline_config)
    doc_types = load_doc_types(settings.doc_types_config)
    domains = load_domains(settings.domains_config)
    if len(doc_types) != 14:
        raise TaxonomyError(f"Expected 14 doc types, got {len(doc_types)}")
    if len(domains) != 7:
        raise TaxonomyError(f"Expected 7 domains, got {len(domains)}")

    cells = build_cells(doc_types, domains)
    personas = load_personas(settings.input_jsonl)
    rows, audit = assign_taxonomy(personas, cells, settings)
    return write_outputs(rows, audit, settings.output_dir)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Stage 2: stratified 14×7 doc-type × domain assignment",
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
    except (TaxonomyError, ValueError, FileNotFoundError) as exc:
        print(f"[s2] FAILED: {exc}", file=sys.stderr)
        return 1

    print("[s2] Taxonomy assignment complete")
    for label, path in paths.items():
        print(f"  {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
