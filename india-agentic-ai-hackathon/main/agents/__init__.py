"""Agentic stage index for the Indic-PHI synthetic data pipeline.

Organizers expect ``main/agents/``. Implementation modules live under
``main.designers`` and ``main.pipeline`` so imports stay stable
(``python -m main.pipeline.run_pipeline``).
"""

from __future__ import annotations

# Re-export stage entry modules for discoverability.
from main.designers import deterministic_auditor as s6_deterministic_auditor
from main.designers import generator as s4_generator
from main.designers import linguistic_judge as s5_linguistic_judge
from main.designers import persona_sampler as s1_persona_sampler
from main.designers import persona_summarizer as s2b_persona_summarizer
from main.designers import prompt_builder as s3_prompt_builder
from main.designers import taxonomy as s2_taxonomy
from main.designers import translator as s4b_translator
from main.pipeline import curate as s7_s8_curate
from main.pipeline import gliner_format as s9_gliner_format
from main.pipeline import run_pipeline
from main.pipeline import split as s10_split

__all__ = [
    "s1_persona_sampler",
    "s2_taxonomy",
    "s2b_persona_summarizer",
    "s3_prompt_builder",
    "s4_generator",
    "s4b_translator",
    "s5_linguistic_judge",
    "s6_deterministic_auditor",
    "s7_s8_curate",
    "s9_gliner_format",
    "s10_split",
    "run_pipeline",
]
