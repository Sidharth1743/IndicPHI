# Stage 6 — Deterministic Auditor

- rows_audited: **130**
- rows_failed: **4**
- pass_rate: **0.969**
- mean_dics: **0.992**
- mean_ecr: **0.992**
- mean_bcr: **0.0022**

## Failures (audited — not silent)

- `5afdbf29e52249fc95146ec7db5e2023` · `insurance_claim` · `as` · ['phi_residue:1']
- `9b16854e981048c59b1bc1efd2685bdf` · `hospital_billing` · `hi` · ['dics_below_threshold:0.0']
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `hospital_billing` · `mni` · ['span_alignment_failure', 'boundary_corruption_rate:0.2857142857142857']
- `5c09bf9c92bb4474a1a128379f250e86` · `hospital_billing` · `sd` · ['missing_required:PATIENT_NAME,HOSPITAL_NAME,MRN,DISTRICT,PIN_CODE,PHONE_NUMBER,AADHAAR_NUMBER,INSURANCE_POLICY_NUMBER,TAX_ID,TELEPHONE_LANDLINE,VEHICLE_REGISTRATION,EMAIL_ADDRESS,RESIDENTIAL_ADDRESS,PAN_NUMBER', 'phi_residue:14']
