# HackGrid — Indic-PHI Synthetic Data Generation Pipeline (Track C: SDG)

**Event:** India Agentic AI Open Hackathon · **Team:** HackGrid · **Track:** C — Synthetic Data Generation
**Goal:** A config-driven, reproducible pipeline that generates a high-quality, multilingual (23 Indic + English)
synthetic clinical-document dataset with inline PII/PHI surrogate annotations, curates & deduplicates it,
formats it for GLiNER, and proves quality via intrinsic metrics + a downstream GLiNER fine-tuning learning curve.

---

## 1. Problem & Approach

Real Indian clinical text can't be shared (DPDP Act). We synthesize it instead:

- **Generate** realistic clinical docs (14 doc types × 7 domains × 23 languages) seeded by
  `Nemotron-Personas-India`, using **NeMo Data Designer** + **Sarvam-30B** (NIM) with _inline surrogate PHI/PII_.
- **Audit** every doc through a two-lane loop:
  - **Lane A — Linguistic Judge (LLM):** Sarvam-105B → dialect/script purity, instruction drift, entity shift, surrogate plausibility. Judge meta-metrics (calibration, consistency, positional bias, label dist).
  - **Lane B — Deterministic Python:** Aadhaar/PAN/IFSC checksums, pincode/phone regex, PHI-residue scan, span-alignment (tokenization/truncation), Entity-Type-Collapse stats, **DICS** (Doc Internal Consistency Score). Zero hallucination.
- **Curate** with **NeMo Curator (pip module)**: MinHash+LSH near-dup removal (Jaccard>0.8) + language-stratified distribution balancing.
- **Format** to span-based token-indexed JSON for **GLiNER**; compute intrinsic metrics (ECR, ISED, span P/R/F1 vs gold).
- **Split** 50/50 stratified by language; **Release** as a Hugging Face dataset + card + DPDP audit trail.
- **Prove** value: fine-tune GLiNER, report downstream NER F1, per-entity F1, and a 10/20/30…% learning curve.

**Design principles (from user):** everything scales via **configs** only; use **`nemo-curator` as a pip module**
(do NOT depend on the cloned `Curator/` repo); codebase is **lightweight, neat, reproducible** — no dead code.

---

## 2. Folder Structure (aligned to organizer's recommended layout)

```text
nvidia-hack/                         # repo root (existing)
├── README.md                        # quickstart, architecture summary, repro steps
├── LICENSE
├── .gitignore                       # ignore .venv, Curator/, data/generated, artifacts, .env
├── pyproject.toml                   # deps: data-designer, nemo-curator, gliner, datasets, ...
│
├── docs/
│   ├── architecture.md              # the 12-stage pipeline + this flowchart, rendered
│   ├── demo-script.md               # step-by-step live demo walkthrough
│   └── evaluation-plan.md           # intrinsic + extrinsic metric definitions & targets
│
├── app/                             # the pipeline "agents" + orchestration (importable pkg)
│   ├── __init__.py
│   ├── agents/                      # per-stage logic (the flowchart boxes)
│   │   ├── persona_sampler.py       # S1  sample Nemotron-Personas-India (HF)
│   │   ├── taxonomy.py              # S2  14 docs × 7 domains combinatorics
│   │   ├── prompt_builder.py        # S3  persona+doc+domain+inline-annotation-rules → prompt
│   │   ├── generator.py             # S4  Sarvam-30B via Data Designer LLM column
│   │   ├── linguistic_judge.py      # S5  Sarvam-105B judge + retry/fail routing
│   │   └── deterministic_auditor.py # S6  python validators + DICS + fail routing
│   ├── pipeline/
│   │   ├── designer_config.py       # build DataDesignerConfigBuilder from YAML configs
│   │   ├── curate.py                # S7-8 nemo-curator MinHash+LSH dedup + balancing
│   │   ├── gliner_format.py         # S9  inline-tags → span token-indexed JSON
│   │   ├── split.py                 # S10 stratified-by-language train/test split
│   │   ├── release.py               # S11 HF dataset + card + DPDP audit trail
│   │   └── run.py                   # end-to-end orchestrator (reads configs, drives S1→S11)
│   ├── entities/
│   │   ├── schema.py                # 50-entity PII/PHI taxonomy (from flowchart-with-entities)
│   │   └── surrogate.py             # Indic-plausible surrogate generators per entity type
│   ├── validators/
│   │   ├── checksums.py             # Aadhaar(Verhoeff), PAN, IFSC, pincode, phone
│   │   ├── phi_residue.py           # scan for un-replaced real-looking PHI
│   │   ├── spans.py                 # span↔string alignment, tokenization/truncation checks
│   │   └── dics.py                  # Document Internal Consistency Score
│   ├── metrics/
│   │   ├── judge_metrics.py         # calibration, consistency, positional bias, label dist
│   │   └── intrinsic.py             # ECR, ISED, span Precision/Recall/F1 vs gold
│   ├── train/
│   │   └── gliner_finetune.py       # S12 fine-tune + per-entity F1 + learning curve
│   ├── api/                         # optional: FastAPI to trigger/preview a run
│   │   └── main.py
│   └── ui/                          # optional: Streamlit demo (preview a generated doc + spans)
│       └── app.py
│
├── configs/
│   ├── nim.env.example              # NVIDIA_API_KEY=..., model IDs (Sarvam-30B/105B)
│   ├── synthetic-data/
│   │   ├── pipeline.yaml            # SCALE KNOBS: docs_per_persona, total target, thresholds, models
│   │   ├── languages.yaml           # 23 Indic + English
│   │   ├── domains.yaml             # 7 clinical domains
│   │   ├── doc_types.yaml           # 14 document types
│   │   ├── entities.yaml            # PII/PHI taxonomy + inline tag format
│   │   └── annotation_rules.yaml    # inline surrogate annotation spec
│   ├── training/
│   │   └── gliner.yaml              # base model, epochs, lr, learning-curve fractions
│   └── nat/                         # (placeholder for NeMo Agent Toolkit config if used)
│
├── data/
│   ├── samples/                     # tiny committed example outputs (smoke-test scale)
│   ├── eval/                        # hand-curated GOLD set for span P/R/F1 + downstream eval
│   └── generated/                   # (gitignored) full pipeline outputs
│
├── notebooks/
│   ├── 01_explore_personas.ipynb
│   ├── 02_preview_generation.ipynb
│   └── 03_learning_curve.ipynb      # plot F1 vs train size
│
├── scripts/
│   ├── smoke_test.sh                # tiny end-to-end run (few docs) — CI-friendly
│   └── run_demo.sh                  # demo-scale run for judges
│
└── results/
    ├── screenshots/
    └── eval_report.md               # final intrinsic + extrinsic numbers
```

**Note on existing files:** Existing prototype snippets were folded into `notebooks/02_preview_generation.ipynb` and `app/pipeline/designer_config.py`, then removed from standalone scratch files. The cloned `Curator/` repo stays local for reference but is `.gitignored`; this project depends on `nemo-curator` from PyPI.

---

## 3. Stage → Module Map

| Stage | Flowchart box                     | Module                                                              |
| ----- | --------------------------------- | ------------------------------------------------------------------- |
| S0    | Foundation / NIM setup            | `configs/nim.env.example`, `pyproject.toml`                         |
| S1    | Persona sampling (3 docs/persona) | `app/agents/persona_sampler.py`                                     |
| S2    | Doc taxonomy (14×7)               | `app/agents/taxonomy.py`, `configs/synthetic-data/*`                |
| S3    | Prompt construction               | `app/agents/prompt_builder.py`                                      |
| S4    | Generator (Sarvam-30B)            | `app/agents/generator.py`, `app/pipeline/designer_config.py`        |
| S5    | Linguistic judge (Sarvam-105B)    | `app/agents/linguistic_judge.py`, `app/metrics/judge_metrics.py`    |
| S6    | Deterministic auditor             | `app/agents/deterministic_auditor.py`, `app/validators/*`           |
| S7    | Dedup (MinHash+LSH)               | `app/pipeline/curate.py`                                            |
| S8    | Distribution balancing            | `app/pipeline/curate.py`                                            |
| S9    | GLiNER format + intrinsic         | `app/pipeline/gliner_format.py`, `app/metrics/intrinsic.py`         |
| S10   | Train/test split                  | `app/pipeline/split.py`                                             |
| S11   | Dataset release (HF + DPDP)       | `app/pipeline/release.py`                                           |
| S12   | GLiNER fine-tune + curve          | `app/train/gliner_finetune.py`, `notebooks/03_learning_curve.ipynb` |

---

## 4. Todos (tracked in SQL)

Build order is dependency-driven: scaffold → configs/schema → generation → audit → curate → format/metrics → release → fine-tune → docs/demo.

---

## 5. Key Decisions & Notes

- **Scale:** single source of truth = `configs/synthetic-data/pipeline.yaml`. Smoke test = a handful of docs;
  demo/full runs change only config values. No code changes to scale to 120k.
- **Models:** Sarvam-30B (generator) + Sarvam-105B (judge) via NVIDIA NIM (`NVIDIA_API_KEY`). Model IDs live in config.
- **Curator:** `pip install nemo-curator`; do not import from the cloned repo.
- **Compute:** local GPU now → cloud GPU instance for the hackathon (dedup optionally RAPIDS/GPU; GLiNER training needs GPU).
- **Inline annotation format** (proposed): `[[TYPE|surrogate_value]]` in generated text → converted to
  `{text, tokens, spans:[{start,end,label}]}` in S9. Finalize format in `configs/synthetic-data/annotation_rules.yaml`.
- **DPDP audit trail:** release includes provenance (seed persona id, model IDs, config hash, validator pass log) — all synthetic, no real PHI.
- **NVIDIA skills:** optionally use `npx skills add nvidia/skills` (e.g., NIM/Curator helpers) during build.

## 6. Risks / Open Items

- Confirm exact NIM model IDs for Sarvam-30B/105B at build time.
- `nemo-curator` extras (GPU vs CPU) — pick CPU-compatible dedup path for portability, GPU when available.
- Gold eval set (`data/eval/`) must be built carefully — it anchors every quality metric.
- GLiNER base model choice + tokenizer alignment for Indic scripts (validate span offsets on Devanagari/Tamil/etc.).

## 7. Document Types (14)

- OPD Slip (Outpatient Department)
- Prescription
- ASHA Worker Note
- Automated SMS Notifications
- Hospital Billing / Invoice
- Discharge Summary
- Referral Letter
- Radiology / Imaging Report
- ER Triage & Nursing Notes
- Telemedicine / Doctor-Patient Chat Transcript
- Surgical / Operative Note
- Lab Report
- PHC Register Entry (Primary Health Centre)
- Insurance Claim / TPA Form

## 8. Clinical Domains (7)

- General Medicine
- Maternal Health
- Tuberculosis & Non-Communicable Diseases
- Surgical
- Paediatric
- Oncology / Complex Chronic Care
- Psychiatry / Behavioral Health

## 9. Entity Taxonomy

### 9.1 PII (Personally Identifiable Information)

**A. Personal Information**
- Patient Name
- Relative Name (Father/Mother/Spouse/Guardian)
- Date of Birth (DOB)
- Age
- Gender
- Religion
- Caste
- Occupation

**B. Government Identification**
- Aadhaar Number
- PAN Number
- Passport Number
- Driving Licence Number
- Voter ID
- BPL / Ration Card Number
- Tax Identification Number (TIN/GSTIN or other tax IDs)

**C. Contact & Location Information**
- Phone Number
- Telephone Number (Landline)
- Email Address
- Residential Address
- District
- Village
- ZIP / Postal Code (PIN Code)
- IP Address
- URL (Personal Website/Profile)

**D. Financial Information**
- Bank Account Number
- IFSC Code
- Bank Routing Number
- Credit Card Number
- CVV
- PIN

**E. Professional & Institutional Identifiers**
- Employee ID
- Student ID

**F. Device & Digital Identifiers**
- IMEI Number
- MAC Address

**G. Other Identifiers**
- Vehicle Registration Number / Vehicle Identifier

### 9.2 PHI (Protected Health Information)

**A. Patient Healthcare Identifiers**
- ABHA ID
- ABHA Address
- Medical Record Number (MRN)
- Patient ID
- Hospital ID
- Admission Number
- Encounter / Visit ID
- Appointment ID
- Referral ID

**B. Healthcare Provider Information**
- Doctor Name
- ASHA Worker Name
- Hospital / Institution Name

**C. Healthcare Facility Information**
- Bed Number
- Ward Number
- Insurance Policy Number

## 10. Evaluation Framework

### 10.1 Layer A — Judge Model Metrics (Meta-Evaluation)

1. **Calibration**
   - Compare judge score with human ground-truth on a gold set (~200 samples).
   - Metric: Spearman correlation (rho) between judge score and human span-F1 per sample.
   - Target: rho > 0.75; investigate if rho < 0.65.

2. **Judge Consistency (Intra-Judge Reliability)**
   - Run the same sample through the judge 3 times (temperature > 0).
   - Metric: Consistency rate = % of samples with identical verdict across all 3 runs.
   - Target: > 90%.

3. **Positional / Length Bias**
   - Check if judge over-passes longer notes regardless of true annotation quality.
   - Metric: correlation between note_length (tokens) and judge_pass_rate.
   - Alert threshold: r > 0.3.

4. **Label Distribution Alignment**
   - Compare observed pass/fail ratio against expected quality profile over ~1000 samples.
   - Heuristic flags: pass > 85% (too lenient) or pass < 40% (too strict/broken generator).

### 10.2 Layer B — Dataset Quality Metrics

1. **Entity Coverage Rate (ECR)**
   - ECR = |entity_types_present| / |entity_types_expected_for_this_persona|.
   - Example: if 4 expected entity types appear out of 6, ECR = 0.67.
   - Purpose: detects insufficient PHI/PII surface area.

2. **Inter-Sample Entity Diversity (IED)**
   - IED per entity type = |unique_surrogate_values| / |total_entity_instances|.
   - Example target: IED(PATIENT_NAME) > 0.85.
   - Purpose: prevents memorization of repeated surrogates.

3. **Document-Internal Consistency Score (DICS)**
   - DICS = correct_coreferenced_spans / total_coreferenced_spans.
   - Hard target: DICS = 1.0.
   - Any DICS < 1.0 indicates contradictory training labels in the same document.

4. **Annotation Span Precision / Recall / F1 vs Gold**
   - Evaluate on a manually labeled gold subset (100–200 docs).
   - Exact boundary agreement required for true positive span matches.

### 10.3 Extrinsic Metrics (Does the dataset train GLiNER?)

1. **Downstream NER F1 on Real Gold Data**
   - Train GLiNER on synthetic data and evaluate on held-out real annotated clinical notes (50–100+).
   - Compare against:
     - GLiNER zero-shot baseline
     - GLiNER trained on English-only de-id data

2. **Entity-Type Breakdown**
   - Report F1 per entity type (e.g., PATIENT_NAME, AADHAAR_NUMBER, RELATIVE_NAME).
   - Low F1 on rare types indicates coverage imbalance in generation.

3. **Learning Curve Analysis**
   - Train at 10%, 25%, 50%, 75%, 100% of training set.
   - Plot F1 vs dataset size to evaluate marginal utility of added synthetic data.

## 11. Error Taxonomy (Indic-PHI)

1. **Persona-Document Drift**
   - Symptom: style/register/location cues drift away from persona mid-document.
   - Detection: compare persona anchors (language, district, SES tier, institution type) at 25/50/75/100% of document length.

2. **Entity Type Collapse**
   - Symptom: multiple name-like entities collapse into PATIENT_NAME.
   - Detection: per-document label entropy H = -Σ p(entity_type) * log p(entity_type); low H implies collapse risk.

3. **Cross-Language Entity Shift**
   - Symptom: entity conventions mismatch document language/script context.
   - Detection: cultural plausibility checks (name ↔ script ↔ gender ↔ guardian suffix, institution ↔ district/state).
   - Signal: Cross-Language Entity Shift Rate (CLESR).

4. **Tokenization/Truncation Boundary Failure**
   - Symptom: PHI spans split at invalid boundaries due to subword tokenization/truncation.
   - Detection: validate Unicode character boundary alignment and clean re-tokenization.
   - Signal: Boundary Corruption Rate (BCR) = malformed_spans / total_spans.
   - Target: BCR < 0.01.
