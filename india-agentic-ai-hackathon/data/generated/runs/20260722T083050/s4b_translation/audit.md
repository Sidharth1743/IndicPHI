# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **119**
- rows_skipped: `19`
- soft_fail_count: **15**
- script_fail_count: `2`
- generator_repaired_count: `0`
- max_workers: `24`

## Soft failures (audited — not silent)

- `df61060159844e75aeafcafe43b1bc0d` · `referral_letter` · `mni` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `6e943dc3578249e38b9e61705d0912a9` · `insurance_claim` · `sa` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4;post_repair_translate:Sarvam timeout after 300.0s: The read operation timed out
- `0b19143502244d21a03f71ef838ab4ff` · `automated_sms` · `sat` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `0b19143502244d21a03f71ef838ab4ff` · `hospital_billing` · `sat` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `e899bd99966c4ac6b77d784bae3482f0` · `asha_worker_note` · `sat` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `825c4438c02440dc90d3ddec7ffec8ee` · `automated_sms` · `sd` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · error=dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic
- `825c4438c02440dc90d3ddec7ffec8ee` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `insurance_claim` · `sd` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4;post_repair_translate:Sarvam timeout after 300.0s: The read operation timed out
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · error=dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic;generator_repair_failed:Sarvam timeout after 600.0s: The read operation timed out
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `829db9fbfeda404d89ff9b8a405b5e4d` · `opd_slip` · `ta` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `ce942a5fb5644181ac0db94b6c9c1314` · `automated_sms` · `ta` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `6b15543bcd6545f5803d6887e2a48820` · `radiology_report` · `ur` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
- `bf0de98a0c63491c8877846b6f8dad65` · `radiology_report` · `ur` · error=tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4
