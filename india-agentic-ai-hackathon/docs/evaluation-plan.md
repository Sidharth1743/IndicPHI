# Evaluation plan — Indic-PHI SDG

## Goals

1. Prove the pipeline produces **usable** multilingual clinical NER data
   (intrinsic quality + auditability + repair yield).
2. Prove the data **helps** a downstream GLiNER model (extrinsic learning curve).
3. Keep evaluation **reproducible** via configs and timestamped run folders.

## Intrinsic metrics (pipeline-native)

| Metric | Where | Definition / target |
|--------|-------|---------------------|
| Entity coverage complete rate | S4 | Docs with all required profile entities. Target ≥ 0.9 after repair |
| Generation repaired count | S4 | Docs fixed by generator repair (missing tags / stuffing) |
| Script purity soft-fail count | S4b | Below target-script ratio / wrong Indic script |
| Generator repaired (translation) | S4b | Script fails recovered via rewrite |
| Judge pass rate | S5 | `verdict=pass` and score ≥ threshold (default 0.7) |
| Auditor pass rate | S6 | Checksums / residue / unknown-type / coverage |
| Curated doc count + languages | S7–S8 | Survivors after Curator + balance |
| ECR / ISED / span P/R/F1 | S9 | Annotation quality |
| Near-dup drops | S7 | Curator + semantic |

## Failure taxonomy (`failures.md`)

| Class | Examples |
|-------|----------|
| **hard** | Orchestration / schema |
| **gen_soft** | Missing required entities, stuffing (after repair attempts) |
| **tr_soft** | Script purity / wrong script (after repair) |
| **judge** | `dialect_script_impurity`, `instruction_drift`, `surrogate_plausibility_collapse`, `domain_persona_mismatch`, `invented_entity_type`, `length_violation` |
| **auditor** | Aadhaar Verhoeff, phone format, PHI residue, upstream soft-fail |

### S5 flags (what they mean)

| Flag | Recoverable? | Intent |
|------|--------------|--------|
| `dialect_script_impurity` | Yes — rewrite prose in target script | Prose wrong language (ID tags Latin OK) |
| `instruction_drift` | Yes — domain-anchored regen | Clinical content ignores assigned domain |
| `surrogate_plausibility_collapse` | Yes — bind geo/name to persona | District/ABHA/name inconsistency |
| `domain_persona_mismatch` | Yes — match sex/age clinical fit | e.g. male maternal content |
| `cross_language_entity_shift` | Yes — localize name/place values | Wrong script in PERSON/PLACE tags |
| `invented_entity_type` | Yes — strip/rename to allow-list | e.g. `DATE`, `POLICY_NUMBER` |
| `length_violation` | Yes — compress SMS | Chart dump instead of short alert |

**Design:** flag-targeted generator repair **3–5×** + re-judge; prevent via S3
good-vs-bad examples. Deterministic S6 issues should not remain in the curated set.

## Extrinsic metrics (downstream NER)

Planned with `configs/training/`:

| Metric | Protocol |
|--------|----------|
| Overall NER F1 | Fine-tune GLiNER; eval held-out + optional gold |
| Per-entity / per-language F1 | Stratify by TYPE and language |
| Learning curve | 10/20/30/…% train size |
| Gold span P/R/F1 | `data/eval/` hand labels |

**Split:** S10 persona-held-out (not random doc split).

## Smoke / diversity protocol

```bash
./scripts/smoke_test.sh
python -m main.pipeline.run_pipeline \
  --config configs/synthetic-data/pipeline.diversity.yaml

# Inspect:
#   data/generated/runs/latest/failures.md
#   data/generated/runs/latest/run_results.json
#   …/s4_generation/audit.json  (generation_repaired_count)
#   …/s4b_translation/audit.json (generator_repaired_count)
```

### Documented baselines

| Run | Profile | Coverage | S5 | S6 | Curated | Langs |
|-----|---------|----------|----|----|--------:|------:|
| `20260720T140451` | smoke 10 | 0.80 | 0.80 | 0.88 | 7 | 7 |
| `20260720T180107` | medium 20 | 0.80 | 0.75 | 0.80 | 8 | 8 |
| `20260720T192801` | diversity 69 | **0.93** | 0.61 | 0.88 | **20** | **20/23** |

Diversity notes: S4 repaired **8**, S4b repaired **5**; zero curated for
`brx` / `sat` / `sd` on that seed (script / quality gates). Hard fails: 0.

## Gold / eval set (`data/eval/`)

Placeholder for hand-checked span-aligned docs. Until populated, use
`data/samples/` and run `failures.md` for regression visibility.
