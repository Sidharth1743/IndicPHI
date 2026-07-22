# Stage 4b — Translation Audit

- model: `sarvam-105b`
- rows_translated: **102**
- rows_skipped: `36`
- soft_fail_count: **37**
- script_fail_count: `7`
- generator_repaired_count: `0`
- max_workers: `24`

## Soft failures (audited — not silent)

- `8a02e74c7f104c1fa9f00b8507bac016` · `radiology_report` · `mni` · error=Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `df61060159844e75aeafcafe43b1bc0d` · `discharge_summary` · `mni` · error=script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1
- `df61060159844e75aeafcafe43b1bc0d` · `referral_letter` · `mni` · error=script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1
- `df61060159844e75aeafcafe43b1bc0d` · `radiology_report` · `mni` · error=Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `433eba4ea24144438f7866160103b297` · `radiology_report` · `mr` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `6e943dc3578249e38b9e61705d0912a9` · `insurance_claim` · `sa` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `6e943dc3578249e38b9e61705d0912a9` · `hospital_billing` · `sa` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `0b19143502244d21a03f71ef838ab4ff` · `asha_worker_note` · `sat` · error=Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `0b19143502244d21a03f71ef838ab4ff` · `automated_sms` · `sat` · error=Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `0b19143502244d21a03f71ef838ab4ff` · `hospital_billing` · `sat` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `e899bd99966c4ac6b77d784bae3482f0` · `phc_register` · `sat` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `e899bd99966c4ac6b77d784bae3482f0` · `asha_worker_note` · `sat` · error=Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `e899bd99966c4ac6b77d784bae3482f0` · `insurance_claim` · `sat` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `825c4438c02440dc90d3ddec7ffec8ee` · `automated_sms` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `825c4438c02440dc90d3ddec7ffec8ee` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `insurance_claim` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `discharge_summary` · `sd` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `829db9fbfeda404d89ff9b8a405b5e4d` · `opd_slip` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `829db9fbfeda404d89ff9b8a405b5e4d` · `prescription` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `829db9fbfeda404d89ff9b8a405b5e4d` · `insurance_claim` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `ce942a5fb5644181ac0db94b6c9c1314` · `asha_worker_note` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `ce942a5fb5644181ac0db94b6c9c1314` · `automated_sms` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `ce942a5fb5644181ac0db94b6c9c1314` · `insurance_claim` · `ta` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `57a29898a6944b899059fb674d16f990` · `hospital_billing` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `57a29898a6944b899059fb674d16f990` · `discharge_summary` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `57a29898a6944b899059fb674d16f990` · `referral_letter` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `f0e00cbdb5dd4d33a122229e4883c598` · `hospital_billing` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `f0e00cbdb5dd4d33a122229e4883c598` · `discharge_summary` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `f0e00cbdb5dd4d33a122229e4883c598` · `referral_letter` · `te` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `6b15543bcd6545f5803d6887e2a48820` · `discharge_summary` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `6b15543bcd6545f5803d6887e2a48820` · `referral_letter` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `6b15543bcd6545f5803d6887e2a48820` · `radiology_report` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `bf0de98a0c63491c8877846b6f8dad65` · `discharge_summary` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `bf0de98a0c63491c8877846b6f8dad65` · `referral_letter` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
- `bf0de98a0c63491c8877846b6f8dad65` · `radiology_report` · `ur` · error=tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>
