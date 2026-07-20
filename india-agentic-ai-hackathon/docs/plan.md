# HackGrid — Indic-PHI Synthetic Data Generation Pipeline (Track C: SDG)

**Event:** India Agentic AI Open Hackathon · **Team:** HackGrid · **Track:** C — Synthetic Data Generation  

**Goal:** Config-driven, reproducible pipeline that generates multilingual (22 Indic + English) synthetic clinical documents with inline PHI/PII surrogate annotations, repairs known failures, curates with NeMo Curator, formats for GLiNER, and splits persona-held-out train/eval.

---

## 1. Problem & Approach

Real Indian clinical text can't be shared (DPDP Act). We synthesize it instead:

- **Generate** clinical docs (14 doc types × 7 domains × 23 languages) seeded by
  `Nemotron-Personas-India`, via **NeMo Data Designer** + **Sarvam-105B**
  (native 22 Indic + English) with _inline surrogate PHI/PII_.
- **English-pivot** for S4 tag discipline → **S4b** tag-preserving Indic render.
- **Audit** with a two-lane loop + **generator repair**:
  - **Lane A — Linguistic Judge (LLM):** Grok-4.3 — dialect/script purity,
    instruction drift, entity shift, surrogate plausibility, invented types, length.
  - **Lane B — Deterministic Python:** Aadhaar Verhoeff, PAN/IFSC/phone,
    PHI-residue, spans, **DICS**. Zero hallucination on structure.
  - **Repair:** known fails (missing tags, stuffing, wrong script; design: S5
    flags 3–5×, checksum/phone) → clear instructions → generator → re-check.
- **Curate** with **NeMo Curator** FuzzyDeduplicationWorkflow + semantic near-dup
  + language balance (`cpu_minhash` disabled).
- **Format** to token-indexed JSON for **GLiNER**; intrinsic metrics + `failures.md`.
- **Split** persona-held-out (all docs of a UUID in train **or** eval).

**Design principles:** scale via **configs**; `nemo-curator` and `data-designer`
as pip modules; lightweight, reproducible; **no silent bypass** of Designer/Curator.

---

## 2. Submission layout

```text
india-agentic-ai-hackathon/
├── README.md
├── docs/                 architecture, idea, plan, demo, evaluation, diversification
├── main/
│   ├── agents/           organizer-facing re-exports
│   ├── designers/        S1–S6 (+ repair.py, entity_checks.py)
│   ├── pipeline/         run_pipeline, designer_config, curate, gliner, split, …
│   ├── entities/         schema + surrogates
│   ├── validators/       checksums, script_purity, phi_residue, spans, dics
│   ├── llm/              Sarvam + OpenAI-compatible
│   └── metrics/          judge + intrinsic
├── configs/
│   ├── nim.env.example
│   └── synthetic-data/   pipeline*.yaml, languages, entities, profiles, examples
├── data/                 samples, eval, nemotron shard, generated/ (gitignored)
├── scripts/              smoke_test.sh, run_demo.sh
└── results/              packaged evidence, eval_report.md
```

---

## 3. Stages (implemented)

| Stage | What | Module |
|-------|------|--------|
| S1 | Seeded hash-rank personas + demographics audit | `persona_sampler.py` |
| S2 | 14 × 7 taxonomy assignment | `taxonomy.py` |
| S2b | Clinical English summary (Sarvam-30B, checkpointed) | `persona_summarizer.py` |
| S3 | Prompts + profiles + format/placement examples | `prompt_builder.py` |
| S4 | **NeMo Data Designer** + Sarvam-105B; coverage/stuffing **repair** | `designer_config.py`, `repair.py` |
| S4b | Tag-preserving translation; script **repair** via generator | `translator.py` |
| S5 | Grok linguistic judge (progress-logged) | `linguistic_judge.py` |
| S6 | Deterministic auditor | `deterministic_auditor.py` |
| S7–S8 | **NeMo Curator** + semantic dedup + balance | `curate.py`, `nemo_curator_fuzzy.py` |
| S9 | GLiNER export + metrics | `gliner_format.py` |
| S10 | Persona-held-out split | `split.py` |

Orchestrator: `python -m main.pipeline.run_pipeline --config …`

### Repair loop (current + next)

| Failure | Status | Action |
|---------|--------|--------|
| Missing required tags / stuffing | **Implemented** (S4) | Generator repair → re-check |
| Wrong language/script | **Implemented** (S4b) | Generator rewrite from EN pivot → purity check |
| S5 flags (impurity, drift, plausibility, …) | **Design** | Flag→instruction repair 3–5× → re-judge |
| Aadhaar Verhoeff / phone / PHI residue | **Design** | Deterministic fix or gen repair → re-audit |
| S3 prevention | **Partial** | Placement/domain hints; expand good-vs-bad examples |

---

## 4. Configs

| File | Use |
|------|-----|
| `pipeline.smoke.yaml` | ~10 docs / 10 langs |
| `pipeline.smoke.medium.yaml` | ~20 docs |
| `pipeline.diversity.yaml` | **23 langs**, 1×3 ≈ 69 docs, `allow_underfill: true` |
| `pipeline.yaml` | Full-scale knobs toward 120k |

---

## 5. Observed smoke / diversity baselines

| Run | Profile | Curated | Notes |
|-----|---------|--------:|-------|
| `20260720T140451` | smoke | 7 | Repair path validated end-to-end incl. Curator |
| `20260720T180107` | medium | 8 | OPD `HOSPITAL_NAME` pattern |
| `20260720T192801` | diversity 23-lang | 20 | S4 repaired 8; S4b repaired 5; 20/23 langs curated |

See `docs/evaluation-plan.md` and `results/eval_report.md`.

---

## 6. Evaluation (summary)

**Intrinsic:** entity coverage, script soft-fails, S5/S6 pass rates, curated
counts, ECR/ISED/span F1 at S9, `failures.md` taxonomy.

**Extrinsic (planned):** GLiNER fine-tune F1, per-entity / per-language,
learning curve (`configs/training/`).

---

## 7. Commands

```bash
cd india-agentic-ai-hackathon && source .venv/bin/activate

# Diversity (23 languages)
python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml \
  2>&1 | tee /tmp/pipeline_diversity.log

# Smoke
./scripts/smoke_test.sh

# Resume a run
python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml \
  --run-id <RUN_ID> --from-stage s5_linguistic_judge
```

Secrets: `configs/nim.env.example` → `.env` (`SARVAM_API_KEY`, `AZURE_FOUNDRY_API_KEY`).
