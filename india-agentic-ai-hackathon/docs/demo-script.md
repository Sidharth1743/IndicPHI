# Demo script — HackGrid Indic-PHI SDG

**Audience:** judges / mentors (≈ 8–10 minutes)  
**Goal:** Show a reproducible agentic pipeline from personas → repaired & audited
GLiNER-ready clinical docs, with real failure audits.

## Prep (before the stage)

1. Open `india-agentic-ai-hackathon/`.
2. Copy `configs/nim.env.example` → `.env` and set:
   - `SARVAM_API_KEY`
   - `AZURE_FOUNDRY_API_KEY`
3. `uv sync` (or activate `.venv`) — needs `data-designer` + `nemo-curator`.
4. Optional: pre-run smoke or diversity so `data/generated/runs/latest` and
   `failures.md` exist (API latency can eat live time).

## Live walkthrough

### 1. Problem (45s)

- Indian clinical text is DPDP-sensitive → we **synthesize** it.
- Target: multilingual clinical docs with **inline surrogate PHI** for NER
  (GLiNER). Sarvam-105B covers **22 Indic + English**.

### 2. Architecture (90s)

Open `docs/architecture.md`:

- S1–S3: Nemotron personas → taxonomy → prompts + entity profiles  
- S4–S4b: **NeMo Data Designer** (EN pivot) → Indic translation + **generator repair**  
- S5–S6: Grok judge + deterministic auditor (checksums)  
- S7–S10: **NeMo Curator** → GLiNER JSON → persona-held-out split  

Emphasize **two-lane audit** + **repair known fails** (tags, script) instead of
dropping everything on first soft-fail.

### 3. Config as control plane (60s)

Show `configs/synthetic-data/pipeline.diversity.yaml` or smoke:

- 23 languages (diversity) or 10 (smoke)  
- `generation.engine: data_designer`, `curation.dedup.backend: nemo_curator`  
- `entity_profiles.yaml` + `doc_format_examples.yaml`

### 4. Run or replay (2–3 min)

```bash
./scripts/run_demo.sh
# or smoke:
./scripts/smoke_test.sh
# or diversity:
python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml
```

Open `data/generated/runs/latest/failures.md`. Call out:

- **Diversity `20260720T192801`:** 20 curated / 23 langs; S4 repaired 8; S4b
  repaired 5; remaining soft fails on hard scripts / S5 quality flags  
- **Smoke `20260720T140451`:** Curator path green; soft fails audited (not silent)

### 5. Output artifact (60s)

- `s9_gliner_format/` or `data/samples/s9_gliner_preview.jsonl`  
- Highlight `tokenized_text` + `ner` triples  
- `s10_split/` persona-held-out train/eval

### 6. NVIDIA angle (45s)

- Personas: **Nemotron-Personas-India**  
- Generation: **NeMo Data Designer** (required)  
- Curation: **NeMo Curator** (required; RAPIDS-aligned install)

### 7. Close (30s)

- Next: S5 flag-targeted repair 3–5× + S6 checksum repair; GLiNER learning curve

## Backup if APIs are down

1. Walk `data/samples/*_preview.jsonl`.  
2. Read `data/generated/runs/20260720T192801/failures.md` or `results/`.  
3. Summarize `results/eval_report.md`.

## Commands cheat-sheet

```bash
./scripts/smoke_test.sh
./scripts/smoke_test.sh configs/synthetic-data/pipeline.smoke.medium.yaml

python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml \
  2>&1 | tee /tmp/pipeline_diversity.log

python -m main.pipeline.failures_report --run-id 20260720T192801
```
