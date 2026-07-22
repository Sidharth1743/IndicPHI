# Failures audit — `20260722T083050`

- **run status:** `failed`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260722T083050/pipeline.resolved.yaml`
- **issue count:** **177** (hard=1, gen_soft=1, tr_soft=37, judge=138, auditor=0)
- **S4 entity_coverage_complete_rate:** `0.9927536231884058`
- **S4b script_fail_count:** `7`
- **S5 pass_rate:** `0.0`
- **S6 pass_rate / passed:** `0.0` / `0`
- **curated docs:** `0`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| hard `s10_split` | — | — | — | 'eval_fraction_actual_docs' |
| S4 soft | `0fbde0cc3f544c77b260ef63a5a3a8d8` | `or` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4b soft | `8a02e74c7f104c1fa9f00b8507bac016` | `mni` | `radiology_report` | `Sarvam network error: <urlopen error [Errno -2] Name or service not known>` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `discharge_summary` | `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `radiology_report` | `Sarvam network error: <urlopen error [Errno -2] Name or service not known>` |
| S4b soft | `433eba4ea24144438f7866160103b297` | `mr` | `radiology_report` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `asha_worker_note` | `Sarvam network error: <urlopen error [Errno -2] Name or service not known>` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | `Sarvam network error: <urlopen error [Errno -2] Name or service not known>` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `phc_register` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | `Sarvam network error: <urlopen error [Errno -2] Name or service not known>` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `insurance_claim` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `opd_slip` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `prescription` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `insurance_claim` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `asha_worker_note` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `automated_sms` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `insurance_claim` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `57a29898a6944b899059fb674d16f990` | `te` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `57a29898a6944b899059fb674d16f990` | `te` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `57a29898a6944b899059fb674d16f990` | `te` | `referral_letter` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `hospital_billing` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `referral_letter` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `referral_letter` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `radiology_report` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `discharge_summary` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `referral_letter` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S4b soft | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `radiology_report` | `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not…` |
| S5 fail | `3a14ecc1de8648689a3311540c7cdd2e` | `as` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3a14ecc1de8648689a3311540c7cdd2e` | `as` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3a14ecc1de8648689a3311540c7cdd2e` | `as` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b55ee0c5013c4310a8939d0e6dd22e8d` | `as` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b55ee0c5013c4310a8939d0e6dd22e8d` | `as` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b55ee0c5013c4310a8939d0e6dd22e8d` | `as` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7cf3cf4f60be4edabe12ffd948079164` | `bn` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7cf3cf4f60be4edabe12ffd948079164` | `bn` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7cf3cf4f60be4edabe12ffd948079164` | `bn` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fdc875f657c1440c8e243a6845fb17a5` | `bn` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fdc875f657c1440c8e243a6845fb17a5` | `bn` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fdc875f657c1440c8e243a6845fb17a5` | `bn` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `a0e6acd7770d41b5812edc8bbfbda7ee` | `brx` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `a0e6acd7770d41b5812edc8bbfbda7ee` | `brx` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `a0e6acd7770d41b5812edc8bbfbda7ee` | `brx` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `29189dcea56e4d3d9df1aa7573656171` | `en` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `29189dcea56e4d3d9df1aa7573656171` | `en` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `29189dcea56e4d3d9df1aa7573656171` | `en` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `1f7da27d8fe544a191d7adc016e62971` | `gu` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `1f7da27d8fe544a191d7adc016e62971` | `gu` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `1f7da27d8fe544a191d7adc016e62971` | `gu` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `00930e6ff6e94bbfb1ce26958434c1af` | `hi` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `00930e6ff6e94bbfb1ce26958434c1af` | `hi` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `00930e6ff6e94bbfb1ce26958434c1af` | `hi` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7e1fefa3b81344778d2739efd7575c6c` | `hi` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7e1fefa3b81344778d2739efd7575c6c` | `hi` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7e1fefa3b81344778d2739efd7575c6c` | `hi` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `59e7e12eb3d44dfbacf8755ef02f52c7` | `kn` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `59e7e12eb3d44dfbacf8755ef02f52c7` | `kn` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `59e7e12eb3d44dfbacf8755ef02f52c7` | `kn` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `9a97560e03a846c8929c9b78a488affb` | `kn` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `9a97560e03a846c8929c9b78a488affb` | `kn` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `9a97560e03a846c8929c9b78a488affb` | `kn` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `25a8008cbebf4abda209c7d28427bb99` | `kok` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `25a8008cbebf4abda209c7d28427bb99` | `kok` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `25a8008cbebf4abda209c7d28427bb99` | `kok` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bfa3ca76f88b4b8f9ee3a47d5e04dae6` | `kok` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bfa3ca76f88b4b8f9ee3a47d5e04dae6` | `kok` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bfa3ca76f88b4b8f9ee3a47d5e04dae6` | `kok` | `phc_register` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `60ff3470cf8340efaa474e13896d8568` | `ks` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `60ff3470cf8340efaa474e13896d8568` | `ks` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `60ff3470cf8340efaa474e13896d8568` | `ks` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `885a67d0071948ac8a8336b278e81003` | `ks` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `885a67d0071948ac8a8336b278e81003` | `ks` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `885a67d0071948ac8a8336b278e81003` | `ks` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `07483932a3354f04a67c4b8846a2873f` | `mai` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `07483932a3354f04a67c4b8846a2873f` | `mai` | `phc_register` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `07483932a3354f04a67c4b8846a2873f` | `mai` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57bb67467d7c4747ac5af1eeb8f4a56a` | `mai` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57bb67467d7c4747ac5af1eeb8f4a56a` | `mai` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57bb67467d7c4747ac5af1eeb8f4a56a` | `mai` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `13f43defce4c471ba920ef1ff92efba0` | `ml` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `13f43defce4c471ba920ef1ff92efba0` | `ml` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `13f43defce4c471ba920ef1ff92efba0` | `ml` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `80435bdcef24479390d6e6ae0b2aeeb1` | `ml` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `80435bdcef24479390d6e6ae0b2aeeb1` | `ml` | `telemedicine_transcript` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `80435bdcef24479390d6e6ae0b2aeeb1` | `ml` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8a02e74c7f104c1fa9f00b8507bac016` | `mni` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8a02e74c7f104c1fa9f00b8507bac016` | `mni` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8a02e74c7f104c1fa9f00b8507bac016` | `mni` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `433eba4ea24144438f7866160103b297` | `mr` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `433eba4ea24144438f7866160103b297` | `mr` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `433eba4ea24144438f7866160103b297` | `mr` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `5c5a472d66774bdc9e232a4893422f0c` | `mr` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `5c5a472d66774bdc9e232a4893422f0c` | `mr` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `5c5a472d66774bdc9e232a4893422f0c` | `mr` | `er_triage_notes` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ca088f3e9d4400e893c3f00c17d4ff5` | `ne` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ca088f3e9d4400e893c3f00c17d4ff5` | `ne` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `3ca088f3e9d4400e893c3f00c17d4ff5` | `ne` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8d7895d6831e4b31956f868182103764` | `ne` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8d7895d6831e4b31956f868182103764` | `ne` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `8d7895d6831e4b31956f868182103764` | `ne` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0fbde0cc3f544c77b260ef63a5a3a8d8` | `or` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0fbde0cc3f544c77b260ef63a5a3a8d8` | `or` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0fbde0cc3f544c77b260ef63a5a3a8d8` | `or` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `67bf2f4af82d452db4c95cd1c7f59330` | `or` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `67bf2f4af82d452db4c95cd1c7f59330` | `or` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `67bf2f4af82d452db4c95cd1c7f59330` | `or` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7c5ed5ed53ea43189c76c8f6d4bef1a8` | `pa` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7c5ed5ed53ea43189c76c8f6d4bef1a8` | `pa` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `7c5ed5ed53ea43189c76c8f6d4bef1a8` | `pa` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b18798ffecf04ecc87455c46e724894f` | `pa` | `surgical_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b18798ffecf04ecc87455c46e724894f` | `pa` | `lab_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `b18798ffecf04ecc87455c46e724894f` | `pa` | `phc_register` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `phc_register` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `opd_slip` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `prescription` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `asha_worker_note` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `automated_sms` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `insurance_claim` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57a29898a6944b899059fb674d16f990` | `te` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57a29898a6944b899059fb674d16f990` | `te` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `57a29898a6944b899059fb674d16f990` | `te` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `hospital_billing` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `radiology_report` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `discharge_summary` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `referral_letter` | score=0.0 flags=['judge_network_error'] |
| S5 fail | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `radiology_report` | score=0.0 flags=['judge_network_error'] |

## Per-failure audit

### Hard stage failure 1: `s10_split`

- **error:** `'eval_fraction_actual_docs'`
- **started:** `2026-07-22T03:36:10.703785+00:00`
- **finished:** `2026-07-22T03:36:10.710284+00:00`

### S4 generation soft-fail 1

- **What:** generation soft-fail on `opd_slip` (`or`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ଅପରେସନ୍ ଟିପ୍ପଣୀ — [[HOSPITAL_NAME|Jajpur District Hospital]] ଭର୍ତ୍ତି [[ADMISSION_NUMBER|ADM-2024-0815-001]] ୱାର୍ଡ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Sushila Devi]] [[AGE|25]] [[GENDER|Female]] ଶଲ୍ୟ ଚିକିତ୍ସକ [[DOCTOR_NAME|Dr. Ramesh Patnaik]]
ପ୍ରକ୍ରିୟା: ଜରୁରୀକାଳୀନ ଲାପାରୋସ୍କୋପିକ୍ ଆପେଣ୍ଡେକ୍ଟୋମି
ନିଶ୍ଚେତକ: ସାଧାରଣ ନିଶ୍ଚେତକ
ଅସ୍ତ୍ରୋପଚାର ପୂର୍ବ ରୋଗ ନିରୂପଣ: ତୀବ୍ର ଆପେଣ୍ଡିସାଇଟିସ୍
ଅସ୍ତ୍ରୋପଚାର ପରବର୍ତ୍ତୀ ରୋଗ ନିରୂପଣ: ତୀବ୍ର ଆପେଣ୍ଡିସାଇଟିସ୍ ସହିତ ଛିଦ୍ର
ପର୍ଯ୍ୟବେକ୍ଷଣ: ଆପେଣ୍ଡିକ୍ସରେ ଶେଷରେ 2cm ଛିଦ୍ର ଥିଲା। ପେରିଟୋନାଇଟିସ୍‌ର କୌଣସି ପ୍ରମାଣ ନାହିଁ। ଆପେଣ୍ଡେକ୍ଟୋମି ସଫଳତାର ସହ କରାଯାଇଥିଲା।
ରୋଗୀ ପ୍ରକ୍ରିୟାକୁ ଭଲ ଭାବରେ ସହ୍ୟ କଲେ। ଅନୁମାନି…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `radiology_report` (`mni`).
- **Error:** `Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Leima Devi Leishangthem]] DOB [[DOB|1945-03-15]] [[AGE|79]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-0315]] Ward [[WARD_NUMBER|B1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Sharma]] | Course / advice: Patient admitted with pulmonary tuberculosis complicated by type 2 diabetes mellitus and hype…
```
- **Translated preview:**

```
ꯗꯤꯁꯆꯥꯔꯖ ꯁꯝꯃꯔꯤ — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Leima Devi Leishangthem]] ꯄꯣꯛꯄꯒꯤ ꯆꯍꯤ [[DOB|1945-03-15]] [[AGE|79]] [[GENDER|Female]]
ꯑꯦꯗꯃꯤꯠ [[ADMISSION_NUMBER|ADM-2024-0315]] ꯋꯥꯔꯗ [[WARD_NUMBER|B1]] ꯕꯦꯗ [[BED_NUMBER|05]]
ꯗꯣꯛꯇꯔ [[DOCTOR_NAME|Dr. Rajesh Sharma]] | ꯀꯣꯔꯁ / ꯄꯥꯎꯇꯥꯛ: ꯄꯜꯃꯣꯅꯔꯤ ꯇ꯭ꯌꯨꯕꯔꯀꯨꯂꯣꯁꯤꯁ ꯇꯥꯏꯞ 2 ꯗꯥꯏꯕꯤꯇꯤꯁ ꯃꯦꯂꯤꯇꯁ ꯑꯃꯁꯨꯡ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟꯅ ꯀꯝꯞꯂꯤꯀꯦꯠ ꯇꯧꯔꯕ ꯄꯦꯁꯤꯑꯦꯟꯠ …
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] DOB [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice: Patient underwent emergency appendectomy on 12th March 2024 at 02:30 hours for acute appendicitis. Procedure was …
```
- **Translated preview:**

```
থোকপা মশিং তাকপা — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] জন্ম তারিখ [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Admission [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Doctor [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice:
রোগীনা ১২ মার্চ ২০২৪ তারিখ ০২:৩০ ঘণ্টায় তীব্র অ্যাপেন্ডিসাইটিসৰ বাবে জরুরি অ্যাপেন্ডেক্টমি করখি।…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] DOB [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice: Patient underwent emergency appendectomy on 12th March 2024 at 02:30 hours for acute appendicitis. Procedure was …
```
- **Translated preview:**

```
থোকপা মশিং তাকপা — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] জন্ম তারিখ [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Admission [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Doctor [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice:
রোগীনা ১২ মার্চ ২০২৪ তারিখ ০২:৩০ ঘণ্টায় তীব্র অ্যাপেন্ডিসাইটিসৰ বাবে জরুরি অ্যাপেন্ডেক্টমি করখি।…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `radiology_report` (`mni`).
- **Error:** `Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] DOB [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice: Patient underwent emergency appendectomy on 12th March 2024 at 02:30 hours for acute appendicitis. Procedure was …
```
- **Translated preview:**

```
থোকপা মশিং তাকপা — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] জন্ম তারিখ [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Admission [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Doctor [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice:
রোগীনা ১২ মার্চ ২০২৪ তারিখ ০২:৩০ ঘণ্টায় তীব্র অ্যাপেন্ডিসাইটিসৰ বাবে জরুরি অ্যাপেন্ডেক্টমি করখি।…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `radiology_report` (`mr`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College, Hingoli]]
[[PATIENT_NAME|Ramesh Patil]] DOB [[DOB|1957-03-15]] [[AGE|67]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0412]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] | Course / advice: Patient presents with major depressive disorder with anxious distress. Symptoms include persistent low …
```
- **Translated preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|Government Medical College, Hingoli]]
[[PATIENT_NAME|Ramesh Patil]] DOB [[DOB|1957-03-15]] [[AGE|67]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0412]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] | उपचार / मार्गदर्शन: रुग्ण अस्वस्थतेसह मोठ्या नैराश्य विकारासह येतो. लक्षणांमध्ये सतत कमी मनस्थिती, ॲनहेडोनिया, झोपेत अडथळे …
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `insurance_claim` (`sa`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Rohan Kumar]], your TB follow-up appointment is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] on 15-May at 10:30 AM with [[DOCTOR_NAME|Dr. Amit Singh]]. Please bring your [[MRN|MRN-2024-0815-001]] and arrive 15 minutes early. Contact us at [[PHONE_NUMBER|9876543210]] for any queries. Appointment ID: [[APPOINTMENT_ID|APT-240515-01]].
```
- **Translated preview:**

```
प्रिय [[PATIENT_NAME|Rohan Kumar]], भवतः क्षयरोग-अनुवर्ती-नियुक्तिः [[HOSPITAL_NAME|District Hospital Kanpur]] दिनाङ्के 15-मै प्रातः 10:30 वादने [[DOCTOR_NAME|Dr. Amit Singh]] इत्यनेन सह नियोजिता अस्ति। कृपया स्वकीयं [[MRN|MRN-2024-0815-001]] आनयन्तु आगत्य 15 निमेषान् पूर्वम्। कस्यापि प्रश्नाय [[PHONE_NUMBER|9876543210]] सम्पर्कं कुर्वन्तु। नियुक्ति-परिचयः: [[APPOINTMENT_ID|APT-240515-01]]।
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `hospital_billing` (`sa`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Rohan Kumar]], your TB follow-up appointment is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] on 15-May at 10:30 AM with [[DOCTOR_NAME|Dr. Amit Singh]]. Please bring your [[MRN|MRN-2024-0815-001]] and arrive 15 minutes early. Contact us at [[PHONE_NUMBER|9876543210]] for any queries. Appointment ID: [[APPOINTMENT_ID|APT-240515-01]].
```
- **Translated preview:**

```
प्रिय [[PATIENT_NAME|Rohan Kumar]], भवतः क्षयरोग-अनुवर्ती-नियुक्तिः [[HOSPITAL_NAME|District Hospital Kanpur]] दिनाङ्के 15-मै प्रातः 10:30 वादने [[DOCTOR_NAME|Dr. Amit Singh]] इत्यनेन सह नियोजिता अस्ति। कृपया स्वकीयं [[MRN|MRN-2024-0815-001]] आनयन्तु आगत्य 15 निमेषान् पूर्वम्। कस्यापि प्रश्नाय [[PHONE_NUMBER|9876543210]] सम्पर्कं कुर्वन्तु। नियुक्ति-परिचयः: [[APPOINTMENT_ID|APT-240515-01]]।
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss of 5 kg. She reports occasional shortness of breath and night sweats. Blood press…
```
- **Translated preview:**

```
ASHA Karya Patra — Gaon [[VILLAGE|Baidpur]], Jila [[DISTRICT|Dumka]]
Labharthi [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Bhraman Phal: Rogi dekhay lagatar khansi tin hapta se, kam jwar, aur 5 kg vajan kam hona. Unhe batate hain kabhi-kabhi saans phoolna aur raat ko paseena aana. Rakt chapa 145/90 mmHg li…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `automated_sms` (`sat`).
- **Error:** `Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss of 5 kg. She reports occasional shortness of breath and night sweats. Blood press…
```
- **Translated preview:**

```
ASHA Karya Patra — Gaon [[VILLAGE|Baidpur]], Jila [[DISTRICT|Dumka]]
Labharthi [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Bhraman Phal: Rogi dekhay lagatar khansi tin hapta se, kam jwar, aur 5 kg vajan kam hona. Unhe batate hain kabhi-kabhi saans phoolna aur raat ko paseena aana. Rakt chapa 145/90 mmHg li…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `hospital_billing` (`sat`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss of 5 kg. She reports occasional shortness of breath and night sweats. Blood press…
```
- **Translated preview:**

```
ASHA Karya Patra — Gaon [[VILLAGE|Baidpur]], Jila [[DISTRICT|Dumka]]
Labharthi [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Bhraman Phal: Rogi dekhay lagatar khansi tin hapta se, kam jwar, aur 5 kg vajan kam hona. Unhe batate hain kabhi-kabhi saans phoolna aur raat ko paseena aana. Rakt chapa 145/90 mmHg li…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `phc_register` (`sat`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```
- **Translated preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```
- **Translated preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```
- **Translated preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathban…
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `automated_sms` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `insurance_claim` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 18

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 19

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 20

- **What:** translation soft-fail on `opd_slip` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```

### S4b translation soft-fail 21

- **What:** translation soft-fail on `prescription` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```

### S4b translation soft-fail 22

- **What:** translation soft-fail on `insurance_claim` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NU…
```

### S4b translation soft-fail 23

- **What:** translation soft-fail on `asha_worker_note` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```

### S4b translation soft-fail 24

- **What:** translation soft-fail on `automated_sms` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```

### S4b translation soft-fail 25

- **What:** translation soft-fail on `insurance_claim` (`ta`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest i…
```

### S4b translation soft-fail 26

- **What:** translation soft-fail on `hospital_billing` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```
- **Translated preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```

### S4b translation soft-fail 27

- **What:** translation soft-fail on `discharge_summary` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```
- **Translated preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```

### S4b translation soft-fail 28

- **What:** translation soft-fail on `referral_letter` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```
- **Translated preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AAB…
```

### S4b translation soft-fail 29

- **What:** translation soft-fail on `hospital_billing` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```

### S4b translation soft-fail 30

- **What:** translation soft-fail on `discharge_summary` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```

### S4b translation soft-fail 31

- **What:** translation soft-fail on `referral_letter` (`te`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>;post_repair_translate:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|06…
```

### S4b translation soft-fail 32

- **What:** translation soft-fail on `discharge_summary` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```

### S4b translation soft-fail 33

- **What:** translation soft-fail on `referral_letter` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```

### S4b translation soft-fail 34

- **What:** translation soft-fail on `radiology_report` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum …
```

### S4b translation soft-fail 35

- **What:** translation soft-fail on `discharge_summary` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```

### S4b translation soft-fail 36

- **What:** translation soft-fail on `referral_letter` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```

### S4b translation soft-fail 37

- **What:** translation soft-fail on `radiology_report` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Sarvam network error: <urlopen error [Errno -2] Name or service not known>`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 202…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `surgical_note` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
অপাৰেটিভ নোট — [[HOSPITAL_NAME|Tinsukia District Hospital]] ভৰ্তি [[ADMISSION_NUMBER|ADM-2024-0815-001]] ৱাৰ্ড [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Anjali Borah]] [[AGE|22]] [[GENDER|Female]] শল্য চিকিৎসক [[DOCTOR_NAME|Dr. Priyanka Sharma]]
পদ্ধতি / ফলাফল:
ৰোগীজনীৰ বাবে নিৰ্বাচিত নিম্ন ট্ৰেন্সভাৰ্ছ চিজেৰিয়ান চেক্সনৰ পৰামৰ্শ লোৱা হৈছিল গৰ্ভধাৰণৰ 39 সপ্তাহত ব্ৰীচ প্ৰেজেণ্টেচনৰ বাবে। অস্ত্ৰোপচাৰৰ পূৰ্বৰ মূল্যায়নত স্বাভাৱিক ভাইটেলছ, পৰ্যাপ্ত হিম’গ্লবিনৰ মাত্ৰা আৰু কোনো বিৰোধিতা পোৱা নগ’ল। জটিলতা নোহ…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `lab_report` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
পৰীক্ষাগাৰৰ প্ৰতিবেদন — [[HOSPITAL_NAME|Tinsukia Civil Hospital]] জিলা [[DISTRICT|Tinsukia]]
MRN [[MRN|MRN-AS-2024-0815]] ৰোগীৰ পৰিচয় পত্ৰ [[PATIENT_ID|PID-AS-7781]]
[[PATIENT_NAME|Rina Borah]] [[AGE|22]] [[GENDER|Female]] ফোন [[PHONE_NUMBER|9876543210]]
দ্বাৰা নিৰ্দেশিত [[DOCTOR_NAME|Dr. Sanjay Sharma]]
তাৰিখ: 15 August 2024

ক্লিনিকেল বিৱৰণ:
ৰোগীয়ে যোৱা 5 দিন ধৰি ভাগৰ, সামান্য জ্বৰ আৰু গোটেই শৰীৰৰ বিষৰ অভিযোগ কৰিছে। পূৰ্বৰ কোনো গুৰুত্বপূৰ্ণ চিকিৎসা ইতিহাস নাই। ৰোগী এগৰাকী গৃহিণী, বিবাহিত, প…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `opd_slip` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
OPD স্লিপ | [[HOSPITAL_NAME|Tinsukia Civil Hospital]] | ID [[HOSPITAL_ID|THC-001]]
ৰোগী: [[PATIENT_NAME|Jonaki Gogoi]] | জন্মৰ তাৰিখ [[DOB|1999-05-20]] | বয়স: [[AGE|22]] | লিংগ: [[GENDER|Female]]
বৃত্তি: [[OCCUPATION|Homemaker]] | MRN: [[MRN|OPD-2024-TNS-001]]
চিকিৎসক: [[DOCTOR_NAME|Dr. Bhabani Barua]]
আত্মীয়: [[RELATIVE_NAME|Pranjal Sharma]] | ফোন: [[PHONE_NUMBER|9876543210]]
পঞ্জীয়ক কৰ্মচাৰী ID: [[EMPLOYEE_ID|REG-0042]] | জিলা: [[DISTRICT|Tinsukia]]
মুখ্য অভিযোগ: ৩ সপ্তাহ ধৰি নিম্ন-স্তৰৰ জ…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `surgical_note` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
অস্ত্ৰোপচাৰ টোকা — [[HOSPITAL_NAME|আসাম চিকিৎসা মহাবিদ্যালয়]] অস্ত্ৰোপচাৰ কক্ষ ৱাৰ্ড [[WARD_NUMBER|OT-3]] [[ADMISSION_NUMBER|ADM-2024-0815]] [[PATIENT_NAME|প্ৰীতি বৰা]] [[AGE|27]] [[GENDER|Female]] শল্য চিকিৎসক [[DOCTOR_NAME|ডাঃ ৰাজেন শৰ্মা]] [[MRN|MRN-2024-0815-001]] [[PATIENT_ID|PID-78451]] [[BED_NUMBER|12]] [[RELATIVE_NAME|মাক]]

ৰোগীগৰাকী এগৰাকী 27 বছৰীয়া মহিলা কৃষক, নগাঁও জিলাৰ, যিয়ে সোঁ ডিঙিৰ অংশত 3 মাহৰ বিষহীন ফুলাৰ ইতিহাসৰ সৈতে উপস্থাপন কৰিছে। ফাইন নিডল এছপিৰেচন চাইট’লজীয়ে কেচিয়েটি…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `lab_report` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|Mina Boro]] [[AGE|27]] [[GENDER|Female]] ফোন [[PHONE_NUMBER|9876543210]]
[[HOSPITAL_NAME|Nagaon Civil Hospital]] জিলা [[DISTRICT|Nagaon]]
MRN [[MRN|MRN-AS-2024-0815]] ৰোগীৰ পৰিচয় পত্ৰ [[PATIENT_ID|PID-AS-7781]]
নিৰ্দেশ দিছে [[DOCTOR_NAME|Dr. Anjali Sharma]]
নমুনা সংগ্ৰহৰ তাৰিখ: ১৫ আগষ্ট ২০২৪

পৰীক্ষাগাৰৰ প্ৰতিবেদন

ৰোগীৰ বিৱৰণ:
নাম: [[PATIENT_NAME|Mina Boro]]
বয়স: [[AGE|27]]
লিংগ: [[GENDER|Female]]
MRN: [[MRN|MRN-AS-2024-0815]]
ৰোগীৰ পৰিচয় পত্ৰ: [[PATIENT_ID|PID-AS-7781]]
ফোন:…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `opd_slip` (`as`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
বহিঃবিভাগীয় স্লিপ | [[HOSPITAL_NAME|Nagaon Civil Hospital]] | ID [[HOSPITAL_ID|NCH-001]]
ৰোগী: [[PATIENT_NAME|Bina Boro]] | জন্মৰ তাৰিখ [[DOB|1997-05-15]] | বয়স: [[AGE|27]] | লিংগ: [[GENDER|Female]]
বৃত্তি: [[OCCUPATION|Cultivator]] | MRN: [[MRN|MRN-2024-0515-001]] | চিকিৎসক: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
আত্মীয়: [[RELATIVE_NAME|Jadab Boro]] | ফোন: [[PHONE_NUMBER|9876543210]]
পঞ্জীয়ক কৰ্মচাৰী ID: [[EMPLOYEE_ID|EMP-4521]] | জিলা: [[DISTRICT|Nagaon]]
মুখ্য অভিযোগ: ৩ দিনৰ বাবে জ্বৰ আৰু শৰীৰ…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `opd_slip` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
বহির্বিভাগ স্লিপ | [[HOSPITAL_NAME|Karimganj District Hospital]] | আই.ডি. [[HOSPITAL_ID|KDH-2024-001]]
রোগী: [[PATIENT_NAME|Hanik Haq]] | জন্ম তারিখ [[DOB|1973-05-15]] | বয়স: [[AGE|51]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Screener, Mica]] | এম.আর.এন: [[MRN|MRN-KDH-2024-051]] | চিকিৎসক: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
আত্মীয়: [[RELATIVE_NAME|Firoz Haq]] | ফোন: [[PHONE_NUMBER|9876543210]]
রেজিস্ট্রার এম্পি.আই.ডি: [[EMPLOYEE_ID|EMP-KDH-023]] | জেলা: [[DISTRICT|Karimganj]]
প্রধান অভিযোগ:…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `surgical_note` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
অপারেশন রিপোর্ট — [[HOSPITAL_NAME|মেট্রোপলিটন জেনারেল হাসপাতাল]] ভর্তি [[ADMISSION_NUMBER|ADM-2024-0815]] ওয়ার্ড [[WARD_NUMBER|OT-3]]
[[PATIENT_NAME|রাহুল শর্মা]] [[AGE|51]] [[GENDER|Male]] সার্জন [[DOCTOR_NAME|ডাঃ অনির্বাণ ব্যানার্জি]]
পদ্ধতি / ফলাফল:
রোগী ৩ মাস ধরে দীর্ঘস্থায়ী কাশি, ওজন হ্রাস এবং হেমোপ্টিসিস নিয়ে উপস্থিত হয়েছিলেন। বুকের এক্স-রে ডান উপরের লোবে ক্যাভিটারি লিশন দেখিয়েছে। কফ AFB পজিটিভ। সিটি স্ক্যান পার্শ্ববর্তী কনসোলিডেশন সহ ৪.৫ সেমি ক্যাভিটারি লিশন প্রকাশ করেছে। পোস্টেরোল্…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `prescription` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
প্রেসক্রিপশন — [[HOSPITAL_NAME|হাসপাতালে_নাম]]
রোগী [[PATIENT_NAME|রোগীর_নাম]], [[AGE|51]] / [[GENDER|Male]], এম.আর.এন [[MRN|RX-2024-0915-001]]
ডঃ [[DOCTOR_NAME|ডাক্তারের_নাম]]
ফোন: [[PHONE_NUMBER|9876543210]]
ঠিকানা: [[RESIDENTIAL_ADDRESS|আবাসিক_ঠিকানা]]
জেলা: [[DISTRICT|জেলা]]
রোগীর_আইডি: [[PATIENT_ID|PID-KH-2024-001]]
আভা_আইডি: [[ABHA_ID|1234-5678-9012-3456]]

রোগনির্ণয়: তীব্র অ্যাপেন্ডিসাইটিস, সিটি স্ক্যান দ্বারা নিশ্চিত করা হয়েছে
পদ্ধতি: ল্যাপারোস্কোপিক অ্যাপেন্ডেক্টমি সম্পন্ন হয়েছে 15 …
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `surgical_note` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
অপারেশন রিপোর্ট — [[HOSPITAL_NAME|সিটি হাসপাতাল]] ভর্তি [[ADMISSION_NUMBER|ADM-2024-0915]] ওয়ার্ড [[WARD_NUMBER|Surgical]]
[[PATIENT_NAME|রাহুল শর্মা]] [[AGE|44]] [[GENDER|Female]] সার্জন [[DOCTOR_NAME|ডা. অঞ্জলি সেন]]
পদ্ধতি / ফলাফল:
রোগীর ২৪ ঘণ্টার জন্য জ্বর এবং বমির সাথে তীব্র ডানদিকের নিচের পেটে ব্যথা ছিল। পরীক্ষায় McBurney's point-এ স্পর্শ করলে ব্যথা এবং পেশি শক্ত হয়ে থাকা দেখা গেছে। আল্ট্রাসাউন্ডে ৮ মিমি ব্যাস এবং চারপাশের তরল জমাটবদ্ধতা সহ প্রদাহযুক্ত অ্যাপেন্ডিক্স দেখা গেছে। সাধারণ অ…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `opd_slip` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ও.পি.ডি স্লিপ | [[HOSPITAL_NAME|South 24 Parganas District Hospital]] | আইডি [[HOSPITAL_ID|S24P-DH-001]]
রোগী: [[PATIENT_NAME|Sujata Mondal]] | জন্ম তারিখ [[DOB|1980-07-22]] | বয়স: [[AGE|44]] | লিঙ্গ: [[GENDER|Female]]
পেশা: [[OCCUPATION|Sales Supervisor, Retail Trade]] | এম.আর.এন: [[MRN|OPD-2024-0892]] | চিকিৎসক: [[DOCTOR_NAME|Dr. Amit Kumar]]
আত্মীয়: [[RELATIVE_NAME|Bijoy Mondal]] | ফোন: [[PHONE_NUMBER|9876543210]]
রেজিস্ট্রার এম্পিআইডি: [[EMPLOYEE_ID|EMP-4412]] | জেলা: [[DISTRICT|South Twe…
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `lab_report` (`bn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ল্যাব রিপোর্ট
হাসপাতাল_নাম [[HOSPITAL_NAME|S.S.K.M. Hospital]]
জেলা [[DISTRICT|South Twenty Four Parganas]]
রোগীর_নাম [[PATIENT_NAME|Rashmi Mondal]]
বয়স [[AGE|44]]
লিঙ্গ [[GENDER|Female]]
এম.আর.এন [[MRN|MRN-WB-2024-0815]]
রোগী_আইডি [[PATIENT_ID|PID-WB-7781]]
ফোন_নম্বর [[PHONE_NUMBER|9876543210]]
ডাক্তার_নাম [[DOCTOR_NAME|Dr. Anirban Chatterjee]]

সংগ্রহের তারিখ: 2024-05-20

পরীক্ষার ফলাফল
--------------------------------------------------------------------------------
| অ্যানালাইট            |…
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `opd_slip` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बाह्य रोगी विभाग (OPD) पर्ची | [[HOSPITAL_NAME|Baksa District Hospital]] | ID [[HOSPITAL_ID|BDH-001]]
बिरामी: [[PATIENT_NAME|Rina Boro]] | [[DOB|[[DOB|1994-02-15]]]] | [[AGE|[[AGE|30]]]] | [[GENDER|[[GENDER|Female]]]] | [[OCCUPATION|Hawker]] | [[MRN|[[MRN|BDH-2024-0156]]]] | [[DOCTOR_NAME|Dr. Priyanka Das]] | [[RELATIVE_NAME|Binita Boro]] | [[PHONE|[[PHONE_NUMBER|9876543210]]]] | [[REGISTRAR_EMPID|[[EMPLOYEE_ID|EMP-2024-087]]]] | [[DISTRICT|Baksa]]

मुख्य शिकायत: बिरामीलाई पछिल्लो ३ महिनादेखि न…
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `prescription` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|Baksa Civil Hospital]]
रोगी [[PATIENT_NAME|Jalali Boro]], [[AGE|30]] / [[GENDER|Female]], MRN [[MRN|RX-BAK-2024-001]]
डाक्टर [[DOCTOR_NAME|Dr. Rina Kalita]]
तारीख: 2024-05-21
[[PHONE_NUMBER|9875432109]]
[[DISTRICT|Baksa]]
[[RESIDENTIAL_ADDRESS|Village: Goroimari, P.O. Goroimari, Baksa, Assam]]
[[PATIENT_ID|PID-BAK-3001]]
[[ABHA_ID|12-3456-7890-1234]]

मुख्य शिकायत: दोन दिनको ज्वर र देहा सानाय।

वर्तमान बीमारीको इतिहास: रोगी लगभग 102°F को गंभीर ज्वर लिएर आएकी छिन्, जसमा …
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-AS-2024-4567]]
[[PATIENT_NAME|Rina Boro]] [[AGE|30]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|239847561023]]
हस्पताल [[HOSPITAL_NAME|Baksa District Civil Hospital]] जिला [[DISTRICT|Baksa]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|AS01AB1234]] (एक बार मात्र)।
पॅन [[PAN_NUMBER|BOKRB1234C]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30912345678901]]

मरीज रीना बोरो, 30 बर्षकी महिला फेरीवाला बक्ससा जिलाबाट 28 हप्ताको गर्भकालमा नियमित प्रस…
```

### S5 judge fail 16

- **What:** linguistic judge **fail** on `surgical_note` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
शल्यक्रिया विवरण — [[HOSPITAL_NAME|Sonitpur District Hospital]] भर्ना [[ADMISSION_NUMBER|ADM-2024-0912]] वार्ड [[WARD_NUMBER|B2]]
[[PATIENT_NAME|Bina Boro]] [[AGE|71]] [[GENDER|Female]] शल्यचिकित्सक [[DOCTOR_NAME|Dr. Rajiv Sharma]]
प्रक्रिया / निष्कर्ष:
रोगी गंभीर उपचार-प्रतिरोधी गंभीर अवसाद विकार मनोविकृति लक्षण सहित प्रस्तुत भेल छल। औषधि-चिकित्सा आ मनोचिकित्साक कएकटा विफल प्रयासक बाद, मानक प्रोटोकॉलक अनुसार इलेक्ट्रोकन्वल्सिव थेरेपी (ECT) शुरू कयल गेल। शल्यक्रिया-पूर्व मूल्यांकनमे सामान्य जीव…
```

### S5 judge fail 17

- **What:** linguistic judge **fail** on `lab_report` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्रयोगशाला रिपोर्ट — [[HOSPITAL_NAME|Sonitpur Civil Hospital]] जिला [[DISTRICT|Sonitpur]]
MRN [[MRN|MRN-AS-2024-0715-001]] रोगी ID [[PATIENT_ID|PID-AS-7101]]
[[PATIENT_NAME|Mina Boro]] [[AGE|71]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
[[DOCTOR_NAME|Dr. Anjali Sharma]] द्वारा आदेशित

रोगी का नाम: मीना बोरो
आयु: 71 वर्ष
लिंग: महिला
रिपोर्ट की तिथि: 15 जुलाई 2024
संदर्भित चिकित्सक: डॉ. अंजलि शर्मा

मुख्य शिकायत: पिछले दो हफ्तों से पूरे शरीर में दर्द और थकान।

वर्तमान बीमारी का इतिहास: र…
```

### S5 judge fail 18

- **What:** linguistic judge **fail** on `prescription` (`brx`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|जिला अस्पताल]]
रोगी [[PATIENT_NAME|राम सिंह]], [[AGE|71]] / [[GENDER|Female]], MRN [[MRN|MRN-AS-2024-001]], [[PATIENT_ID|PID-AS-001]], [[ABHA_ID|12-3456-7890-1234]]
नि थाग्रा [[RESIDENTIAL_ADDRESS|गां, पिन-123456]], [[DISTRICT|कोकराझार]]
सम्पर्क: [[PHONE_NUMBER|9875432109]]
डाक्टर [[DOCTOR_NAME|डा. बी. बरगोहाइन]]

Rx:
गहन चरण (2 महिना):
 - Isoniazid 300mg दिनैसेयाव खेबसे
 - Rifampicin 600mg दिनैसेयाव खेबसे
 - Pyrazinamide 1500mg दिनैसेयाव खेबसे
 - Ethambutol 800mg दिनैस…
```

### S5 judge fail 19

- **What:** linguistic judge **fail** on `opd_slip` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बाह्य रोगी पर्ची | [[HOSPITAL_NAME|District Hospital Kathua]] | आई डी [[HOSPITAL_ID|DH-JK-001]]
रोगी: [[PATIENT_NAME|Anuradha Devi]] | जन्म तिथि [[DOB|1986-05-15]] | आयु: [[AGE|38]] | लिंग: [[GENDER|Female]]
पेशे: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
संबंधित: [[RELATIVE_NAME|Ramesh Kumar]] | फोन: [[PHONE_NUMBER|9419876543]]
रजिस्ट्रार कर्मचारी आईडी: [[EMPLOYEE_ID|EMP-2024-001]] | जिला: [[DISTRICT|Kathua]]

मुख्य शिकायत: पिछले …
```

### S5 judge fail 20

- **What:** linguistic judge **fail** on `prescription` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|District Hospital Kathua]]
मरीज [[PATIENT_NAME|Anuradha Devi]], [[AGE|38]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-001]]
डाक्टर [[DOCTOR_NAME|Dr. Rajesh Kumar]]
फोन: [[PHONE_NUMBER|9876543210]]
पता: [[RESIDENTIAL_ADDRESS|Village Nagri, Tehsil Hiranagar, Kathua]]
ABHA: [[ABHA_ID|12-3456-7890-1234]]
मरीज ID: [[PATIENT_ID|PID-2024-001]]
जिला: [[DISTRICT|Kathua]]

नुस्खा:
1. Paracetamol 500mg - 1 टैबलेट दिन च दो बारी खाना खाने दे बाद बुखार ते शरीर दे दर्द लेई
2. Azithromyci…
```

### S5 judge fail 21

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA दावा — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
दावेदार [[PATIENT_NAME|Anuradha Devi]] [[AGE|38]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|238745619012]]
अस्पताल [[HOSPITAL_NAME|District Hospital Kathua]] जिला [[DISTRICT|Kathua]]
[[BANK_ROUTING_NUMBER|123456789]]
मोटर / आर टी ए वाहन [[VEHICLE_REGISTRATION|JK02D-456789]] (सिर्फ इक बारी)।
पैन [[PAN_NUMBER|JKPAB1234C]] आई एफ एस सी [[IFSC_CODE|SBIN0005678]] खाता [[BANK_ACCOUNT_NUMBER|002345678901]]
[[CREDIT_CARD_NUMBER|512345678901234…
```

### S5 judge fail 22

- **What:** linguistic judge **fail** on `asha_worker_note` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
आशा वर्कर नोट — गाँव [[VILLAGE|Jammu Urban]], ज़िला [[DISTRICT|Jammu]]
लाभार्थी [[PATIENT_NAME|Shanti Devi]], [[AGE|48]] / [[GENDER|Female]]
आशा वर्कर: [[ASHA_WORKER_NAME|Kamla Kumari]] | फोन [[PHONE_NUMBER|9419876543]]
भेंट दे नतीजे: मरीज दस्सदा ऐ जे पिछले दो हफ्तें शा बधदी होई घबराहट ते नींद च खलल ऐ। ओह् दस्सदी ऐ जे घर दे कम्मै दे बोझ करी दबे दा महसूस करदी ऐ ते अपनी मानसिक सेहत दी चिंता ज़ाहर करदी ऐ।

[[RELATIVE_NAME|Ramesh Kumar]] (पति) भेंट दे दौरान मजूद हा। [[BPL_RATION_CARD|BPL-JK-2024-00…
```

### S5 judge fail 23

- **What:** linguistic judge **fail** on `automated_sms` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|रवि कुमार]]: अपॉइंटमेंट [[APPOINTMENT_ID|APT-240615-02]] पर [[HOSPITAL_NAME|गवर्नमेंट सिविल हॉस्पिटल]] पर 15-जून 10:30 डॉ. [[DOCTOR_NAME|डॉ. शर्मा]] के साथ। MRN [[MRN|MRN-JMC-2024-045]]। पुष्टि करो पर [[PHONE_NUMBER|9419234567]]।
```

### S5 judge fail 24

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA claim — बीमा पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
[[PATIENT_NAME|रमेश कुमार]] [[AGE|48]] [[GENDER|Female]] [[MRN|GMCJ-2024-0456]] Aadhaar [[AADHAAR_NUMBER|203835321155]]
Hospital [[HOSPITAL_NAME|शिमला अस्पताल]] जिला [[DISTRICT|शिमला जिला]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|JK02AB1234]] (सिर्फ इक बारी)।
PAN [[PAN_NUMBER|JKPAB1234C]] IFSC [[IFSC_CODE|SBIN0005678]] खाता [[BANK_ACCOUNT_NUMBER|0078901234567]] [[BANK_ROUTING_NUMBER|123456789012]]

मरीज ने दस्सेआ जे 3 महीने तक्…
```

### S5 judge fail 25

- **What:** linguistic judge **fail** on `radiology_report` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Radiology report — [[HOSPITAL_NAME|Chitradurga District Hospital]] | [[PATIENT_NAME|Savitri Bai]] [[AGE|59]] [[GENDER|Female]]
MRN [[MRN|MRN-CHIT-2024-001]] Encounter [[ENCOUNTER_ID|ENC-CHIT-2024-0815-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Kavita Reddy]]
Findings: Plain radiograph of the right lower limb demonstrates a well-defined, lytic lesion in the distal femur, measuring approximately 4.5 x 3.8 cm, with a thin sclerotic rim. No periosteal reaction or soft tissue mass is identified. The l…
```

### S5 judge fail 26

- **What:** linguistic judge **fail** on `er_triage_notes` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Chitradurga District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Savitri Bai]] [[AGE|59]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Arrived by ambulance [[VEHICLE_REGISTRATION|KA01AB1234]]
Relative [[RELATIVE_NAME|Ramesh]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Ramesh Kumar]]
Vitals: BP 140/90, Pulse 98, Temp 101.2°F, RR 20, SpO2 96% on room air. Patient appears anxious, pale, diaphoretic.

Chief compla…
```

### S5 judge fail 27

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|Lakshmi Bai]] [[AGE|59]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-2024-0815-001]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|lakshmi.bai@example.com]] Hospital [[HOSPITAL_NAME|Chitradurga District Hospital]]
--- chat ---
Patient: Good morning doctor. I have been having a persis…
```

### S5 judge fail 28

- **What:** linguistic judge **fail** on `radiology_report` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Radiology Report — [[HOSPITAL_NAME|Kasturba Medical College Hospital]] | [[PATIENT_NAME|Shanthi Shetty]] [[AGE|45]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Priya Nair]]
Findings: Bilateral breast ultrasound reveals a 2.3 cm irregular hypoechoic mass in the left upper outer quadrant with spiculated margins and posterior acoustic shadowing. The mass demonstrates increased vascularity on Doppler evaluation. No suspicio…
```

### S5 judge fail 29

- **What:** linguistic judge **fail** on `er_triage_notes` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|KMC Hospital Mangalore]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Shanthi Shetty]] [[AGE|45]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|ER-05]]
Arrived by ambulance [[VEHICLE_REGISTRATION|KA-19-AB-1234]]
Relative [[RELATIVE_NAME|Shetty]] Phone [[PHONE_NUMBER|9880123456]] Dr [[DOCTOR_NAME|Dr. Ramesh Pai]]
Vitals / acuity: Patient presents with persistent cough for 3 weeks, low-grade fever, night sweats, and weight loss of 5 kg. Oxyg…
```

### S5 judge fail 30

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`en`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|Shanthi Shetty]] [[AGE|45]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-2024-0315-001]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|shanthi.shetty@email.com]] Hospital [[HOSPITAL_NAME|Mangalore City Hospital]]
--- chat ---
Patient: Good morning Doctor. I've been having lower back p…
```

### S5 judge fail 31

- **What:** linguistic judge **fail** on `hospital_billing` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
બીલ — [[HOSPITAL_NAME|S.S.G. Hospital]] જિલ્લો [[DISTRICT|Vadodara]]
પિન [[PIN_CODE|390001]] દર્દી [[PATIENT_NAME|Jaymeenbhai Mehta]] MRN [[MRN|MRN-GJ-2024-0815]]
સરનામું [[RESIDENTIAL_ADDRESS|Chhani Village, Taluka Vadodara, District Vadodara, Gujarat 390001]]
ફોન [[PHONE_NUMBER|9876543210]] ઈમેલ [[EMAIL_ADDRESS|jaymeen.mehta@example.com]]
આધાર [[AADHAAR_NUMBER|291512345678]] પાન [[PAN_NUMBER|AAAPM1234C]]
લેન્ડલાઇન [[TELEPHONE_LANDLINE|0265-2424242]] વાહન [[VEHICLE_REGISTRATION|GJ-06-AB-1234]]…
```

### S5 judge fail 32

- **What:** linguistic judge **fail** on `discharge_summary` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ડિસ્ચાર્જ સમરી — [[HOSPITAL_NAME|District Hospital Vadodara]]
[[PATIENT_NAME|Jaymeenbhai Mehta]] જન્મ તારીખ [[DOB|1976-05-15]] [[AGE|48]] [[GENDER|Male]]
પ્રવેશ [[ADMISSION_NUMBER|ADM-2024-0512]] વોર્ડ [[WARD_NUMBER|B1]] બેડ [[BED_NUMBER|08]]
ડૉ. [[DOCTOR_NAME|Dr. Rajesh Patel]] | સારવાર / સલાહ:
દર્દી તીવ્ર ગેસ્ટ્રોએન્ટેરાઇટિસ અને નિર્જલીકરણ સાથે દાખલ થયા હતા. પ્રારંભિક વાઇટલ્સમાં BP 90/60 mmHg, HR 110 bpm, તાપમાન 101.2°F દર્શાવ્યું હતું. 2 કલાક દરમિયાન 1L નોર્મલ સેલાઇન સાથે IV ફ્લુઇડ રિસસિટેશન…
```

### S5 judge fail 33

- **What:** linguistic judge **fail** on `referral_letter` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-TB-001]] થી [[HOSPITAL_NAME|Primary Health Center, Vadodara]] / [[DOCTOR_NAME|Dr. Rajesh Patel]]
વિષે: [[PATIENT_NAME|Jaymeenbhai Mehta]], [[AGE|48]] / [[GENDER|Male]], જિલ્લો [[DISTRICT|Vadodara]]

કારણ: સતત ઉધરસ સાથે શારીરિક લક્ષણો અને નવું નિદાન થયેલ Type 2 Diabetes Mellitus માટે વિશિષ્ટ મૂલ્યાંકન અને સંચાલન.

પ્રિય સહકર્મી,

હું [[PATIENT_NAME|Jaymeenbhai Mehta]], 48 વર્ષનો પુરુષ દુકાનદાર ગ્રામીણ વડોદરાથી, શંકાસ્પદ ફેફસાના ક્ષય રોગના મૂલ્યાંકન અને નવા નિદાન થયેલ…
```

### S5 judge fail 34

- **What:** linguistic judge **fail** on `hospital_billing` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
બિલ
દર્દીની વિગતો
દર્દીનું નામ: [[PATIENT_NAME|Dahiben Muchadiya]]
MRN: [[MRN|MRN-GJ-2024-001]]
ઉંમર: 58, જાતિ: સ્ત્રી
સરનામું: [[RESIDENTIAL_ADDRESS|Village Dholka, Taluka Himmatnagar, District Sabar Kantha, Gujarat 383001]]
ફોન નંબર: [[PHONE_NUMBER|9876543210]]
ઈમેલ સરનામું: [[EMAIL_ADDRESS|dahiben.muchadiya@example.com]]
આધાર નંબર: [[AADHAAR_NUMBER|291512345678]]
PAN નંબર: [[PAN_NUMBER|AAAPL1234C]]
વીમા પોલિસી નંબર: [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-7890]]
વાહન નોંધણી: [[VEHICLE_REGISTRA…
```

### S5 judge fail 35

- **What:** linguistic judge **fail** on `discharge_summary` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ડિસ્ચાર્જ સમરી — [[HOSPITAL_NAME|હોસ્પિટલનું નામ]]
[[PATIENT_NAME|દર્દીનું નામ]] જન્મ તારીખ [[DOB|1966-03-15]] [[AGE|58]] [[GENDER|Female]]
પ્રવેશ [[ADMISSION_NUMBER|ADM-2024-0315]] વોર્ડ [[WARD_NUMBER|B2]] બેડ [[BED_NUMBER|12]]
ડોક્ટર [[DOCTOR_NAME|ડોક્ટરનું નામ]] | સારવાર યોજના / સલાહ: 

દર્દી દહિબેન મુચડિયા, 58 વર્ષની મહિલા ખેતમજૂર સાબરકાંઠા જિલ્લાથી, સતત ઉધરસ, વજન ઘટાડો અને થાકની ફરિયાદો સાથે દાખલ કરવામાં આવ્યા હતા. પ્રારંભિક તપાસમાં ફેફસાંનો ક્ષય જોવા મળ્યો, જેમાં હાઈ બ્લડ પ્રેશર અને ટાઇપ …
```

### S5 judge fail 36

- **What:** linguistic judge **fail** on `referral_letter` (`gu`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-01]] થી [[HOSPITAL_NAME|Primary Health Center Himmatnagar]] / [[DOCTOR_NAME|Dr. Rajesh Patel]]
વિષે: [[PATIENT_NAME|Dahiben Muchadiya]], [[AGE|58]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Sabar Kantha]]
કારણ: સતત માથાનો દુખાવો અને ચક્કર સાથે વધારેલું બ્લડ પ્રેશર માપન

પ્રિય નિષ્ણાત,

અમે સંદર્ભિત કરીએ છીએ [[PATIENT_NAME|Dahiben Muchadiya]], 58 વર્ષની મહિલા ખેતીની દેખરેખ રાખનાર ગ્રામીણ સાબરકાંઠાથી, વધુ મૂલ્યાંકન માટે ઉચ્ચ રક્તચાપ અને મેટાબોલિક મૂલ્યાંકન. દર્દી છેલ્લા …
```

### S5 judge fail 37

- **What:** linguistic judge **fail** on `automated_sms` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्रिय [[PATIENT_NAME|Ramesh Chandra]], आपका TB फॉलो-अप [[APPOINTMENT_ID|APT-240615-02]] को [[HOSPITAL_NAME|Jalpaiguri District Hospital]] पर [[DOCTOR_NAME|Dr. Amit Kumar]] के साथ है। कृपया अपना [[MRN|MRN-2024-0615-001]] लेकर आएं और 15 मिनट पहले पहुंचें। पुष्टि के लिए [[PHONE_NUMBER|9876543210]] पर कॉल करें।
```

### S5 judge fail 38

- **What:** linguistic judge **fail** on `insurance_claim` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
तृतीय पक्ष प्रशासक दावा — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-WB-2024-8901]]
[[PATIENT_NAME|Ramesh Chandra Roy]] [[AGE|40]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|238745612938]]
अस्पताल [[HOSPITAL_NAME|Jalpaiguri District Hospital]] जिला [[DISTRICT|Jalpaiguri]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|WB08R1234]] (केवल एक बार)।
PAN [[PAN_NUMBER|WBPCR1234D]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|3456789012345678]]
बैंक रूटिंग [[BANK_ROUTING_NUMBER|SBIN0001234]] क्रेडिट कार्ड [[…
```

### S5 judge fail 39

- **What:** linguistic judge **fail** on `hospital_billing` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|Jalpaiguri District Hospital]] जिला [[DISTRICT|Jalpaiguri]]
पिन [[PIN_CODE|736101]] रोगी [[PATIENT_NAME|Ramesh Chandra]] MRN [[MRN|MRN-WB-2024-0815-001]]
पता [[RESIDENTIAL_ADDRESS|15/2 Bhabani Path, Ward No. 7, Malbazar, Jalpaiguri]] फोन [[PHONE_NUMBER|9876543210]] ईमेल [[EMAIL_ADDRESS|ramesh.chandra@example.com]]
आधार [[AADHAAR_NUMBER|206501253007]] पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-WB-7781]] GSTIN [[TAX_ID|19ABCDE1234F1Z5]]
लैंडलाइन [[TELEPHONE_LANDLINE|03562-222334]…
```

### S5 judge fail 40

- **What:** linguistic judge **fail** on `insurance_claim` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA दावा — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-MP-2024-1123]]
[[PATIENT_NAME|Shiv Lal]] [[AGE|42]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|234567890123]]
अस्पताल [[HOSPITAL_NAME|District Hospital Mandsaur]] जिला [[DISTRICT|Mandsaur]]
मोटर / आर टी ए वाहन [[VEHICLE_REGISTRATION|MP04AB1234]] (केवल एक बार)।
पैन [[PAN_NUMBER|ABCDE1234F]] आई एफ एस सी [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|50200098765432]]
बैंक रूटिंग [[BANK_ROUTING_NUMBER|SBIN0001234]] क्रेडिट कार्ड [[CREDIT_CARD_NUMBER|…
```

### S5 judge fail 41

- **What:** linguistic judge **fail** on `automated_sms` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|राम कुमार]]: आपका सर्जरी अपॉइंटमेंट [[APPOINTMENT_ID|APT-240521-01]], 21-May को [[HOSPITAL_NAME|अखिल भारतीय आयुर्विज्ञान संस्थान]] में [[DOCTOR_NAME|डॉ. शर्मा]] के साथ है। MRN [[MRN|MRN-2024-0815-001]]. पुष्टि के लिए [[PHONE_NUMBER|9876512340]] पर कॉल करें।
```

### S5 judge fail 42

- **What:** linguistic judge **fail** on `hospital_billing` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|Mandsaur District Hospital]] [[DISTRICT|Mandsaur]] जिला
पिन [[PIN_CODE|458001]] रोगी [[PATIENT_NAME|Shiv Lal]] मेडिकल रिकॉर्ड नंबर [[MRN|MRN-MP-2024-0815-001]]
पता [[RESIDENTIAL_ADDRESS|45, Civil Lines, Mandsaur, Madhya Pradesh 458001]] फोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|shiv.lal.teacher@example.com]] पैन [[PAN_NUMBER|ABCDE1234F]]
आधार [[AADHAAR_NUMBER|234567890123]] पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-MP-2024-7781]] जीएसटीआईएन [[TAX_ID|23ABCDE1234F1Z5]…
```

### S5 judge fail 43

- **What:** linguistic judge **fail** on `opd_slip` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಹೊರರೋಗಿ ಚೀಟಿ | [[HOSPITAL_NAME|Gadag District Hospital]] | ಐಡಿ [[HOSPITAL_ID|GDS-01]]
ರೋಗಿ: [[PATIENT_NAME|Basavaraj]] | ಜನ್ಮ ದಿನಾಂಕ [[DOB|1975-08-15]] | ವಯಸ್ಸು: [[AGE|49]] | ಲಿಂಗ: [[GENDER|Male]]
ವೃತ್ತಿ: [[OCCUPATION|Market-Oriented Crop and Animal Producers, Other]] | ಎಂ.ಆರ್.ಎನ್: [[MRN|OPD-2024-0815-001]]
ವೈದ್ಯರು: [[DOCTOR_NAME|Dr. Prakash Hegde]]
ಸಂಬಂಧಿ: [[RELATIVE_NAME|Siddappa]] | ಫೋನ್: [[PHONE_NUMBER|9876543210]]
ನೋಂದಣಿ ಉದ್ಯೋಗಿ ಐಡಿ: [[EMPLOYEE_ID|REG-102]]
ಜಿಲ್ಲೆ: [[DISTRICT|Gadag]]

ಮುಖ್…
```

### S5 judge fail 44

- **What:** linguistic judge **fail** on `surgical_note` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಯ ಟಿಪ್ಪಣಿ — [[HOSPITAL_NAME|ಆಸ್ಪತ್ರೆ ಹೆಸರು]] ದಾಖಲೆ [[ADMISSION_NUMBER|ADM-2024-1025]] ವಾರ್ಡ್ [[WARD_NUMBER|Surgical ICU]]
[[PATIENT_NAME|ರೋಗಿಯ ಹೆಸರು]] [[AGE|49]] [[GENDER|Male]] ಶಸ್ತ್ರಚಿಕಿತ್ಸಕ [[DOCTOR_NAME|ವೈದ್ಯರ ಹೆಸರು]]
ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಗೆ ಮುನ್ನಿನ ರೋಗನಿರ್ಣಯ: ಎದೆಗೂಡಿನ ಬೆನ್ನುಮೂಳೆಯ ಪಾಟ್ಸ್ ಕಾಯಿಲೆ (T8-T9) ಬೆನ್ನುಹುರಿಯ ಸಂಕೋಚನ ಮತ್ತು ಪಾರ್ಶ್ವವಾಯು.
ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಯ ನಂತರದ ರೋಗನಿರ್ಣಯ: ಎದೆಗೂಡಿನ ಬೆನ್ನುಮೂಳೆಯ ಪಾಟ್ಸ್ ಕಾಯಿಲೆ (T8-T9) ಬೆನ್ನುಹುರಿಯ ಸಂಕೋಚನ ಮತ್ತು ಪಾರ್ಶ್ವವಾಯು.
ವಿಧಾನ: T8 ಮತ್ತು T9 ಕಶೇರುಖಂಡಗಳ ಮು…
```

### S5 judge fail 45

- **What:** linguistic judge **fail** on `prescription` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ — [[HOSPITAL_NAME|District Hospital Gadag]]
[[HOSPITAL_ID|HSP-KA-GAD-001]]

ರೋಗಿ [[PATIENT_NAME|Basavaraj Patil]], [[AGE|49]] / [[GENDER|Male]], MRN [[MRN|MRN-2024-05-15-001]]
[[PATIENT_ID|PID-GAD-2024-001]]
[[PHONE_NUMBER|9886543210]]
[[ABHA_ID|12-3456-7890-1234]]
[[ABHA_ADDRESS|basavaraj.patil@abdm]]
[[RESIDENTIAL_ADDRESS|Near Kudalasangama, Gadag Taluk, Karnataka]]
[[DISTRICT|Gadag]]

ಡಾ. [[DOCTOR_NAME|Dr. Ramesh]]

Rx:
1. ಪ್ಯಾರಸಿಟಮಾಲ್ 500mg ಮಾತ್ರೆ, ಒಂದು ಮಾತ್ರೆ ಊಟದ ನಂತರ ದಿನಕ್…
```

### S5 judge fail 46

- **What:** linguistic judge **fail** on `surgical_note` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ಟಿಪ್ಪಣಿ — [[HOSPITAL_NAME|Mandya District Hospital]] ದಾಖಲೆ [[ADMISSION_NUMBER|ADM-2024-0915]] ವಾರ್ಡ್ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Shanthi Gowda]] [[AGE|22]] [[GENDER|Female]] ಶಸ್ತ್ರಚಿಕಿತ್ಸಕ [[DOCTOR_NAME|Dr. Ramesh Kumar]]
ಕಾರ್ಯವಿಧಾನ / ಸಂಶೋಧನೆಗಳು: ರೋಗಿಯವರು ಎರಡು ದಿನಗಳಿಂದ ಜ್ವರ ಮತ್ತು ವಾಂತಿಯೊಂದಿಗೆ ತೀವ್ರವಾದ ಬಲ ಕೆಳ ಹೊಟ್ಟೆಯ ನೋವಿನೊಂದಿಗೆ ಬಂದರು. ಪರೀಕ್ಷೆಯಲ್ಲಿ McBurney's point ನಲ್ಲಿ ಮರುಬರುವ ನೋವಿನೊಂದಿಗೆ ನೋವು ಕಂಡುಬಂದಿತು. ಅಲ್ಟ್ರಾಸೌಂಡ್ ತೀವ್ರವಾದ ಅಪೆಂಡಿಸೈಟಿಸ್ ತೋರಿಸಿದೆ. ರೋಗಿಯನ್ನು ಲ್ಯಾಪ್ರೊಸ್ಕೋಪ…
```

### S5 judge fail 47

- **What:** linguistic judge **fail** on `lab_report` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಪ್ರಯೋಗಶಾಲೆ ವರದಿ — [[HOSPITAL_NAME|Mandya District Hospital]] ಜಿಲ್ಲೆ [[DISTRICT|Mandya]]
MRN [[MRN|MRN-KA-2024-0815]] ರೋಗಿಯ ಐಡಿ [[PATIENT_ID|PID-KA-7781]]
[[PATIENT_NAME|Shwetha Gowda]] [[AGE|22]] [[GENDER|Female]] ಫೋನ್ [[PHONE_NUMBER|9876543210]]
ಆದೇಶಿಸಿದವರು [[DOCTOR_NAME|Dr. Priya Ramesh]]
ದಿನಾಂಕ: 15 ಆಗಸ್ಟ್ 2024

ರೋಗಿಯ ಮಾಹಿತಿ:
[[PATIENT_NAME|Shwetha Gowda]] ಇವರು 22 ವರ್ಷದ ಅವಿಭಕ್ತ ಮಹಿಳೆ ಮರಗೆಲಸದ ಯಂತ್ರದ ಕೆಲಸಗಾರ ಗ್ರಾಮೀಣ ಮಂಡ್ಯ ಜಿಲ್ಲೆ, ಕರ್ನಾಟಕದಿಂದ. ಅವರು 16 ವಾರಗಳ ಗರ್ಭಾವಸ್ಥೆಯಲ್ಲಿ ಸಾಮಾನ್ಯ ಪ್ರಸವಪೂರ್ವ ಆರೈ…
```

### S5 judge fail 48

- **What:** linguistic judge **fail** on `opd_slip` (`kn`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ಬಾಹ್ಯರೋಗಿ ಚೀಟಿ | [[HOSPITAL_NAME|Mandya District Hospital]] | ID [[HOSPITAL_ID|MDH-2024-01]]
ರೋಗಿ: [[PATIENT_NAME|Shanthi Gowda]] | ಜನ್ಮ ದಿನಾಂಕ: [[DOB|2002-08-22]] | ವಯಸ್ಸು: [[AGE|22]] | ಲಿಂಗ: [[GENDER|Female]]
ವೃತ್ತಿ: [[OCCUPATION|Wood Working Machine Operative]] | MRN: [[MRN|OPD-2024-1157]] | ವೈದ್ಯರು: [[DOCTOR_NAME|Dr. Priya N.]]
ಸಂಬಂಧಿ: [[RELATIVE_NAME|Siddaraju Gowda]] | ಫೋನ್: [[PHONE_NUMBER|9886543210]]
ನೋಂದಣಿ ಐಡಿ: [[EMPLOYEE_ID|REG-4589]] | ಜಿಲ್ಲೆ: [[DISTRICT|Mandya]]
ಮುಖ್ಯ ದೂರು: ಮೂರು ವಾರ…
```

### S5 judge fail 49

- **What:** linguistic judge **fail** on `prescription` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
औषधपत्र — [[HOSPITAL_NAME|South Goa District Hospital]]
रुग्ण [[PATIENT_NAME|Natalina D'Souza]], [[AGE|46]] / [[GENDER|Female]], MRN [[MRN|MRN-GOA-2024-001]]
डॉक्टर [[DOCTOR_NAME|Dr. Priya Naik]]
फोन: [[PHONE_NUMBER|9822345678]]
पत्तो: [[RESIDENTIAL_ADDRESS|Cavelossim, Salcete, South Goa]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
रुग्ण आयडी: [[PATIENT_ID|PID-GOA-46-001]]
जिल्लो: [[DISTRICT|South Goa]]

मुख्य तक्रार: 3 सप्तकां सावन सतत सुकी खोकली, 5 किलो वजन उणें जावप, वाडपी थकवो आनी केन्ना केन्ना…
```

### S5 judge fail 50

- **What:** linguistic judge **fail** on `lab_report` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|Goa Medical College Hospital]] जिल्हा [[DISTRICT|South Goa]]
MRN [[MRN|GMCH-2024-0815-001]] रुग्ण आयडी [[PATIENT_ID|PID-GOA-7894]]
[[PATIENT_NAME|Natalina Goes]] [[AGE|46]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
द्वारे आदेशित [[DOCTOR_NAME|Dr. Priya Naik]]

मानसोपचार मूल्यांकन अहवाल
तारीख: 15 ऑगस्ट 2024

रुग्णाची मुख्य तक्रार गेल्या 6 म्हयन्यांपासून सतत चिंता लक्षणां आहे. तो अहवाल देतो की झोपायला त्रास, कुटुंबाच्या गोष्टींबद्दल जास्त काळजी आणि अधूनम…
```

### S5 judge fail 51

- **What:** linguistic judge **fail** on `asha_worker_note` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ASHA नोंद: गांव [[VILLAGE|Cavelossim]], जिल्लो [[DISTRICT|South Goa]]
रुग्ण [[PATIENT_NAME|Savitri Naik]], [[AGE|46]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rita Fernandes]] | फोन [[PHONE_NUMBER|9876543210]]
भेटेचीं सोद: रुग्ण सतत तकली दुखप आनी थकवा फाटल्या दोन सप्तकां खातीर सांगता. रक्तदाब वाचन 140/90 mmHg. सांगलें विश्रांती आनी परत तपासणी प्राथमीक आरोग्य केंद्रांत.

कुटुंबाची म्हायती: पती मत्स्योद्योगी आसा. [[RELATIVE_NAME|Ramesh Naik]] आसा जोडीदार. [[BPL_RATION_CARD|BPL-GOA-2024-001234…
```

### S5 judge fail 52

- **What:** linguistic judge **fail** on `lab_report` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|Jalgaon Civil Hospital]] जिल्हा [[DISTRICT|Jalgaon]]
MRN [[MRN|MRN-MH-2024-0815]] रुग्ण आयडी [[PATIENT_ID|PID-MH-7781]]
[[PATIENT_NAME|Sunita Patil]] [[AGE|34]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
[[DOCTOR_NAME|Dr. Rajesh Deshmukh]] हाणें सुचयल्लें
तारीख: 15 ऑगस्ट 2024

वैद्यकीय माहिती:
रुग्ण सतत थकवा, 3 म्हयन्यांत 8 किलो वजन उणें जावप आनी मदीं-मदीं पोट दुखप घेवन येता. कुटुंबांत इतिहास स्तनाच्या कॅन्सरचो (आवयचो 42 वर्सां पिरायेर निदान जालो) आसा. …
```

### S5 judge fail 53

- **What:** linguistic judge **fail** on `opd_slip` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
OPD पाटी | [[HOSPITAL_NAME|District Hospital Jalgaon]] | ID [[HOSPITAL_ID|DH-JLG-001]]
रुग्ण: [[PATIENT_NAME|Lalita Tirvadekar]] | DOB [[DOB|1990-05-15]] | पिराय: [[AGE|34]] | लिंग: [[GENDER|Female]]
वेवसाय: [[OCCUPATION|Mono Operator]] | MRN: [[MRN|MRN-2024-0815-001]] | दोतोर: [[DOCTOR_NAME|Dr. Priya Deshmukh]]
नातेवाईक: [[RELATIVE_NAME|Ramesh Tirvadekar]] | फोन: [[PHONE_NUMBER|9876543210]]
रजिस्ट्रार EmpID: [[EMPLOYEE_ID|EMP-4412]] | जिल्लो: [[DISTRICT|Jalgaon]]
मुखेल तक्रार: रुग्णाक सतत तकली…
```

### S5 judge fail 54

- **What:** linguistic judge **fail** on `phc_register` (`kok`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्राथमिक आरोग्य केंद्र नोंद — [[HOSPITAL_NAME|Primary Health Centre, Jalgaon]] गांव [[VILLAGE|Kopargaon]] जिल्हा [[DISTRICT|Jalgaon]]
[[PATIENT_NAME|Lalita Tirvadekar]] [[AGE|34]] [[GENDER|Female]] | प्रसूतीपूर्व तपासणी - २८ सप्तकांचें गर्भधारणा

रुग्ण ललिता तिरवाडेकर, ३४ वर्सांची बायल, २८ सप्तकांचें गर्भधारणा वेळार नियमित प्रसूतीपूर्व तपासणी खातीर आयली. मुख्य तक्रार: सौम्य सकयल्या पोटांतली अस्वस्थता आनी केन्ना केन्नाय तकली दुखप. जीवनावश्यक चिन्नां: BP 110/70 mmHg, Pulse 80/min, Temperature 98.…
```

### S5 judge fail 55

- **What:** linguistic judge **fail** on `er_triage_notes` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ایمرجنسی ٹریاج — [[HOSPITAL_NAME|ہسپتال]] ملاقات [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|علی احمد]] [[AGE|28]] [[GENDER|Male]] وارڈ [[WARD_NUMBER|ER]] بستر [[BED_NUMBER|03]]
ایمبولینس ذٔریعہ ووت [[VEHICLE_REGISTRATION|JK01AB1234]] (صرف اکھ لٹہ)۔
رشتہ دار [[RELATIVE_NAME|عائشہ بیگم]] فون [[PHONE_NUMBER|9419234567]] ڈاکٹر [[DOCTOR_NAME|ڈاکٹر راشد]]
حیاتی علامات: BP 140/90، HR 110، RR 22، Temp 38.2°C، SpO2 94% کمرے کی ہوا پر۔ مریض کی شکایت ہے بتدریج سانس پھولنا، 3 مہینوں میں 8 کلوگرام وز…
```

### S5 judge fail 56

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- سیشن ---
مریض [[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]]
اپوائنٹمنٹ [[APPOINTMENT_ID|APT-2024-0815-001]] پورٹل [[URL|https://tele.example.in/visit]]
کلائنٹ IP [[IP_ADDRESS|103.21.244.12]] ڈیوائس IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] فون [[PHONE_NUMBER|9876512340]]
ای میل [[EMAIL_ADDRESS|jammer.shamar@example.com]] ہسپتال [[HOSPITAL_NAME|SMHS Hospital Srinagar]]
--- چیٹ ---
مریض: سلام ڈاکٹر صاحب، بہٕ چھس پچھلے شامہٕ پؠٹھ تپَس منٛز۔ درجہ حرا…
```

### S5 judge fail 57

- **What:** linguistic judge **fail** on `opd_slip` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
آؤٹ پیشنٹ سلپ | [[HOSPITAL_NAME|Sher-i-Kashmir Institute of Medical Sciences]] | آئی ڈی [[HOSPITAL_ID|SKIMS-SRI-001]]
مریض: [[PATIENT_NAME|Mohammad Yousuf]] | تاریخِ پیدائش [[DOB|1996-05-15]] | عُمر: [[AGE|28]] | صِنف: [[GENDER|Male]]
پیشہ: [[OCCUPATION|Keypunch Operator]] | MRN: [[MRN|OPD-SKIMS-2024-0876]] | ڈاکٹر: [[DOCTOR_NAME|Dr. Abdul Rashid]]
رشتہ دار: [[RELATIVE_NAME|Fatima Begum]] | فون: [[PHONE_NUMBER|9419012345]]
رجسٹرار ایمپلائی آئی ڈی: [[EMPLOYEE_ID|REG-2024-0156]] | ضلع: [[DISTRICT…
```

### S5 judge fail 58

- **What:** linguistic judge **fail** on `er_triage_notes` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ایمرجنسی ٹریاج — [[HOSPITAL_NAME|SKIMS Soura]] ملاقات [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] وارڈ [[WARD_NUMBER|ER]] بید [[BED_NUMBER|07]]
ایمبولینس ذٔریعہ آمُت [[VEHICLE_REGISTRATION|JK01AB5678]]
رشتہ دار [[RELATIVE_NAME|Mohammad Yousuf]] فون [[PHONE_NUMBER|9419234567]] ڈاکٹر [[DOCTOR_NAME|Dr. Farooq Ahmad]]
وائٹلز / حالت: ہوشس منٛز تہٕ 3 طرفہٕ باخبر، BP 120/80، HR 78، RR 16، Temp 36.8°C، SpO2 98% کمرے کی ہوا پر۔ مریض چھُ پریشان نظر یوان نفسی…
```

### S5 judge fail 59

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- session ---
مریض [[PATIENT_NAME|إمام]] [[AGE|19]] [[GENDER|Male]]
ملاقات [[APPOINTMENT_ID|APT-2024-0315-001]] پورٹل [[URL|https://tele.skims.edu.in/visit]]
کلائنٹ IP [[IP_ADDRESS|103.21.244.12]] ڈیوائس IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] فون [[PHONE_NUMBER|9876543210]]
ای میل [[EMAIL_ADDRESS|imran.khan@example.com]] ہسپتال [[HOSPITAL_NAME|ایس کے آئی ایم ایس]]
--- chat ---
مریض: سلام ڈاکٹر صاحب، مےٚ چھُ مُستقل کھوٚس پتیمن ترٛیون ہفتن پؠٹھ، تہٕ تپہٕ تہٕ …
```

### S5 judge fail 60

- **What:** linguistic judge **fail** on `opd_slip` (`ks`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
خارِجِ مَرکَزِ طِب تِکِٹ | [[HOSPITAL_NAME|SMHS Hospital]] | پَہچان نَمبَر [[HOSPITAL_ID|SMHS-SRG-001]]
مَریٖض: [[PATIENT_NAME|Mohammad Riyaz]] | تٲریٖخِ زاد [[DOB|2005-07-15]] | عُمر: [[AGE|19]] | جِنْس: [[GENDER|Male]]
پیشہٕ: [[OCCUPATION|Unemployed]] | طِبّی رِکارڈ نَمبَر: [[MRN|OPD-2024-0815-001]] | ڈاکٹَر: [[DOCTOR_NAME|Dr. Abdul Ahad]]
رِشتہٕ دار: [[RELATIVE_NAME|Mohammad Yousuf (Father)]] | فون نَمبَر: [[PHONE_NUMBER|9419212345]]
رجسٹرار مُلازم نَمبَر: [[EMPLOYEE_ID|EMP-2024-089]] | زِلہ…
```

### S5 judge fail 61

- **What:** linguistic judge **fail** on `opd_slip` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बाह्य रोगी विभागक पर्ची | [[HOSPITAL_NAME|District Hospital Saharsa]] | ID [[HOSPITAL_ID|DH-SAH-001]]
रोगी: [[PATIENT_NAME|Devanti Kumari]] | जन्म तिथि [[DOB|2001-05-20]] | आयु: [[AGE|23]] | लिंग: [[GENDER|Female]]
व्यवसाय: [[OCCUPATION|Supervisor, Jewellery, Engraving and Precision Metal Workers]]
चिकित्सा रिकॉर्ड संख्या: [[MRN|OPD-2024-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
रिश्तेदार: [[RELATIVE_NAME|Ramesh Kumar]] | फोन: [[PHONE_NUMBER|9431056789]]
पंजीयक कर्मचारी आईडी: [[EMPLOYEE_…
```

### S5 judge fail 62

- **What:** linguistic judge **fail** on `phc_register` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्राथमिक स्वास्थ्य केंद्र रजिस्टर — [[HOSPITAL_NAME|Primary Health Centre, Saharsa]] गाँव [[VILLAGE|Kharagpur]] जिला [[DISTRICT|Saharsa]]
[[PATIENT_NAME|Devanti Kumari]] [[AGE|23]] [[GENDER|Female]] | प्रसव पूर्व देखभाल पंजीकरण

मरीज देवंती कुमारी, 23 वर्षक महिला खड़गपुर गामसँ, 12 सप्ताहक गर्भावस्था मे पहिल प्रसव पूर्व देखभालक भेटक लेल आयल छथि। मुख्य शिकायत: हल्का उबकाई आ थकान। महत्वपूर्ण लक्षण: रक्तचाप 110/70 mmHg, नाड़ी 80/min, वजन 52 kg। पेटक जाँच: गर्भाशय क आकार तारीखक अनुसार सही अछि। मूत्र…
```

### S5 judge fail 63

- **What:** linguistic judge **fail** on `prescription` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|Saharsa District Hospital]]
मरीज [[PATIENT_NAME|Devanti Kumari]], [[AGE|23]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-SAH-001]]
डाक्टर [[DOCTOR_NAME|Dr. Rajiv Kumar]]
मुख्य शिकायत: तीन सप्ताह सँ लगातार खाँसी, कम बुखार साँझमे, आ वजन कम होनाय।
इतिहास: मरीज 23 सालक महिला छथि, विवाहित, ग्रामीण मधुपुर सँ। व्यवसाय: आभूषण पर्यवेक्षक। कखनो-कखनो सिगरेट पीयबाक जानकारी दैत छथि। कोनो ज्ञात अन्य बीमारी नहि अछि।
जाँच: हल्का रक्ताल्पता आ कैशेक्सिया। छातीक स्टेथोस्कोप सँ जाँचमे दाहिना ऊ…
```

### S5 judge fail 64

- **What:** linguistic judge **fail** on `surgical_note` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
शल्य चिकित्सा नोट — [[HOSPITAL_NAME|Hazaribagh District Hospital]] भर्ति [[ADMISSION_NUMBER|ADM-2024-0815]] वार्ड [[WARD_NUMBER|B2]]
[[PATIENT_NAME|Sita Devi]] [[AGE|65]] [[GENDER|Female]] शल्य चिकित्सक [[DOCTOR_NAME|Dr. Rajesh Kumar]]
प्रक्रिया / निष्कर्ष: रोगी लक्षणयुक्त पित्त पथरी आ तीव्र पित्ताशय शोथक संग प्रस्तुत भेल छलाह। शल्य चिकित्सा पूर्व मूल्यांकनमे हल्का उच्च रक्तचाप आ टाइप 2 मधुमेहक पता चलल। सामान्य एनेस्थीसियाक अंतर्गत लॅपरोस्कोपिक कोलेसिस्टेक्टोमी कयल गेल। शल्य चिकित्साक दौरानक नि…
```

### S5 judge fail 65

- **What:** linguistic judge **fail** on `opd_slip` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ओपीडी स्लिप | [[HOSPITAL_NAME|Hazaribagh District Hospital]] | आईडी [[HOSPITAL_ID|HDH-JH-001]]
रोगी: [[PATIENT_NAME|Phoolmani Devi]] | जन्म तिथि [[DOB|1959-04-15]] | आयु: [[AGE|65]] | लिंग: [[GENDER|Female]]
व्यवसाय: [[OCCUPATION|Homemaker]] | एमआरएन: [[MRN|MRN-2024-0815-001]] | चिकित्सक: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
रिश्तेदार: [[RELATIVE_NAME|Sushila Devi]] | फोन: [[PHONE_NUMBER|9431023456]]
पंजीयक कर्मचारी आईडी: [[EMPLOYEE_ID|EMP-2024-008]] | जिला: [[DISTRICT|Hazaribagh]]
मुख्य शिकायत: 3 …
```

### S5 judge fail 66

- **What:** linguistic judge **fail** on `prescription` (`mai`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|Shri Krishna Hospital, Hazaribagh]]
मरीज [[PATIENT_NAME|Sita Devi]], [[AGE|65]] / [[GENDER|Female]], MRN [[MRN|MRN-JH-2024-001]]
[[RESIDENTIAL_ADDRESS|Village Barkagaon, Hazaribagh, Jharkhand]]
[[DISTRICT|Hazaribagh]]
डाक्टर [[DOCTOR_NAME|Dr. Rajiv Kumar]]
ABHA [[ABHA_ID|12-3456-7890-1234]]
मरीज [[PATIENT_ID|PID-JH-65-001]]
संपर्क [[PHONE_NUMBER|9431056789]]
Rx: ऑपरेशनक बादक देखभाल laparoscopic cholecystectomy.
1. Tab. Paracetamol 500mg, एक गोली दिनमे दू बेर भोजनक बाद प…
```

### S5 judge fail 67

- **What:** linguistic judge **fail** on `er_triage_notes` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
അടിയന്തര വിഭാഗം ട്രയാജ് — [[HOSPITAL_NAME|മെഡിക്കൽ കോളേജ് ആശുപത്രി]] സമ്പർക്കം [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|ലക്ഷ്മി നായർ]] [[AGE|56]] [[GENDER|Female]] വാർഡ് [[WARD_NUMBER|ER]] ബെഡ് [[BED_NUMBER|05]]
ആംബുലൻസ് വാഹനത്തിൽ എത്തി [[VEHICLE_REGISTRATION|KL02AB1234]] (ഒരിക്കൽ മാത്രം).
ബന്ധു [[RELATIVE_NAME|മോഹൻ നായർ]] ഫോൺ [[PHONE_NUMBER|9876543210]] ഡോ. [[DOCTOR_NAME|ഡോ. ഷെർലി വർഗ്ഗീസ്]]
വൈറ്റൽസ് / തീവ്രത:
രോഗിയുടെ പരാതികൾ: 3 ദിവസമായി കഠിനമായ വയറുവേദന, ഓക്കാനവും ഛർദ്ദിയും. മുൻപ് ര…
```

### S5 judge fail 68

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- സെഷൻ ---
രോഗി [[PATIENT_NAME|Mary Thomas]] [[AGE|56]] [[GENDER|Female]]
അപ്പോയിന്റ്‌മെന്റ് [[APPOINTMENT_ID|APT-2024-0815-001]] പോർട്ടൽ [[URL|https://tele.example.in/visit]]
ക്ലയന്റ് ഐപി [[IP_ADDRESS|103.21.244.12]] ഡിവൈസ് IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] ഫോൺ [[PHONE_NUMBER|9876543210]]
ഇമെയിൽ [[EMAIL_ADDRESS|mary.thomas@example.com]] ആശുപത്രി [[HOSPITAL_NAME|Medical College Hospital Thrissur]]
--- ചാറ്റ് ---
രോഗി: നമസ്കാരം ഡോക്ടർ, കഴിഞ്ഞ മൂന്ന് ദിവ…
```

### S5 judge fail 69

- **What:** linguistic judge **fail** on `opd_slip` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ഔട്ട്‌പേഷ്യന്റ് സ്ലിപ്പ് | [[HOSPITAL_NAME|District Hospital Thrissur]] | ID [[HOSPITAL_ID|DH-KL-027]]
രോഗി: [[PATIENT_NAME|Marykutty Thomas]] | DOB [[DOB|1968-07-22]] | പ്രായം: [[AGE|56]] | ലിംഗം: [[GENDER|Female]]
തൊഴിൽ: [[OCCUPATION|Retired Homemaker]] | MRN: [[MRN|OPD-2024-0815-004]] | ഡോക്ടർ: [[DOCTOR_NAME|Dr. Anjali Nair]]
ബന്ധു: [[RELATIVE_NAME|Thomas Thomas]] | ഫോൺ: [[PHONE_NUMBER|9876543210]]
രജിസ്ട്രാർ എംപ്ലോയി ഐഡി: [[EMPLOYEE_ID|EMP-KL-0089]] | ജില്ല: [[DISTRICT|Thrissur]]
പ്രധാന പരാ…
```

### S5 judge fail 70

- **What:** linguistic judge **fail** on `er_triage_notes` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
എമർജൻസി വിഭാഗം ട്രയാജ് ഉം നഴ്സിംഗ് കുറിപ്പുകളും
എമർജൻസി വിഭാഗം ട്രയാജ് — [[HOSPITAL_NAME|Government Medical College Hospital Thiruvananthapuram]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Megha John]] [[AGE|32]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
ആംബുലൻസ് വാഹനത്തിൽ എത്തി [[VEHICLE_REGISTRATION|KL01AB1234]] (കൃത്യം ഒരു തവണ).
ബന്ധു [[RELATIVE_NAME|John Varghese]] ഫോൺ [[PHONE_NUMBER|9876543210]] ഡോ. [[DOCTOR_NAME|Dr. Priya Nair]]
വൈറ്റൽസ് / തീവ്രത: BP…
```

### S5 judge fail 71

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
--- സെഷൻ ---
രോഗി [[PATIENT_NAME|Megha John]] [[AGE|32]] [[GENDER|Female]]
അപ്പോയിന്റ്‌മെന്റ് [[APPOINTMENT_ID|APT-2024-0815-001]] പോർട്ടൽ [[URL|https://tele.example.in/visit]]
ക്ലയന്റ് ഐപി [[IP_ADDRESS|103.21.244.12]] ഡിവൈസ് IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] ഫോൺ [[PHONE_NUMBER|9876543210]]
ഇമെയിൽ [[EMAIL_ADDRESS|megha.john@example.com]] ആശുപത്രി [[HOSPITAL_NAME|Government Medical College Thiruvananthapuram]]
--- ചാറ്റ് ---
രോഗി: നമസ്കാരം ഡോക്ടർ, ഞാൻ മേഘ…
```

### S5 judge fail 72

- **What:** linguistic judge **fail** on `surgical_note` (`ml`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ശസ്ത്രക്രിയ കുറിപ്പ് — [[HOSPITAL_NAME|Government Medical College Hospital Thiruvananthapuram]] പ്രവേശനം [[ADMISSION_NUMBER|ADM-2024-0912]] വാർഡ് [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Megha John]] [[AGE|32]] [[GENDER|Female]] ശസ്ത്രക്രിയാ വിദഗ്ധൻ [[DOCTOR_NAME|Dr. Priya Nair]]
നടപടിക്രമം / കണ്ടെത്തലുകൾ:
രോഗിക്ക് 2 ദിവസത്തേക്ക് തീവ്രമായ വലതുവശത്തെ താഴത്തെ വയറുവേദന ഉണ്ടായിരുന്നു.
പരിശോധനയിൽ, McBurney's point-ൽ rebound tenderness-ഓടെയുള്ള വേദന.
അൾട്രാസൗണ്ട് 8mm വ്യാസമുള്ള വീക്കമുള്ള അപ്പെൻഡിക്സ് കാണിച…
```

### S5 judge fail 73

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ꯗꯤꯁꯆꯥꯔꯖ ꯁꯝꯃꯔꯤ — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Leima Devi Leishangthem]] ꯄꯣꯛꯄꯒꯤ ꯆꯍꯤ [[DOB|1945-03-15]] [[AGE|79]] [[GENDER|Female]]
ꯑꯦꯗꯃꯤꯠ [[ADMISSION_NUMBER|ADM-2024-0315]] ꯋꯥꯔꯗ [[WARD_NUMBER|B1]] ꯕꯦꯗ [[BED_NUMBER|05]]
ꯗꯣꯛꯇꯔ [[DOCTOR_NAME|Dr. Rajesh Sharma]] | ꯀꯣꯔꯁ / ꯄꯥꯎꯇꯥꯛ: ꯄꯜꯃꯣꯅꯔꯤ ꯇ꯭ꯌꯨꯕꯔꯀꯨꯂꯣꯁꯤꯁ ꯇꯥꯏꯞ 2 ꯗꯥꯏꯕꯤꯇꯤꯁ ꯃꯦꯂꯤꯇꯁ ꯑꯃꯁꯨꯡ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟꯅ ꯀꯝꯞꯂꯤꯀꯦꯠ ꯇꯧꯔꯕ ꯄꯦꯁꯤꯑꯦꯟꯠ ꯑꯗꯨ ꯑꯦꯗꯃꯤꯠ ꯇꯧꯈꯤ꯫ ꯑꯍꯥꯟꯕ ꯁ꯭ꯄꯨꯇꯝ ꯃꯥꯏꯀ꯭ꯔꯣꯁ꯭ꯀꯣꯄꯤꯗ ꯑꯦꯁꯤꯗ-ꯐꯥꯁꯠ ꯕꯦꯁꯤꯂꯤ ꯎꯠꯈꯤ꯫ ꯆꯦꯁꯠ ꯑꯦꯛꯁ-ꯔꯦꯗ ꯇꯧꯕꯗ ꯔꯥꯏꯠ ꯑꯞꯄꯔ ꯂꯣ…
```

### S5 judge fail 74

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ꯔꯦꯐꯔꯦꯜ [[REFERRAL_ID|REF-2024-01]] ꯗꯒꯤ [[HOSPITAL_NAME|ꯑꯄꯣꯂꯣ ꯍꯣꯁꯄꯤꯇꯥꯜ]] / [[DOCTOR_NAME|ꯗꯣꯛꯇꯔ ꯁꯔꯃꯥ]]
Regarding: [[PATIENT_NAME|ꯁ꯭ꯔꯤꯃꯇꯤ ꯗꯦꯕꯤ]], [[AGE|79]] / [[GENDER|Female]], District [[DISTRICT|ꯏꯝꯐꯥꯜ ꯏꯁꯠ]]
ꯃꯔꯝ: ꯂꯦꯞꯇꯅ ꯂꯩꯕ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟ ꯃꯇꯝ ꯃꯇꯝꯒꯤ ꯑꯣꯏꯅ ꯀꯣꯛ ꯀꯣꯏꯕ ꯑꯃꯁꯨꯡ ꯀꯥꯎꯊꯣꯛꯄ

Dear colleague,

ꯑꯩꯈꯣꯏꯅ ꯔꯦꯐꯔ ꯇꯧꯔꯤ [[PATIENT_NAME|ꯁ꯭ꯔꯤꯃꯇꯤ ꯗꯦꯕꯤ]], ꯆꯍꯤ [[AGE|79]] ꯒꯤ [[GENDER|Female]] ꯅꯥꯕ ꯃꯤꯑꯣꯏ [[DISTRICT|Thoubal]] ꯗꯒꯤ ꯀꯟꯇ꯭ꯔꯣꯜ ꯇꯧꯕ ꯉꯝꯗꯕ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟ ꯃꯈꯥ ꯇꯥꯅ ꯊꯤꯖꯤꯟꯕ ꯑꯃꯁꯨꯡ ꯂꯥꯌꯦꯡꯕꯒꯤꯗꯃꯛ꯫ ꯅꯥꯕ ꯃꯤꯑꯣꯏ ꯑꯁꯤ ꯑꯩꯈꯣꯏꯒꯤ ꯌꯦꯡꯁꯤꯟꯕ…
```

### S5 judge fail 75

- **What:** linguistic judge **fail** on `radiology_report` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ৰেডিঅ’লজী ৰিপৰ্ট — [[HOSPITAL_NAME|Regional Hospital Imphal]] | [[PATIENT_NAME|Lalita Devi]] [[AGE|79]] [[GENDER|Female]]
MRN [[MRN|RH-2024-0045]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Rajesh Khuman]]
ফাইনডিংছ:
পেটৰ আল্ট্ৰাচাউণ্ডত সোঁফালৰ ওপৰৰ অংশত এটা 6.2 cm কমপ্লেক্স সিস্টিক মাছ দেখা গৈছে, যাৰ আভ্যন্তৰীণ চেপ্টেচন আৰু কঠিন অংশ আছে। ডপলাৰ ষ্টাডিজে মাছটোৰ ভিতৰত বৃদ্ধি পোৱা ভাস্কুলাৰিটি দেখুৱাইছে। গলষ্টোন বা বিলিয়ারি ডাক্টাল ডাইলেচনৰ কোনো প্ৰমাণ নাই। লিভ…
```

### S5 judge fail 76

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
থোকপা মশিং তাকপা — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] জন্ম তারিখ [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
Admission [[ADMISSION_NUMBER|ADM-2024-0312]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Doctor [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | Course / advice:
রোগীনা ১২ মার্চ ২০২৪ তারিখ ০২:৩০ ঘণ্টায় তীব্র অ্যাপেন্ডিসাইটিসৰ বাবে জরুরি অ্যাপেন্ডেক্টমি করখি। ল্যাপারোস্কোপিক পদ্ধতিৰে অপারেশনটি জটিলতাহীন আছিল। অপারেশন পরবর্তী সুস্থতা স্বাভাবিক ভাইটালৰ সৈতে ভ…
```

### S5 judge fail 77

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]]
থেকে [[HOSPITAL_NAME|Regional Medical Center Imphal]] / [[DOCTOR_NAME|Dr. Raj Kumar Singh]]
বিষয়ে: [[PATIENT_NAME|Thokchom Sanjit]], [[AGE|38]] / [[GENDER|Male]], জেলা [[DISTRICT|Imphal East]]
কারণ: ওজন হ্রাস এবং উচ্চ রক্তচাপ মূল্যায়নের সাথে দীর্ঘস্থায়ী কাশি

প্রিয় সহকর্মী,

আমি রেফার করছি [[PATIENT_NAME|Thokchom Sanjit]], একজন ৩৮ বছরের পুরুষ ধর্মীয় কর্মী ইম্ফল ইস্ট জেলা থেকে, সন্দেহজনক ফুসফুসের যক্ষ্মা মূল্যায়নের জন্য এবং নতুনভাবে নির্ণয় করা উচ্চ র…
```

### S5 judge fail 78

- **What:** linguistic judge **fail** on `radiology_report` (`mni`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Radiology Report — [[HOSPITAL_NAME|Regional Institute of Medical Sciences, Imphal]] | [[PATIENT_NAME|Lal Singh]] [[AGE|38]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Kh. Ratan Singh]]
Findings: Chest plain radiograph was performed. The lungs are clear without any consolidations, pleural effusions, or pneumothorax. The heart size is within normal limits. The bony thorax, including the ribs and clavicles, appears unremark…
```

### S5 judge fail 79

- **What:** linguistic judge **fail** on `discharge_summary` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|Government Medical College, Hingoli]]
[[PATIENT_NAME|Ramesh Patil]] DOB [[DOB|1957-03-15]] [[AGE|67]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0412]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] | उपचार / मार्गदर्शन: रुग्ण अस्वस्थतेसह मोठ्या नैराश्य विकारासह येतो. लक्षणांमध्ये सतत कमी मनस्थिती, ॲनहेडोनिया, झोपेत अडथळे आणि आर्थिक परिस्थितीबद्दलची अतिशय चिंता यांचा समावेश आहे. रुग्ण घरी वाढलेली चिडचिड आणि कॉल सेंटर ऑपर…
```

### S5 judge fail 80

- **What:** linguistic judge **fail** on `referral_letter` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
संदर्भ पत्र [[REFERRAL_ID|REF-2024-0815]] कडून [[HOSPITAL_NAME|Rural Health Centre Hingoli]] / [[DOCTOR_NAME|Dr. Prakash Kadam]]
विषय: [[PATIENT_NAME|Ramesh Patil]], [[AGE|67]] / [[GENDER|Male]], जिल्हा [[DISTRICT|Hingoli]]
कारण: गेल्या तीन आठवड्यांपासून सतत खोकला आणि श्वास घेण्यास त्रास, सोबत टाइप 2 मधुमेह आणि उच्च रक्तदाबाचा इतिहास आहे.

आदरणीय महोदय/महोदया,

आम्ही आमच्या रुग्णाला पुढील मूल्यमापन आणि व्यवस्थापनासाठी संदर्भित करत आहोत. रुग्ण रमेश पाटील, हिंघोळीतील ग्रामीण भागातील 67 वर्षांचा प…
```

### S5 judge fail 81

- **What:** linguistic judge **fail** on `radiology_report` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Imaging report — [[HOSPITAL_NAME|District Hospital Hingoli]] | [[PATIENT_NAME|Ramesh Patil]] [[AGE|67]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Prakash Deshmukh]]
Findings: Chest radiograph reveals bilateral upper zone fibrotic changes consistent with healed pulmonary tuberculosis. Multiple calcified lymph nodes noted in bilateral hilar regions. Evidence of chronic obstructive pulmonary disease with hyperinflation. No…
```

### S5 judge fail 82

- **What:** linguistic judge **fail** on `referral_letter` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
संदर्भ [[REFERRAL_ID|REF-2024-TB-001]]
[[HOSPITAL_NAME|Jalna District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Deshmukh]] कडून
विषय: [[PATIENT_NAME|Savitri Patil]], [[AGE|64]] / [[GENDER|Female]], जिल्हा [[DISTRICT|Jalna]]
कारण: ३ महिन्यांपासून सतत खोकला, वजन कमी होणे आणि श्वास घेण्यास त्रास, तसेच उच्च रक्तदाब आणि टाईप २ मधुमेह मेलिटसचा इतिहास.

आदरणीय सहकारी,

आम्ही [[PATIENT_NAME|Savitri Patil]] या ६४ वर्षीय गृहिणी, शहरी जालना येथील, संशयित फुफ्फुसाचा क्षयरोग आणि सह-व्याधी असलेल्या असंसर्गजन्य आ…
```

### S5 judge fail 83

- **What:** linguistic judge **fail** on `radiology_report` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
रेडिओलॉजी अहवाल — [[HOSPITAL_NAME|Jalna District Hospital]] | [[PATIENT_NAME|Savitri Bai]] [[AGE|64]] [[GENDER|Female]]
एमआरएन [[MRN|MRN-2024-0915-001]] एनकाउंटर [[ENCOUNTER_ID|ENC-2024-0915-001]] | डॉ. [[DOCTOR_NAME|Dr. Prakash Deshmukh]] यांनी कळवले आहे.
निष्कर्ष:
छातीचा साधा क्ष-किरण [[PATIENT_NAME|Savitri Bai]] वर केला गेला, जी जालना जिल्ह्यातील ६४ वर्षांची महिला आहे. हा अभ्यास १५ सप्टेंबर २०२४ रोजी केला गेला.
कोणतेही सक्रिय इन्फिल्ट्रेट्स किंवा कन्सोलिडेशनशिवाय फुफ्फुसे स्पष्ट आहेत. कोणतेह…
```

### S5 judge fail 84

- **What:** linguistic judge **fail** on `er_triage_notes` (`mr`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
आपत्कालीन विभाग तपासणी — [[HOSPITAL_NAME|Jalna District Civil Hospital]] भेट [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|Savitri Bai]] [[AGE|64]] [[GENDER|Female]] वॉर्ड [[WARD_NUMBER|ER]] बेड [[BED_NUMBER|15]]
रुग्णवाहिकेने सकाळी 08:30 वाजता आले. वाहनाचा नोंदणी क्रमांक: [[VEHICLE_REGISTRATION|MH-22-AB-1234]].
पतीसोबत आलेले, [[RELATIVE_NAME|Ramesh Patil]]. संपर्क क्रमांक: [[PHONE_NUMBER|9876543210]].
उपचार करणारे डॉक्टर: [[DOCTOR_NAME|Dr. Vijay Deshmukh]].
मुख्य तक्रार: घरी पडल्यामुळे डाव…
```

### S5 judge fail 85

- **What:** linguistic judge **fail** on `automated_sms` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|Geeta Das]]: तपाईँको oncology फलो-अप [[APPOINTMENT_ID|APT-240521-01]] मा [[HOSPITAL_NAME|Jalpaiguri District Hospital]] सँग [[DOCTOR_NAME|Dr. Ananda Roy]] छ। कृपया आफ्नो [[MRN|MRN-2024-0815-001]] ल्याउनुहोस् र 15 min अगाडि आउनुहोस्। पुष्टि गर्नका लागि [[PHONE_NUMBER|9876543210]] मा कल गर्नुहोस्।
```

### S5 judge fail 86

- **What:** linguistic judge **fail** on `insurance_claim` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA दाबी — नीति [[INSURANCE_POLICY_NUMBER|POL-WB-2024-1234]]
[[PATIENT_NAME|Geeta Das]] [[AGE|48]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|203835321155]]
अस्पताल [[HOSPITAL_NAME|District Hospital Jalpaiguri]] जिल्ला [[DISTRICT|Jalpaiguri]]
मोटर / आर टी ए सवारी साधन [[VEHICLE_REGISTRATION|WB02AB1234]] (एक पटक मात्र)।
PAN [[PAN_NUMBER|ABCDE1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30912345678901]]
MRN [[MRN|WB-2024-001]]
डाक्टरको नाम [[DOCTOR_NAME|Ananda Sharma]]

हालैको क…
```

### S5 judge fail 87

- **What:** linguistic judge **fail** on `hospital_billing` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
बिल — [[HOSPITAL_NAME|Jalpaiguri District Hospital]] जिल्ला [[DISTRICT|Jalpaiguri]]
पिन [[PIN_CODE|736101]] बिरामी [[PATIENT_NAME|Geeta Das]] MRN [[MRN|WB-JDH-2024-0815-001]]
ठेगाना [[RESIDENTIAL_ADDRESS|Village: Madhabdi, Post: Jalpaiguri, West Bengal 736101]] फोन [[PHONE_NUMBER|9876543210]]
इमेल [[EMAIL_ADDRESS|geeta.das.jh@example.com]] PAN [[PAN_NUMBER|WBJPD1234F]]
ल्यान्डलाइन [[TELEPHONE_LANDLINE|03562-222333]] गाडी [[VEHICLE_REGISTRATION|WB58AB1234]] (एक पटक)
आधार [[AADHAAR_NUMBER|2915123…
```

### S5 judge fail 88

- **What:** linguistic judge **fail** on `prescription` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|काठमाण्डौ मेडिकल सेन्टर]]
बिरामी [[PATIENT_NAME|रमेश शर्मा]], [[AGE|18]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-0815-001]]
डाक्टर [[DOCTOR_NAME|डा. आनन्द अधिकारी]]
फोन: [[PHONE_NUMBER|9876543210]]

निदान: Acute Lymphoblastic Leukemia (ALL), B-cell type, Stage III
बिरामीमा थकान, फिक्कापन र पुनरावर्ती सङ्क्रमणका लक्षणहरू छन्। अस्थि मज्जा बायोप्सीले निदान पुष्टि गर्दछ।

उपचार योजना:
1. इन्डक्सन केमोथेरापी:
   - Vincristine 2 mg IV पहिलो दिन
   - Prednisone 60 mg PO २८ दिन…
```

### S5 judge fail 89

- **What:** linguistic judge **fail** on `asha_worker_note` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
आशा टिपोट — गाउँ [[VILLAGE|Rangit]], जिल्ला [[DISTRICT|Darjiling]]
बिरामी [[PATIENT_NAME|Sunita Rai]], [[AGE|18]] / [[GENDER|Female]]
आशा: [[ASHA_WORKER_NAME|Meera Tamang]] | फोन [[PHONE_NUMBER|9876543210]]
भ्रमणको निष्कर्ष: बिरामीलाई 3 दिनदेखि ज्वरो र शरीर दुख्ने समस्या छ। बिरामीले टाउको दुख्ने र हल्का खोकी लागेको बताएका छन्। ज्वरोका लागि प्यारासिटामोल खान सल्लाह दिइएको छ र थप जाँचका लागि PHC पठाइएको छ। [[RELATIVE_NAME|Ramesh Rai]] (बुबा) बिरामीसँगै आउनुभएको थियो। [[BPL_RATION_CARD|BPL-WB-DARJ…
```

### S5 judge fail 90

- **What:** linguistic judge **fail** on `automated_sms` (`ne`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
नमस्ते [[PATIENT_NAME|Sunita Thapa]] तपाईँको ANC अपोइन्टमेन्ट [[APPOINTMENT_ID|APT-240521-01]] [[HOSPITAL_NAME|Darjiling PHC]] मा २१-मे १०:३० मा [[DOCTOR_NAME|Dr. Maya Gurung]] सँग पुष्टि गरिएको छ। कृपया तपाईँको [[MRN|MRN-2024-0815-001]] ल्याउनुहोस्। पुष्टि गर्नका लागि [[PHONE_NUMBER|9876512340]] मा कल गर्नुहोस्।
```

### S5 judge fail 91

- **What:** linguistic judge **fail** on `surgical_note` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ଅପରେସନ୍ ଟିପ୍ପଣୀ — [[HOSPITAL_NAME|Jajpur District Hospital]] ଭର୍ତ୍ତି [[ADMISSION_NUMBER|ADM-2024-0815-001]] ୱାର୍ଡ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Sushila Devi]] [[AGE|25]] [[GENDER|Female]] ଶଲ୍ୟ ଚିକିତ୍ସକ [[DOCTOR_NAME|Dr. Ramesh Patnaik]]
ପ୍ରକ୍ରିୟା: ଜରୁରୀକାଳୀନ ଲାପାରୋସ୍କୋପିକ୍ ଆପେଣ୍ଡେକ୍ଟୋମି
ନିଶ୍ଚେତକ: ସାଧାରଣ ନିଶ୍ଚେତକ
ଅସ୍ତ୍ରୋପଚାର ପୂର୍ବ ରୋଗ ନିରୂପଣ: ତୀବ୍ର ଆପେଣ୍ଡିସାଇଟିସ୍
ଅସ୍ତ୍ରୋପଚାର ପରବର୍ତ୍ତୀ ରୋଗ ନିରୂପଣ: ତୀବ୍ର ଆପେଣ୍ଡିସାଇଟିସ୍ ସହିତ ଛିଦ୍ର
ପର୍ଯ୍ୟବେକ୍ଷଣ: ଆପେଣ୍ଡିକ୍ସରେ ଶେଷରେ 2cm ଛିଦ୍ର ଥିଲା। ପେରିଟୋନାଇଟିସ୍‌ର…
```

### S5 judge fail 92

- **What:** linguistic judge **fail** on `lab_report` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ପରୀକ୍ଷା ରିପୋର୍ଟ — ଜିଲ୍ଲା ଡାକ୍ତରଖାନା ଜଜପୁର ଜିଲ୍ଲା [[DISTRICT|Jajapur]]
[[MRN|[[MRN|JH-2024-0815-001]]]] ରୋଗୀ ପରିଚୟ [[PATIENT_ID|[[PATIENT_ID|JH-2024-0815-001]]]]
[[PATIENT_NAME|Sushila Devi]] [[AGE|25]] [[GENDER|Female]] ଫୋନ୍ [[PHONE_NUMBER|9438765432]]
ଦ୍ୱାରା ନିର୍ଦ୍ଦେଶିତ [[DOCTOR_NAME|Dr. Priya Patnaik]]
ତାରିଖ: 15 August 2024

ରୋଗୀ ବିବରଣୀ:
25 ବର୍ଷର ମହିଳା, G2P1, 28 ସପ୍ତାହ ଗର୍ଭଧାରଣ, ନିୟମିତ ପ୍ରସବ ପୂର୍ବ ଯାଞ୍ଚ। ଶେଷ ଋତୁସ୍ରାବ ତାରିଖ: 15 January 2024। ରକ୍ତ ଗୋଷ୍ଠୀ: O positive। କୌଣସି ଜଣାଶୁଣା ଆଲର୍ଜି ନାହିଁ।…
```

### S5 judge fail 93

- **What:** linguistic judge **fail** on `opd_slip` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ଆଉଟପେସେଣ୍ଟ ବିଭାଗ ସ୍ଲିପ୍ | ଜିଲ୍ଲା ଡାକ୍ତରଖାନା ଯାଜପୁର | ID [[HOSPITAL_ID|DH-JJ-001]]
ରୋଗୀ: [[PATIENT_NAME|Sushila Devi]] | ଜନ୍ମ ତାରିଖ [[DOB|1999-05-15]] | ବୟସ: [[AGE|25]] | ଲିଙ୍ଗ: [[GENDER|Female]]
ବୃତ୍ତି: [[OCCUPATION|Homemaker]] | MRN: [[MRN|OPD-2024-0892]] | ଡାକ୍ତର: [[DOCTOR_NAME|Dr. Pravat Kumar]]
ସମ୍ପର୍କୀୟ: [[RELATIVE_NAME|Radhika Devi]] | ଫୋନ୍: [[PHONE_NUMBER|9438765432]]
ରେଜିଷ୍ଟ୍ରାର୍ କର୍ମଚାରୀ ID: [[EMPLOYEE_ID|EMP-4412]] | ଜିଲ୍ଲା: [[DISTRICT|Jajapur]]
ମୁଖ୍ୟ ଅଭିଯୋଗ: 3 ସପ୍ତାହ ଧରି କ୍ରମାଗତ କାଶ …
```

### S5 judge fail 94

- **What:** linguistic judge **fail** on `opd_slip` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ଆଉଟପେସେଣ୍ଟ ବିଭାଗ ସ୍ଲିପ୍ | [[HOSPITAL_NAME|ମେଟ୍ରୋ ହସ୍ପିଟାଲ୍]] | ID [[HOSPITAL_ID|DH-NAB-001]]
ରୋଗୀ: [[PATIENT_NAME|ରମେଶ ଚନ୍ଦ୍ର ପାତ୍ର]] | ଜନ୍ମ ତାରିଖ [[DOB|1965-03-15]] | ବୟସ: [[AGE|59]] | ଲିଙ୍ଗ: [[GENDER|Female]]
ଚାକିରି: [[OCCUPATION|ସରକାରୀ କର୍ମଚାରୀ]] | MRN: [[MRN|OPD-2024-0815-001]] | ଡାକ୍ତର: [[DOCTOR_NAME|ଡାକ୍ତର ପ୍ରଦୀପ କୁମାର]]
ସମ୍ପର୍କୀୟ: [[RELATIVE_NAME|ସୁନିତା ଦେବୀ]] | ଫୋନ୍: [[PHONE_NUMBER|9437812345]]
ରେଜିଷ୍ଟ୍ରାର EmpID: [[EMPLOYEE_ID|EMP-2024-001]] | ଜିଲ୍ଲା: [[DISTRICT|ଖୋର୍ଦ୍ଧା]]
ମୁଖ୍ୟ ଅଭିଯୋଗ:…
```

### S5 judge fail 95

- **What:** linguistic judge **fail** on `surgical_note` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ଅପରେସନ୍ ରିପୋର୍ଟ — [[HOSPITAL_NAME|ସିଟି ହସ୍ପିଟାଲ୍]] ଭର୍ତ୍ତି [[ADMISSION_NUMBER|ADM-2024-1123]] ୱାର୍ଡ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|ରାମ ପ୍ରସାଦ]] [[AGE|59]] [[GENDER|Female]] ଶଲ୍ୟ ଚିକିତ୍ସକ [[DOCTOR_NAME|ଡକ୍ଟର କୁମାର]]
ପ୍ରକ୍ରିୟା / ଅନୁସନ୍ଧାନ:
ସାଧାରଣ ନିଶ୍ଚେତକ ଅଧୀନରେ ରୋଗୀଙ୍କର ସନ୍ଦେହଜନକ ଯକ୍ଷ୍ମା ଜନିତ ଲିମ୍ଫାଡେନାଇଟିସ୍ ପାଇଁ ଡାହାଣ ଗ୍ରୀବା ଲିମ୍ଫ ନୋଡ୍ ଅପସାରଣ କରାଯାଇଥିଲା। ଅସ୍ତ୍ରୋପଚାର ପୂର୍ବରୁ ପରୀକ୍ଷାଗୁଡ଼ିକରେ ବୃଦ୍ଧି ପାଇଥିବା ESR ଏବଂ ପଜିଟିଭ୍ ମାଣ୍ଟୋକ୍ସ ଟେଷ୍ଟ ଦେଖାଯାଇଥିଲା। ଅସ୍ତ୍ରୋପଚାର ସମୟରେ ଅନୁସନ୍ଧାନରେ ଏକାଧିକ ପରସ୍ପର…
```

### S5 judge fail 96

- **What:** linguistic judge **fail** on `prescription` (`or`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ପ୍ରେସକ୍ରିପସନ୍ — [[HOSPITAL_NAME|Nabarangapur District Hospital]]
ରୋଗୀ [[PATIENT_NAME|Malti Devi]], [[AGE|59]] / [[GENDER|Female]], MRN [[MRN|RX-2024-001]]
ଡାକ୍ତର [[DOCTOR_NAME|Dr. Ramesh Patnaik]]
ଔଷଧ: Amoxicillin 500mg tablet ଦିନକୁ ତିନିଥର, 5 ଦିନ ପାଇଁ
Paracetamol 500mg tablet ଯନ୍ତ୍ରଣା ପାଇଁ ଆବଶ୍ୟକ ଅନୁଯାୟୀ, ଦିନକୁ ଚାରିଥର
Metronidazole 400mg tablet ଦିନକୁ ଦୁଇଥର, 3 ଦିନ ପାଇଁ
ସମ୍ପୂର୍ଣ୍ଣ ଶଯ୍ୟା ବିଶ୍ରାମ 48 ଘଣ୍ଟା ପାଇଁ, 2 ସପ୍ତାହ ପାଇଁ ଭାରୀ ଜିନିଷ ଉଠାଇବା ବର୍ଜନ କରନ୍ତୁ
ଅନୁବର୍ତ୍ତନ ସାକ୍ଷାତକାର 7 ଦିନ ପରେ [[HOSPITAL_…
```

### S5 judge fail 97

- **What:** linguistic judge **fail** on `opd_slip` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ਬਾਹਰੀ ਮਰੀਜ਼ ਪਰਚੀ | [[HOSPITAL_NAME|District Hospital Moga]] | ID [[HOSPITAL_ID|DH-MOG-001]]
ਮਰੀਜ਼: [[PATIENT_NAME|Salkhan Varma]] | ਜਨਮ ਮਿਤੀ [[DOB|2006-05-15]] | ਉਮਰ: [[AGE|18]] | ਲਿੰਗ: [[GENDER|Male]]
ਕਿੱਤਾ: [[OCCUPATION|Stall and Market Salespersons, Other]] | MRN: [[MRN|OPD-2024-MOG-001]] | ਡਾਕਟਰ: [[DOCTOR_NAME|Dr. Gurpreet Singh]]
ਸੰਬੰਧੀ: [[RELATIVE_NAME|Balwinder Singh]] | ਫ਼ੋਨ: [[PHONE_NUMBER|9876543210]]
ਰਜਿਸਟਰਾਰ EmpID: [[EMPLOYEE_ID|REG-2024-015]] | ਜ਼ਿਲ੍ਹਾ: [[DISTRICT|Moga]]

ਮੁੱਖ ਸ਼ਿਕ…
```

### S5 judge fail 98

- **What:** linguistic judge **fail** on `surgical_note` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ਸਰਜੀਕਲ ਨੋਟ — [[HOSPITAL_NAME|ਗੁਰੂ ਨਾਨਕ ਹਸਪਤਾਲ]] ਦਾਖਲਾ [[ADMISSION_NUMBER|ADM-2024-0815-001]] ਵਾਰਡ [[WARD_NUMBER|B2]]
[[PATIENT_NAME|ਜਸਵੀਰ ਸਿੰਘ]] [[AGE|18]] [[GENDER|Male]] ਸਰਜਨ [[DOCTOR_NAME|ਡਾ. ਅਮਰਿੰਦਰ ਸਿੰਘ]]
ਪ੍ਰਕਿਰਿਆ / ਖੋਜਾਂ:
ਮਰੀਜ਼ 24 ਘੰਟੇ ਤੋਂ ਤੇਜ਼ ਸੱਜੇ ਹੇਠਲੇ ਪੇਟ ਵਿੱਚ ਦਰਦ ਨਾਲ ਪੇਸ਼ ਹੋਇਆ। ਪਰੀਖਣ 'ਤੇ, McBurney's point 'ਤੇ ਰੀਬਾਉਂਡ ਟੈਂਡਰਨੈੱਸ ਦੇ ਨਾਲ ਦਰਦ ਪਾਇਆ ਗਿਆ। CT ਸਕੈਨ ਨੇ ਸ਼ੁਰੂਆਤੀ ਪਰਫੋਰੇਸ਼ਨ ਦੇ ਨਾਲ ਤੇਜ਼ ਅਪੈਂਡਿਸਾਈਟਿਸ ਦਿਖਾਇਆ। ਮਰੀਜ਼ ਨੂੰ ਐਮਰਜੈਂਸੀ ਅਪੈਂਡੇਕਟੋਮੀ ਲਈ OT ਵਿੱਚ ਲਿਜਾਇਆ ਗਿਆ।
ਖੋਜਾਂ: ਸਿਖਰ 'ਤੇ 2cm ਪ…
```

### S5 judge fail 99

- **What:** linguistic judge **fail** on `prescription` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ਪਰਚੀ — ਜ਼ਿਲ੍ਹਾ ਹਸਪਤਾਲ ਮੋਗਾ
[[HOSPITAL_NAME|ਜ਼ਿਲ੍ਹਾ ਹਸਪਤਾਲ ਮੋਗਾ]]
ਮਰੀਜ਼ [[PATIENT_NAME|Gurpreet Singh]], [[AGE|18]] / [[GENDER|Male]], MRN [[MRN|RX-2024-001]]
ਡਾਕਟਰ [[DOCTOR_NAME|Dr. Harpreet Kaur]]
ਫ਼ੋਨ: [[PHONE_NUMBER|9876543210]]
ਪਤਾ: [[RESIDENTIAL_ADDRESS|123 Gandhi Nagar, Moga, Punjab 142001]]
ਜ਼ਿਲ੍ਹਾ: [[DISTRICT|Moga]]
ਮਰੀਜ਼ ਆਈ ਡੀ: [[PATIENT_ID|PID-MGH-2024-001]]
ਆਭਾ ਆਈ ਡੀ: [[ABHA_ID|12-3456-7890-1234]]

Rx: Paracetamol 500mg, 1 ਗੋਲੀ ਹਰ 6 ਘੰਟੇ ਬਾਅਦ ਬੁਖ਼ਾਰ ਲਈ ਲੋੜ ਅਨੁਸਾਰ
     Azithromycin 25…
```

### S5 judge fail 100

- **What:** linguistic judge **fail** on `surgical_note` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ਸਰਜੀਕਲ ਨੋਟ — [[HOSPITAL_NAME|Civil Hospital Jalandhar]] ਦਾਖਲਾ [[ADMISSION_NUMBER|ADM-2024-0315]] ਵਾਰਡ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Kiran Kaur]] [[AGE|29]] [[GENDER|Female]] ਸਰਜਨ [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ਪ੍ਰਕਿਰਿਆ / ਨਤੀਜੇ:
ਮਰੀਜ਼ ਦੀ 38 ਹਫ਼ਤਿਆਂ ਦੀ ਗਰਭ ਅਵਸਥਾ ਵਿੱਚ ਭਰੂਣ ਦੀ ਤਕਲੀਫ਼ ਲਈ ਐਮਰਜੈਂਸੀ ਹੇਠਲਾ ਹਿੱਸਾ ਸੀਜ਼ੇਰੀਅਨ ਸੈਕਸ਼ਨ ਹੋਈ ਹੈ। ਪ੍ਰਕਿਰਿਆ ਸਫਲਤਾਪੂਰਵਕ ਪੂਰੀ ਹੋਈ ਅਤੇ ਜੀਵਤ ਬੱਚੀ ਦਾ ਜਨਮ ਹੋਇਆ। ਅਨੁਮਾਨਿਤ ਖੂਨ ਦਾ ਨੁਕਸਾਨ ਘੱਟੋ-ਘੱਟ ਸੀ। ਮਰੀਜ਼ ਸਰਜਰੀ ਤੋਂ ਬਾਅਦ ਸਥਿਰ ਹੈ।

[[BED_NUMBER|OT-07]] [[MRN|MRN-2024-0315…
```

### S5 judge fail 101

- **What:** linguistic judge **fail** on `lab_report` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ਲੈਬ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|Civil Hospital Jalandhar]] ਜ਼ਿਲ੍ਹਾ [[DISTRICT|Jalandhar]]
MRN [[MRN|JH-2024-0815-001]] ਮਰੀਜ਼ ਆਈ ਡੀ [[PATIENT_ID|JH-78945]]
[[PATIENT_NAME|Jaspreet Kaur]] [[AGE|29]] [[GENDER|Female]] ਫੋਨ [[PHONE_NUMBER|9876543210]]
ਦੁਆਰਾ ਆਰਡਰ ਕੀਤਾ ਗਿਆ [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ਮਿਤੀ: 15 August 2024

ਮਰੀਜ਼ ਸ਼ਿਕਾਇਤਾਂ ਨਾਲ ਪੇਸ਼ ਹੁੰਦਾ ਹੈ ਪਿਛਲੇ 5 ਦਿਨਾਂ ਤੋਂ ਥਕਾਵਟ, ਹਲਕਾ ਬੁਖਾਰ, ਅਤੇ ਸਰੀਰ ਵਿੱਚ ਦਰਦ। ਇਤਿਹਾਸ ਤੋਂ ਪਤਾ ਲੱਗਦਾ ਹੈ ਘਰੇਲੂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਕਾਰਨ ਨਵੀਨਤਮ ਤਣਾਅ। ਕੋਈ ਮਹੱਤਵਪੂਰਨ ਪੁਰਾਣਾ ਡਾਕਟਰੀ ਇ…
```

### S5 judge fail 102

- **What:** linguistic judge **fail** on `phc_register` (`pa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
PHC ਰਜਿਸਟਰ — [[HOSPITAL_NAME|Primary Health Centre Bhikhiwind]] ਪਿੰਡ [[VILLAGE|Bhikhiwind]] ਜ਼ਿਲ੍ਹਾ [[DISTRICT|Jalandhar]]
[[PATIENT_NAME|Harpreet Kaur]] [[AGE|29]] [[GENDER|Female]] | ਮਰੀਜ਼ ਲਗਾਤਾਰ ਖੰਘ ਅਤੇ ਭਾਰ ਘਟਣ ਦੀ ਜਾਂਚ ਲਈ ਪੇਸ਼ ਹੋਈ।

ਮਰੀਜ਼ 29 ਸਾਲ ਦੀ ਕੁਆਰੀ ਘਰੇਲੂ ਔਰਤ ਹੈ, ਜੋ ਭਿਖੀਵਿੰਡ ਪਿੰਡ ਤੋਂ ਹੈ। ਉਹ ਪਿਛਲੇ ਤਿੰਨ ਹਫ਼ਤਿਆਂ ਤੋਂ ਖੰਘ ਦੀ ਰਿਪੋਰਟ ਕਰਦੀ ਹੈ, ਜੋ ਕਦੇ-ਕਦੇ ਘੱਟ ਬਲਗ਼ਮ ਨਾਲ ਹੁੰਦੀ ਹੈ ਅਤੇ ਸ਼ਾਮ ਨੂੰ ਘੱਟ ਬੁਖ਼ਾਰ ਰਹਿੰਦਾ ਹੈ। ਉਸ ਨੂੰ ਪੂਰੇ ਸਰੀਰ ਵਿੱਚ ਕਮਜ਼ੋਰੀ ਮਹਿਸੂਸ ਹੁੰਦੀ ਹੈ ਅਤੇ ਪਿਛਲੇ ਮਹੀਨੇ ਲਗਭਗ 3 ਕਿਲੋ ਭਾਰ ਘਟਾਇਆ …
```

### S5 judge fail 103

- **What:** linguistic judge **fail** on `prescription` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
औषध-पत्रम् — [[HOSPITAL_NAME|Bundi District Hospital]]
रोगी [[PATIENT_NAME|Kavita Kumari]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|BUN-2024-0012]]
वैद्यः [[DOCTOR_NAME|Dr. Rajesh Sharma]]
दूरभाषः: [[PHONE_NUMBER|9414012345]]
आभा-परिचयः: [[ABHA_ID|12-3456-7890-1234]]
रोगी-परिचयः: [[PATIENT_ID|PID-BUN-2024-0012]]
मण्डलम्: [[DISTRICT|Bundi]]
सङ्केतः: [[RESIDENTIAL_ADDRESS|15 Nehru Colony, Ward 12, Bundi]]

मुख्य-आक्षेपः: त्रि-सप्ताह-पर्यन्तं मन्द-ज्वरेण सह 2 किलोग्राम-भार-हानिः।

निदानम्: (प्रथ…
```

### S5 judge fail 104

- **What:** linguistic judge **fail** on `insurance_claim` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
तृतीय-पक्ष-प्रशासक-दावा — नीति [[INSURANCE_POLICY_NUMBER|POL-RJ-2024-1123]]
[[PATIENT_NAME|Kavita Kumari]] [[AGE|19]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|239874651023]]
चिकित्सालय [[HOSPITAL_NAME|Bundi District Hospital]] जनपद [[DISTRICT|Bundi]]
मोटर / RTA वाहनम् [[VEHICLE_REGISTRATION|RJ03AB1234]] (एकवारम् एव)।
पैन [[PAN_NUMBER|RJUKP1234C]] आई एफ एस सी [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30200012345678]]
[[BANK_ROUTING_NUMBER|SBIN0001234]] [[CREDIT_CARD_NUMBER|411111111111…
```

### S5 judge fail 105

- **What:** linguistic judge **fail** on `asha_worker_note` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
आशा-कार्यकर्ता-टिप्पणी — ग्रामः [[VILLAGE|Keshavpura]], जनपदः [[DISTRICT|Bundi]]
हितग्राही [[PATIENT_NAME|Kavita Sharma]], [[AGE|19]] / [[GENDER|Female]]
आशा-कार्यकर्ता: [[ASHA_WORKER_NAME|Suman Devi]] | दूरभाषः [[PHONE_NUMBER|9876543210]]
भ्रमण-प्रतिवेदनम्: रोगी ज्वरं, शरीरशूलं, मृदुशिरोवेदनां च द्विभ्यां दिवसौ उपस्थापयति। सा अल्पाहारं सामान्य-दुर्बलतां च सूचयति। न किमपि महत्त्वपूर्णः पूर्व-चिकित्सा-इतिहासः लिखितः।

चिकित्सा-मूल्याङ्कनम्: तापः 100.8°F, नाडी 92/min, श्वसन-गतिः 18/min, रक्तचापः …
```

### S5 judge fail 106

- **What:** linguistic judge **fail** on `automated_sms` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
प्रिय [[PATIENT_NAME|Rohan Kumar]], भवतः क्षयरोग-अनुवर्ती-नियुक्तिः [[HOSPITAL_NAME|District Hospital Kanpur]] दिनाङ्के 15-मै प्रातः 10:30 वादने [[DOCTOR_NAME|Dr. Amit Singh]] इत्यनेन सह नियोजिता अस्ति। कृपया स्वकीयं [[MRN|MRN-2024-0815-001]] आनयन्तु आगत्य 15 निमेषान् पूर्वम्। कस्यापि प्रश्नाय [[PHONE_NUMBER|9876543210]] सम्पर्कं कुर्वन्तु। नियुक्ति-परिचयः: [[APPOINTMENT_ID|APT-240515-01]]।
```

### S5 judge fail 107

- **What:** linguistic judge **fail** on `insurance_claim` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-UP-2024-9876]]
[[PATIENT_NAME|Aarav Khan]] [[AGE|19]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|876543210987]]
[[DISTRICT|Kanpur Nagar]]

Patient History and Clinical Summary:
The patient, a 19-year-old male student from Kanpur Nagar, presented with persistent fatigue, recurrent fevers, and unexplained bruising over the past three months. Initial blood work revealed pancytopenia. A subsequent bone marrow aspiration and biopsy confirmed a diagnosis…
```

### S5 judge fail 108

- **What:** linguistic judge **fail** on `hospital_billing` (`sa`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|District Hospital Kanpur]] District [[DISTRICT|Kanpur Nagar]]
PIN [[PIN_CODE|208001]] Patient [[PATIENT_NAME|Rohan Sharma]] MRN [[MRN|MRN-UP-2024-0815]]
Address [[RESIDENTIAL_ADDRESS|15 Shivaji Nagar, Ward 12]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.sharma@example.com]] PAN [[PAN_NUMBER|ABCDE1234F]]
Landline [[TELEPHONE_LANDLINE|0512-2345678]] Vehicle [[VEHICLE_REGISTRATION|UP78AB1234]] (once)
Aadhaar [[AADHAAR_NUMBER|157815659387]] Policy [[INSU…
```

### S5 judge fail 109

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ASHA Karya Patra — Gaon [[VILLAGE|Baidpur]], Jila [[DISTRICT|Dumka]]
Labharthi [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Santi Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Bhraman Phal: Rogi dekhay lagatar khansi tin hapta se, kam jwar, aur 5 kg vajan kam hona. Unhe batate hain kabhi-kabhi saans phoolna aur raat ko paseena aana. Rakt chapa 145/90 mmHg likha gaya hai. Random rakt sharkara 180 mg/dL dikhta hai. Rogi ek jaani-maani diabetic hai, metformin…
```

### S5 judge fail 110

- **What:** linguistic judge **fail** on `automated_sms` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|Purani Devi]]: Aŋa buku [[APPOINTMENT_ID|APT-240521-01]] te [[DOCTOR_NAME|Dr. Kumar]] te [[HOSPITAL_NAME|Dumka PHC]] te ᱒᱑-May te ᱑᱐:᱓᱐ AM. Dayak Aŋa [[MRN|MRN-2024-0815-001]] card. Dayak te [[PHONE_NUMBER|9876512340]] te buku.
```

### S5 judge fail 111

- **What:** linguistic judge **fail** on `hospital_billing` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
INVOICE
[[HOSPITAL_NAME|Dumka District Hospital]]
[[DISTRICT|Dumka]]
PIN [[PIN_CODE|814101]]
Patient [[PATIENT_NAME|Purani Devi]] MRN [[MRN|MRN-JH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Village Shivpur, PO Dumka, Jharkhand]]
Phone [[PHONE_NUMBER|9431023456]]
Email [[EMAIL_ADDRESS|purani.devi@example.com]]
PAN [[PAN_NUMBER|AXYPA1234C]]
Landline [[TELEPHONE_LANDLINE|03432-254367]]
Vehicle [[VEHICLE_REGISTRATION|JH01AB1234]] (Ambulance Parking)
Aadhaar [[AADHAAR_NUMBER|241587693456]]
Policy…
```

### S5 judge fail 112

- **What:** linguistic judge **fail** on `phc_register` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] Village [[VILLAGE|Hathbandh]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | Referred for evaluation of persistent cough
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
Patient is an 18-year-old male loader from Hathbandh village, Bankura district, referred by ASHA worker [[ASHA_WORKER_NAME|Phulo Murmu]]. He presents …
```

### S5 judge fail 113

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ASHA note — Gaon [[VILLAGE|Barjora]], Jila [[DISTRICT|Bankura]]
Rogee [[PATIENT_NAME|Ranjan Murmu]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Santi Tudu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit reyag findings: Rogee baya hath kata te kam jagat reyag durghatna tayom hej lena. Ghat sapha ar suture huy akana Jila Hospital te. Rogee 3 din re follow-up lagid ruwar lagid lay akana.

Family reyag biboron: Baba [[RELATIVE_NAME|Sukhu Murmu]] jogajog huy akana. BPL [[BPL_RATION_CARD|BPL-W…
```

### S5 judge fail 114

- **What:** linguistic judge **fail** on `insurance_claim` (`sat`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA Claim Form for General Medicine Admission

Patient Details:
[[PATIENT_NAME|Lal Mohan Murmu]] [[AGE|18]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|987654321098]]

Hospital Details:
Admitted at [[HOSPITAL_NAME|Bankura District Hospital]] located in [[DISTRICT|Bankura]], West Bengal.

Policy and Financial Information:
Policy Number: [[INSURANCE_POLICY_NUMBER|POL-WB-2024-1123]]
PAN: [[PAN_NUMBER|ABCDE1234F]]
Bank Account: [[BANK_ACCOUNT_NUMBER|50200012345678]]
IFSC Code: [[IFSC_CODE|SBIN0001234]…
```

### S5 judge fail 115

- **What:** linguistic judge **fail** on `automated_sms` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S5 judge fail 116

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[HOSPITAL_NAME|Lilavati Hospital, Bandra West, Mumbai]] [[DISTRICT|Mumbai Suburban]]
PIN [[PIN_CODE|400050]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|MRN-MH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|45, Shivaji Park, Dadar West]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|ramesh.kumar@example.com]] PAN [[PAN_NUMBER|ABCDE1234F]]
Landline [[TELEPHONE_LANDLINE|022-23456789]] Vehicle [[VEHICLE_REGISTRATION|MH01AB1234]] (ambulance parking)
Aadhaar [[AADHAAR_NUMBER|2065012530…
```

### S5 judge fail 117

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Sion Hospital, Mumbai]]
[[PATIENT_NAME|Rajesh Kumar]] DOB [[DOB|1992-03-15]] [[AGE|32]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0315]] Ward [[WARD_NUMBER|B3]] Bed [[BED_NUMBER|07]]
Dr [[DOCTOR_NAME|Dr. Amit Patel]] | Course / advice: Patient presented with persistent cough for 3 weeks, low-grade fever, and weight loss of 5 kg. Sputum examination revealed acid-fast bacilli. Chest X-ray showed infiltrates in right upper lobe. Patient also has hypertensi…
```

### S5 judge fail 118

- **What:** linguistic judge **fail** on `insurance_claim` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|Shilpaben Patel]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] account [[BANK_ACCOUNT_NUMBER|6140200123456789]]
Bank routing number [[BANK_ROUTING_NUMBER|SBIN0005678]]
Cre…
```

### S5 judge fail 119

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|Shri Sayaji Hospital]] District [[DISTRICT|Vadodara]]
PIN [[PIN_CODE|390001]] Patient [[PATIENT_NAME|Shilpaben Vasava]] MRN [[MRN|MRN-GJ-2024-0815]]
Address [[RESIDENTIAL_ADDRESS|12, Madhavpura Society, Near Sayaji Baug]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|shilpaben.vasava@example.com]] PAN [[PAN_NUMBER|GJVAP1234C]]
Landline [[TELEPHONE_LANDLINE|0265-2345678]] Vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (once)
Aadhaar [[AADHAAR_NUMBER|291512345678]…
```

### S5 judge fail 120

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Shri Sayaji Hospital]]
[[PATIENT_NAME|Shilpaben Vasava]] DOB [[DOB|1949-04-15]] [[AGE|75]] [[GENDER|Female]]
[[ADMISSION_NUMBER|ADM-2024-0815-042]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patel]] | Course / advice: Patient admitted with acute exacerbation of chronic obstructive pulmonary disease and community-acquired pneumonia. Initial treatment included intravenous antibiotics (Ceftriaxone and Azithromycin), bronchodilators…
```

### S5 judge fail 121

- **What:** linguistic judge **fail** on `opd_slip` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] | ID [[HOSPITAL_ID|GMCH-TVL-001]]
Patient: [[PATIENT_NAME|Lakshmi Narayanan]] | DOB [[DOB|1984-06-15]] | Age: [[AGE|40]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|News Paper Boy]] | MRN: [[MRN|MRN-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Sharma]]
Relative: [[RELATIVE_NAME|Ramesh Kumar]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|REG-001]] | District: [[DISTRICT|Thiruvallur]]
Chie…
```

### S5 judge fail 122

- **What:** linguistic judge **fail** on `prescription` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Government Thiruvallur Medical College Hospital]]
Patient [[PATIENT_NAME|Lakshmi Narayanan]], [[AGE|40]] / [[GENDER|Female]], MRN [[MRN|MRN-TVL-2024-001]]
Dr. [[DOCTOR_NAME|Dr. S. Vijayalakshmi]]

Chief Complaint: Fever and body ache for 3 days.

Diagnosis: Acute viral fever with myalgia.

Rx:
1. Paracetamol 500mg tablet, one tablet every 8 hours as needed for fever.
2. Cetirizine 10mg tablet, one tablet at night.
3. Cough Syrup (Levocetirizine 2.5mg + Montelukast…
```

### S5 judge fail 123

- **What:** linguistic judge **fail** on `insurance_claim` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-TN-2024-8901]]
[[PATIENT_NAME|Lakshmi Narayanan]] [[AGE|40]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] District [[DISTRICT|Thiruvallur]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|TN21K1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0005678]] account [[BANK_ACCOUNT_NUMBER|678901234567]]
Bank routing [[BANK_ROUTING_NUMBER|SBIN000567…
```

### S5 judge fail 124

- **What:** linguistic judge **fail** on `asha_worker_note` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety and sleep disturbances for the past two weeks. He mentions feeling overwhelmed with work responsibilities and has lost interest in his daily walks along Marina Beach. Patient appears withdrawn and reports occasional panic attacks…
```

### S5 judge fail 125

- **What:** linguistic judge **fail** on `automated_sms` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Dear [[PATIENT_NAME|Mahavir Jain]], your appointment [[APPOINTMENT_ID|APT-240521-01]] with [[DOCTOR_NAME|Dr. Anand]] at [[HOSPITAL_NAME|Government General Hospital Chennai]] is confirmed. Please arrive 15 mins early. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876512340]] to reschedule.
```

### S5 judge fail 126

- **What:** linguistic judge **fail** on `insurance_claim` (`ta`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
TPA Claim Form for Tuberculosis & Non-Communicable Diseases

Patient Details:
[[PATIENT_NAME|Mahavir Jain]] [[AGE|34]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|687543210987]]

Claim Details:
Policy [[INSURANCE_POLICY_NUMBER|POL-TN-2024-98765]]
Hospital [[HOSPITAL_NAME|Government Stanley Medical College Hospital]] District [[DISTRICT|Chennai]]

Financial Information:
Bank Account [[BANK_ACCOUNT_NUMBER|6114578901234567]] IFSC [[IFSC_CODE|SBIN0000611]] Routing Number [[BANK_ROUTING_NUMBER|SBIN0006…
```

### S5 judge fail 127

- **What:** linguistic judge **fail** on `hospital_billing` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
[[HOSPITAL_NAME|Government Medical College and Hospital, Nanded]]
District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]]
Patient [[PATIENT_NAME|Rohan Patil]] MRN [[MRN|MRN-NND-2024-001]]
Address [[RESIDENTIAL_ADDRESS|Shivaji Chowk, Nanded City, Maharashtra]]
Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|rohan.patil@example.com]]
Aadhaar [[AADHAAR_NUMBER|203835321155]]
PAN [[PAN_NUMBER|AABPR1234C]]
Insurance [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
Tax ID [[TAX_ID|27AAAPL1234C1ZV]]
L…
```

### S5 judge fail 128

- **What:** linguistic judge **fail** on `discharge_summary` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Nanded]]
[[PATIENT_NAME|Ravi Kumar]] DOB [[DOB|2006-03-15]] [[AGE|18]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0315-001]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient presented with acute gastroenteritis characterized by watery diarrhea, vomiting, and abdominal cramps. Initial management included IV fluid resuscitation with 0.9% Normal Saline, antiemet…
```

### S5 judge fail 129

- **What:** linguistic judge **fail** on `referral_letter` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815-001]] from [[HOSPITAL_NAME|Government Medical College Hospital Nanded]] / [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Re: [[PATIENT_NAME|Ravi Kumar]], [[AGE|18]] / [[GENDER|Male]], District [[DISTRICT|Nanded]]
Reason: Acute appendicitis requiring surgical intervention

Dear Colleague,

This is to refer [[PATIENT_NAME|Ravi Kumar]], an 18-year-old male patient from Nanded, for surgical evaluation and management of acute appendicitis. The patient presented to our emergenc…
```

### S5 judge fail 130

- **What:** linguistic judge **fail** on `hospital_billing` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|SCB Medical College and Hospital]] District [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] Phone [[PHONE_NUMBER|9438765432]]
Email [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
Landline [[TELEPHONE_LANDLINE|0674-2225678]] Vehicle [[VEHICLE_REGISTRATION|OD07AB1234]] (once)
Aadhaar [[AADHAAR_NUMBER|23456789012…
```

### S5 judge fail 131

- **What:** linguistic judge **fail** on `discharge_summary` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|SCB Medical College Hospital]]
[[PATIENT_NAME|Ramesh Kumar]] DOB [[DOB|2003-04-15]] [[AGE|21]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0876]] Ward [[WARD_NUMBER|B1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Sanjay Patnaik]] | Course / advice: Patient presented with persistent cough for 3 weeks, low-grade fever, and weight loss of 5 kg. Chest X-ray showed right upper lobe infiltrates. Sputum examination revealed acid-fast bacilli. Diagnosed with pulm…
```

### S5 judge fail 132

- **What:** linguistic judge **fail** on `referral_letter` (`te`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815-001]] from [[HOSPITAL_NAME|SCB Medical College Hospital]] / [[DOCTOR_NAME|Dr. Ramesh Patnaik]]
Re: [[PATIENT_NAME|Sanjay Kumar]], [[AGE|21]] / [[GENDER|Male]], District [[DISTRICT|Ganjam]]
Reason: Persistent cough and breathlessness for 3 weeks

Dear Sir/Madam,

This is to refer [[PATIENT_NAME|Sanjay Kumar]], a 21-year-old male window cleaner residing in urban Ganjam, Odisha, who presents with complaints of productive cough and progressive dyspnea for the pa…
```

### S5 judge fail 133

- **What:** linguistic judge **fail** on `discharge_summary` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Rajesh Patil]] | Course / advice: Patient admitted with pulmonary tuberculosis and comorbid hypertension. Initial sputum examination positive for acid-fast bacilli. Started on standard anti-tubercular therapy (ATT) regime…
```

### S5 judge fail 134

- **What:** linguistic judge **fail** on `referral_letter` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Government Medical College Hospital Amravati]] / [[DOCTOR_NAME|Dr. Priya Deshmukh]]
Re: [[PATIENT_NAME|Ayesha Begum]], [[AGE|56]] / [[GENDER|Female]], District [[DISTRICT|Amravati]]
Reason: Persistent hypertension and type 2 diabetes mellitus requiring specialist consultation

Patient presents with uncontrolled blood pressure readings despite current medication regimen. Blood pressure measurements over the past month have ranged from 1…
```

### S5 judge fail 135

- **What:** linguistic judge **fail** on `radiology_report` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Radiology Report — [[HOSPITAL_NAME|District Hospital Amravati]] | [[PATIENT_NAME|Ayesha Begum]] [[AGE|56]] [[GENDER|Female]] MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] [[DISTRICT|Amravati]] [[PHONE_NUMBER|9876543210]] [[HOSPITAL_ID|HSP-MH-045]] [[ABHA_ID|12-3456-7890-1234]] Findings: Patient presents with acute right lower quadrant abdominal pain for 24 hours. Ultrasound examination reveals an enlarged appendix measurin…
```

### S5 judge fail 136

- **What:** linguistic judge **fail** on `discharge_summary` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] DOB [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-08-10]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Priya Nair]] | Course / advice: Patient is a 22-year-old G1P0 from rural Gulbarga, Karnataka, who presented in labor on 10 August 2024. Her antenatal course was uncomplicated with regular check-ups. She was admitted with spontaneous …
```

### S5 judge fail 137

- **What:** linguistic judge **fail** on `referral_letter` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-GUL-089]] from [[HOSPITAL_NAME|District Hospital Gulbarga]] / [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Re: [[PATIENT_NAME|Ayesha Begum]], [[AGE|22]] / [[GENDER|Female]], District [[DISTRICT|Gulbarga]]
Reason: Persistent cough with weight loss and night sweats for 3 weeks

Dear Sir/Madam,

I am referring [[PATIENT_NAME|Ayesha Begum]], a 22-year-old female homemaker from rural Gulbarga, for further evaluation and management of suspected pulmonary tuberculosis. The patient …
```

### S5 judge fail 138

- **What:** linguistic judge **fail** on `radiology_report` (`ur`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['judge_network_error']`
- **Reasoning:** Soft-fail after 3 attempts (timeout/network). Logged — not silent. error=OpenAI-compatible network error: <urlopen error [Errno -2] Name or service not known>
- **Preview:**

```
Imaging report — Gulbarga District Hospital | [[PATIENT_NAME|Ayesha Begum]] [[AGE|22]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0456]] Encounter [[ENCOUNTER_ID|ENC-2024-0891]] | Reported by Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Findings: Chest radiograph reveals clear lung fields bilaterally with no acute infiltrates or consolidations. Cardiac silhouette is within normal limits. Bony structures including ribs and clavicles appear intact without any fractures. Soft tissue shadows are unremarkable. No …
```


_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
