# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **125**
- rows_skipped: `13`
- soft_fail_count: **8**
- script_fail_count: `1`
- generator_repaired_count: `3`
- max_workers: `12`

## Soft failures (audited — not silent)

- `57e0ccc76318480b91dca7f2d464c122` · `hospital_billing` · `gu` · error=tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'
- `59e7e12eb3d44dfbacf8755ef02f52c7` · `opd_slip` · `kn` · error=tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `60ff3470cf8340efaa474e13896d8568` · `opd_slip` · `ks` · error=prefer_chat_1:Translation lost protected ID tag '[[GENDER|Male]]';dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)
- `22ef884ce12247309d07fc3f601a3c59` · `asha_worker_note` · `sa` · error=dedicated_translate_failed:Translation lost protected ID tag '[[AGE|19]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[AGE|19]]'
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · error=dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-2024-0815-001]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|400022]]'
- `825c4438c02440dc90d3ddec7ffec8ee` · `discharge_summary` · `sd` · error=dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);script_purity_failed:wrong_indic_script:Devanagari>Arabic;dedicated_translate_failed:Translation lost protected ID tag '[[DOB|1992-06-15]]'
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · error=dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|390001]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|390001]]'
- `ce942a5fb5644181ac0db94b6c9c1314` · `automated_sms` · `ta` · error=tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'PATIENT_NAME' (placeholder ⟦NM0⟧)
