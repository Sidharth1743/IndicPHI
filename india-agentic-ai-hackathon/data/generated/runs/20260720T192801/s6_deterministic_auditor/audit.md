# Stage 6 — Deterministic Auditor

- rows_audited: **42**
- rows_failed: **5**
- pass_rate: **0.881**
- mean_dics: **1.000**
- mean_ecr: **0.987**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `3c0199017c7c4f00bbb3de4770ce25fc` · `hospital_billing` · `as` · ['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:1']
- `8b08baf3bcbf412eaace2d648074de01` · `surgical_note` · `bn` · ['missing_required:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER', 'upstream_generation_soft_fail:missing_required_entities:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER']
- `72db01dc59584f27949df74b76c51edf` · `radiology_report` · `mai` · ['missing_required:HOSPITAL_ID', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_ID']
- `259f783314be4a6ca9979240d0de82cd` · `telemedicine_transcript` · `ne` · ['format:PHONE_NUMBER:phone_format']
- `c8cbb5811e2a4a05bfe15b06b2be3a52` · `insurance_claim` · `ur` · ['format:AADHAAR_NUMBER:aadhaar_verhoeff']
