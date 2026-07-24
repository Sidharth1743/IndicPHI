# Architecture — Indic-PHI Agentic Synthetic Data Pipeline

## Overview

HackGrid’s submission is a **config-driven, multi-agent SDG pipeline** that
produces synthetic Indian clinical documents with **inline PHI/PII surrogate
tags**, then audits, repairs known failures, curates, and formats them for
**GLiNER** fine-tuning.

**Generation model:** Sarvam-105B with native support for **all 22 official
Indian languages + English** (native script, romanized, and code-mixed).
**English-pivot** is still used for S4 (stable tag coverage), then S4b
renders the target Indic language/script while preserving tags.

Quality is enforced by a **two-lane audit** plus a **generator repair loop**
for known, recoverable failures:

1. **Lane A — Linguistic judge (LLM):** Grok-4.3 via Azure Foundry — dialect /
   script purity, instruction drift, domain–persona fit, surrogate plausibility,
   invented types, length.
2. **Lane B — Deterministic auditor (Python):** Aadhaar Verhoeff, PAN/IFSC/
   phone/pincode regex, PHI-residue scan, span alignment, DICS. No LLM on
   structural rules.

```text
 Personas (Nemotron India)  — 23 languages
            │
            ▼
   S1 sample → S2 taxonomy → S2b summarize → S3 prompts
            │                    (placement + domain + format examples)
            ▼
   S4 NeMo Data Designer (Sarvam-105B EN + tags)
            │  ↻ repair: missing tags / stuffing (generator)
            ▼
   S4b translate → target script
            │  rare: dedicated /translate first + few-shots
            │  ↻ timeout → dedicated; language-locked
            ▼
   S5 LLM judge (Grok)     S6 deterministic auditor
            │  ↻ persona: tag patch → LLM (≤2)
            │  ↻ other flags: language-locked LLM
            │  flag-targeted        │  checksum / phone /
            │  repair               │  tag / PHI repair
            └──────────┬────────────┘
                       ▼
   S7–S8 NeMo Curator fuzzy dedup + semantic near-dup + balance
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
| `main/designers/` | Stage logic: sample, taxonomy, prompts, gen, translate, judge, audit |
| `main/designers/repair.py` | Targeted generator repair for known soft failures |
| `main/designers/entity_checks.py` | Shared coverage / stuffing checks (S4 + repair) |
| `main/pipeline/` | Orchestration, Data Designer bridge, Curator, GLiNER, split, failures |
| `main/entities/` | Entity schema + surrogate generators |
| `main/validators/` | Checksums, script purity, PHI residue, spans, DICS |
| `main/llm/` | Sarvam + OpenAI-compatible clients, rate limits |
| `main/metrics/` | Judge meta-metrics + intrinsic ECR / ISED / span F1 |
| `configs/synthetic-data/` | Scale knobs, languages, entities, profiles, examples |

`REPO_ROOT` is resolved from `main/pipeline/config_io.py` — this folder is a
self-contained submission root.

## Stage detail

### S1 — Persona sampling
Seeded hash-rank sampling from `nvidia/Nemotron-Personas-India` with
demographics audit. Stratified by `languages.yaml` (23 codes).

### S2 / S2b — Taxonomy + persona summary
Assigns each persona a cell in the **14 × 7** doc-type × domain grid
(prefer unique cells). S2b compresses lifestyle fields into a short **clinical
English** summary (Sarvam-30B), row-checkpointed.

### S3 — Prompt construction
Merges persona + doc type + domain + **entity profiles** + annotation rules +
**doc format examples**. Placement hints cover OPD (`HOSPITAL_NAME` vs
`HOSPITAL_ID`), radiology (`DOCTOR_NAME`), telemedicine (header-once metadata),
and domain anchoring. Prompts require **all profile entities** as inline tags.

### S4 — Generation (NeMo Data Designer)
- **Required** engine: `generation.engine: data_designer` (no silent HTTP bypass).
- Seed = S3 prompts parquet; column = `LLMTextColumnConfig` with Jinja
  `{{system_prompt}}` / `{{user_prompt}}`.
- Sarvam-105B registered as Designer provider (`api-subscription-key`).
- After Designer returns rows: **coverage + total-tag stuffing** checks.
- **Repair (implemented):** missing tags / stuffing → send draft back to
  generator with fix instructions (`repair_retries` / `empty_content_retries`),
  then re-check. Soft-fail only if repairs exhaust.
- Row-level `checkpoint.jsonl` for resume.

### S4b — Tag-preserving translation
- Translates EN pivot → target language/script.
- **ID entity values** byte-stable; **name/place** values may localize.
- Script purity gate (ratio + wrong-Indic-script detection; aliases e.g.
  `Ol_Chiki` → `Ol Chiki`).
- **Rare scripts** (`brx`, `mni`, `sat`, `ks`, `sd`, `doi`, `sa`):
  recover **at S4b** (not S5): dedicated `/translate` first (except prefer-chat
  `doi`/`ks`/`sd`), then short chat recovery, then dedicated again; for Arabic
  script (`sd`/`ks`) a script-lock rewrite if Devanagari leaks; `sd` gets longer
  chat timeout + ≥2 prefer-chat attempts (dedicated often drops ID tags);
  shared Translate RPM limiter; keep non-English wrong-script over English.
- Common langs: chat translate; first timeout → dedicated.
- Chat workers kept lower than generation so Translate API is not starved.
- **Transport (DNS / timeout / connection):** if the *final* ladder error is
  transport, checkpoint as `hard_fail` and fail the stage for resume. Mid-ladder
  timeouts that end in tag/script quality fails stay soft-fail.
- **Repair:** non-rare script fails may rewrite via generator; rare stays on
  the S4b ladder (language-locked) so judge does not burn CoT on English.

### S5 — Linguistic judge
Grok-4.3 (Azure Foundry). Returns `verdict`, `score`, `flags`, `reasoning`.
Pass if `verdict=pass` and `score ≥ pass_threshold` (default 0.7).

| Flag | Meaning |
|------|---------|
| `dialect_script_impurity` | Clinical **prose** wrong language/script (Latin IDs inside tags OK) |
| `instruction_drift` | Ignores assigned domain / structure |
| `surrogate_plausibility_collapse` | Implausible geo/name/ABHA vs persona |
| `domain_persona_mismatch` | Sex/age vs clinical content |
| `cross_language_entity_shift` | Person/place values wrong script |
| `invented_entity_type` | TYPE outside allow-list |
| `length_violation` | SMS / short form is a chart dump |

**Repair (implemented):**
- First generation stays free (no pre-S5 persona pin — preserves diversity).
- After judge fails on persona flags → **tag-only patch** from large name pools
  (PATIENT_NAME / GENDER / DISTRICT / AGE) → re-judge.
- Same persona failure again → **one** language-locked LLM repair with locked
  surrogates (max **2** repairs on persona-only path).
- Additional flags (script, drift, …) → act accordingly (language-locked LLM;
  rare still capped; dedicated `/translate` last resort for rare script fails).
- No tiny Python pre-gate before judge; no neighbor-lang soft-pass.

### S6 — Deterministic auditor
Checksums (Aadhaar Verhoeff, phone, …), unknown types, PHI residue, DICS,
upstream soft-fail propagation. Fail-closed on structure.

**Repair (design — next):** Verhoeff/phone can be fixed deterministically;
missing tags → generator repair; then re-audit. Goal: curated set has
**no** leftover checksum / tag / script soft junk.

### S7–S8 — Curation
**Required** `nemo_curator` FuzzyDeduplicationWorkflow on English-pivot /
PHI-masked text; then semantic near-dup; language balance
(`allow_underfill` on diversity profile). `cpu_minhash` disabled.

### S9 — GLiNER format
Inline tags → token spans; intrinsic metrics; orchestrator writes
**`failures.md`** per run.

### S10 — Persona-held-out split
All docs for a persona UUID go to train **or** eval (never both), stratified
by language × doc_type × domain.

## Configs (scale knobs)

| Config | Scale |
|--------|-------|
| `pipeline.smoke.yaml` | 10 langs × 1 persona × 1 doc ≈ 10 docs |
| `pipeline.smoke.medium.yaml` | 10 langs × 2 personas ≈ 20 docs |
| `pipeline.diversity.yaml` | **23 langs** × 1 persona × 3 docs ≈ 69 docs |
| `pipeline.yaml` | Full path toward 120k (equal language slices) |

## Models & secrets

| Role | Model | Env |
|------|-------|-----|
| Generator / translator | Sarvam-105B (22 Indic + EN) | `SARVAM_API_KEY` |
| Persona summarizer | Sarvam-30B | `SARVAM_API_KEY` |
| Linguistic judge | Grok-4.3 (Azure Foundry) | `AZURE_FOUNDRY_API_KEY` |

See `configs/nim.env.example`. Never commit `.env`.

## Run layout

```bash
python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml \
  2>&1 | tee /tmp/pipeline_diversity.log

# data/generated/runs/<timestamp>/
#   pipeline.resolved.yaml  manifest.json  failures.md
#   s1_… s10_…  artifacts/nemo_curator_dedup/
# data/generated/runs/latest → <timestamp>
```

## Design principles

- **Configs scale the system**, not code forks.
- **LLM for language; Python for structure.**
- **English pivot** for tag discipline; Indic render in S4b.
- **Repair known failures** before soft-fail / drop — cheaper than regenerating
  whole batches; persona patch is **post-judge** only (keeps generation diverse).
- **Language-locked** rare-script path (dedicated first + few-shots); no
  neighbor-lang soft-pass.
- **Fail closed** on checksum / unknown types after repairs exhaust.
- **NeMo Data Designer (S4) + NeMo Curator (S7)** are required — no silent
  bypass backends.
- Code-switching / code-mix generation is deferred (not implemented).
