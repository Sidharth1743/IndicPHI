"""Shared constants for the demo UI API."""

from __future__ import annotations

# Presentation nodes → underlying orchestrator stage labels (run_results.json).
NODE_STAGES: dict[str, tuple[str, ...]] = {
    "seed": (
        "s1_persona_sampling",
        "s2_taxonomy",
        "s2b_persona_summary",
        "s3_prompt_construction",
    ),
    "generate": ("s4_generation",),
    "translate": ("s4b_translation",),
    "judge": ("s5_linguistic_judge",),
    "audit": ("s6_deterministic_auditor",),
    "curate": ("s7_s8_curation",),
    "export": ("s9_gliner_format", "s10_split"),
}

NODE_ORDER: tuple[str, ...] = (
    "seed",
    "generate",
    "translate",
    "judge",
    "audit",
    "curate",
    "export",
)

STAGE_TO_NODE: dict[str, str] = {
    stage: node for node, stages in NODE_STAGES.items() for stage in stages
}

STAGE_FOLDER: dict[str, str] = {
    "s1_persona_sampling": "s1_persona_sampling",
    "s2_taxonomy": "s2_taxonomy",
    "s2b_persona_summary": "s2b_persona_summary",
    "s3_prompt_construction": "s3_prompts",
    "s4_generation": "s4_generation",
    "s4b_translation": "s4b_translation",
    "s5_linguistic_judge": "s5_linguistic_judge",
    "s6_deterministic_auditor": "s6_deterministic_auditor",
    "s7_s8_curation": "s7_s8_curation",
    "s9_gliner_format": "s9_gliner_format",
    "s10_split": "s10_split",
}

NODE_MODELS: dict[str, str] = {
    "seed": "Nemotron-Personas-India",
    "generate": "NeMo Data Designer + Sarvam-105B",
    "translate": "Sarvam-105B",
    "judge": "Grok-4.3",
    "audit": "Checksums / DICS",
    "curate": "NeMo Curator",
    "export": "GLiNER + split",
}

MODELS_BLURB: dict[str, str] = {
    "generation": "NeMo Data Designer + Sarvam-105B",
    "translation": "Sarvam-105B",
    "judge": "Grok-4.3",
    "curator": "NeMo Curator",
    "personas": "Nemotron-Personas-India",
}

# Target wall-clock for replay animation (seconds).
REPLAY_DURATION_S = 40.0
