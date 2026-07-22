# Stage 6 — Deterministic Auditor

- rows_audited: **15**
- rows_failed: **3**
- pass_rate: **0.800**
- mean_dics: **1.000**
- mean_ecr: **0.985**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `12e31823de794a7ba4bbdd82d74370f3` · `telemedicine_transcript` · `bn` · ['entity_stuffing_total_tags:30>24', 'entity_stuffing:AGE,EMAIL_ADDRESS,GENDER,HOSPITAL_NAME,PHONE_NUMBER', 'upstream_generation_soft_fail:entity_stuffing:AGE,GENDER,PHONE_NUMBER,EMAIL_ADDRESS,HOSPITAL_NAME']
- `6368e3f4fd8448f69e688a500e614e9a` · `opd_slip` · `bn` · ['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME']
- `92bfd5dd40004d968c6c58538433407c` · `opd_slip` · `ta` · ['missing_required:HOSPITAL_NAME,EMPLOYEE_ID', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME,EMPLOYEE_ID']
