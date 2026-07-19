# Evaluation plan — Indic-PHI SDG

## Goals

1. Prove the pipeline produces **usable** multilingual clinical NER data
   (intrinsic quality + auditability).
2. Prove the data **helps** a downstream GLiNER model (extrinsic learning curve).
3. Keep evaluation **reproducible** via configs and timestamped run folders.

## Intrinsic metrics (pipeline-native)

Computed primarily at S5 / S6 / S9 and summarized in `failures.md` /
`run_results.json`.

| Metric | Where | Definition / target |
|--------|-------|---------------------|
| Entity coverage complete rate | S4 | Fraction of docs with all required profile entities tagged. Smoke target ≥ 0.9 |
| Script purity soft-fail count | S4b | Docs below target-script ratio threshold |
| Judge pass rate | S5 | Fraction with verdict pass / score above threshold. Smoke observed ~0.85–0.90 |
| Auditor pass rate | S6 | Fraction passing checksums / residue / unknown-type checks |
| Curated doc count | S7–S8 | Survivors after dedup + balance |
| ECR / ISED / span P/R/F1 | S9 | Intrinsic annotation quality vs gold or self-consistency |
| Near-dup rate | S7 | MinHash Jaccard ≥ 0.8 removals |

**Judge meta-metrics** (calibration, consistency, positional bias, label
distribution) live in `main/metrics/judge_metrics.py` for deeper audits.

## Failure taxonomy (operator-facing)

`main.pipeline.failures_report` classifies issues into:

- **hard** — should not proceed (orchestration / schema)
- **gen_soft** — missing required entities, stuffing
- **tr_soft** — translation / script purity
- **judge** — linguistic fail flags
- **auditor** — deterministic format / PHI residue / unknown types

Every smoke run writes `failures.md` with UUID, language, doc type, and
preview snippets for judges.

## Extrinsic metrics (downstream NER)

Planned once `configs/training/` and GLiNER fine-tune land:

| Metric | Protocol |
|--------|----------|
| Overall NER F1 | Fine-tune GLiNER on curated train split; eval on held-out synthetic + optional gold |
| Per-entity F1 | Stratify by PHI type (AADHAAR, PAN, PATIENT_NAME, …) |
| Per-language F1 | Stratify by `document_language_code` |
| Learning curve | Train on 10/20/30/…% of data; plot F1 vs size |
| Gold span P/R/F1 | Against hand-curated set in `data/eval/` (to be expanded) |

Train/test split: stratified by language (planned S10). Release card + DPDP
audit trail planned for HF upload (S11).

## Smoke evaluation protocol (what we run now)

```bash
./scripts/smoke_test.sh
# Inspect:
#   data/generated/runs/latest/failures.md
#   data/generated/runs/latest/run_results.json
#   data/generated/runs/latest/s9_gliner_format/
```

Documented smoke baselines (see `results/eval_report.md`):

- **20260719T211827** (seed 303): status ok, curated 9 docs, S5 pass ≈ 0.85,
  S6 pass ≈ 0.88, entity coverage 1.0
- **20260719T191524** (prior): status ok, curated 9 docs, S5 pass 0.9,
  coverage 0.9

## Gold / eval set (`data/eval/`)

Placeholder for a small hand-checked set of span-aligned documents used for:

- span Precision / Recall / F1 vs human labels  
- regression checks when prompts or validators change  

Until populated, use `data/samples/` previews and smoke `failures.md` as
evidence packs for the hackathon demo.

## Out of scope for Track C demo

- Full 23-language production-scale generation cost study  
- Replacing IndicTrans2 wholesale eval dumps (kept outside submission bulk)
