# Stage 6 — Deterministic Auditor

- rows_audited: **58**
- rows_failed: **4**
- pass_rate: **0.931**
- mean_dics: **0.991**
- mean_ecr: **1.000**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `611b1570604d4b8b8d4b06736a0ea305` · `referral_letter` · `bn` · ['dics_below_threshold:0.5']
- `b244567803e34199a9bba1a5e6910e49` · `insurance_claim` · `kok` · ['format:PAN_NUMBER:pan_format', 'format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio:0.033<0.35']
- `c44c080bc5434b75800bf9f1d3a12729` · `lab_report` · `mr` · ['unknown_entity_types:DATE']
- `6e943dc3578249e38b9e61705d0912a9` · `lab_report` · `sa` · ['script_purity:target_script_ratio:0.000<0.35']
