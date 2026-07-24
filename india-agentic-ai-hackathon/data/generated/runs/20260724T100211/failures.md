# Failures audit — `20260724T100211`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260724T100211/pipeline.resolved.yaml`
- **issue count:** **91** (hard=0, gen_soft=46, tr_soft=18, judge=14, auditor=13)
- **S4 entity_coverage_complete_rate:** `0.9130434782608695`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.9723320158102767`
- **S6 pass_rate / passed:** `0.9735772357723578` / `479`
- **curated docs:** `382`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `c36e6f40b5b54d01aad2c9b0d29fc043` | `as` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `c36e6f40b5b54d01aad2c9b0d29fc043` | `as` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `ff5183030c4443eb8619d8ed622ce962` | `as` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `79e1e0bff3044effab3659ac879fecc8` | `bn` | `asha_worker_note` | `['missing_required_entities:VOTER_ID,RELIGION']` |
| S4 soft | `79e1e0bff3044effab3659ac879fecc8` | `bn` | `referral_letter` | `['missing_required_entities:RELATIVE_NAME']` |
| S4 soft | `f594af83f49d4547947752d58c0e45a9` | `bn` | `hospital_billing` | `['missing_required_entities:HOSPITAL_NAME,DISTRICT,PIN_CODE']` |
| S4 soft | `f619d5abd8244e93aab697fe1a8241a8` | `brx` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `d21516b79dbe4fb78827faca53231bb6` | `doi` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `d21516b79dbe4fb78827faca53231bb6` | `doi` | `discharge_summary` | `['missing_required_entities:DISTRICT']` |
| S4 soft | `7568f8e67bea4c959a480fd295d29db7` | `en` | `referral_letter` | `['entity_stuffing:HOSPITAL_NAME']` |
| S4 soft | `7568f8e67bea4c959a480fd295d29db7` | `en` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `9a7013a761314576999588794d2811cd` | `en` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `9a7013a761314576999588794d2811cd` | `en` | `asha_worker_note` | `['missing_required_entities:RELATIVE_NAME']` |
| S4 soft | `9e6b1442143d466a9594f34920f107cf` | `gu` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `9adda18066ec40f3ab6b33a531b52784` | `hi` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `07e9532716ae495cbcc16b67e6aeb464` | `kn` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUMBER']` |
| S4 soft | `9e10c9ebc51946eaad9364b1b8e0329a` | `kok` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `ba9480c1ca6a41458712603104065e74` | `kok` | `referral_letter` | `['missing_required_entities:PASSPORT_NUMBER']` |
| S4 soft | `8b96070203834ab1a5d6aae624425c6c` | `mai` | `radiology_report` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `8b96070203834ab1a5d6aae624425c6c` | `mai` | `surgical_note` | `['missing_required_entities:BED_NUMBER,MRN,RELATIVE_NAME,PATIENT_ID']` |
| S4 soft | `8b96070203834ab1a5d6aae624425c6c` | `mai` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `c2eca376dacc4c65bc6097c63376f49f` | `mai` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `9d2d55242ddb4c2f9f68dd62fe538b3d` | `ml` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `ffc851ec5afe45e7920df93ce2dbe4ab` | `mr` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `ffc851ec5afe45e7920df93ce2dbe4ab` | `mr` | `er_triage_notes` | `['missing_required_entities:PATIENT_NAME,AGE,GENDER,DOCTOR_NAME,HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUM…` |
| S4 soft | `093fd825483c42618796923e84fdb6f0` | `ne` | `hospital_billing` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `093fd825483c42618796923e84fdb6f0` | `ne` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `6886de1121f1401595e50fbe778b2d42` | `ne` | `insurance_claim` | `['entity_stuffing:BANK_ACCOUNT_NUMBER,BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV,IFSC_CODE,INSURANC…` |
| S4 soft | `6886de1121f1401595e50fbe778b2d42` | `ne` | `referral_letter` | `['missing_required_entities:MRN']` |
| S4 soft | `b6b35bc6f61841c1ac6d9e8581a2144b` | `or` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME,HOSPITAL_ID']` |
| S4 soft | `b6b35bc6f61841c1ac6d9e8581a2144b` | `or` | `surgical_note` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `dc5ecaa9f7e84391ad0f873de4b38e07` | `or` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `dc5ecaa9f7e84391ad0f873de4b38e07` | `or` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `0538f3faf4324debbd546bf332d419f6` | `pa` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `45add1637b8c4cdbb97d91677348819a` | `pa` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `prescription` | `['missing_required_entities:DISTRICT']` |
| S4 soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `discharge_summary` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,ABHA_ADDRESS,CASTE']` |
| S4 soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `surgical_note` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `dfdd30d26dc24c94a8e5a3cd4aa57a2e` | `sat` | `prescription` | `['missing_required_entities:DISTRICT']` |
| S4 soft | `228cb6f1c22941279fc07428487acd05` | `sd` | `asha_worker_note` | `['missing_required_entities:BPL_RATION_CARD,RELIGION']` |
| S4 soft | `6227e1809b0743be8c7473f02961d290` | `sd` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV,PIN,PHONE_NUMBER']` |
| S4 soft | `6227e1809b0743be8c7473f02961d290` | `sd` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `6227e1809b0743be8c7473f02961d290` | `sd` | `surgical_note` | `['missing_required_entities:MRN,PATIENT_ID']` |
| S4 soft | `a9d809d8ae7147fca1bb8d78a5c50cbc` | `ta` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `36935bf173e3478495baf6420bc875be` | `te` | `phc_register` | `['missing_required_entities:BPL_RATION_CARD']` |
| S4b soft | `f619d5abd8244e93aab697fe1a8241a8` | `brx` | `lab_report` | `dedicated_translate_failed:Translation under-counted [[PATIENT_NAME|…]] tags: found=0 expected>=1;s…` |
| S4b soft | `86619deb5c4b4de093d32fe24c54bddc` | `doi` | `hospital_billing` | `prefer_chat_1:Missing ID placeholder restore for ⟦ID22⟧;prefer_chat_2:Sarvam timeout after 180.0s: …` |
| S4b soft | `9e6b1442143d466a9594f34920f107cf` | `gu` | `hospital_billing` | `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_transla…` |
| S4b soft | `9e6b1442143d466a9594f34920f107cf` | `gu` | `opd_slip` | `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place T…` |
| S4b soft | `07e9532716ae495cbcc16b67e6aeb464` | `kn` | `referral_letter` | `tag_restore_or_translate_failed:dedicated_translate_failed:Translation under-counted [[RELATIVE_NAM…` |
| S4b soft | `de067f8b897840cab8ecbde4a00e2add` | `ks` | `hospital_billing` | `prefer_chat_1:Sarvam timeout after 180.0s: The read operation timed out;prefer_chat_2:Sarvam timeou…` |
| S4b soft | `75419f1fe22f409c8108d2a13f2e677f` | `mni` | `referral_letter` | `dedicated_translate_failed:Translation lost protected ID tag '[[STATE|Manipur]]';rare_recovery_1:Sa…` |
| S4b soft | `d5d814fb7aea4a538977615de1180c4e` | `mni` | `radiology_report` | `dedicated_translate_failed:Translation lost protected ID tag '[[ABHA_ID|12-3456-7890-1234]]';rare_r…` |
| S4b soft | `ffc851ec5afe45e7920df93ce2dbe4ab` | `mr` | `er_triage_notes` | `no_valid_entity_tags_to_protect` |
| S4b soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `hospital_billing` | `dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MC-WB-2024-0815]]';rare_recover…` |
| S4b soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `discharge_summary` | `dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder…` |
| S4b soft | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `er_triage_notes` | `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder…` |
| S4b soft | `dfdd30d26dc24c94a8e5a3cd4aa57a2e` | `sat` | `automated_sms` | `dedicated_translate_failed:Translation lost protected ID tag '[[APPOINTMENT_ID|APT-240815-02]]';rar…` |
| S4b soft | `dfdd30d26dc24c94a8e5a3cd4aa57a2e` | `sat` | `insurance_claim` | `dedicated_translate_failed:Translation lost protected ID tag '[[INSURANCE_POLICY_NUMBER|POL-OD-2024…` |
| S4b soft | `dfdd30d26dc24c94a8e5a3cd4aa57a2e` | `sat` | `radiology_report` | `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder…` |
| S4b soft | `6227e1809b0743be8c7473f02961d290` | `sd` | `opd_slip` | `prefer_chat_1:Sarvam timeout after 240.0s: The read operation timed out;prefer_chat_2:Sarvam timeou…` |
| S4b soft | `043f5fb0c78c482298663bcaa05618fe` | `te` | `asha_worker_note` | `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place T…` |
| S4b soft | `da2b757620cf4d158906f012278641f2` | `ur` | `hospital_billing` | `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_transla…` |
| S5 fail | `f619d5abd8244e93aab697fe1a8241a8` | `brx` | `lab_report` | score=0.25 flags=['dialect_script_impurity', 'invented_entity_type'] |
| S5 fail | `f619d5abd8244e93aab697fe1a8241a8` | `brx` | `asha_worker_note` | score=0.35 flags=['dialect_script_impurity', 'cross_language_entity_shift', 'surrogate_plausibility_collapse'] |
| S5 fail | `fee4de17dbbf4d15b95ef10f6a01c60c` | `brx` | `referral_letter` | score=0.65 flags=['invented_entity_type'] |
| S5 fail | `e90c7788a683415497f7cf0718f7966b` | `ks` | `telemedicine_transcript` | score=0.55 flags=['surrogate_plausibility_collapse'] |
| S5 fail | `75419f1fe22f409c8108d2a13f2e677f` | `mni` | `referral_letter` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `hospital_billing` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `discharge_summary` | score=0.55 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `er_triage_notes` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `228cb6f1c22941279fc07428487acd05` | `sd` | `radiology_report` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `228cb6f1c22941279fc07428487acd05` | `sd` | `telemedicine_transcript` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `6227e1809b0743be8c7473f02961d290` | `sd` | `automated_sms` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `6227e1809b0743be8c7473f02961d290` | `sd` | `discharge_summary` | score=0.55 flags=['cross_language_entity_shift', 'surrogate_plausibility_collapse'] |
| S5 fail | `043f5fb0c78c482298663bcaa05618fe` | `te` | `insurance_claim` | score=0.62 flags=['invented_entity_type'] |
| S6 fail | `f594af83f49d4547947752d58c0e45a9` | `bn` | `insurance_claim` | `['phi_residue:2']` |
| S6 fail | `f594af83f49d4547947752d58c0e45a9` | `bn` | `hospital_billing` | `['script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `d21516b79dbe4fb78827faca53231bb6` | `doi` | `insurance_claim` | `['missing_required:BANK_ROUTING_NUMBER', 'phi_residue:4', 'script_purity:target_script_ratio:0.000<…` |
| S6 fail | `39f3b8aa1d6b43a7bb32ef3cbb8bd25c` | `gu` | `hospital_billing` | `['entity_stuffing:TAX_ID,TELEPHONE_LANDLINE', 'phi_residue:1']` |
| S6 fail | `ba9480c1ca6a41458712603104065e74` | `kok` | `referral_letter` | `['dics_below_threshold:0.0']` |
| S6 fail | `666ba63c7da84db8a643943d59820646` | `ml` | `hospital_billing` | `['dics_below_threshold:0.0']` |
| S6 fail | `ffc851ec5afe45e7920df93ce2dbe4ab` | `mr` | `hospital_billing` | `['phi_residue:1']` |
| S6 fail | `093fd825483c42618796923e84fdb6f0` | `ne` | `hospital_billing` | `['format:PAN_NUMBER:pan_format']` |
| S6 fail | `0538f3faf4324debbd546bf332d419f6` | `pa` | `telemedicine_transcript` | `['dics_below_threshold:0.0']` |
| S6 fail | `3bc580120add4e55b09a0e1ac85b643f` | `sat` | `prescription` | `['script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `dfdd30d26dc24c94a8e5a3cd4aa57a2e` | `sat` | `hospital_billing` | `['format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `228cb6f1c22941279fc07428487acd05` | `sd` | `prescription` | `['dics_below_threshold:0.0']` |
| S6 fail | `6227e1809b0743be8c7473f02961d290` | `sd` | `insurance_claim` | `['phi_residue:8', 'dics_below_threshold:0.5', 'script_purity:wrong_indic_script:Devanagari>Arabic']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `insurance_claim` (`as`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ranjan Sharma]], আপোনাৰ টি বি অনুসৰণ [[DOCTOR_NAME|Dr. B. Kalita]] ৰ সৈতে [[APPOINTMENT_ID|APT-240521-001]] ত [[HOSPITAL_NAME|Kamrup Urban PHC]] ত হ'ব। অনুগ্ৰহ কৰি [[PHONE_NUMBER|9876543210]] ত নিশ্চিত কৰক। MRN [[MRN|MRN-2024-0521-001]]।
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `radiology_report` (`as`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ranjan Sharma]], আপোনাৰ টি বি অনুসৰণ [[DOCTOR_NAME|Dr. B. Kalita]] ৰ সৈতে [[APPOINTMENT_ID|APT-240521-001]] ত [[HOSPITAL_NAME|Kamrup Urban PHC]] ত হ'ব। অনুগ্ৰহ কৰি [[PHONE_NUMBER|9876543210]] ত নিশ্চিত কৰক। MRN [[MRN|MRN-2024-0521-001]]।
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `insurance_claim` (`as`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
TPA দাবী — পলিচি [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Biren Borah]] [[AGE|59]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
হাস্পতাল [[HOSPITAL_NAME|Sonitpur District Hospital]] জিলা [[DISTRICT|Sonitpur]]
Motor / RTA বাহন [[VEHICLE_REGISTRATION|AS01AB1234]] (একেইবাৰ)।
PAN [[PAN_NUMBER|ABCPB1234D]] IFSC [[IFSC_CODE|SBIN0001234]] একাউণ্ট [[BANK_ACCOUNT_NUMBER|30200012345678]]

ৰোগীৰ উপস্থাপন কৰা হৈছিল ৩ মাহৰ বাবে দীৰ্ঘদিনীয়া কাহ, ৮ কেজি ওজন হ্ৰাস, আৰু জ্বৰৰ সৈতে। শ্লেষ্মা পৰীক্ষা AFB-ৰ বাবে ইতিবাচক। বুকুৰ X-ray-এ সোঁ ওপৰৰ খণ্ডত গহ্বৰযুক্ত ঘা দেখুৱাইছে। ফুসফুসী…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `asha_worker_note` (`bn`).
- **Missing required tags:** `['VOTER_ID', 'RELIGION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:VOTER_ID,RELIGION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ওপিডি স্লিপ | [[HOSPITAL_NAME|Birbhum District Hospital]] | আইডি [[HOSPITAL_ID|BDH-WB-001]]
রোগীর নাম: [[PATIENT_NAME|Satyajit Chatterjee]] | জন্ম তারিখ [[DOB|1939-07-22]] | বয়স: [[AGE|85]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Supervisor and Foreman, Photo Litho, Photo Engraving and Dark Room Operations]] | এম.আর.এন: [[MRN|BDH-2024-0856]] | চিকিৎসক: [[DOCTOR_NAME|Dr. Amitava Mukherjee]]
আত্মীয়: [[RELATIVE_NAME|Anjali Chatterjee]] | ফোন: [[PHONE_NUMBER|9832145678]]
রেজিস্ট্রার এম্পআইডি: [[EMPLOYEE_ID|EMP-BDH-042]] | জেলা: [[DISTRICT|Birbhum]]

প্রধান অভিযোগ: ৩ মাস ধরে কাশি, ওজন কমা এব…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `referral_letter` (`bn`).
- **Missing required tags:** `['RELATIVE_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:RELATIVE_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ওপিডি স্লিপ | [[HOSPITAL_NAME|Birbhum District Hospital]] | আইডি [[HOSPITAL_ID|BDH-WB-001]]
রোগীর নাম: [[PATIENT_NAME|Satyajit Chatterjee]] | জন্ম তারিখ [[DOB|1939-07-22]] | বয়স: [[AGE|85]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Supervisor and Foreman, Photo Litho, Photo Engraving and Dark Room Operations]] | এম.আর.এন: [[MRN|BDH-2024-0856]] | চিকিৎসক: [[DOCTOR_NAME|Dr. Amitava Mukherjee]]
আত্মীয়: [[RELATIVE_NAME|Anjali Chatterjee]] | ফোন: [[PHONE_NUMBER|9832145678]]
রেজিস্ট্রার এম্পআইডি: [[EMPLOYEE_ID|EMP-BDH-042]] | জেলা: [[DISTRICT|Birbhum]]

প্রধান অভিযোগ: ৩ মাস ধরে কাশি, ওজন কমা এব…
```

### S4 generation soft-fail 6

- **What:** generation soft-fail on `hospital_billing` (`bn`).
- **Missing required tags:** `['HOSPITAL_NAME', 'DISTRICT', 'PIN_CODE']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME,DISTRICT,PIN_CODE']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
অপারেশন নোট — [[HOSPITAL_NAME|হাসপাতাল]] ভর্তি [[ADMISSION_NUMBER|ADM-2024-0815-001]] ওয়ার্ড [[WARD_NUMBER|OT]]
[[PATIENT_NAME|রমেশ চন্দ্র]] [[AGE|50]] [[GENDER|Male]] সার্জন [[DOCTOR_NAME|ডাঃ অনিল কুমার]]
অপারেশন পদ্ধতি / পর্যবেক্ষণ: রোগীর উপসর্গ ছিল ৩ মাস ধরে দীর্ঘস্থায়ী কাশি, ওজন হ্রাস এবং ডানদিকের বুকের ব্যথা। সিটি স্ক্যানে দেখা গেছে লোকিউলেটেড এম্পাইমা সহ ডানদিকের প্লুরাল পুরুত্ব। সাধারণ অ্যানেস্থেশিয়ার অধীনে ৭ম ইন্টারকোস্টাল স্পেসের মাধ্যমে ডানদিকের থোরাকোটমি করা হয়েছে। একাধিক আসঞ্জন সাধানে ব্যবচ্ছেদ করা হয়েছে। কেসিয়েটিং গ্র্যানুলোমা সহ পুরু প্লুরা দেখা গেছে। এম্পাইমা ক্যাভিটি নিষ…
```

### S4 generation soft-fail 7

- **What:** generation soft-fail on `radiology_report` (`brx`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
प्रिस्क्रिप्शन — [[HOSPITAL_NAME|Chirang District Hospital]]
बेरामि [[PATIENT_NAME|Jiran Basumatary]], [[AGE|33]] / [[GENDER|Male]], एम.आर.एन. [[MRN|MRN-2024-CHIR-001]]
डक्टर [[DOCTOR_NAME|Dr. Pranab Kalita]]
जायगानि सुलुं: [[PHONE_NUMBER|9876543210]]
थं: [[RESIDENTIAL_ADDRESS|Bhurkunda, Chirang, Assam]]
जिल्ला: [[DISTRICT|Chirang]]
बेरामिनि आइ.डि.: [[PATIENT_ID|PID-CHIR-2024-001]]
ए.बि.एच.ए. आइ.डि.: [[ABHA_ID|12-3456-7890-1234]]

दिनाव: 2024-05-21

गाहाय जेंना: थांनाय 5 साननिफ्राय देहायाव सरासनस्रा सानाय आरो मेग्लिनाय, जायखौ संख्रि हाखराव खामानि मावनाय समाव गोबां गोलोमनायजों सोमोन्दो गोनां।
…
```

### S4 generation soft-fail 8

- **What:** generation soft-fail on `insurance_claim` (`doi`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
लैब रिपोर्ट - कठुआ जिला हस्पताल कठुआ
मेडिकल रिकॉर्ड नंबर [[MRN|MRN-JK-2024-0815]] पेशेंट ID [[PATIENT_ID|PID-JK-7781]]
[[PATIENT_NAME|सुनीता देवी]] [[AGE|47]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9419012345]]
द्वारा आदेशित [[DOCTOR_NAME|राजेश शर्मा]]
तारीख: 15 अगस्त 2024

मरीज ने पिछले 3 हफ्तें थमां थकावट, हल्के जोड़ें दा दर्द, ते कदे-कदे सिरदर्द दी शिकायत दस्सी ऐ। बुखार या वजन घट्ट होने दी कोई रिपोर्ट नेईं ऐ। मरीज कठुआ जिले दी इक हस्तशिल्प अध्यापिका ऐ।

लैब जांच दे नतीजे:
पूरा रक्त गणना:
- हीमोग्लोबिन: 11.8 g/dL (सामान्य: 12.0-15.5)
- श्वेत रक्त कोशिकाएं: 6,500/μL (सामान्य: 4,500-11,000)
- प…
```

### S4 generation soft-fail 9

- **What:** generation soft-fail on `discharge_summary` (`doi`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
लैब रिपोर्ट - कठुआ जिला हस्पताल कठुआ
मेडिकल रिकॉर्ड नंबर [[MRN|MRN-JK-2024-0815]] पेशेंट ID [[PATIENT_ID|PID-JK-7781]]
[[PATIENT_NAME|सुनीता देवी]] [[AGE|47]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9419012345]]
द्वारा आदेशित [[DOCTOR_NAME|राजेश शर्मा]]
तारीख: 15 अगस्त 2024

मरीज ने पिछले 3 हफ्तें थमां थकावट, हल्के जोड़ें दा दर्द, ते कदे-कदे सिरदर्द दी शिकायत दस्सी ऐ। बुखार या वजन घट्ट होने दी कोई रिपोर्ट नेईं ऐ। मरीज कठुआ जिले दी इक हस्तशिल्प अध्यापिका ऐ।

लैब जांच दे नतीजे:
पूरा रक्त गणना:
- हीमोग्लोबिन: 11.8 g/dL (सामान्य: 12.0-15.5)
- श्वेत रक्त कोशिकाएं: 6,500/μL (सामान्य: 4,500-11,000)
- प…
```

### S4 generation soft-fail 10

- **What:** generation soft-fail on `referral_letter` (`en`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['HOSPITAL_NAME']`
- **Raw reasons:** `['entity_stuffing:HOSPITAL_NAME']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-05-15-001]] from [[HOSPITAL_NAME|Sion Hospital]] / [[DOCTOR_NAME|Dr. Anjali Sharma]]
Re: [[PATIENT_NAME|Priya Deshmukh]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Mumbai Suburban]]
Reason: Evaluation for chronic low back pain with radiculopathy, considering surgical intervention.

Dear Colleague,

This is to refer our patient, [[PATIENT_NAME|Priya Deshmukh]], a 32-year-old female oil expeller, for your expert surgical opinion. She has been under my care at [[HOSPITAL_NAME|Sion Hospital]] for the past six months for progressive low back pain.

The pat…
```

### S4 generation soft-fail 11

- **What:** generation soft-fail on `radiology_report` (`en`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-05-15-001]] from [[HOSPITAL_NAME|Sion Hospital]] / [[DOCTOR_NAME|Dr. Anjali Sharma]]
Re: [[PATIENT_NAME|Priya Deshmukh]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Mumbai Suburban]]
Reason: Evaluation for chronic low back pain with radiculopathy, considering surgical intervention.

Dear Colleague,

This is to refer our patient, [[PATIENT_NAME|Priya Deshmukh]], a 32-year-old female oil expeller, for your expert surgical opinion. She has been under my care at [[HOSPITAL_NAME|Sion Hospital]] for the past six months for progressive low back pain.

The pat…
```

### S4 generation soft-fail 12

- **What:** generation soft-fail on `radiology_report` (`en`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Goa Medical College Hospital]] / [[DOCTOR_NAME|Dr. Priya Fernandes]]
Re: [[PATIENT_NAME|Sweta Naik]], [[AGE|21]] / [[GENDER|Female]], District [[DISTRICT|North Goa]]
Reason: Complex chronic care evaluation for suspected hereditary breast cancer syndrome with family history of early-onset malignancy

Dear Oncology Department,

This is to refer [[PATIENT_NAME|Sweta Naik]] for comprehensive evaluation and management of complex chronic care needs. The patient presents with concerning clinical findings including multiple atypical nevi, ea…
```

### S4 generation soft-fail 13

- **What:** generation soft-fail on `asha_worker_note` (`en`).
- **Missing required tags:** `['RELATIVE_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:RELATIVE_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Goa Medical College Hospital]] / [[DOCTOR_NAME|Dr. Priya Fernandes]]
Re: [[PATIENT_NAME|Sweta Naik]], [[AGE|21]] / [[GENDER|Female]], District [[DISTRICT|North Goa]]
Reason: Complex chronic care evaluation for suspected hereditary breast cancer syndrome with family history of early-onset malignancy

Dear Oncology Department,

This is to refer [[PATIENT_NAME|Sweta Naik]] for comprehensive evaluation and management of complex chronic care needs. The patient presents with concerning clinical findings including multiple atypical nevi, ea…
```

### S4 generation soft-fail 14

- **What:** generation soft-fail on `radiology_report` (`gu`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
આશા કાર્યકર નોંધ — ગામ [[VILLAGE|Kankrol]], જિલ્લા [[DISTRICT|Junagadh]]
લાભાર્થી [[PATIENT_NAME|Valukbhai Singh]], [[AGE|50]] / [[GENDER|Male]]
આશા: [[ASHA_WORKER_NAME|Kiranben Rathod]] | ફોન [[PHONE_NUMBER|9876543210]]
મુલાકાતના તારણો: દર્દી વધતી જતી થાક અને છાતીમાં વચ્ચે-વચ્ચે થતા દુખાવાની જાણ કરે છે. બ્લડ પ્રેશર રીડિંગ 145/90 mmHg છે. મૌખિક કીમોથેરાપી દવાઓનું પાલન અનિયમિત છે. પરિવાર સારવારના આર્થિક બોજ વિશે ચિંતા વ્યક્ત કરે છે.

ક્લિનિકલ મૂલ્યાંકન: શ્રી વલુકભાઈ સિંહ, 50 વર્ષના પુરુષ ગાલીચા વણકર ગ્રામીણ જામનગર જિલ્લાના, નિયમિત ઓન્કોલોજી ફોલો-અપ માટે રજૂ થાય છે. દર્દી છેલ્લા 6 મહિનાથી સ્ટેજ…
```

### S4 generation soft-fail 15

- **What:** generation soft-fail on `insurance_claim` (`hi`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Janjgir]] | पहचान [[HOSPITAL_ID|DH-JG-001]]
रोगी: [[PATIENT_NAME|Lakshmi Mahunt]] | जन्म तिथि [[DOB|1992-05-15]] | आयु: [[AGE|32]] | लिंग: [[GENDER|Female]]
व्यवसाय: [[OCCUPATION|Packer, Hand]] | चिकित्सा रिकॉर्ड संख्या: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
रिश्तेदार: [[RELATIVE_NAME|Sanjay Mahunt]] | फोन: [[PHONE_NUMBER|9876543210]] | पंजीयक कर्मचारी आईडी: [[EMPLOYEE_ID|EMP-JG-045]] | जिला: [[DISTRICT|Janjgir]]
मुख्य शिकायत: लगातार खांसी 3 सप्ताह से वजन घटने और थकान के साथ

वर्तमान बीमारी का इतिहास: रोगी के साथ 21 द…
```

### S4 generation soft-fail 16

- **What:** generation soft-fail on `er_triage_notes` (`kn`).
- **Missing required tags:** `['HOSPITAL_NAME', 'ENCOUNTER_ID', 'WARD_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ — [[HOSPITAL_NAME|Koppal District Hospital]]
ರೋಗಿ [[PATIENT_NAME|Savitri Gowda]], [[AGE|55]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
ವೈದ್ಯರು [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ಸೂಚನೆ: Ceftriaxone 1g IV ಪ್ರತಿ 12 ಗಂಟೆಗಳು 5 ದಿನಗಳು, Metronidazole 500mg IV ಪ್ರತಿ 8 ಗಂಟೆಗಳು 7 ದಿನಗಳು, Paracetamol 500mg ಬಾಯಿಯ ಮೂಲಕ ಪ್ರತಿ 6 ಗಂಟೆಗಳು ನೋವಿಗೆ ಅಗತ್ಯವಿದ್ದಲ್ಲಿ. ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಯ ನಂತರದ ಸೂಚನೆಗಳು: ಗಾಯದ ಆರೈಕೆ ಕ್ರಿಮಿಮುಕ್ತ ಸಲೈನ್ ಡ್ರೆಸ್ಸಿಂಗ್‌ನೊಂದಿಗೆ ದಿನಕ್ಕೆ ಎರಡು ಬಾರಿ, ಭಾರವಾದ ವಸ್ತುಗಳನ್ನು ಎತ್ತುವುದನ್ನು ತಪ್ಪಿಸಿ 4 ವಾರಗಳವರೆಗೆ, 7 ದಿನಗಳಲ್ಲಿ ಮರುಪರಿಶೀಲನೆ.
[[PHONE_NUMBER|9876543210]]
[[DISTRICT|Koppal]]
[[R…
```

### S4 generation soft-fail 17

- **What:** generation soft-fail on `er_triage_notes` (`kok`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|District Hospital, Kumta]] जिल्लो [[DISTRICT|Uttara Kannada]]
PIN [[PIN_CODE|581426]] रुग्ण [[PATIENT_NAME|Shobha Hegde]] MRN [[MRN|DH-UK-2024-0815]]
पतो [[RESIDENTIAL_ADDRESS|34 Main Road, Kumta]] फोन [[PHONE_NUMBER|9880123456]]
ईमेल [[EMAIL_ADDRESS|shobha.hegde@example.com]] PAN [[PAN_NUMBER|FGHIJ5678K]]
लँडलाईन [[TELEPHONE_LANDLINE|08382-222334]] वाहन [[VEHICLE_REGISTRATION|KA19AB5678]] (एकदां)
आधार [[AADHAAR_NUMBER|876543210987]] पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-KA-2024-9981]] GSTIN [[TAX_ID|29FGHIJ5678K1Z9]]
पावती क्र. INV-2024-0815 कर्नाटक
सल्ला शुल्क: 1500.00…
```

### S4 generation soft-fail 18

- **What:** generation soft-fail on `referral_letter` (`kok`).
- **Missing required tags:** `['PASSPORT_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:PASSPORT_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Goa Medical College Hospital]]
[[PATIENT_NAME|Ramesh Naik]] जन्म तारीख [[DOB|1978-04-15]] [[AGE|46]] [[GENDER|Male]]
भरती [[ADMISSION_NUMBER|ADM-2024-0815-004]] विभाग [[WARD_NUMBER|B1]] खाट [[BED_NUMBER|08]]
डॉ. [[DOCTOR_NAME|Dr. Prakash Kulkarni]] | उपचार / सल्ला: रुग्णाक फुफ्फुसाचो क्षयरोग आनी उच्च रक्तदाब हाका लागून भरती केलो. सुरुवातीच्या थुंकीच्या तपासणेंत AFB positive 3+ बॅक्टेरियाचो भार दिसलो. आयसोनिआझिड, रिफॅम्पिसिन, पायराझिनामाइड आनी इथाम्ब्युटोल हांच्या वांगडा कॅटेगरी I DOTS उपचार पद्दत सुरू केली. भरती वेळार रक्तदाब 160/100 mmHg आशिल्लो. दिसाक 50m…
```

### S4 generation soft-fail 19

- **What:** generation soft-fail on `radiology_report` (`mai`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
विकिरण विज्ञान रिपोर्ट — जिला अस्पताल सहर्सा | [[PATIENT_NAME|Sunita Devi]] [[AGE|23]] [[GENDER|Female]]
मेडिकल रिकॉर्ड नंबर [[MRN|MRN-2024-0815-001]] मुलाकात [[ENCOUNTER_ID|ENC-55601]] | डॉ. [[DOCTOR_NAME|Dr. Rajesh Kumar]] द्वारा रिपोर्ट किया गया
निष्कर्ष:
रोगी के साथ एक जटिल उदर द्रव्यमान है जो घातकता के लिए चिंताजनक है। कंट्रास्ट के साथ पेट और श्रोणि का सी टी स्कैन एक 7.2 x 5.8 cm विषम द्रव्यमान दर्शाता है जो दाईं एडनेक्सल क्षेत्र से उत्पन्न हो रहा है, जिसमें नेक्रोसिस और कैल्सीफिकेशन के क्षेत्र हैं। द्रव्यमान आर्टेरियल फेज में 120 HU और पोर्टल वेनस फेज में 85 HU का एन्हांसमेंट दिखाता है।…
```

### S4 generation soft-fail 20

- **What:** generation soft-fail on `surgical_note` (`mai`).
- **Missing required tags:** `['BED_NUMBER', 'MRN', 'RELATIVE_NAME', 'PATIENT_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BED_NUMBER,MRN,RELATIVE_NAME,PATIENT_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
विकिरण विज्ञान रिपोर्ट — जिला अस्पताल सहर्सा | [[PATIENT_NAME|Sunita Devi]] [[AGE|23]] [[GENDER|Female]]
मेडिकल रिकॉर्ड नंबर [[MRN|MRN-2024-0815-001]] मुलाकात [[ENCOUNTER_ID|ENC-55601]] | डॉ. [[DOCTOR_NAME|Dr. Rajesh Kumar]] द्वारा रिपोर्ट किया गया
निष्कर्ष:
रोगी के साथ एक जटिल उदर द्रव्यमान है जो घातकता के लिए चिंताजनक है। कंट्रास्ट के साथ पेट और श्रोणि का सी टी स्कैन एक 7.2 x 5.8 cm विषम द्रव्यमान दर्शाता है जो दाईं एडनेक्सल क्षेत्र से उत्पन्न हो रहा है, जिसमें नेक्रोसिस और कैल्सीफिकेशन के क्षेत्र हैं। द्रव्यमान आर्टेरियल फेज में 120 HU और पोर्टल वेनस फेज में 85 HU का एन्हांसमेंट दिखाता है।…
```

### S4 generation soft-fail 21

- **What:** generation soft-fail on `insurance_claim` (`mai`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
विकिरण विज्ञान रिपोर्ट — जिला अस्पताल सहर्सा | [[PATIENT_NAME|Sunita Devi]] [[AGE|23]] [[GENDER|Female]]
मेडिकल रिकॉर्ड नंबर [[MRN|MRN-2024-0815-001]] मुलाकात [[ENCOUNTER_ID|ENC-55601]] | डॉ. [[DOCTOR_NAME|Dr. Rajesh Kumar]] द्वारा रिपोर्ट किया गया
निष्कर्ष:
रोगी के साथ एक जटिल उदर द्रव्यमान है जो घातकता के लिए चिंताजनक है। कंट्रास्ट के साथ पेट और श्रोणि का सी टी स्कैन एक 7.2 x 5.8 cm विषम द्रव्यमान दर्शाता है जो दाईं एडनेक्सल क्षेत्र से उत्पन्न हो रहा है, जिसमें नेक्रोसिस और कैल्सीफिकेशन के क्षेत्र हैं। द्रव्यमान आर्टेरियल फेज में 120 HU और पोर्टल वेनस फेज में 85 HU का एन्हांसमेंट दिखाता है।…
```

### S4 generation soft-fail 22

- **What:** generation soft-fail on `insurance_claim` (`mai`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
रेडियोलॉजी रिपोर्ट: [[HOSPITAL_NAME|Sitamarhi District Hospital]] | [[PATIENT_NAME|Ram Prasad Yadav]] [[AGE|70]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | डॉ. [[DOCTOR_NAME|Dr. Sanjay Kumar]] द्वारा रिपोर्ट किया गया
निष्कर्ष:
मस्तिष्क MRI T1, T2, FLAIR, आउर DWI sequences के साथ किया गया। कोनो तीव्र इंट्राक्रैनियल हेमोरेज आउर मास इफेक्ट नहीं पाया गया। वेंट्रिकल्स सामान्य आकार के हैं, हाइड्रोसिफ़लस के साक्ष्य के बिना। सेरेब्रल सल्की आउर गाइरी सुरक्षित हैं। तीव्र इन्फार्क्ट के साक्ष्य नहीं हैं। व्हाइट मैटर में हल्के उम्र से संबंधित बदलाव दिख रहे हैं, जो…
```

### S4 generation soft-fail 23

- **What:** generation soft-fail on `er_triage_notes` (`ml`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
PHC രജിസ്റ്റർ — [[HOSPITAL_NAME|Primary Health Centre Mahe]] ഗ്രാമം [[VILLAGE|Mahe Town]] ജില്ല [[DISTRICT|Mahe]]
[[PATIENT_NAME|രമ്യ]] [[AGE|46]] [[GENDER|Female]] | സ്തനാർബുദ ചികിത്സയ്ക്കായുള്ള ഓങ്കോളജി ഫോളോ-അപ്പ്

രോഗി പതിവ് ഓങ്കോളജി ഫോളോ-അപ്പിനായി എത്തുന്നു. ആറ് മാസം മുമ്പ് സ്റ്റേജ് II സ്തനാർബുദം സ്ഥിരീകരിച്ച ചരിത്രം. നിലവിൽ അഡ്ജുവന്റ് കീമോതെറാപ്പി ചികിത്സയിലാണ്. നേരിയ തളർച്ചയും ഇടയ്ക്കിടെയുള്ള ഓക്കാനം റിപ്പോർട്ട് ചെയ്യുന്നു, ഇത് ആന്റി എമെറ്റിക്സ് ഉപയോഗിച്ച് നന്നായി നിയന്ത്രിക്കപ്പെടുന്നു. ശാരീരിക പരിശോധനയിൽ സ്തനത്തിലെ മുഴ സ്ഥിരമാണെന്നും ലിംഫ് നോഡുകളിൽ വീക്കമില്ലെന്നും കണ്ടെത്തി. പ്രധാന ല…
```

### S4 generation soft-fail 24

- **What:** generation soft-fail on `radiology_report` (`mr`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|सिव्हिल हॉस्पिटल अहमदनगर]] जिल्हा [[DISTRICT|Ahmednagar]]
एमआरएन [[MRN|MH-AHM-2024-0815]] रुग्ण आयडी [[PATIENT_ID|PID-MH-78945]]
[[PATIENT_NAME|Ramesh Patil]] [[AGE|22]] [[GENDER|Male]] फोन [[PHONE_NUMBER|9876543210]]
द्वारे [[DOCTOR_NAME|Dr. Priya Deshmukh]] आदेशित
दिनांक: 15 आगस्ट 2024

रुग्णाची माहिती:
[[PATIENT_NAME|Ramesh Patil]] ग्रामीण महाराष्ट्रातील 22 वर्षांचा पुरुष, सध्या विवाहित, हस्तसामुद्रिक तज्ज्ञ म्हणून काम करत आहे. रुग्ण जुनाट आजाराच्या नियमित देखरेखीसाठी आणि ऑटोइम्यून विकाराच्या इतिहासासह नियमित प्रयोगशाळा देखरेखीसाठी आला आहे.

वैद्यकीय संदर…
```

### S4 generation soft-fail 25

- **What:** generation soft-fail on `er_triage_notes` (`mr`).
- **Missing required tags:** `['PATIENT_NAME', 'AGE', 'GENDER', 'DOCTOR_NAME', 'HOSPITAL_NAME', 'ENCOUNTER_ID', 'WARD_NUMBER', 'RELATIVE_NAME', 'PHONE_NUMBER', 'BED_NUMBER', 'VEHICLE_REGISTRATION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:PATIENT_NAME,AGE,GENDER,DOCTOR_NAME,HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUMBER,RELATIVE_NAME,PHONE_NUMBER,BED_NUMBER,VEHICLE_REGISTRATION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|सिव्हिल हॉस्पिटल अहमदनगर]] जिल्हा [[DISTRICT|Ahmednagar]]
एमआरएन [[MRN|MH-AHM-2024-0815]] रुग्ण आयडी [[PATIENT_ID|PID-MH-78945]]
[[PATIENT_NAME|Ramesh Patil]] [[AGE|22]] [[GENDER|Male]] फोन [[PHONE_NUMBER|9876543210]]
द्वारे [[DOCTOR_NAME|Dr. Priya Deshmukh]] आदेशित
दिनांक: 15 आगस्ट 2024

रुग्णाची माहिती:
[[PATIENT_NAME|Ramesh Patil]] ग्रामीण महाराष्ट्रातील 22 वर्षांचा पुरुष, सध्या विवाहित, हस्तसामुद्रिक तज्ज्ञ म्हणून काम करत आहे. रुग्ण जुनाट आजाराच्या नियमित देखरेखीसाठी आणि ऑटोइम्यून विकाराच्या इतिहासासह नियमित प्रयोगशाळा देखरेखीसाठी आला आहे.

वैद्यकीय संदर…
```

### S4 generation soft-fail 26

- **What:** generation soft-fail on `hospital_billing` (`ne`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Thapa]]: तपाईँको केमोथेरापी फलो-अप [[APPOINTMENT_ID|APT-240521-01]] मा [[HOSPITAL_NAME|Kullu District Hospital]] मा [[DOCTOR_NAME|Dr. Anjali Sharma]] सँग हुनेछ। कृपया [[PHONE_NUMBER|9876512340]] मा पुष्टि गर्नुहोस्। MRN [[MRN|MRN-2024-0815-001]]।
```

### S4 generation soft-fail 27

- **What:** generation soft-fail on `radiology_report` (`ne`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Thapa]]: तपाईँको केमोथेरापी फलो-अप [[APPOINTMENT_ID|APT-240521-01]] मा [[HOSPITAL_NAME|Kullu District Hospital]] मा [[DOCTOR_NAME|Dr. Anjali Sharma]] सँग हुनेछ। कृपया [[PHONE_NUMBER|9876512340]] मा पुष्टि गर्नुहोस्। MRN [[MRN|MRN-2024-0815-001]]।
```

### S4 generation soft-fail 28

- **What:** generation soft-fail on `insurance_claim` (`ne`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['BANK_ACCOUNT_NUMBER', 'BANK_ROUTING_NUMBER', 'CREDIT_CARD_NUMBER', 'CVV', 'IFSC_CODE', 'INSURANCE_POLICY_NUMBER', 'PHONE_NUMBER', 'PIN', 'VEHICLE_REGISTRATION']`
- **Raw reasons:** `['entity_stuffing:BANK_ACCOUNT_NUMBER,BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV,IFSC_CODE,INSURANCE_POLICY_NUMBER,PHONE_NUMBER,PIN,VEHICLE_REGISTRATION']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
TPA दाबी — नीति [[INSURANCE_POLICY_NUMBER|POL-WB-2024-7781]]
[[PATIENT_NAME|राम शर्मा]] [[AGE|59]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|234567890123]]
अस्पताल [[HOSPITAL_NAME|सुकराज अस्पताल]] जिल्ला [[DISTRICT|झापा]]
मोटर / RTA सवारी साधन [[VEHICLE_REGISTRATION|WB02A1234]] (एक पटक मात्र)।
PAN [[PAN_NUMBER|ABCDE1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|50200012345678]]

बिरामीमा निरन्तर खोकी, 3 महिनामा 15 केजी तौल घट्नु, र बीच-बीचमा रगत खोक्ने (हेमोप्टिसिस) समस्या देखिएको छ। अघिल्लो चिकित्सा इतिहासमा उच्च रक्तचाप र टाइप 2 मधुमेह मेलिटस समावेश छ। शारीरिक परीक्षणले फिय…
```

### S4 generation soft-fail 29

- **What:** generation soft-fail on `referral_letter` (`ne`).
- **Missing required tags:** `['MRN']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:MRN']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
TPA दाबी — नीति [[INSURANCE_POLICY_NUMBER|POL-WB-2024-7781]]
[[PATIENT_NAME|राम शर्मा]] [[AGE|59]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|234567890123]]
अस्पताल [[HOSPITAL_NAME|सुकराज अस्पताल]] जिल्ला [[DISTRICT|झापा]]
मोटर / RTA सवारी साधन [[VEHICLE_REGISTRATION|WB02A1234]] (एक पटक मात्र)।
PAN [[PAN_NUMBER|ABCDE1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|50200012345678]]

बिरामीमा निरन्तर खोकी, 3 महिनामा 15 केजी तौल घट्नु, र बीच-बीचमा रगत खोक्ने (हेमोप्टिसिस) समस्या देखिएको छ। अघिल्लो चिकित्सा इतिहासमा उच्च रक्तचाप र टाइप 2 मधुमेह मेलिटस समावेश छ। शारीरिक परीक्षणले फिय…
```

### S4 generation soft-fail 30

- **What:** generation soft-fail on `opd_slip` (`or`).
- **Missing required tags:** `['HOSPITAL_NAME', 'HOSPITAL_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME,HOSPITAL_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ଇମେଜିଂ ପରୀକ୍ଷା ରିପୋର୍ଟ — [[HOSPITAL_NAME|Jagatsinghapur District Hospital]] | [[PATIENT_NAME|Hadi Pradhan]] [[AGE|42]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | ରିପୋର୍ଟ କରିଛନ୍ତି ଡାକ୍ତର [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ଫଳାଫଳ: ଉଦର ଏବଂ ପେଲଭିସ୍‌ର CT ସ୍କାନରୁ ଡାହାଣ ଯକୃତ୍ ଲୋବ୍‌ରେ ଏକ 4.2 cm ର ବିଷମଜାତୀୟ ପିଣ୍ଡୁଳା ଦେଖାଯାଉଛି, ଯାହାର ସୀମା ଅନିୟମିତ ଏବଂ ପାର୍ଶ୍ୱବର୍ତ୍ତୀ ଉନ୍ନତି ରହିଛି। ଏହି କ୍ଷତ କେନ୍ଦ୍ରୀୟ ନେକ୍ରୋସିସ୍ ଏବଂ ସାମାନ୍ୟ ପରିବେଷ୍ଟିତ ଯକୃତ୍ ପାରେନକାଇମାଲ୍ ଏଡିମା ପ୍ରଦର୍ଶନ କରୁଛି। ରକ୍ତବାହିକା ଆକ୍ରମଣ କିମ୍ବା ପିତ୍ତକୋଷ ଅବରୋଧର କୌଣସି ପ୍ରମାଣ ମିଳିନାହିଁ। ବାମ ଲୋବ୍‌ରେ ଏକାଧିକ କ୍ଷୁଦ୍ର (<…
```

### S4 generation soft-fail 31

- **What:** generation soft-fail on `surgical_note` (`or`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ଇମେଜିଂ ପରୀକ୍ଷା ରିପୋର୍ଟ — [[HOSPITAL_NAME|Jagatsinghapur District Hospital]] | [[PATIENT_NAME|Hadi Pradhan]] [[AGE|42]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | ରିପୋର୍ଟ କରିଛନ୍ତି ଡାକ୍ତର [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ଫଳାଫଳ: ଉଦର ଏବଂ ପେଲଭିସ୍‌ର CT ସ୍କାନରୁ ଡାହାଣ ଯକୃତ୍ ଲୋବ୍‌ରେ ଏକ 4.2 cm ର ବିଷମଜାତୀୟ ପିଣ୍ଡୁଳା ଦେଖାଯାଉଛି, ଯାହାର ସୀମା ଅନିୟମିତ ଏବଂ ପାର୍ଶ୍ୱବର୍ତ୍ତୀ ଉନ୍ନତି ରହିଛି। ଏହି କ୍ଷତ କେନ୍ଦ୍ରୀୟ ନେକ୍ରୋସିସ୍ ଏବଂ ସାମାନ୍ୟ ପରିବେଷ୍ଟିତ ଯକୃତ୍ ପାରେନକାଇମାଲ୍ ଏଡିମା ପ୍ରଦର୍ଶନ କରୁଛି। ରକ୍ତବାହିକା ଆକ୍ରମଣ କିମ୍ବା ପିତ୍ତକୋଷ ଅବରୋଧର କୌଣସି ପ୍ରମାଣ ମିଳିନାହିଁ। ବାମ ଲୋବ୍‌ରେ ଏକାଧିକ କ୍ଷୁଦ୍ର (<…
```

### S4 generation soft-fail 32

- **What:** generation soft-fail on `opd_slip` (`or`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ରେଡିଓଲୋଜି ରିପୋର୍ଟ — [[HOSPITAL_NAME|District Medical College Hospital Bastar]] | [[PATIENT_NAME|Ramesh Kumar]] [[AGE|21]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-1123]] ପରାମର୍ଶ [[ENCOUNTER_ID|ENC-2024-0891]] | ଦ୍ୱାରା ରିପୋର୍ଟ କରାଯାଇଛି ଡକ୍ଟର [[DOCTOR_NAME|Dr. Sanjay Patel]]
ଫୋନ୍: [[PHONE_NUMBER|9425123456]] | ABHA: [[ABHA_ID|12-3456-7890-1234]]
ହସ୍ପିଟାଲ୍ ID: [[HOSPITAL_ID|HSP-CG-007]] | ଜିଲ୍ଲା: [[DISTRICT|Bastar]]

କ୍ଲିନିକାଲ୍ ସୂଚନା: 21 ବର୍ଷର ପୁରୁଷ କ୍ରସର ଆଟେଣ୍ଡାଣ୍ଟଙ୍କଠାରେ ଆଚରଣଗତ ପରିବର୍ତ୍ତନ ଏବଂ ଆକ୍ରମଣର ଘଟଣାଗୁଡ଼ିକର ମୂଲ୍ୟାଙ୍କନ, ସାମାନ୍ୟ ମୁଣ୍ଡରେ ଆଘାତର ଇତିହାସ ସହିତ।

ପଦ୍ଧତି: 15 ଅଗଷ୍ଟ 2024 ରେ 1.5 ଟେସଲା ସ୍କାନ…
```

### S4 generation soft-fail 33

- **What:** generation soft-fail on `insurance_claim` (`or`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ରେଡିଓଲୋଜି ରିପୋର୍ଟ — [[HOSPITAL_NAME|District Medical College Hospital Bastar]] | [[PATIENT_NAME|Ramesh Kumar]] [[AGE|21]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-1123]] ପରାମର୍ଶ [[ENCOUNTER_ID|ENC-2024-0891]] | ଦ୍ୱାରା ରିପୋର୍ଟ କରାଯାଇଛି ଡକ୍ଟର [[DOCTOR_NAME|Dr. Sanjay Patel]]
ଫୋନ୍: [[PHONE_NUMBER|9425123456]] | ABHA: [[ABHA_ID|12-3456-7890-1234]]
ହସ୍ପିଟାଲ୍ ID: [[HOSPITAL_ID|HSP-CG-007]] | ଜିଲ୍ଲା: [[DISTRICT|Bastar]]

କ୍ଲିନିକାଲ୍ ସୂଚନା: 21 ବର୍ଷର ପୁରୁଷ କ୍ରସର ଆଟେଣ୍ଡାଣ୍ଟଙ୍କଠାରେ ଆଚରଣଗତ ପରିବର୍ତ୍ତନ ଏବଂ ଆକ୍ରମଣର ଘଟଣାଗୁଡ଼ିକର ମୂଲ୍ୟାଙ୍କନ, ସାମାନ୍ୟ ମୁଣ୍ଡରେ ଆଘାତର ଇତିହାସ ସହିତ।

ପଦ୍ଧତି: 15 ଅଗଷ୍ଟ 2024 ରେ 1.5 ଟେସଲା ସ୍କାନ…
```

### S4 generation soft-fail 34

- **What:** generation soft-fail on `radiology_report` (`pa`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ਰੈਫਰਲ [[REFERRAL_ID|REF-2024-0815]] ਤੋਂ [[HOSPITAL_NAME|Sri Ganganagar Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ਬਾਰੇ [[PATIENT_NAME|Jaswant Singh]], [[AGE|60]] / [[GENDER|Male]], ਜ਼ਿਲ੍ਹਾ [[DISTRICT|Ganganagar]]
ਕਾਰਨ: ਪੇਟ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਦੀ ਹਰਨੀਆ ਦੀ ਸਰਜਰੀ

ਮਰੀਜ਼ [[PATIENT_NAME|Jaswant Singh]] 60 ਸਾਲ ਦਾ ਮਰਦ ਪਿੰਡ ਗੰਗਾਨਗਰ, ਰਾਜਸਥਾਨ ਤੋਂ ਲਗਭਗ 3 ਮਹੀਨੇ ਪੁਰਾਣੀ ਸੱਜੇ ਪਾਸੇ ਦੀ ਪੇਟ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਦੀ ਹਰਨੀਆ ਲਈ ਆਇਆ ਹੈ। ਹਰਨੀਆ ਵੱਡੀ ਹੁੰਦੀ ਜਾ ਰਹੀ ਹੈ ਅਤੇ ਹੁਣ ਸਰੀਰਕ ਗਤੀਵਿਧੀ ਦੌਰਾਨ ਹਲਕੇ ਦਰਦ ਦੇ ਨਾਲ ਘਟਣਯੋਗ ਹੈ। ਸਰੀਰਕ ਜਾਂਚ ਵਿੱਚ ਸੱਜੇ ਪੇਟ ਦੇ ਹੇਠਲੇ ਹਿੱਸੇ ਵਿੱਚ 4x3 ਸੈਂਟੀਮੀਟਰ ਦੀ ਘਟਣਯੋਗ ਗੰਢ ਮਿਲੀ ਹੈ, ਜੋ ਦਰਦ ਰਹਿਤ ਹੈ ਅਤੇ ਕੈਦ ਦੇ …
```

### S4 generation soft-fail 35

- **What:** generation soft-fail on `insurance_claim` (`pa`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ਰੈਫਰਲ [[REFERRAL_ID|REF-2024-0891]] ਤੋਂ [[HOSPITAL_NAME|Civil Hospital Amritsar]] / [[DOCTOR_NAME|Dr. Rajinder Singh]]
ਵਿਸ਼ਾ: [[PATIENT_NAME|Melo Kaur]], [[AGE|45]] / [[GENDER|Female]], ਜ਼ਿਲ੍ਹਾ [[DISTRICT|Amritsar]]
ਕਾਰਨ: ਲਗਾਤਾਰ ਪੇਟ ਦਰਦ ਦੇ ਨਾਲ ਭਾਰ ਘਟਣਾ ਅਤੇ ਥਕਾਵਟ

ਸਤਿਕਾਰਯੋਗ ਸਾਥੀ,

ਮੈਂ ਰੈਫਰ ਕਰ ਰਿਹਾ ਹਾਂ [[PATIENT_NAME|Melo Kaur]], ਇੱਕ 45 ਸਾਲ ਦੀ ਮਹਿਲਾ ਮਰੀਜ਼, ਅੰਮ੍ਰਿਤਸਰ ਤੋਂ, ਕੈਂਸਰ ਵਿਗਿਆਨਕ ਮੁਲਾਂਕਣ ਅਤੇ ਪ੍ਰਬੰਧਨ ਲਈ। ਮਰੀਜ਼ 3 ਮਹੀਨੇ ਦਾ ਇਤਿਹਾਸ ਪੇਸ਼ ਕਰਦਾ ਹੈ ਵਧਦੇ ਪੇਟ ਦਰਦ, ਜਲਦੀ ਪੇਟ ਭਰਨਾ, ਅਤੇ ਅਣਜਾਣੇ ਵਿੱਚ ਲਗਭਗ 8 ਕਿਲੋ ਭਾਰ ਘਟਣਾ।

ਲੈਬਾਰਟਰੀ ਜਾਂਚ ਦਿਖਾਉਂਦੇ ਹਨ ਹਲਕਾ ਅਨੀਮੀਆ ਹੀਮੋਗਲੋਬਿਨ 9.8 g/dL ਦੇ ਨਾਲ ਅਤੇ ਵਧੇ ਹੋਏ ਜਿਗਰ ਦੇ…
```

### S4 generation soft-fail 36

- **What:** generation soft-fail on `insurance_claim` (`sa`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
शल्यचिकित्सा टिप्पणी — [[HOSPITAL_NAME|Bundi District Hospital]] प्रवेशः [[ADMISSION_NUMBER|ADM-2024-1123]] कक्षः [[WARD_NUMBER|OT]] [[BED_NUMBER|12]]
[[PATIENT_NAME|Kavita Sharma]] [[AGE|19]] [[GENDER|Female]] शल्यचिकित्सकः [[DOCTOR_NAME|Dr. Rajesh Kumar]]
प्रक्रिया / निष्कर्षः: रोगी शङ्कितघातक अर्बुदस्य कृते लेप्रोस्कोपिक-उजवाण्ड-अर्बुद-छेदनं कृतवती। शल्यचिकित्सा-पूर्व-चित्रणे 7 से.मी. जटिलं पुटीय-पिण्डं ठोस-घटकैः सह उच्च-CA-125 स्तरैः सह प्रकटितम्। शल्यचिकित्सा-मध्ये शीतलीकृत-खण्डने सीमा-रेखा-अर्बुदः पुष्टः। नकारात्मक-सीमाभिः सह पूर्ण-अर्बुद-छेदनं प्राप्तम्। अवस्थापनाय ओमेन्टेक्टोमी कृतम्।…
```

### S4 generation soft-fail 37

- **What:** generation soft-fail on `prescription` (`sat`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨᱮ ᱡᱚᱡᱚᱢ ᱪᱮᱛᱟᱱ ᱞᱳᱵᱽ ᱨᱮ infiltrates ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ ᱯᱮᱥᱮᱱᱴ ᱫᱚ Pulmonary Tuberculosis ᱛᱮ ᱰᱟᱭᱜᱽᱱᱳᱥᱤᱥ ᱦᱩᱭ ᱟᱠᱟᱱᱟ ᱾

Rx:
- Isoniazid 300mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ
- Rifampicin 600mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ  
- Pyrazina…
```

### S4 generation soft-fail 38

- **What:** generation soft-fail on `discharge_summary` (`sat`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'ABHA_ADDRESS', 'CASTE']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,ABHA_ADDRESS,CASTE']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨᱮ ᱡᱚᱡᱚᱢ ᱪᱮᱛᱟᱱ ᱞᱳᱵᱽ ᱨᱮ infiltrates ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ ᱯᱮᱥᱮᱱᱴ ᱫᱚ Pulmonary Tuberculosis ᱛᱮ ᱰᱟᱭᱜᱽᱱᱳᱥᱤᱥ ᱦᱩᱭ ᱟᱠᱟᱱᱟ ᱾

Rx:
- Isoniazid 300mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ
- Rifampicin 600mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ  
- Pyrazina…
```

### S4 generation soft-fail 39

- **What:** generation soft-fail on `surgical_note` (`sat`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨᱮ ᱡᱚᱡᱚᱢ ᱪᱮᱛᱟᱱ ᱞᱳᱵᱽ ᱨᱮ infiltrates ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ ᱯᱮᱥᱮᱱᱴ ᱫᱚ Pulmonary Tuberculosis ᱛᱮ ᱰᱟᱭᱜᱽᱱᱳᱥᱤᱥ ᱦᱩᱭ ᱟᱠᱟᱱᱟ ᱾

Rx:
- Isoniazid 300mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ
- Rifampicin 600mg ᱢᱤᱫ ᱫᱤᱱ ᱨᱮ ᱢᱤᱫ ᱫᱷᱟᱣ  
- Pyrazina…
```

### S4 generation soft-fail 40

- **What:** generation soft-fail on `prescription` (`sat`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4 generation soft-fail 41

- **What:** generation soft-fail on `asha_worker_note` (`sd`).
- **Missing required tags:** `['BPL_RATION_CARD', 'RELIGION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BPL_RATION_CARD,RELIGION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
نسخہ — [[HOSPITAL_NAME|Dr. S.N. Medical College Hospital]]
مريضو [[PATIENT_NAME|Jareen Bano]], [[AGE|38]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0915-002]]
ڊاڪٽر [[DOCTOR_NAME|Dr. Rajesh Kumar]]
فون [[PHONE_NUMBER|9876543210]]
ABHA [[ABHA_ID|12-3456-7890-1234]]
مريضو ID [[PATIENT_ID|PID-BKN-2024-789]]
پتھ [[RESIDENTIAL_ADDRESS|House No. 45, Gandhi Colony, Ward 12, Bikaner]]
ضلعو [[DISTRICT|Bikaner]]

تشخيص: اسٽيج III ڇاتيءَ جو ڪينسر سان ميٽاسٽيٽڪ لمف نوڊس

نسخہ:
1. Paclitaxel 175mg/m² IV انفيوژن دھن، اٺن، پندرهن تي ٢٨-ڏينهن چڪر
2. Trastuzumab 8mg/kg IV لوڊنگ ڊوز، پھرين 6mg/kg هفتي وار
3. Onda…
```

### S4 generation soft-fail 42

- **What:** generation soft-fail on `insurance_claim` (`sd`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER', 'CREDIT_CARD_NUMBER', 'CVV', 'PIN', 'PHONE_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV,PIN,PHONE_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: تُہُنٛد آنڪولوجي فالو اپ [[DOCTOR_NAME|Dr. Anjali Sharma]] سان [[HOSPITAL_NAME|Jabalpur Cancer Centre]] پؠٹھ [[APPOINTMENT_ID|APT-240521-01]] لاءِ تصديق ٿي ويو آهي۔ مહેરباني ڪري پنهنجو [[MRN|MRN-2024-0815-001]] ڪارڊ آڻيو۔ تصديق لاءِ [[PHONE_NUMBER|9876512340]] فون ڪيو۔
```

### S4 generation soft-fail 43

- **What:** generation soft-fail on `er_triage_notes` (`sd`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: تُہُنٛد آنڪولوجي فالو اپ [[DOCTOR_NAME|Dr. Anjali Sharma]] سان [[HOSPITAL_NAME|Jabalpur Cancer Centre]] پؠٹھ [[APPOINTMENT_ID|APT-240521-01]] لاءِ تصديق ٿي ويو آهي۔ مહેરباني ڪري پنهنجو [[MRN|MRN-2024-0815-001]] ڪارڊ آڻيو۔ تصديق لاءِ [[PHONE_NUMBER|9876512340]] فون ڪيو۔
```

### S4 generation soft-fail 44

- **What:** generation soft-fail on `surgical_note` (`sd`).
- **Missing required tags:** `['MRN', 'PATIENT_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:MRN,PATIENT_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: تُہُنٛد آنڪولوجي فالو اپ [[DOCTOR_NAME|Dr. Anjali Sharma]] سان [[HOSPITAL_NAME|Jabalpur Cancer Centre]] پؠٹھ [[APPOINTMENT_ID|APT-240521-01]] لاءِ تصديق ٿي ويو آهي۔ مહેરباني ڪري پنهنجو [[MRN|MRN-2024-0815-001]] ڪارڊ آڻيو۔ تصديق لاءِ [[PHONE_NUMBER|9876512340]] فون ڪيو۔
```

### S4 generation soft-fail 45

- **What:** generation soft-fail on `insurance_claim` (`ta`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
வெளிநோயாளி சீட்டு | [[HOSPITAL_NAME|Government Medical College Hospital, Dharmapuri]] | ID [[HOSPITAL_ID|GMCH-DH-001]]
நோயாளி: [[PATIENT_NAME|Karthik Raj]] | DOB [[DOB|2002-05-15]] | வயது: [[AGE|22]] | பாலினம்: [[GENDER|Male]]
தொழில்: [[OCCUPATION|Student]] | MRN: [[MRN|OPD-2024-0815-001]] | மருத்துவர்: [[DOCTOR_NAME|Dr. S. Anand]]
உறவினர்: [[RELATIVE_NAME|R. Murugan]] | தொலைபேசி: [[PHONE_NUMBER|9876543210]]
பதிவாளர் அடையாள எண்: [[EMPLOYEE_ID|REG-2024-0815-003]] | மாவட்டம்: [[DISTRICT|Dharmapuri]]

முக்கியமான புகார்: 3 மாதங்களாகத் தொடரும் சோர்வு, உடல் எடை குறைவு மற்றும் வீங்கிய நிணநீர் முடிச்…
```

### S4 generation soft-fail 46

- **What:** generation soft-fail on `phc_register` (`te`).
- **Missing required tags:** `['BPL_RATION_CARD']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BPL_RATION_CARD']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
PHC రిజిస్టర్ — [[HOSPITAL_NAME|PHC Kommuru]] గ్రామం [[VILLAGE|Kommuru]] జిల్లా [[DISTRICT|Krishna]]
[[PATIENT_NAME|Ravi Kumar]] [[AGE|22]] [[GENDER|Male]] | 3 రోజుల నుండి జ్వరం మరియు దగ్గు
రోగి 21 మే 2024 ఉదయం గత 3 రోజుల నుండి తీవ్రమైన జ్వరం, వణుకు మరియు పొడి దగ్గుతో వచ్చారు. అతను శరీరం అంతటా నొప్పులు మరియు బలహీనత ఉందని చెబుతున్నాడు. శ్వాస తీసుకోవడంలో ఇబ్బంది లేదా ఛాతీ నొప్పి చరిత్ర లేదు. అతను స్థానిక దుకాణం నుండి పారాసెటమాల్ స్వయంగా తీసుకున్నాడు, కొంత ఉపశమనం కలిగింది.

పరీక్షలో, వైటల్స్: ఉష్ణోగ్రత 102.4°F, నాడి 98/నిమిషానికి, BP 120/80 mmHg, RR 18/నిమిషానికి. సాధారణ స్థితి: స్పృహలో, అప్రమత్…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `lab_report` (`brx`).
- **Error:** `dedicated_translate_failed:Translation under-counted [[PATIENT_NAME|…]] tags: found=0 expected>=1;script_purity_failed:wrong_indic_script:Bengali>Devanagari;dedicated_translate_failed:Translation under-counted [[PATIENT_NAME|…]] tags: found=0 expected>=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Chirang District Hospital]]
Patient [[PATIENT_NAME|Jiran Basumatary]], [[AGE|33]] / [[GENDER|Male]], MRN [[MRN|MRN-2024-CHIR-001]]
Dr. [[DOCTOR_NAME|Dr. Pranab Kalita]]
Contact: [[PHONE_NUMBER|9876543210]]
Address: [[RESIDENTIAL_ADDRESS|Bhurkunda, Chirang, Assam]]
District: [[DISTRICT|Chirang]]
Patient ID: [[PATIENT_ID|PID-CHIR-2024-001]]
ABHA ID: [[ABHA_ID|12-3456-…
```
- **Translated preview:**

```
प्रिस्क्रिप्शन — [[HOSPITAL_NAME|Chirang District Hospital]]
बेरामि [[PATIENT_NAME|Jiran Basumatary]], [[AGE|33]] / [[GENDER|Male]], एम.आर.एन. [[MRN|MRN-2024-CHIR-001]]
डक्टर [[DOCTOR_NAME|Dr. Pranab Kalita]]
जायगानि सुलुं: [[PHONE_NUMBER|9876543210]]
थं: [[RESIDENTIAL_ADDRESS|Bhurkunda, Chirang, Assam]]
जिल्ला: [[DISTRICT|Chirang]]
बेरामिनि आइ.डि.: [[PATIENT_ID|PID-CHIR-2024-001]]
ए.बि.एच.ए. आइ.…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `hospital_billing` (`doi`).
- **Error:** `prefer_chat_1:Missing ID placeholder restore for ⟦ID22⟧;prefer_chat_2:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|180012]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Government Medical College Hospital, Jammu]]
Patient [[PATIENT_NAME|Ramesh Kumar]], [[AGE|25]] / [[GENDER|Male]], MRN [[MRN|MRN-JK-2024-0156]]
Dr. [[DOCTOR_NAME|Dr. Ajay Sharma]]
[[PATIENT_ID|PID-JK-2024-0089]]
[[ABHA_ID|12-3456-7890-1234]]
[[PHONE_NUMBER|9419876543]]
[[DISTRICT|Jammu]]
[[RESIDENTIAL_ADDRESS|Village Bishnah, Tehsil Bishnah, Jammu]]

Date: 2024-10-26…
```
- **Translated preview:**

```
नुस्खा — [[HOSPITAL_NAME|Government Medical College Hospital, Jammu]]
मरीज [[PATIENT_NAME|Ramesh Kumar]], [[AGE|25]] / [[GENDER|Male]], MRN [[MRN|MRN-JK-2024-0156]]
डाक्टर [[DOCTOR_NAME|Dr. Ajay Sharma]]
[[PATIENT_ID|PID-JK-2024-0089]]
[[ABHA_ID|12-3456-7890-1234]]
[[PHONE_NUMBER|9419876543]]
[[DISTRICT|Jammu]]
[[RESIDENTIAL_ADDRESS|Village Bishnah, Tehsil Bishnah, Jammu]]

तारीख: 2024-10-26

मरी…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `hospital_billing` (`gu`).
- **Error:** `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Kankrol]], District [[DISTRICT|Junagadh]]
Beneficiary [[PATIENT_NAME|Valukbhai Singh]], [[AGE|50]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Kiranben Rathod]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased fatigue and intermittent chest discomfort. Blood pressure reading 145/90 mmHg. Adherence to oral chemotherapy medications is incons…
```
- **Translated preview:**

```
આશા કાર્યકર નોંધ — ગામ [[VILLAGE|Kankrol]], જિલ્લા [[DISTRICT|Junagadh]]
લાભાર્થી [[PATIENT_NAME|Valukbhai Singh]], [[AGE|50]] / [[GENDER|Male]]
આશા: [[ASHA_WORKER_NAME|Kiranben Rathod]] | ફોન [[PHONE_NUMBER|9876543210]]
મુલાકાતના તારણો: દર્દી વધતી જતી થાક અને છાતીમાં વચ્ચે-વચ્ચે થતા દુખાવાની જાણ કરે છે. બ્લડ પ્રેશર રીડિંગ 145/90 mmHg છે. મૌખિક કીમોથેરાપી દવાઓનું પાલન અનિયમિત છે. પરિવાર સારવારના …
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `opd_slip` (`gu`).
- **Error:** `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Kankrol]], District [[DISTRICT|Junagadh]]
Beneficiary [[PATIENT_NAME|Valukbhai Singh]], [[AGE|50]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Kiranben Rathod]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased fatigue and intermittent chest discomfort. Blood pressure reading 145/90 mmHg. Adherence to oral chemotherapy medications is incons…
```
- **Translated preview:**

```
આશા કાર્યકર નોંધ — ગામ [[VILLAGE|Kankrol]], જિલ્લા [[DISTRICT|Junagadh]]
લાભાર્થી [[PATIENT_NAME|Valukbhai Singh]], [[AGE|50]] / [[GENDER|Male]]
આશા: [[ASHA_WORKER_NAME|Kiranben Rathod]] | ફોન [[PHONE_NUMBER|9876543210]]
મુલાકાતના તારણો: દર્દી વધતી જતી થાક અને છાતીમાં વચ્ચે-વચ્ચે થતા દુખાવાની જાણ કરે છે. બ્લડ પ્રેશર રીડિંગ 145/90 mmHg છે. મૌખિક કીમોથેરાપી દવાઓનું પાલન અનિયમિત છે. પરિવાર સારવારના …
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `referral_letter` (`kn`).
- **Error:** `tag_restore_or_translate_failed:dedicated_translate_failed:Translation under-counted [[RELATIVE_NAME|…]] tags: found=1 expected>=2`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Koppal District Hospital]]
Patient [[PATIENT_NAME|Savitri Gowda]], [[AGE|55]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Rx: Ceftriaxone 1g IV every 12 hours for 5 days, Metronidazole 500mg IV every 8 hours for 7 days, Paracetamol 500mg orally every 6 hours as needed for pain. Post-operative instructions: Wound care with s…
```
- **Translated preview:**

```
ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ — [[HOSPITAL_NAME|Koppal District Hospital]]
ರೋಗಿ [[PATIENT_NAME|Savitri Gowda]], [[AGE|55]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
ವೈದ್ಯರು [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ಸೂಚನೆ: Ceftriaxone 1g IV ಪ್ರತಿ 12 ಗಂಟೆಗಳು 5 ದಿನಗಳು, Metronidazole 500mg IV ಪ್ರತಿ 8 ಗಂಟೆಗಳು 7 ದಿನಗಳು, Paracetamol 500mg ಬಾಯಿಯ ಮೂಲಕ ಪ್ರತಿ 6 ಗಂಟೆಗಳು ನೋವಿಗೆ ಅಗತ್ಯವಿದ್ದಲ್ಲಿ. ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಯ ನಂತರದ ಸೂಚನೆಗಳು…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `hospital_billing` (`ks`).
- **Error:** `prefer_chat_1:Sarvam timeout after 180.0s: The read operation timed out;prefer_chat_2:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[VEHICLE_REGISTRATION|JK01AB1234]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Srinagar]], District [[DISTRICT|Srinagar]]
Beneficiary [[PATIENT_NAME|Naseema Bano]], [[AGE|35]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Amina Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss. Chest X-ray shows infiltrates consistent with pulmonary TB. Also reports hy…
```
- **Translated preview:**

```
آشا ورکر نوٹ — گام [[VILLAGE|عائشہ بیگم]]، ضلع [[DISTRICT|بڈگام]]
مریض [[PATIENT_NAME|عائشہ بیگم]]، [[AGE|35]] / [[GENDER|Female]]
آشا: [[ASHA_WORKER_NAME|عائشہ]] | فون [[PHONE_NUMBER|9876543210]]
معائنے کے نتائج: مریضہ میں تین ہفتوں سے مستقل کھانسی، ہلکا تپہٕ، اور وزن میں کمی ہے۔ تھوراکس ایکس-رے میں انفلٹریٹس دکھتے ہیں، جو پلمونری ٹی بی کے مطابق ہیں۔ اس کے علاوہ، مریضہ ہائپر ٹینشن اور ذیابیطس بت…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[STATE|Manipur]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[STATE|Manipur]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Leima Chanu]], your oncology follow-up is scheduled for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Imphal East Cancer Center]] with [[DOCTOR_NAME|Dr. Thoudam Singh]]. Please bring your [[MRN|MRN-2024-0615-001]] and arrive 15 minutes early. Contact [[PHONE_NUMBER|9876543210]] for queries.
```
- **Translated preview:**

```
ꯅꯨꯡꯁꯤꯕ [[PATIENT_NAME|Leima Chanu]], ꯅꯍꯥꯛꯀꯤ ꯑꯣꯟꯀꯣꯂꯣꯖꯤ ꯐꯣꯂꯣ-ꯑꯞ ꯑꯁꯤ [[HOSPITAL_NAME|Imphal East Cancer Center]]ꯗ [[HOSPITAL_NAME|Imphal East Cancer Center]]ꯗ [[DOCTOR_NAME|Dr. Thoudam Singh]]ꯒ ꯂꯣꯏꯅꯅ [[APPOINTMENT_ID|APT-240615-02]]ꯒꯤꯗꯃꯛ ꯁꯦꯗ꯭ꯌꯨꯜ ꯇꯧꯔꯦ꯫ ꯅꯍꯥꯛꯀꯤ [[MRN|MRN-2024-0615-001]] ꯑꯗꯨ ꯄꯨꯔꯛꯄꯤꯌꯨ ꯑꯃꯁꯨꯡ ꯃꯤꯅꯤꯠ 15 ꯃꯃꯥꯡꯗ ꯂꯥꯛꯄꯤꯌꯨ꯫ ꯋꯥꯍꯪ ꯀꯌꯥꯒꯤꯗꯃꯛ [[PHONE_NUMBER|9876543210]]ꯒ ꯄꯥꯎ ꯐꯥꯎꯅꯕꯤꯌꯨ꯫
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `radiology_report` (`mni`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[ABHA_ID|12-3456-7890-1234]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[ABHA_ID|12-3456-7890-1234]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Rina Boro]]: Your appointment [[APPOINTMENT_ID|APT-240521-01]] with [[DOCTOR_NAME|Dr. Anjali Sharma]] at [[HOSPITAL_NAME|Silchar Medical College]] on 21-May at 10:30 AM. Please confirm on [[PHONE_NUMBER|9876543210]]. MRN [[MRN|MRN-2024-0815-001]].
```
- **Translated preview:**

```
[[PATIENT_NAME|Rina Boro]]: ꯅꯍꯥꯀꯀꯤ ꯑꯦꯄꯣꯏꯟꯃꯦꯟꯠ [[APPOINTMENT_ID|APT-240521-01]] ꯒꯥ [[DOCTOR_NAME|Dr. Anjali Sharma]] ꯇꯥ [[HOSPITAL_NAME|Silchar Medical College]] ꯇꯥ 21-May ꯇꯥ 10:30 AM. ꯄ꯭ꯂꯤꯁ ꯀꯣꯟꯐꯔ꯭ꯃ ꯇꯧꯕꯤꯅꯕ ꯇꯥ [[PHONE_NUMBER|9876543210]]. MRN [[MRN|MRN-2024-0815-001]].
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `er_triage_notes` (`mr`).
- **Error:** `no_valid_entity_tags_to_protect`
- **script_ok:** `False`
- **EN pivot preview:**

```
Lab Report — [[HOSPITAL_NAME|Civil Hospital Ahmednagar]] District [[DISTRICT|Ahmednagar]]
MRN [[MRN|MH-AHM-2024-0815]] Patient ID [[PATIENT_ID|PID-MH-78945]]
[[PATIENT_NAME|Ramesh Patil]] [[AGE|22]] [[GENDER|Male]] Phone [[PHONE_NUMBER|9876543210]]
Ordered by [[DOCTOR_NAME|Dr. Priya Deshmukh]]
Date: 15 August 2024

Patient Information:
[[PATIENT_NAME|Ramesh Patil]] is a 22-year-old male from rura…
```
- **Translated preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|सिव्हिल हॉस्पिटल अहमदनगर]] जिल्हा [[DISTRICT|Ahmednagar]]
एमआरएन [[MRN|MH-AHM-2024-0815]] रुग्ण आयडी [[PATIENT_ID|PID-MH-78945]]
[[PATIENT_NAME|Ramesh Patil]] [[AGE|22]] [[GENDER|Male]] फोन [[PHONE_NUMBER|9876543210]]
द्वारे [[DOCTOR_NAME|Dr. Priya Deshmukh]] आदेशित
दिनांक: 15 आगस्ट 2024

रुग्णाची माहिती:
[[PATIENT_NAME|Ramesh Patil]] ग्रामीण महाराष्ट्रातील 22 व…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `hospital_billing` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MC-WB-2024-0815]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MC-WB-2024-0815]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss. Sputum smear positive for acid-fast bacilli. Chest X-ray shows infil…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨ…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `discharge_summary` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM3⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM3⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss. Sputum smear positive for acid-fast bacilli. Chest X-ray shows infil…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨ…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `er_triage_notes` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss. Sputum smear positive for acid-fast bacilli. Chest X-ray shows infil…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|27]] / [[GENDER|Female]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9832145678]]

ᱯᱮᱥᱮᱱᱴ ᱟᱜ ᱓ ᱦᱟᱯᱛᱟ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱟᱥᱤ, ᱠᱚᱢ ᱡᱩᱨ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱧᱮᱞᱚᱜ ᱠᱟᱱᱟ ᱾ Sputum smear ᱫᱚ acid-fast bacilli ᱞᱟᱹᱜᱤᱫ ᱯᱚᱡᱤᱴᱤᱵᱽ ᱜᱮᱭᱟ ᱾ Chest X-ray ᱨ…
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `automated_sms` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[APPOINTMENT_ID|APT-240815-02]]';rare_recovery_1:Translation lost or altered name/place TYPE 'DOCTOR_NAME' (placeholder ⟦NM2⟧);dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-OD-2024-001]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[INSURANCE_POLICY_NUMBER|POL-OD-2024-0042]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[INSURANCE_POLICY_NUMBER|POL-OD-2024-0042]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `radiology_report` (`sat`).
- **Error:** `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: appt [[APPOINTMENT_ID|APT-240815-02]] at [[HOSPITAL_NAME|PHC Kendujhar]] on 15-Aug 11:00 with [[DOCTOR_NAME|Dr. S. Mahanta]]. MRN [[MRN|MRN-OD-2024-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `opd_slip` (`sd`).
- **Error:** `prefer_chat_1:Sarvam timeout after 240.0s: The read operation timed out;prefer_chat_2:Sarvam timeout after 240.0s: The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your oncology follow-up at [[HOSPITAL_NAME|Jabalpur Cancer Centre]] is confirmed for [[APPOINTMENT_ID|APT-240521-01]] with [[DOCTOR_NAME|Dr. Anjali Sharma]]. Please bring your [[MRN|MRN-2024-0815-001]] card. Call [[PHONE_NUMBER|9876512340]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: تُہُنٛد آنڪولوجي فالو اپ [[DOCTOR_NAME|Dr. Anjali Sharma]] سان [[HOSPITAL_NAME|Jabalpur Cancer Centre]] پؠٹھ [[APPOINTMENT_ID|APT-240521-01]] لاءِ تصديق ٿي ويو آهي۔ مહેરباني ڪري پنهنجو [[MRN|MRN-2024-0815-001]] ڪارڊ آڻيو۔ تصديق لاءِ [[PHONE_NUMBER|9876512340]] فون ڪيو۔
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `asha_worker_note` (`te`).
- **Error:** `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELATIVE_NAME' (placeholder ⟦NM4⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Gollapalli]], District [[DISTRICT|Anantapur]]
Beneficiary [[PATIENT_NAME|Rama Rao]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi]], Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presented with persistent cough and low-grade fever for the past week. He reports mild breathlessness on exertion and a 2kg weight loss. No known comorbidities.
…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Gollapalli]], District [[DISTRICT|Anantapur]]
Beneficiary [[PATIENT_NAME|Rama Rao]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi]], Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presented with persistent cough and low-grade fever for the past week. He reports mild breathlessness on exertion and a 2kg weight loss. No known comorbidities.
…
```

### S4b translation soft-fail 18

- **What:** translation soft-fail on `hospital_billing` (`ur`).
- **Error:** `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Operative note — [[HOSPITAL_NAME|Osmania General Hospital]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-001]] Ward [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Ayesha Begum]] [[AGE|38]] [[GENDER|Female]] Surgeon [[DOCTOR_NAME|Dr. Priya Reddy]]
[[PATIENT_ID|PID-2024-0815-001]] [[MRN|MRN-2024-0815-001]] Patient presented with placenta previa at 36 weeks gestation with active bleeding. Emergency lower segment cesarea…
```
- **Translated preview:**

```
جراحی نوٹ — [[HOSPITAL_NAME|Osmania General Hospital]] داخل [[ADMISSION_NUMBER|ADM-2024-0815-001]] وارڈ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Ayesha Begum]] [[AGE|38]] [[GENDER|Female]] سرجن [[DOCTOR_NAME|Dr. Priya Reddy]]
[[PATIENT_ID|PID-2024-0815-001]] [[MRN|MRN-2024-0815-001]] مریضہ نے پلاسنٹا پریویا کے ساتھ 36 ہفتوں کے حمل میں سرگرم خون بہنے کی شکایت پیش کی۔ ہنگامی لوئر سیگمنٹ سیزیرین سیکشن اسپا…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `lab_report` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'invented_entity_type']`
- **Reasoning:** Clinical prose uses Bengali-Assamese script and Assamese phrasing instead of required Bodo Devanagari; LABORATORY_TECHNICIAN_NAME and LAB_TECH_ID outside allow-list.
- **Preview:**

```
লেব রিপোর্ট — [[HOSPITAL_NAME|বড়ো মেডিকেল কলেজ হাস্পতাল]] জিলা [[DISTRICT|চিৰাং]]
MRN [[MRN|MRN-AS-2024-0815-001]] ৰোগীৰ পৰিচয় পত্ৰ [[PATIENT_ID|PID-AS-7781]]
[[PATIENT_NAME|ৰঞ্জিত বসুমতাৰী]] [[AGE|33]] [[GENDER|Male]] ফোন [[PHONE_NUMBER|9876543210]]
দ্বাৰা নিৰ্দেশিত [[DOCTOR_NAME|ড° প্ৰমোদ কুমাৰ বৰুৱা]]
তাৰিখ: 15 আগষ্ট 2024

ৰোগীৰ প্ৰফাইল:
চিৰাং জিলাৰ গাঁৱৰ বাসিন্দা, বৃত্তি: নিমখ উৎপাদন কৰা খেতিয়ক। 3 সপ্তাহ ধৰি একেৰাহে কাহ, মৃদু জ্বৰ আৰু 5 কেজি ওজন হ্ৰাস হোৱাৰ লক্ষণ দেখা দিছে। কোনো জ্ঞাত সহ…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `asha_worker_note` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'cross_language_entity_shift', 'surrogate_plausibility_collapse']`
- **Reasoning:** Bodo prose polluted with Hindi phrases; patient name culturally implausible and in wrong script for Devanagari Bodo note.
- **Preview:**

```
आशा नोट — गाम [[VILLAGE|Bongaigaon]], जिल्ला [[DISTRICT|Chirang]]
रोगी [[PATIENT_NAME|Senthil Venkatesh]], [[AGE|33]] / [[GENDER|Male]]
आशा: [[ASHA_WORKER_NAME|अनिमा बसुमतारी]] | फोन [[PHONE_NUMBER|9875432109]]
रिपोर्ट: रोगीयाव हालैनि काट-छाँट प्रक्रिया पछी आगसि आखायआव संक्रमित शल्यक्रिया घाउ नुजादों। घाउयाव सुखाबनायनि लक्षण नुजादों आउर एसे पूय निकास। ड्रेसिंग स्वच्छता बनाए रखननि सलाह दी गई आउर टांका हटाउनका लिए हास्पिटाल फिर्ता आउन। [[RELATIVE_NAME|रमेश बसुमतारी]] (बिफा) रोगीया संगै थांदोंमोन …
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `referral_letter` (`brx`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['invented_entity_type']`
- **Reasoning:** REFERRAL_ID outside allow-list; Bodo Devanagari prose and persona fit otherwise acceptable.
- **Preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-089]] निफ्राय [[HOSPITAL_NAME|Baksa District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Kalita]]
सोमोन्दो: [[PATIENT_NAME|Bikash Boro]], [[AGE|34]] / [[GENDER|Male]], जिला [[DISTRICT|Baksa]]
जाहोन: थाबाय थानाय खोख्लैनायजों ओजोन खम जानाय आरो डायबिटीस मेलिटस

मानगोनां लोगो,

बेयो रेफरेल खालामनो थाखाय [[PATIENT_NAME|Bikash Boro]], बाकस जिला निफ्राय 34 बोसोरनि हौवा, जायनि लक्षणफोरा फुंखायारि हाबनाय बेरामखौ दिनथियो आरो बेयो गोदानै सिनायथिनाय टाइप 2 डायबिटीस मेलिटसजों जेथो गोन…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`ks`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['surrogate_plausibility_collapse']`
- **Reasoning:** Name clash: PATIENT_NAME=Manoj Yadav vs. doctor addressing patient as غلام رسول + ghulam.rasool email; Kashmiri prose and clinical fit otherwise acceptable.
- **Preview:**

```
--- session ---
مریض [[PATIENT_NAME|Manoj Yadav]] [[AGE|33]] [[GENDER|Male]]
ملاقات [[APPOINTMENT_ID|APT-241120-03]] Portal [[URL|https://tele.jkhospital.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9419876543]]
Email [[EMAIL_ADDRESS|ghulam.rasool@example.com]] Hospital [[HOSPITAL_NAME|ایس کے آئی ایم ایس]]
--- chat ---
مریض: سلام ڈاکٹر۔ بہٕ چھس ترےٚ ہفتہٕ پٮ۪ٹھٕ کھانسی ہنٛد شکار، کُنہِ سا…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Manipuri/Meitei script per instructions.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815-001]] from [[HOSPITAL_NAME|Regional Institute of Medical Sciences, Imphal]] / [[DOCTOR_NAME|Dr. Thokchom Sanjit Singh]]
Re: [[PATIENT_NAME|Ngangom Ongbi Leima]], [[AGE|27]] / [[GENDER|Female]], District [[DISTRICT|Imphal East]]
Reason: Persistent cough with constitutional symptoms and comorbid hypertension requiring specialized evaluation

Dear Colleague,

This is to refer [[PATIENT_NAME|Ngangom Ongbi Leima]], a 27-year-old female from [[VILLAGE|Wangjing]], …
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `insurance_claim` (`sa`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Hindi/English (TPA, RTA, PAN, IFSC, दावा) instead of Sanskrit; Devanagari present but language not matching expected sa.
- **Preview:**

```
TPA दावा — नीतिः [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Feroz Khan]] [[AGE|19]] [[GENDER|Male]] आधारः [[AADHAAR_NUMBER|254465626238]]
चिकित्सालयः [[HOSPITAL_NAME|District Hospital Kanpur]] जनपदः [[DISTRICT|Kanpur Nagar]]
मोटर / RTA वाहनम् [[VEHICLE_REGISTRATION|UP78AB1234]] (एकवारम् एव)।
PAN [[PAN_NUMBER|ABCDE1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|50200012345678]]
[[BANK_ROUTING_NUMBER|SBIN0001234]]
[[CREDIT_CARD_NUMBER|4111111111111111]]
[[CVV|12…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `hospital_billing` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All narrative prose in English/Latin; expected Santali Ol Chiki script absent despite correct allow-listed tags and persona fit.
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|Medinipur Cancer Care Centre]] District [[DISTRICT|Paschim Medinipur]] PIN [[PIN_CODE|721134]] Patient [[PATIENT_NAME|Rina Murmu]] MRN [[MRN|MC-WB-2024-0815]] Address [[RESIDENTIAL_ADDRESS|Village: Kharagpur, Post: Kharagpur, Block: Kharagpur]] Phone [[PHONE_NUMBER|9876543210]] Email [[EMAIL_ADDRESS|rina.murmu@example.com]] PAN [[PAN_NUMBER|FGHIJ5678K]] Landline [[TELEPHONE_LANDLINE|03222-254789]] Vehicle [[VEHICLE_REGISTRATION|WB40AB1234]] Aadhaar [[AADHAAR_NUMBER|206…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `discharge_summary` (`sat`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** Female patient described with 'patni' (wife) relative + male name Bijoy; gender/spouse mismatch breaks persona and surrogate plausibility.
- **Preview:**

```
ᱰᱤᱥᱪᱟᱨᱡᱽ ᱥᱟᱨᱟᱝᱥ — [[HOSPITAL_NAME|Paschim Medinipur District Hospital]]
[[PATIENT_NAME|Santi Murmu]] ᱡᱚᱱᱚᱢ ᱢᱟᱹᱦᱤᱛ [[DOB|1997-03-15]] [[AGE|27]] [[GENDER|Female]]
ᱮᱰᱢᱤᱥ [[ADMISSION_NUMBER|ADM-2024-0456]] ᱣᱟᱨᱰ [[WARD_NUMBER|B1]] ᱵᱮᱰ [[BED_NUMBER|08]]
ᱰᱟᱠᱛᱚᱨ [[DOCTOR_NAME|Dr. Priya Chatterjee]] | ᱠᱚᱨᱥ / ᱥᱟᱞᱦᱟ: ᱨᱩᱜᱤ ᱫᱚ ᱠᱟᱹᱣᱰᱤ ᱟᱱᱟᱴ ᱟᱨ ᱞᱚᱦᱚᱫ ᱠᱷᱚᱨᱪᱟ ᱨᱮᱭᱟᱜ ᱟᱱᱟᱴ ᱥᱟᱶ ᱡᱚᱯᱚᱲᱟᱣ ᱟᱱᱟᱴ ᱟᱨ ᱞᱚᱦᱚᱫ ᱠᱷᱚᱨᱪᱟ ᱨᱮᱭᱟᱜ ᱞᱚᱠᱷᱚᱱ ᱥᱟᱶ ᱮ ᱥᱮᱴᱮᱨ ᱟᱠᱟᱱᱟ ᱾ ᱩᱱᱤ ᱫᱚ ᱟᱹᱰᱤ ᱰᱷᱮᱨ ᱠᱤᱨᱤᱧ ᱟᱨ ᱥᱟᱯᱷᱟᱼᱥᱟᱯᱷᱤ ᱵᱟᱧᱪᱟᱣ ᱨᱮᱭᱟᱜ ᱟᱹᱵᱷᱭᱟᱥ ᱛᱟᱦᱮᱸ ᱠᱟᱛᱮᱫ ᱦᱚᱸ ᱠᱷ…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `er_triage_notes` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely English; expected Santali Ol Chiki clinical narrative.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Sub Divisional Hospital Medinipur]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Phulo Murmu]] [[AGE|27]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|WB09J1234]] (exactly once).
Relative [[RELATIVE_NAME|Sanjay Murmu]] Phone [[PHONE_NUMBER|9832145678]] Dr [[DOCTOR_NAME|Dr. Amit Roy]]
Vitals / acuity: Patient presents with fever, body ache, and mild headache. Blood pressure 120/80 mm…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `radiology_report` (`sd`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose mixes Gujarati characters into Sindhi Arabic script; other elements (tags, persona, length, entity types) compliant.
- **Preview:**

```
ريڊيولاجيڪل رپورٽ — [[HOSPITAL_NAME|Bikaner District Hospital]] | [[PATIENT_NAME|Jareen Bano]] [[AGE|38]] [[GENDER|Female]]
[[MRN|MRN-2024-0915-002]] [[ENCOUNTER_ID|ENC-56789]] | ڊاڪٽر پاران رپورٽ ڪيل [[DOCTOR_NAME|Dr. Priya Singh]]
نتيجو:
છાتیءَ جي سادي ريڊييوگرافي: ٻنهي طرفن صاف لنگن جا ميدان نظر اچن ٿا، بغیر ڪنهن شدت سان دخول يا گڏ ٿيڻ جي۔ قلبي جو ماپ نارمل حدن اندر لڳي ٿو۔
هڏن جو ڍانچو، جن ۾ پسليون ۽ تھوراسڪ ورٽيبرائ شامل آهن، سلامت آهي، بغیر ڪنهن ليٽڪ يا بلئسٽڪ زخم جي۔ نرم بافتن جا سایا نا…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Sindhi prose rendered in Devanagari (with Hindi intrusions like 'नमस्ते') instead of required Arabic script; all tags/IDs valid and persona fit ok.
- **Preview:**

```
--- सेशन ---
मरीज़ [[PATIENT_NAME|Jareen Bano]] [[AGE|38]] [[GENDER|Female]]
अपॉइंटमेंट [[APPOINTMENT_ID|APT-240521-01]] पोर्टल [[URL|https://tele.example.in/visit]]
क्लाइंट आईपी [[IP_ADDRESS|103.21.244.12]] डिवाइस आईएमईआई [[IMEI_NUMBER|356938035643809]]
मैक [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] फ़ोन [[PHONE_NUMBER|9876512340]]
ईमेल [[EMAIL_ADDRESS|jareen.bano@example.com]] हॉस्पिटाल [[HOSPITAL_NAME|District Hospital Bikaner]]
--- चैट ---
मरीज़: नमस्ते डॉक्टर। मूंखे गुज़िरियलि टे ॾींहनि खां मुसलसल मथे …
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `automated_sms` (`sd`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Sindhi Arabic prose polluted by Gujarati script intrusion (માટે) and English transliterations; other aspects (persona, entities, length) acceptable.
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: تُہُنٛد آنڪولوجي فالو اپ [[DOCTOR_NAME|Dr. Anjali Sharma]] سان [[HOSPITAL_NAME|Jabalpur Cancer Centre]] پؠٹھ [[APPOINTMENT_ID|APT-240521-01]] માટે تصديق ٿي ويو آهي۔ مહેરباني ڪري پنهنجو [[MRN|MRN-2024-0815-001]] ڪارڊ آڻيو۔ تصديق لاءِ [[PHONE_NUMBER|9876512340]] فون ڪيو۔
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['cross_language_entity_shift', 'surrogate_plausibility_collapse']`
- **Reasoning:** Patient name Latin + South-Indian (Karthik Krishnan) mismatches Sindhi/Arabic-script prose, Memon relative/caste, and Ramesh ABHA; other elements (prose script, domain, tags, length) acceptable.
- **Preview:**

```
خارج ٿيڻ جو خلاصو — [[HOSPITAL_NAME|سرڪاري سول اسپتال]]
[[PATIENT_NAME|Karthik Krishnan]] [[DOB|1986-03-15]] [[AGE|38]] [[GENDER|Male]]
داخل [[ADMISSION_NUMBER|ADM-2024-0815]] وارڊ [[WARD_NUMBER|B2]] بسترو [[BED_NUMBER|12]]
ڊاڪٽر [[DOCTOR_NAME|ڊاڪٽر علي شاه]] | نصيحت / مشورو: مريض کي پلمونري ٽيبرڪولوسس سان گڏوگڏ ٽائپ 2 ڊائبيٽس میلیٽس جي بيماري سبب داخل ڪيو ويو. شروعاتي بلغم جو سميئر ايسڊ فاسٽ بئسيلي لاء مثبت آھي. مريض جو DOTS علاج آئسونiazid, rifampicin, pyrazinamide, ethambutol سان شروع ڪيو وي…
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `insurance_claim` (`te`).
- **Score / verdict:** `0.62` / `fail`
- **Flags:** `['invented_entity_type']`
- **Reasoning:** ZONE outside allow-list; duplicate/misplaced RESIDENTIAL_ADDRESS + PIN reuse create minor admin inconsistency; Telugu clinical prose and persona/domain fit otherwise acceptable.
- **Preview:**

```
TPA క్లెయిమ్ — పాలసీ [[INSURANCE_POLICY_NUMBER|POL-AP-2024-5678]]
రోగి వివరాలు:
[[PATIENT_NAME|రమేష్ రెడ్డి]] [[AGE|56]] [[GENDER|Male]] ఆధార్ [[AADHAAR_NUMBER|203835321155]]
[[PHONE_NUMBER|9876543210]] [[PIN|515001]]
[[RESIDENTIAL_ADDRESS|అనుంతపురం, ఆంధ్రప్రదేశ్]]
[[DISTRICT|అనంతపురం]] [[ZONE|Urban]]
ఆసుపత్రి వివరాలు:
[[HOSPITAL_NAME|అపోలో హాస్పిటల్స్]]
[[HOSPITAL_ID|HSP-AP-001]]
[[RESIDENTIAL_ADDRESS|హైదరాబాద్, తెలంగాణ]]
[[DISTRICT|హైదరాబాద్]] [[PIN|515001]]
ఆర్థిక సమాచారం:
బ్యాంక్ ఖాతా [[BAN…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `insurance_claim` (`bn`).
- **Errors:** `['phi_residue:2']`
- **Preview:**

```
টি.পি.এ দাবি — পলিসি [[INSURANCE_POLICY_NUMBER|POL-WB-2024-1123]]
দাবিকারী বিবরণ:
[[PATIENT_NAME|Ratan Chandra Mondal]] [[AGE|50]] [[GENDER|Male]] আধার [[AADHAAR_NUMBER|203835321155]]
[[MRN|MRN-WB-ND-2024-001]]
হাসপাতাল [[HOSPITAL_NAME|Nadia District Hospital]] জেলা [[DISTRICT|Nadia]]
[[ADMISSION_NUMBER|ADM-WB-ND-2024-05-15-001]]
ডাক্তার [[DOCTOR_NAME|Dr. S. K. Banerjee]]
আবাসিক ঠিকানা [[RESIDENTIAL_ADDRESS|Village: Kalikapur, Post: Tehatta, Nadia, West Bengal - 741623]]
গ্রাম [[VILLAGE|Kalikap…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `hospital_billing` (`bn`).
- **Errors:** `['script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
[[HOSPITAL_NAME|Nadia District Hospital, Nadia]]
[[DISTRICT|Nadia]]
PIN CODE: [[PIN_CODE|741101]]
Invoice — INV-2024-0815-001
Date: August 15, 2024

Patient: [[PATIENT_NAME|Ranjan Kumar Mondal]]
MRN: [[MRN|MRN-WB-2024-0815-001]]
Age: 50
Gender: Male

Address: [[RESIDENTIAL_ADDRESS|Village: Chandpara, Post: Tehatta, Nadia]]
Phone: [[PHONE_NUMBER|9876543210]]
Email: [[EMAIL_ADDRESS|ranjan.mondal.design@example.com]]
Aadhaar: [[AADHAAR_NUMBER|206501253007]]
Insurance Policy: [[INSURANCE_POLICY_NUM…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `insurance_claim` (`doi`).
- **Errors:** `['missing_required:BANK_ROUTING_NUMBER', 'phi_residue:4', 'script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
TPA Claim - Policy [[INSURANCE_POLICY_NUMBER|POL-JK-2024-4567]]
[[PATIENT_NAME|Shanti Kumari]] [[AGE|47]] [[GENDER|Female]] [[AADHAAR_NUMBER|245374831431]]
Hospital [[HOSPITAL_NAME|District Hospital Kathua]] [[DISTRICT|Kathua]]
Motor / RTA Vehicle [[VEHICLE_REGISTRATION|JK02AB1234]] (only once).
[[PAN_NUMBER|JKPAB1234C]] [[IFSC_CODE|SBIN0001234]] [[BANK_ACCOUNT_NUMBER|001234567890]]
The patient presented with chief complaints of persistent anxiety, depressive symptoms, and sleep disturbances fo…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `hospital_billing` (`gu`).
- **Errors:** `['entity_stuffing:TAX_ID,TELEPHONE_LANDLINE', 'phi_residue:1']`
- **Cause:** tag dump / over-repetition of entity TYPEs.
- **Preview:**

```
ઇન્વોઇસ — [[HOSPITAL_NAME|Shri Krishna Multispecialty Hospital]] [[DISTRICT|Ahmedabad]] પિન [[PIN_CODE|380015]] દર્દી [[PATIENT_NAME|Meena Patel]] એમ આર એન [[MRN|MRN-GJ-2024-0815]]
સરનામું [[RESIDENTIAL_ADDRESS|12, Chandola, Ahmedabad]] ફોન [[PHONE_NUMBER|9876543210]]
ઈમેલ [[EMAIL_ADDRESS|meena.patel@example.com]] પાન [[PAN_NUMBER|ABCDE1234F]]
લેન્ડલાઇન [[TELEPHONE_LANDLINE|079-26451234]] વાહન [[VEHICLE_REGISTRATION|GJ01AB1234]] (એક વાર)
આધાર [[AADHAAR_NUMBER|206501253007]] પોલિસી [[INSURANCE_P…
```

### S6 auditor fail 5

- **What:** deterministic auditor **fail** on `referral_letter` (`kok`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
संदर्भ [[REFERRAL_ID|REF-2024-0815-001]] [[HOSPITAL_NAME|गोवा सिव्हिल हॉस्पिटल]] पसून / [[DOCTOR_NAME|डॉ. प्रविण नायक]]
विशीं [[PATIENT_NAME|रमेश नाईक]], [[AGE|46]] / [[GENDER|Male]], जिल्लो [[DISTRICT|दक्षिण गोवा]]
कारण: पोटांतलो सतत त्रास आनी थकवा

आदरणीय सहकारी,

आमी [[PATIENT_NAME|Ramesh Naik]] हाका संदर्भ दितात, जो दक्षिण गोव्याचो 46 वर्सांचो दादलो रहिवासी आसा आनी ताका फाटल्या तीन म्हयन्या पासून पोटांत मधून मधून दूख जावपाची तक्रार आसा. रुग्ण सांगता की ताका epigastric region-आंत मंद दूख जात…
```

### S6 auditor fail 6

- **What:** deterministic auditor **fail** on `hospital_billing` (`ml`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
ഇന്‍വോയിസ് — [[HOSPITAL_NAME|Alappuzha District Hospital]] ജില്ല [[DISTRICT|Alappuzha]]
പിൻ [[PIN_CODE|688001]] രോഗി [[PATIENT_NAME|Leela Nair]] MRN [[MRN|ADMH-KL-2024-0815]]
വിലാസം [[RESIDENTIAL_ADDRESS|Punnapra North, Alappuzha]] ഫോൺ [[PHONE_NUMBER|9447012345]]
ഇമെയിൽ [[EMAIL_ADDRESS|leela.nair@example.com]] PAN [[PAN_NUMBER|KLMNP1234C]]
ലാൻഡ്‌ലൈൻ [[TELEPHONE_LANDLINE|0477-2234567]] വാഹനം [[VEHICLE_REGISTRATION|KL04AB1234]] (ഒരിക്കൽ)
ആധാർ [[AADHAAR_NUMBER|206501253007]] പോളിസി [[INSURANCE_POL…
```

### S6 auditor fail 7

- **What:** deterministic auditor **fail** on `hospital_billing` (`mr`).
- **Errors:** `['phi_residue:1']`
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|District Hospital Ahmadnagar]], [[DISTRICT|Ahmadnagar]] पिन [[PIN_CODE|414001]] रुग्ण [[PATIENT_NAME|Ramesh Patil]] एमआरएन [[MRN|DH-MH-2024-0815-001]]
पत्ता [[RESIDENTIAL_ADDRESS|Village Pathardi, Taluka Rahuri, Ahmadnagar]] फोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|ramesh.patil@example.com]] पॅन [[PAN_NUMBER|MHAPR1234C]]
लँडलाईन [[TELEPHONE_LANDLINE|02422-234567]] वाहन [[VEHICLE_REGISTRATION|MH14AB1234]] (एकदा)
आधार [[AADHAAR_NUMBER|211051591846]] पॉलिसी [[INS…
```

### S6 auditor fail 8

- **What:** deterministic auditor **fail** on `hospital_billing` (`ne`).
- **Errors:** `['format:PAN_NUMBER:pan_format']`
- **Preview:**

```
बीजक
कुल्लू जिल्ला अस्पताल, जिल्ला [[DISTRICT|Kullu]] पिन [[PIN_CODE|175101]]
बिरामी [[PATIENT_NAME|Tenzing Dorjee]] MRN [[MRN|MRN-HP-2024-0815-001]]
ठेगाना [[RESIDENTIAL_ADDRESS|Village: Naggar, Post Office: Naggar, Kullu, Himachal Pradesh 175101]]
फोन [[PHONE_NUMBER|9876543210]] इमेल [[EMAIL_ADDRESS|tenzing.dorjee.kullu@example.com]]
प्यान [[PAN_NUMBER|HIMD1234F]] ल्यान्डलाइन [[TELEPHONE_LANDLINE|01902-222334]]
वाहन [[VEHICLE_REGISTRATION|HP-01-AB-1234]] (मोटर दाबीका लागि)
आधार [[AADHAAR_NUMB…
```

### S6 auditor fail 9

- **What:** deterministic auditor **fail** on `telemedicine_transcript` (`pa`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
--- ਸੈਸ਼ਨ ---
ਮਰੀਜ਼ [[PATIENT_NAME|Baldev Singh]] [[AGE|60]] [[GENDER|Male]]
ਅਪੌਇੰਟਮੈਂਟ [[APPOINTMENT_ID|APT-2024-03-15-001]] ਪੋਰਟਲ [[URL|https://telehealth.rajasthan.gov.in/visit/APT-2024-03-15-001]]
ਕਲਾਇੰਟ IP [[IP_ADDRESS|103.21.244.12]] ਡਿਵਾਈਸ IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] ਫ਼ੋਨ [[PHONE_NUMBER|9876543210]]
ਈਮੇਲ [[EMAIL_ADDRESS|baldev.singh@email.com]] ਹਸਪਤਾਲ [[HOSPITAL_NAME|Sri Ganganagar Hospital]]
--- ਚੈਟ ---
ਮਰੀਜ਼: ਹੈਲੋ ਡਾਕਟਰ, ਪਿਛਲੇ ਹਫ਼ਤੇ ਤੋਂ ਮੇ…
```

### S6 auditor fail 10

- **What:** deterministic auditor **fail** on `prescription` (`sat`).
- **Errors:** `['script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|পাছchim মেদিনীপুর ডিস্ট্রিক্ট হসপিটাল]]
Rogiya [[PATIENT_NAME|সাঁতি মুর্মু]], [[AGE|27]] / [[GENDER|Nari]], MRN [[MRN|PMDH-2024-0892]]
Dr. [[DOCTOR_NAME|Dr. সুব্রত চ্যাটার্জি]]
Phone: [[PHONE_NUMBER|9832145678]]
District: [[DISTRICT|পাছchim মেদিনীপুর]]
Rogiya 3 hapta lagid lagatar khok, kom tap, ar ojon komog saw seter akana. Sputum smear acid-fast bacilli lagid positive kana. Chest X-ray right upper lobe re infiltrates dekhaweda. Rogiya Pulmonary Tuberculosis lag…
```

### S6 auditor fail 11

- **What:** deterministic auditor **fail** on `hospital_billing` (`sat`).
- **Errors:** `['format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
[[HOSPITAL_NAME|Kendujhar District Hospital]]
[[PIN_CODE|758001]]
[[PATIENT_NAME|Sanjay Murmu]]
[[MRN|MRN-OD-2024-0815]]
[[DISTRICT|Kendujhar]]
[[RESIDENTIAL_ADDRESS|Village Bhimpur, Post Office Kendujhar]]
[[PHONE_NUMBER|9438901234]]
[[EMAIL_ADDRESS|sanjay.murmu@example.com]]
[[PAN_NUMBER|ODPM1234F]]
[[TELEPHONE_LANDLINE|06762-234567]]
[[VEHICLE_REGISTRATION|OD04AB1234]] (Ambulance Parking)
[[AADHAAR_NUMBER|206501253007]]
[[INSURANCE_POLICY_NUMBER|POL-OD-2024-7781]]
[[TAX_ID|19ODPM1234F1Z5]]
I…
```

### S6 auditor fail 12

- **What:** deterministic auditor **fail** on `prescription` (`sd`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
نسخہ — [[HOSPITAL_NAME|Dr. S.N. Medical College Hospital]]
مريضو [[PATIENT_NAME|Jareen Bano]], [[AGE|38]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0915-002]]
ڊاڪٽر [[DOCTOR_NAME|Dr. Rajesh Kumar]]
فون [[PHONE_NUMBER|9876543210]]
ABHA [[ABHA_ID|12-3456-7890-1234]]
مريضو ID [[PATIENT_ID|PID-BKN-2024-789]]
پتھ [[RESIDENTIAL_ADDRESS|House No. 45, Gandhi Colony, Ward 12, Bikaner]]
ضلعو [[DISTRICT|Bikaner]]

تشخيص: اسٽيج III ڇاتيءَ جو ڪينسر سان ميٽاسٽيٽڪ لمف نوڊس

نسخہ:
1. Paclitaxel 175mg/m² IV انفيوژ…
```

### S6 auditor fail 13

- **What:** deterministic auditor **fail** on `insurance_claim` (`sd`).
- **Errors:** `['phi_residue:8', 'dics_below_threshold:0.5', 'script_purity:wrong_indic_script:Devanagari>Arabic']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
TPA क्लेम — इंश्योरेंस पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-MP-2024-8901]]
[[PATIENT_NAME|RAMESH SINGH]] [[AGE|38]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|203835321155]]
हस्पताल [[HOSPITAL_NAME|SWAIL HOSPITAL]] [[DISTRICT|JABALPUR]]
वाहन [[VEHICLE_REGISTRATION|MP20AB1234]] (सिर्फ़ हिक वार)।
PAN [[PAN_NUMBER|FGHIJ5678K]] IFSC [[IFSC_CODE|SBIN0005678]] खातो [[BANK_ACCOUNT_NUMBER|6789012345678901]]

मरीज़ जी जानकारी:
नालो: रामे सिंह, उमिर: 38 साल, लिंग: मर्द
आधार: [[AADHAAR_NUMBER|203835321155]], P…
```


## Surviving curated set

- languages: `{'as': 22, 'bn': 18, 'brx': 17, 'doi': 20, 'en': 20, 'gu': 15, 'hi': 19, 'kn': 20, 'kok': 15, 'ks': 15, 'mai': 19, 'ml': 20, 'mni': 17, 'mr': 18, 'ne': 13, 'or': 16, 'pa': 13, 'sa': 15, 'sat': 10, 'sd': 12, 'ta': 14, 'te': 16, 'ur': 18}`
- doc_types: `{'asha_worker_note': 36, 'automated_sms': 40, 'discharge_summary': 32, 'er_triage_notes': 28, 'hospital_billing': 24, 'insurance_claim': 27, 'lab_report': 19, 'opd_slip': 17, 'phc_register': 33, 'prescription': 32, 'radiology_report': 33, 'referral_letter': 24, 'surgical_note': 26, 'telemedicine_transcript': 11}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
