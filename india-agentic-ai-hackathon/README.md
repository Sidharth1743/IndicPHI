# HackGrid — Indic-PHI Synthetic Data Pipeline

**Event:** India Agentic AI Open Hackathon  
**Team:** HackGrid  
**Track:** C — Synthetic Data Generation (SDG)

Config-driven, agentic pipeline that generates multilingual synthetic clinical
documents with inline PHI/PII surrogate annotations, audits them with an LLM
judge + deterministic validators, curates **strictly with NeMo Curator** (plus
semantic near-dup), and exports GLiNER-ready span labels with a persona-held-out
train/eval split.

## Why this exists

Real Indian clinical text cannot be freely shared (DPDP). We synthesize
realistic clinical docs across Indic languages, seeded by
`nvidia/Nemotron-Personas-India`, with checksum-valid surrogates and a
fail-closed audit loop.

## Pipeline stages (S1–S10)

| Stage | Role | Module |
|------|------|--------|
| S1 | Seeded hash-rank persona sampling + demographics audit | `main/designers/persona_sampler.py` |
| S2 | Taxonomy 14 doc types × 7 domains | `main/designers/taxonomy.py` |
| S2b | Persona clinical summary (Sarvam-30B, row-checkpointed) | `main/designers/persona_summarizer.py` |
| S3 | Prompt construction + entity profiles | `main/designers/prompt_builder.py` |
| S4 | **NeMo Data Designer** generation (Sarvam-105B provider) | `main/pipeline/designer_config.py` |
| S4b | Tag-preserving translation (ID vs name/place) | `main/designers/translator.py` |
| S5 | Linguistic judge (Grok-4.3 / Azure Foundry, checkpointed) | `main/designers/linguistic_judge.py` |
| S6 | Deterministic auditor (checksums, PHI residue, DICS) | `main/designers/deterministic_auditor.py` |
| S7–S8 | **NeMo Curator** fuzzy dedup + semantic pass + balance | `main/pipeline/curate.py` |
| S9 | GLiNER format + intrinsic metrics | `main/pipeline/gliner_format.py` |
| S10 | Persona-held-out train/eval split | `main/pipeline/split.py` |

Agent entrypoints are summarized under `main/agents/`.

## Quickstart

```bash
# From this folder (india-agentic-ai-hackathon/)
cp configs/nim.env.example .env   # fill SARVAM_API_KEY, AZURE_FOUNDRY_API_KEY
# Prefer a local venv; scripts also fall back to ../.venv if present
uv sync   # installs data-designer + nemo-curator (required)

./scripts/smoke_test.sh
# New runs write under data/generated/runs/ (orchestrator default).
# Submission evidence already packaged under results/runs/ + results/logs/.

./scripts/run_demo.sh
```

Configs: `configs/synthetic-data/pipeline.yaml` (full),
`pipeline.smoke.yaml` (10 docs), `pipeline.smoke.medium.yaml` (20 docs).

Persona seed shard: `data/nemotron-personas-india/`
(`nvidia/Nemotron-Personas-India` local parquet).

## NVIDIA tooling (required)

- **NeMo Data Designer (S4):** required engine (`generation.engine: data_designer`).
  No silent Sarvam-HTTP bypass around Designer.
- **NeMo Curator (S7):** required backend (`curation.dedup.backend: nemo_curator`).
  `cpu_minhash` is disabled. Semantic near-dup runs after Curator on English-pivot /
  PHI-masked text.
- **Personas:** `nvidia/Nemotron-Personas-India`.

## Layout (organizer track + SDG reason)

```
india-agentic-ai-hackathon/
  README.md  LICENSE  .gitignore
  docs/           architecture, demo-script, evaluation-plan (+ plan/idea)
  main/           agents/  + designers pipeline entities llm …
  configs/        nim.env.example  training/  synthetic-data/
  data/
    samples/                 stage previews
    eval/                    gold/eval placeholders
    nemotron-personas-india/ seed shard for S1
  scripts/        smoke_test.sh  run_demo.sh  …
  results/
    runs/         full pipeline run folders (s1–s10 artifacts)
    logs/         smoke console logs
    audits/       failures_*.md quick views
    eval_report.md
    screenshots/
```

No `notebooks/` (not used).

Docs:

- [`docs/architecture.md`](docs/architecture.md)
- [`docs/demo-script.md`](docs/demo-script.md)
- [`docs/evaluation-plan.md`](docs/evaluation-plan.md)
- [`results/eval_report.md`](results/eval_report.md)
- [`results/README.md`](results/README.md)

## License

MIT — see [`LICENSE`](LICENSE).
