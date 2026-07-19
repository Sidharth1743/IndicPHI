"""NeMo Data Designer config bridge (plan S4 / idea Stage-0→4).

Builds a ``DataDesignerConfigBuilder`` seeded from Stage-3 prompts so
generation can run through Data Designer LLM columns when an OpenAI-compatible
NIM (or gateway) endpoint is configured.

Smoke path today uses ``main.designers.generator`` + Sarvam HTTP directly.
This module is the explicit bridge — no silent fallback between engines.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from main.pipeline.config_io import REPO_ROOT, load_yaml, resolve_repo_path


@dataclass(frozen=True)
class DesignerBridgeSettings:
    seed_path: Path
    model_alias: str
    model_id: str
    provider: str
    temperature: float
    max_tokens: float | int
    system_prompt_column: str
    user_prompt_column: str
    output_column: str


class DesignerConfigError(RuntimeError):
    pass


def load_designer_bridge_settings(pipeline_config: Path) -> DesignerBridgeSettings:
    root = load_yaml(pipeline_config)
    block = root.get("data_designer")
    if not isinstance(block, dict):
        raise DesignerConfigError(
            f"'data_designer' mapping required in {pipeline_config} "
            "when using the Data Designer generation engine"
        )

    required = (
        "seed_path",
        "model_alias",
        "model_id",
        "provider",
        "temperature",
        "max_tokens",
    )
    missing = [key for key in required if key not in block]
    if missing:
        raise DesignerConfigError(f"Missing data_designer keys {missing}")

    return DesignerBridgeSettings(
        seed_path=resolve_repo_path(str(block["seed_path"])),
        model_alias=str(block["model_alias"]),
        model_id=str(block["model_id"]),
        provider=str(block["provider"]),
        temperature=float(block["temperature"]),
        max_tokens=int(block["max_tokens"]),
        system_prompt_column=str(block.get("system_prompt_column", "system_prompt")),
        user_prompt_column=str(block.get("user_prompt_column", "user_prompt")),
        output_column=str(block.get("output_column", "generated_text")),
    )


def load_config_builder(pipeline_config: Path | None = None):
    """Return a DataDesignerConfigBuilder seeded from pipeline prompts.

    Requires the ``data-designer`` package. Seed columns (including prompts)
    are kept; an LLM text column generates the clinical document.
    """
    try:
        import data_designer.config as dd
    except ImportError as exc:
        raise DesignerConfigError(
            "data-designer is not installed. "
            "Install with `pip install data-designer`."
        ) from exc

    config_path = pipeline_config or (
        REPO_ROOT / "configs" / "synthetic-data" / "pipeline.yaml"
    )
    settings = load_designer_bridge_settings(config_path)
    if not settings.seed_path.is_file():
        raise DesignerConfigError(
            f"Data Designer seed not found: {settings.seed_path}. "
            "Run S3 prompt construction first (prompts.parquet preferred)."
        )

    builder = dd.DataDesignerConfigBuilder()
    builder.add_model_config(
        dd.ModelConfig(
            alias=settings.model_alias,
            model=settings.model_id,
            provider=settings.provider,
            inference_parameters=dd.ChatCompletionInferenceParams(
                temperature=settings.temperature,
                max_tokens=settings.max_tokens,
            ),
        )
    )
    builder.with_seed_dataset(dd.LocalFileSeedSource(path=str(settings.seed_path)))
    builder.add_column(
        dd.LLMTextColumnConfig(
            name=settings.output_column,
            model_alias=settings.model_alias,
            system_prompt=f"{{{{{settings.system_prompt_column}}}}}",
            prompt=f"{{{{{settings.user_prompt_column}}}}}",
        )
    )
    return builder


def describe_bridge() -> dict[str, Any]:
    """Capability note for audits / README."""
    return {
        "role": "Optional S4 engine via NeMo Data Designer",
        "seed": "S3 prompts parquet (persona + taxonomy + annotation rules)",
        "when_to_use": "Wire NIM OpenAI-compatible provider into Data Designer, then call load_config_builder()",
        "smoke_default": "main.designers.generator (Sarvam HTTP)",
        "curator": "S7 uses FuzzyDeduplicationWorkflow via main.pipeline.nemo_curator_fuzzy",
        "skills_aligned": [
            "data-designer (seed datasets + LLMTextColumnConfig)",
            "nemo-curator getting-started / fuzzy dedup docs",
        ],
    }
