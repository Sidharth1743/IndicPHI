# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **101**
- rows_skipped: `37`
- soft_fail_count: **33**
- script_fail_count: `2`
- generator_repaired_count: `0`
- max_workers: `12`

## Soft failures (audited — not silent)

- `3a14ecc1de8648689a3311540c7cdd2e` · `lab_report` · `as` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=1
- `3ceb8b6e61ba4069980e557280aa9ba0` · `opd_slip` · `brx` · error=tag_restore_or_translate_failed:None
- `3ceb8b6e61ba4069980e557280aa9ba0` · `insurance_claim` · `brx` · error=tag_restore_or_translate_failed:None
- `18473c8835b140ff8c0b5ed0d35a5271` · `opd_slip` · `doi` · error=tag_restore_or_translate_failed:None
- `18473c8835b140ff8c0b5ed0d35a5271` · `prescription` · `doi` · error=tag_restore_or_translate_failed:None
- `18473c8835b140ff8c0b5ed0d35a5271` · `insurance_claim` · `doi` · error=tag_restore_or_translate_failed:None
- `8116ee5699344b79a2c9c8d1e053dde5` · `asha_worker_note` · `doi` · error=tag_restore_or_translate_failed:None
- `8116ee5699344b79a2c9c8d1e053dde5` · `automated_sms` · `doi` · error=tag_restore_or_translate_failed:None
- `8116ee5699344b79a2c9c8d1e053dde5` · `insurance_claim` · `doi` · error=tag_restore_or_translate_failed:None
- `60ff3470cf8340efaa474e13896d8568` · `er_triage_notes` · `ks` · error=tag_restore_or_translate_failed:None
- `60ff3470cf8340efaa474e13896d8568` · `telemedicine_transcript` · `ks` · error=tag_restore_or_translate_failed:None
- `60ff3470cf8340efaa474e13896d8568` · `opd_slip` · `ks` · error=tag_restore_or_translate_failed:None
- `885a67d0071948ac8a8336b278e81003` · `er_triage_notes` · `ks` · error=tag_restore_or_translate_failed:None
- `885a67d0071948ac8a8336b278e81003` · `telemedicine_transcript` · `ks` · error=tag_restore_or_translate_failed:None
- `885a67d0071948ac8a8336b278e81003` · `opd_slip` · `ks` · error=tag_restore_or_translate_failed:None
- `df61060159844e75aeafcafe43b1bc0d` · `discharge_summary` · `mni` · error=tag_restore_or_translate_failed:None
- `df61060159844e75aeafcafe43b1bc0d` · `referral_letter` · `mni` · error=tag_restore_or_translate_failed:None
- `22ef884ce12247309d07fc3f601a3c59` · `insurance_claim` · `sa` · error=tag_restore_or_translate_failed:None
- `22ef884ce12247309d07fc3f601a3c59` · `asha_worker_note` · `sa` · error=tag_restore_or_translate_failed:None
- `6e943dc3578249e38b9e61705d0912a9` · `automated_sms` · `sa` · error=tag_restore_or_translate_failed:None
- `6e943dc3578249e38b9e61705d0912a9` · `insurance_claim` · `sa` · error=tag_restore_or_translate_failed:None
- `0b19143502244d21a03f71ef838ab4ff` · `asha_worker_note` · `sat` · error=tag_restore_or_translate_failed:None
- `0b19143502244d21a03f71ef838ab4ff` · `automated_sms` · `sat` · error=tag_restore_or_translate_failed:None
- `0b19143502244d21a03f71ef838ab4ff` · `hospital_billing` · `sat` · error=tag_restore_or_translate_failed:None
- `e899bd99966c4ac6b77d784bae3482f0` · `asha_worker_note` · `sat` · error=tag_restore_or_translate_failed:None
- `e899bd99966c4ac6b77d784bae3482f0` · `insurance_claim` · `sat` · error=tag_restore_or_translate_failed:None
- `825c4438c02440dc90d3ddec7ffec8ee` · `automated_sms` · `sd` · error=tag_restore_or_translate_failed:None
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · error=dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic
- `825c4438c02440dc90d3ddec7ffec8ee` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:None
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `insurance_claim` · `sd` · error=tag_restore_or_translate_failed:None
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · error=dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:None
- `57a29898a6944b899059fb674d16f990` · `hospital_billing` · `te` · error=tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'
