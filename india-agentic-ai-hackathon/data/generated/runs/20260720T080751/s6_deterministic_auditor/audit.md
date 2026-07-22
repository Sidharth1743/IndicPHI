# Stage 6 — Deterministic Auditor

- rows_audited: **18**
- rows_failed: **2**
- pass_rate: **0.889**
- mean_dics: **1.000**
- mean_ecr: **0.996**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `877a805cf7d24d64b693bbfb59bf4e58` · `insurance_claim` · `kn` · ['format:AADHAAR_NUMBER:aadhaar_verhoeff']
- `81ed007d28a447e3952a9359d6e9e528` · `opd_slip` · `ta` · ['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME']
