# Stage 6 — Deterministic Auditor

- rows_audited: **492**
- rows_failed: **13**
- pass_rate: **0.974**
- mean_dics: **0.991**
- mean_ecr: **1.000**
- mean_bcr: **0.0000**

## Failures (audited — not silent)

- `f594af83f49d4547947752d58c0e45a9` · `insurance_claim` · `bn` · ['phi_residue:2']
- `f594af83f49d4547947752d58c0e45a9` · `hospital_billing` · `bn` · ['script_purity:target_script_ratio:0.000<0.35']
- `d21516b79dbe4fb78827faca53231bb6` · `insurance_claim` · `doi` · ['missing_required:BANK_ROUTING_NUMBER', 'phi_residue:4', 'script_purity:target_script_ratio:0.000<0.35']
- `39f3b8aa1d6b43a7bb32ef3cbb8bd25c` · `hospital_billing` · `gu` · ['entity_stuffing:TAX_ID,TELEPHONE_LANDLINE', 'phi_residue:1']
- `ba9480c1ca6a41458712603104065e74` · `referral_letter` · `kok` · ['dics_below_threshold:0.0']
- `666ba63c7da84db8a643943d59820646` · `hospital_billing` · `ml` · ['dics_below_threshold:0.0']
- `ffc851ec5afe45e7920df93ce2dbe4ab` · `hospital_billing` · `mr` · ['phi_residue:1']
- `093fd825483c42618796923e84fdb6f0` · `hospital_billing` · `ne` · ['format:PAN_NUMBER:pan_format']
- `0538f3faf4324debbd546bf332d419f6` · `telemedicine_transcript` · `pa` · ['dics_below_threshold:0.0']
- `3bc580120add4e55b09a0e1ac85b643f` · `prescription` · `sat` · ['script_purity:target_script_ratio:0.000<0.35']
- `dfdd30d26dc24c94a8e5a3cd4aa57a2e` · `hospital_billing` · `sat` · ['format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio:0.000<0.35']
- `228cb6f1c22941279fc07428487acd05` · `prescription` · `sd` · ['dics_below_threshold:0.0']
- `6227e1809b0743be8c7473f02961d290` · `insurance_claim` · `sd` · ['phi_residue:8', 'dics_below_threshold:0.5', 'script_purity:wrong_indic_script:Devanagari>Arabic']
