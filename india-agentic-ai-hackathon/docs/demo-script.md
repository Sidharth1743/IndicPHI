# Demo script — HackGrid Indic-PHI SDG

**Audience:** judges / mentors (≈ 8–10 minutes)  
**Goal:** Show a reproducible agentic pipeline from personas → audited
GLiNER-ready clinical docs, with real failure audits.

## Prep (before the stage)

1. Clone / open `india-agentic-ai-hackathon/`.
2. Copy `configs/nim.env.example` → `.env` and set:
   - `SARVAM_API_KEY`
   - `AZURE_FOUNDRY_API_KEY` (+ chat base URL if needed)
3. Ensure a venv exists (local `.venv` or parent `../.venv` with deps).
4. Optional: pre-run `./scripts/smoke_test.sh` so `data/generated/runs/latest`
   and `failures.md` already exist (API latency can eat live time).

## Live walkthrough

### 1. Problem (45s)

- Indian clinical text is DPDP-sensitive → we **synthesize** it.
- Target: multilingual clinical docs with **inline surrogate PHI** for NER
  (GLiNER), not raw real PII.

### 2. Architecture slide (90s)

Open `docs/architecture.md` or a one-page diagram:

- S1–S3: Nemotron personas → taxonomy → English prompts + entity profiles  
- S4–S4b: Sarvam-105B English-pivot → Indic translation + script check  
- S5–S6: Grok linguistic judge + deterministic checksum auditor  
- S7–S9: MinHash/NeMo Curator → GLiNER JSON + `failures.md`

Emphasize **two-lane audit** (LLM language vs Python structure).

### 3. Config as the control plane (60s)

Show `configs/synthetic-data/pipeline.smoke.yaml`:

- 10 languages, seed, Sarvam-105B generator, Grok judge  
- Point at `entity_profiles.yaml` (required entities per doc type)

### 4. Run or replay smoke (2–3 min)

```bash
./scripts/run_demo.sh
# or: ./scripts/smoke_test.sh
```

If already run, open `data/generated/runs/latest/failures.md` and
`results/eval_report.md`.

Call out concrete failure modes from seed **303** run `20260719T211827`:

- Malayalam insurance claim: **script purity 0** (stayed English) → judge fail  
- Punjabi telemedicine: **gendered verb / persona mismatch**  
- Tamil Aadhaar: **Verhoeff checksum fail** (deterministic lane working)

### 5. Output artifact (60s)

Show a curated GLiNER sample:

- `data/samples/s9_gliner_preview.jsonl` or smoke preview under `data/samples/`  
- Highlight `tokenized_text` + `ner` span triples

### 6. NVIDIA angle (45s)

- Personas: **Nemotron-Personas-India**  
- Generation: **NeMo Data Designer** (required S4 engine)  
- Curation: **NeMo Curator** (required S7 backend; no cpu_minhash)

### 7. Close / ask (30s)

- Next: GLiNER fine-tune learning curve (`configs/training/` stub)

## Backup if APIs are down

1. Walk `data/samples/*_preview.jsonl` stage-by-stage.  
2. Read `results/smoke/failures_20260719T211827.md`.  
3. Summarize metrics from `results/eval_report.md` (S5/S6 pass rates,
   curated doc counts).

## Commands cheat-sheet

```bash
./scripts/smoke_test.sh
./scripts/smoke_test.sh configs/synthetic-data/pipeline.smoke.medium.yaml
./scripts/run_demo.sh
python -m main.pipeline.failures_report --run-id 20260719T211827
```
