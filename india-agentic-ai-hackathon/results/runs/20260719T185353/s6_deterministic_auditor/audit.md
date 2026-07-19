# Stage 6 — Deterministic Auditor

- rows_audited: **9**
- rows_failed: **1**
- pass_rate: **0.889**
- mean_dics: **1.000**
- mean_ecr: **0.981**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `7568f8e67bea4c959a480fd295d29db7` · `telemedicine_transcript` · `en` · ['missing_required:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME', 'upstream_generation_soft_fail:missing_required_entities:AGE,GENDER;entity_stuffing:DOCTOR_NAME,PATIENT_NAME']
