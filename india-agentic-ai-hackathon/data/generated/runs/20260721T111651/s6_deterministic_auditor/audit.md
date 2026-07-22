# Stage 6 — Deterministic Auditor

- rows_audited: **108**
- rows_failed: **8**
- pass_rate: **0.926**
- mean_dics: **0.997**
- mean_ecr: **0.996**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `fe2793cf648244fa8cc427adc569983a` · `hospital_billing` · `as` · ['unknown_entity_types:BANK_NAME']
- `a215dd216aff46e7add35a2cb913a177` · `referral_letter` · `en` · ['entity_stuffing:PHONE_NUMBER,RELATIVE_NAME', 'dics_below_threshold:0.625']
- `a215dd216aff46e7add35a2cb913a177` · `radiology_report` · `en` · ['missing_required:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']
- `d89930b893984d4b96fbd0b492413321` · `insurance_claim` · `kn` · ['entity_stuffing:DISTRICT', 'phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']
- `18a30340943543c59236f8f4e9379b8d` · `asha_worker_note` · `ks` · ['phi_residue:1']
- `18a30340943543c59236f8f4e9379b8d` · `automated_sms` · `ks` · ['script_purity:target_script_ratio:0.000<0.35']
- `efe93c7f20fc46b7aa8ef936a09c90c6` · `insurance_claim` · `mr` · ['format:PAN_NUMBER:pan_format']
- `6319018329714b92a0a64f8228dc39b6` · `prescription` · `ne` · ['missing_required:HOSPITAL_NAME']
