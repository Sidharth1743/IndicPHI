"""Entity taxonomy schema loaded from configs/synthetic-data/entities.yaml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

from main.pipeline.config_io import load_yaml


@dataclass(frozen=True)
class EntitySpec:
    id: str
    name: str
    category: str


def load_entity_specs(path: Path) -> dict[str, EntitySpec]:
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


def require_known_entities(
    entity_ids: list[str] | tuple[str, ...],
    known: Mapping[str, EntitySpec],
    *,
    context: str,
) -> None:
    unknown = [entity_id for entity_id in entity_ids if entity_id not in known]
    if unknown:
        raise ValueError(f"{context}: unknown entity ids {unknown}")
