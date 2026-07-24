# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **467**
- rows_skipped: `39`
- soft_fail_count: **18**
- script_fail_count: `1`
- generator_repaired_count: `3`
- max_workers: `0`

## Soft failures (audited — not silent)

- `f619d5abd8244e93aab697fe1a8241a8` · `lab_report` · `brx` · error=dedicated_translate_failed:Translation under-counted [[PATIENT_NAME|…]] tags: found=0 expected>=1;script_purity_failed:wrong_indic_script:Bengali>Devanagari;dedicated_translate_failed:Translation under-counted [[PATIENT_NAME|…]] tags: found=0 expected>=1
- `86619deb5c4b4de093d32fe24c54bddc` · `hospital_billing` · `doi` · error=prefer_chat_1:Missing ID placeholder restore for ⟦ID22⟧;prefer_chat_2:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|180012]]'
- `9e6b1442143d466a9594f34920f107cf` · `hospital_billing` · `gu` · error=tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'
- `9e6b1442143d466a9594f34920f107cf` · `opd_slip` · `gu` · error=tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `07e9532716ae495cbcc16b67e6aeb464` · `referral_letter` · `kn` · error=tag_restore_or_translate_failed:dedicated_translate_failed:Translation under-counted [[RELATIVE_NAME|…]] tags: found=1 expected>=2
- `de067f8b897840cab8ecbde4a00e2add` · `hospital_billing` · `ks` · error=prefer_chat_1:Sarvam timeout after 180.0s: The read operation timed out;prefer_chat_2:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[VEHICLE_REGISTRATION|JK01AB1234]]'
- `75419f1fe22f409c8108d2a13f2e677f` · `referral_letter` · `mni` · error=dedicated_translate_failed:Translation lost protected ID tag '[[STATE|Manipur]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[STATE|Manipur]]'
- `d5d814fb7aea4a538977615de1180c4e` · `radiology_report` · `mni` · error=dedicated_translate_failed:Translation lost protected ID tag '[[ABHA_ID|12-3456-7890-1234]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[ABHA_ID|12-3456-7890-1234]]'
- `ffc851ec5afe45e7920df93ce2dbe4ab` · `er_triage_notes` · `mr` · error=no_valid_entity_tags_to_protect
- `3bc580120add4e55b09a0e1ac85b643f` · `hospital_billing` · `sat` · error=dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MC-WB-2024-0815]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MC-WB-2024-0815]]'
- `3bc580120add4e55b09a0e1ac85b643f` · `discharge_summary` · `sat` · error=dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM3⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM3⟧)
- `3bc580120add4e55b09a0e1ac85b643f` · `er_triage_notes` · `sat` · error=dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `dfdd30d26dc24c94a8e5a3cd4aa57a2e` · `automated_sms` · `sat` · error=dedicated_translate_failed:Translation lost protected ID tag '[[APPOINTMENT_ID|APT-240815-02]]';rare_recovery_1:Translation lost or altered name/place TYPE 'DOCTOR_NAME' (placeholder ⟦NM2⟧);dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-OD-2024-001]]'
- `dfdd30d26dc24c94a8e5a3cd4aa57a2e` · `insurance_claim` · `sat` · error=dedicated_translate_failed:Translation lost protected ID tag '[[INSURANCE_POLICY_NUMBER|POL-OD-2024-0042]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[INSURANCE_POLICY_NUMBER|POL-OD-2024-0042]]'
- `dfdd30d26dc24c94a8e5a3cd4aa57a2e` · `radiology_report` · `sat` · error=dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `6227e1809b0743be8c7473f02961d290` · `opd_slip` · `sd` · error=prefer_chat_1:Sarvam timeout after 240.0s: The read operation timed out;prefer_chat_2:Sarvam timeout after 240.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `043f5fb0c78c482298663bcaa05618fe` · `asha_worker_note` · `te` · error=tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM4⟧)
- `da2b757620cf4d158906f012278641f2` · `hospital_billing` · `ur` · error=tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'
