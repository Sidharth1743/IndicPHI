# Architecture — Indic-PHI Agentic Synthetic Data Pipeline

## Overview

HackGrid’s submission is a **config-driven, multi-agent SDG pipeline** that
produces synthetic Indian clinical documents with **inline PHI/PII surrogate
tags**, then audits, curates, and formats them for **GLiNER** fine-tuning.

Generation is **English-pivot**: Sarvam-105B writes English clinical prose with
`[[ENTITY_TYPE|surrogate]]` tags; a translation stage (S4b) renders target
Indic script while preserving tags. Quality is enforced by a **two-lane audit**:

1. **Lane A — Linguistic judge (LLM):** Grok-4.3 via Azure Foundry — dialect /
   script purity, instruction drift, domain–persona fit, surrogate plausibility.
2. **Lane B — Deterministic auditor (Python):** Aadhaar Verhoeff, PAN/IFSC/
   phone/pincode regex, PHI-residue scan, span alignment, DICS (Document
   Internal Consistency Score). No LLM hallucination on structural rules.

Failed docs are routed out; survivors are deduplicated and balanced, then
exported as token-indexed NER JSON.

```text
 Personas (Nemotron India)
            │
            ▼
   S1 sample → S2 taxonomy → S2b summarize → S3 prompts
            │
            ▼
   S4 generate (EN + inline tags, Sarvam-105B)
            │
            ▼
   S4b translate → target script (soft-fail on script purity)
            │
     ┌──────┴──────┐
     ▼             ▼
   S5 LLM judge   S6 deterministic auditor
     │             │
     └──────┬──────┘
            ▼
   S7–S8 dedup + balance (**NeMo Curator** required + semantic near-dup)
            │
            ▼
   S9 GLiNER JSON + intrinsic metrics + failures.md
            │
            ▼
   S10 persona-held-out train/eval split
```

## Package map

| Path | Responsibility |
|------|----------------|
| `main/agents/` | Organizer-facing agent index (re-exports stage modules) |
| `main/designers/` | Per-stage agent logic (S1–S6 + translation) |
| `main/pipeline/` | Orchestration, curation, GLiNER, run layout, failures report |
| `main/entities/` | Entity schema + surrogate generators |
| `main/validators/` | Checksums, script purity, PHI residue, spans, DICS |
| `main/llm/` | Sarvam + OpenAI-compatible clients, rate limits |
| `main/metrics/` | Judge meta-metrics + intrinsic ECR / ISED / span F1 |
| `configs/synthetic-data/` | Scale knobs, languages, entities, entity profiles |

`REPO_ROOT` is resolved from `main/pipeline/config_io.py` (parents of the
`main/` package), so this folder is a self-contained submission root.

## Stage detail

### S1 — Persona sampling
Samples `nvidia/Nemotron-Personas-India` stratified by language codes from
`languages.yaml`. Smoke: 10 languages × 1 persona × 1 doc.

### S2 / S2b — Taxonomy + persona summary
Assigns each persona a cell in the **14 × 7** doc-type × domain grid.
S2b compresses lifestyle fields into a short **clinical English** summary
(Sarvam-30B) for prompting without leaking long free-text noise.

### S3 — Prompt construction
Merges persona + doc type + domain + **entity profiles** (required /
optional PHI types per doc) + annotation rules + format examples.
Prompts require **all profile entities** as inline tags.

### S4 / S4b — Generation + translation
- **S4:** **NeMo Data Designer** is the required engine (`generation.engine:
  data_designer`). Sarvam-105B is registered as a Designer provider
  (`api-subscription-key`). Row-level checkpoints make resume idempotent.
  Soft-fails on missing required entities / stuffing when Designer returns them.
- **S4b:** Translates to target language with **ID tags fully protected** and
  **name/place values** free to localize; **script purity** (incl. cross-Indic
  script detection + `Ol_Chiki`→`Ol Chiki` aliases) must clear a threshold
  (e.g. ≥ 0.35). Romanized / Latin-only output soft-fails and is usually also
  failed by the judge.

### S5 — Linguistic judge
Grok-4.3 chat completions (Azure Foundry). Scores dialect/script purity,
domain–persona mismatch, instruction drift, surrogate plausibility.
Pass rate is logged; fails appear in `failures.md`.

### S6 — Deterministic auditor
Checksum & format validators (notably Aadhaar Verhoeff), unknown entity
types, PHI residue, DICS. Failures are hard-structural and fail-closed.

### S7–S8 — Curation
Near-dup removal (Jaccard ≥ 0.8) **requires** `nemo_curator`
FuzzyDeduplicationWorkflow on English-pivot / PHI-masked text, then a
semantic near-dup pass (`main/pipeline/semantic_dedup.py`). `cpu_minhash`
is disabled. Language balancing warns when equalize-to-min discards >20%.

### S9 — GLiNER format
Inline tags → token spans; writes `gliner_docs.jsonl` / train JSON and
intrinsic metrics. Orchestrator writes **`failures.md`** per run for audit.

### S10 — Persona-held-out split
All docs for a persona UUID go to train **or** eval (never both), stratified
by language × doc_type × domain.

## Models & secrets

| Role | Model / endpoint | Env |
|------|------------------|-----|
| Generator / translator / summarizer | Sarvam-105B / 30B | `SARVAM_API_KEY` |
| Linguistic judge | Grok-4.3 (Azure Foundry) | `AZURE_FOUNDRY_API_KEY` |
| Optional NIM | NVIDIA endpoints | `NVIDIA_API_KEY`, `NIM_BASE_URL` |

See `configs/nim.env.example`. Never commit `.env`.

## Run layout

```bash
./scripts/smoke_test.sh
# data/generated/runs/<timestamp>/
#   pipeline.resolved.yaml  manifest.json  failures.md
#   s1_persona_sampling/ … s9_gliner_format/  s10_split/
# data/generated/runs/latest → <timestamp>
```

Each run is timestamped; stages never overwrite prior runs.

## Design principles

- **Configs scale the system** (`pipeline.yaml`), not code forks.
- **LLM for language; Python for structure.**
- **English pivot** improves entity coverage before Indic rendering.
- **Fail closed** on checksum / unknown types; soft-fail + report on
  coverage and script purity for operator visibility.
