# Stage 6 — Deterministic Auditor

- rows_audited: **115**
- rows_failed: **3**
- pass_rate: **0.974**
- mean_dics: **0.983**
- mean_ecr: **1.000**
- mean_bcr: **0.0004**

## Failures (audited — not silent)

- `1f7da27d8fe544a191d7adc016e62971` · `referral_letter` · `gu` · ['dics_below_threshold:0.0']
- `57e0ccc76318480b91dca7f2d464c122` · `hospital_billing` · `gu` · ['span_alignment_failure', 'boundary_corruption_rate:0.05']
- `829db9fbfeda404d89ff9b8a405b5e4d` · `insurance_claim` · `ta` · ['dics_below_threshold:0.0']
