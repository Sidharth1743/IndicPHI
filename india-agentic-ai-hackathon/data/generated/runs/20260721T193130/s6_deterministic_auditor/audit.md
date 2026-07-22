# Stage 6 — Deterministic Auditor

- rows_audited: **127**
- rows_failed: **5**
- pass_rate: **0.961**
- mean_dics: **1.000**
- mean_ecr: **1.000**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `fe2793cf648244fa8cc427adc569983a` · `hospital_billing` · `as` · ['unknown_entity_types:ADDRESS_NUMBER', 'phi_residue:2']
- `e2083507b6fc4542853ff740cac47edf` · `hospital_billing` · `bn` · ['unknown_entity_types:RECEIPT_NUMBER']
- `62bbda52de29443287ee799e3f265919` · `hospital_billing` · `hi` · ['phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']
- `efe93c7f20fc46b7aa8ef936a09c90c6` · `insurance_claim` · `mr` · ['format:PAN_NUMBER:pan_format']
- `e9f9b9a22bcb47f28198db61b9bd4966` · `hospital_billing` · `sd` · ['unknown_entity_types:CONTACT_EMAIL,EMAIL']
