# Stage 6 — Deterministic Auditor

- rows_audited: **18**
- rows_failed: **2**
- pass_rate: **0.889**
- mean_dics: **1.000**
- mean_ecr: **0.996**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `7568f8e67bea4c959a480fd295d29db7` · `discharge_summary` · `en` · ['missing_required:DOB', 'upstream_generation_soft_fail:missing_required_entities:DOB']
- `66f87f0087064abda3938f2c4aba879e` · `insurance_claim` · `pa` · ['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:3']
