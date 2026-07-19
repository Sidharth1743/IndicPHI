"""Entity package exports."""

from main.entities.schema import EntitySpec, load_entity_specs, require_known_entities

__all__ = ["EntitySpec", "load_entity_specs", "require_known_entities"]
