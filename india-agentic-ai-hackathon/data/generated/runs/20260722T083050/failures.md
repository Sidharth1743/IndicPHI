# Failures audit — `20260722T083050`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260722T083050/pipeline.resolved.yaml`
- **issue count:** **42** (hard=0, gen_soft=1, tr_soft=15, judge=23, auditor=3)
- **S4 entity_coverage_complete_rate:** `0.9927536231884058`
- **S4b script_fail_count:** `2`
- **S5 pass_rate:** `0.8333333333333334`
- **S6 pass_rate / passed:** `0.9739130434782609` / `112`
- **curated docs:** `99`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `0fbde0cc3f544c77b260ef63a5a3a8d8` | `or` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic;generator_repair_failed:Sarvam …` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `opd_slip` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `automated_sms` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `radiology_report` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `bf0de98a0c63491c8877846b6f8dad65` | `ur` | `radiology_report` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S5 fail | `fdc875f657c1440c8e243a6845fb17a5` | `bn` | `surgical_note` | score=0.6 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `a0e6acd7770d41b5812edc8bbfbda7ee` | `brx` | `lab_report` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `opd_slip` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `insurance_claim` | score=0.65 flags=['invented_entity_type'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `automated_sms` | score=0.45 flags=['domain_persona_mismatch', 'dialect_script_impurity'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `insurance_claim` | score=0.38 flags=['domain_persona_mismatch', 'instruction_drift'] |
| S5 fail | `25a8008cbebf4abda209c7d28427bb99` | `kok` | `lab_report` | score=0.42 flags=['domain_persona_mismatch', 'dialect_script_impurity'] |
| S5 fail | `60ff3470cf8340efaa474e13896d8568` | `ks` | `er_triage_notes` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `885a67d0071948ac8a8336b278e81003` | `ks` | `er_triage_notes` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `8a02e74c7f104c1fa9f00b8507bac016` | `mni` | `referral_letter` | score=0.45 flags=['dialect_script_impurity', 'cross_language_entity_shift'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `8d7895d6831e4b31956f868182103764` | `ne` | `prescription` | score=0.3 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse', 'instruction_drift'] |
| S5 fail | `67bf2f4af82d452db4c95cd1c7f59330` | `or` | `opd_slip` | score=0.55 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | score=0.25 flags=['dialect_script_impurity', 'instruction_drift'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | score=0.35 flags=['dialect_script_impurity', 'cross_language_entity_shift'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | score=0.4 flags=['dialect_script_impurity'] |
| S5 fail | `f0e00cbdb5dd4d33a122229e4883c598` | `te` | `hospital_billing` | score=0.35 flags=['instruction_drift'] |
| S6 fail | `1f7da27d8fe544a191d7adc016e62971` | `gu` | `referral_letter` | `['dics_below_threshold:0.0']` |
| S6 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `hospital_billing` | `['span_alignment_failure', 'boundary_corruption_rate:0.05']` |
| S6 fail | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `insurance_claim` | `['dics_below_threshold:0.0']` |

## Per-failure audit

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

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ꯗꯤꯁꯆꯥꯔꯖ ꯁꯝꯃꯔꯤ — [[HOSPITAL_NAME|Regional Hospital Imphal]]
[[PATIENT_NAME|Lal Singh]] ꯗꯣꯕꯤꯜ [[DOB|1986-04-15]] [[AGE|38]] [[GENDER|Male]]
ꯑꯦꯗꯃꯤꯠ [[ADMISSION_NUMBER|ADM-2024-0312]] ꯋꯥꯔꯗ [[WARD_NUMBER|A1]] ꯕꯦꯗ [[BED_NUMBER|05]]
ꯗꯣꯛꯇꯔ [[DOCTOR_NAME|Dr. Th. Kumarjit Singh]] | ꯀꯣꯔꯁ / ꯄꯥꯎꯇꯥꯛ: ꯃꯔꯨꯑꯣꯏꯕ ꯑꯦꯄꯦꯟꯗꯤꯁꯥꯏꯇꯤꯁꯀꯤꯗꯃꯛ ꯏꯪ 2024ꯒꯤ ꯃꯥꯔꯆ 12ꯗ ꯄꯦꯁꯦꯟꯇ ꯑꯗꯨ ꯄꯨꯡ 2:30ꯗ ꯏꯃꯔꯖꯦꯟꯁꯤ ꯑꯦꯄꯦꯟꯗꯦꯛꯇꯣꯃꯤ ꯇꯧꯈꯤ꯫ ꯄ꯭ꯔꯣꯁꯤꯖꯔ ꯑꯗꯨ ꯂꯦꯄ…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `insurance_claim` (`sa`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4;post_repair_translate:Sarvam timeout after 300.0s: The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Rohan Kumar]], your TB follow-up appointment is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] on 15-May at 10:30 AM with [[DOCTOR_NAME|Dr. Amit Singh]]. Please bring your [[MRN|MRN-2024-0815-001]] and arrive 15 minutes early. Contact us at [[PHONE_NUMBER|9876543210]] for any queries. Appointment ID: [[APPOINTMENT_ID|APT-240515-01]].
```
- **Translated preview:**

```
प्रिय [[PATIENT_NAME|Rohan Kumar]], भवतः क्षयरोग-अनुवर्ती-नियुक्तिः [[HOSPITAL_NAME|District Hospital Kanpur]] दिनाङ्के 15-मै प्रातः 10:30 वादने [[DOCTOR_NAME|Dr. Amit Singh]] इत्यनेन सह नियोजिता अस्ति। कृपया स्वकीयं [[MRN|MRN-2024-0815-001]] आनयन्तु आगत्य 15 निमेषान् पूर्वम्। कस्यापि प्रश्नाय [[PHONE_NUMBER|9876543210]] सम्पर्कं कुर्वन्तु। नियुक्ति-परिचयः: [[APPOINTMENT_ID|APT-240515-01]]।
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `automated_sms` (`sat`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ᱟᱥᱟ ᱱᱚᱴ — ᱟᱛᱳ [[VILLAGE|Baidpur]], ᱡᱤᱞᱟ [[DISTRICT|Dumka]]
ᱵᱷᱟᱹᱞᱟᱹᱭ ᱧᱟᱢᱤᱡ [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ᱟᱥᱟ: [[ASHA_WORKER_NAME|Santi Murmu]] | ᱯᱷᱳᱱ [[PHONE_NUMBER|9876543210]]
ᱧᱟᱢ ᱟᱠᱟᱱ ᱠᱟᱛᱷᱟ ᱧᱮᱞ: ᱨᱩᱣᱟᱹᱜᱤ ᱫᱚ 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱞᱟᱜᱟᱛᱟᱨ ᱠᱷᱩᱜ, ᱦᱩᱰᱤᱧ ᱡᱚᱨ, ᱟᱨ 5 ᱠᱤᱞᱳ ᱵᱚᱡᱚᱱ ᱠᱚᱢ ᱟᱠᱟᱱᱟ ᱾ ᱩᱱᱤ ᱫᱚ ᱛᱤᱥᱼᱛᱤᱥ ᱫᱷᱟᱣ ᱥᱟᱦᱮᱫ ᱦᱟᱨᱟ ᱟᱨ ᱧᱤᱫᱟᱹ ᱨᱮ ᱦᱚᱲᱢᱚ ᱨᱮ ᱫᱟᱜ ᱡᱚᱨᱚᱜ ᱨᱮᱭᱟᱜ ᱠᱟᱛᱷᱟᱭ ᱞᱟᱹᱭ ᱟᱠᱟᱫᱟ ᱾ ᱵᱞᱚᱰ …
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `hospital_billing` (`sat`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ᱟᱥᱟ ᱱᱚᱴ — ᱟᱛᱳ [[VILLAGE|Baidpur]], ᱡᱤᱞᱟ [[DISTRICT|Dumka]]
ᱵᱷᱟᱹᱞᱟᱹᱭ ᱧᱟᱢᱤᱡ [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ᱟᱥᱟ: [[ASHA_WORKER_NAME|Santi Murmu]] | ᱯᱷᱳᱱ [[PHONE_NUMBER|9876543210]]
ᱧᱟᱢ ᱟᱠᱟᱱ ᱠᱟᱛᱷᱟ ᱧᱮᱞ: ᱨᱩᱣᱟᱹᱜᱤ ᱫᱚ 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱞᱟᱜᱟᱛᱟᱨ ᱠᱷᱩᱜ, ᱦᱩᱰᱤᱧ ᱡᱚᱨ, ᱟᱨ 5 ᱠᱤᱞᱳ ᱵᱚᱡᱚᱱ ᱠᱚᱢ ᱟᱠᱟᱱᱟ ᱾ ᱩᱱᱤ ᱫᱚ ᱛᱤᱥᱼᱛᱤᱥ ᱫᱷᱟᱣ ᱥᱟᱦᱮᱫ ᱦᱟᱨᱟ ᱟᱨ ᱧᱤᱫᱟᱹ ᱨᱮ ᱦᱚᱲᱢᱚ ᱨᱮ ᱫᱟᱜ ᱡᱚᱨᱚᱜ ᱨᱮᱭᱟᱜ ᱠᱟᱛᱷᱟᱭ ᱞᱟᱹᱭ ᱟᱠᱟᱫᱟ ᱾ ᱵᱞᱚᱰ …
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ᱯᱤ ᱮᱪ ᱥᱤ ᱨᱮᱡᱤᱥᱴᱟᱨ — [[HOSPITAL_NAME|Primary Health Centre, Bankura]] ᱟᱛᱳ [[VILLAGE|Hathbandh]] ᱡᱤᱞᱟ [[DISTRICT|Bankura]]
[[PATIENT_NAME|Lal Murmu]] [[AGE|18]] [[GENDER|Male]] | ᱞᱟᱜᱟᱛᱟᱨ ᱠᱷᱩᱜ ᱨᱮᱭᱟᱜ ᱡᱚᱠᱷᱟ ᱞᱟᱹᱜᱤᱫ ᱨᱮᱯᱷᱟᱨ ᱦᱩᱭ ᱟᱠᱟᱱᱟ
[[PHONE_NUMBER|9832145678]] [[BPL_RATION_CARD|BPL-WB-BAK-2023-9876]] [[VOTER_ID|WB0123456789]] [[ABHA_ID|12-3456-7890-1234]]
ᱨᱩᱣᱟᱹᱜᱤ ᱫᱚ ᱦᱟᱛᱷᱵᱟᱸᱫᱷ ᱟᱛᱳ, ᱵᱟᱝᱠᱩᱨᱟ ᱡᱤᱞᱟ ᱨᱮᱱ ᱢᱤᱫᱴᱟ…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `automated_sms` (`sd`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: Your psychiatry follow-up is confirmed for [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|Sion Hospital]] with Dr. [[DOCTOR_NAME|Dr. Patel]]. MRN [[MRN|MRN-2024-0615-001]]. Please arrive 15 mins early. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `insurance_claim` (`sd`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4;post_repair_translate:Sarvam timeout after 300.0s: The read operation timed out`
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

### S4b translation soft-fail 10

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic;generator_repair_failed:Sarvam timeout after 600.0s: The read operation timed out`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
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

### S4b translation soft-fail 11

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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

### S4b translation soft-fail 12

- **What:** translation soft-fail on `opd_slip` (`ta`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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

### S4b translation soft-fail 13

- **What:** translation soft-fail on `automated_sms` (`ta`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ஆஷா குறிப்பு — கிராமம் [[VILLAGE|T. Nagar]], மாவட்டம் [[DISTRICT|Chennai]]
பயனாளி [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ஆஷா: [[ASHA_WORKER_NAME|Lakshmi Devi]] | தொலைபேசி [[PHONE_NUMBER|9876543210]]
கண்டுபிடிப்புகளைப் பார்வையிடவும்: நோயாளி கடந்த இரண்டு வாரங்களாக அதிகரித்த பதட்டம் மற்றும் தூக்கக் கலக்கங்கள் இருப்பதாகக் கூறுகிறார். வேலைப் பொறுப்புகளால் அதிகமாக உணர்வதாகக் குறிப்…
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `radiology_report` (`ur`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ڈسچارج سمری — [[HOSPITAL_NAME|Government Medical College Hospital, Amravati]]
[[PATIENT_NAME|Ayesha Begum]] تاریخ پیدائش [[DOB|1968-04-15]] [[AGE|56]] [[GENDER|Female]]
ایڈمِشن [[ADMISSION_NUMBER|ADM-2024-03-12-0045]] وارڈ [[WARD_NUMBER|B2]] بیڈ [[BED_NUMBER|08]]
ڈاکٹر [[DOCTOR_NAME|Dr. Rajesh Patil]] | کورس / مشورہ: مریضہ کو پلمونری ٹیوبرکلوسس اور ہائی بلڈ پریشر کے ساتھ داخل کیا گیا۔ ابتدائی سپٹ…
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `radiology_report` (`ur`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=4`
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
ڈسچارج سمری — [[HOSPITAL_NAME|Gulbarga Institute of Medical Sciences]]
[[PATIENT_NAME|Ayesha Begum]] تاریخ پیدائش [[DOB|2002-10-15]] [[AGE|22]] [[GENDER|Female]]
ایڈمِشن [[ADMISSION_NUMBER|ADM-2024-08-10]] وارڈ [[WARD_NUMBER|B2]] بیڈ [[BED_NUMBER|12]]
ڈاکٹر [[DOCTOR_NAME|Dr. Priya Nair]] | کورس/مشورہ: مریضہ 22 سالہ، گونہ پی او، دیہی گلبڑگہ، کرناٹک سے تعلق رکھتی ہے، جو 10 اگست 2024 کو دردِ زہ کے س…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `surgical_note` (`bn`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** Male name 'Rahul Sharma' assigned to female patient with husband; persona-gender mismatch despite Bengali prose and valid tags.
- **Preview:**

```
অপারেশন রিপোর্ট — [[HOSPITAL_NAME|সিটি হাসপাতাল]] ভর্তি [[ADMISSION_NUMBER|ADM-2024-0915]] ওয়ার্ড [[WARD_NUMBER|Surgical]]
[[PATIENT_NAME|রাহুল শর্মা]] [[AGE|44]] [[GENDER|Female]] সার্জন [[DOCTOR_NAME|ডা. অঞ্জলি সেন]]
পদ্ধতি / ফলাফল:
রোগীর ২৪ ঘণ্টার জন্য জ্বর এবং বমির সাথে তীব্র ডানদিকের নিচের পেটে ব্যথা ছিল। পরীক্ষায় McBurney's point-এ স্পর্শ করলে ব্যথা এবং পেশি শক্ত হয়ে থাকা দেখা গেছে। আল্ট্রাসাউন্ডে ৮ মিমি ব্যাস এবং চারপাশের তরল জমাটবদ্ধতা সহ প্রদাহযুক্ত অ্যাপেন্ডিক্স দেখা গেছে। সাধারণ অ…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose in Nepali/Hindi Devanagari, not Bodo; all other elements (tags, persona, domain) acceptable.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-AS-2024-4567]]
[[PATIENT_NAME|Rina Boro]] [[AGE|30]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|259046509647]]
हस्पताल [[HOSPITAL_NAME|Baksa District Civil Hospital]] जिला [[DISTRICT|Baksa]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|AS01AB1234]] (एक बार मात्र)।
पॅन [[PAN_NUMBER|BOKRB1234C]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30912345678901]]

मरीज रीना बोरो, 30 बर्षकी महिला फेरीवाला बक्ससा जिलाबाट 28 हप्ताको गर्भकालमा नियमित प्रस…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `lab_report` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in Hindi (wrong language) despite Bodo/Devanagari requirement; all tags, IDs, persona fit, and lab content otherwise valid and plausible.
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

### S5 judge fail 4

- **What:** linguistic judge **fail** on `opd_slip` (`doi`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses standard Hindi vocabulary/grammar instead of Dogri; all entity tags, persona fit and clinical content otherwise valid.
- **Preview:**

```
बाह्य रोगी पर्ची | [[HOSPITAL_NAME|District Hospital Kathua]] | आई डी [[HOSPITAL_ID|DH-JK-001]]
रोगी: [[PATIENT_NAME|Anuradha Devi]] | जन्म तिथि [[DOB|1986-05-15]] | आयु: [[AGE|38]] | लिंग: [[GENDER|Female]]
पेशे: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
संबंधित: [[RELATIVE_NAME|Ramesh Kumar]] | फोन: [[PHONE_NUMBER|9419876543]]
रजिस्ट्रार कर्मचारी आईडी: [[EMPLOYEE_ID|EMP-2024-001]] | जिला: [[DISTRICT|Kathua]]

मुख्य शिकायत: पिछले …
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['invented_entity_type']`
- **Reasoning:** DATE_OF_ADMISSION and DATE_OF_DISCHARGE outside allow-list; prose in Devanagari with partial Dogri lexical flavor but mostly standard Hindi medical phrasing.
- **Preview:**

```
माता स्वास्थ्य दावा
पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]

दावेदार [[PATIENT_NAME|Anuradha Devi]] [[AGE|38]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|238745619012]]

अस्पताल [[HOSPITAL_NAME|District Hospital Kathua]] जिला [[DISTRICT|Kathua]]

मुख्य शिकायत: पेट दर्द ते प्रसव पीड़ा।
निदान: प्रसव पीड़ा, भ्रूण संकट।
प्रक्रिया: सिजेरियन डिलीवरी।
भर्ती तारीख: [[DATE_OF_ADMISSION|15/08/2024]]
छोड़ने दी तारीख: [[DATE_OF_DISCHARGE|18/08/2024]]

पैन [[PAN_NUMBER|JKPAB1234C]] आई एफ एस सी [[IF…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `automated_sms` (`doi`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['domain_persona_mismatch', 'dialect_script_impurity']`
- **Reasoning:** Male name 'रवि कुमार' for female persona; prose is Hindi not Dogri.
- **Preview:**

```
[[PATIENT_NAME|रवि कुमार]]: अपॉइंटमेंट [[APPOINTMENT_ID|APT-240615-02]] पर [[HOSPITAL_NAME|गवर्नमेंट सिविल हॉस्पिटल]] पर 15-जून 10:30 डॉ. [[DOCTOR_NAME|डॉ. शर्मा]] के साथ। MRN [[MRN|MRN-JMC-2024-045]]। पुष्टि करो पर [[PHONE_NUMBER|9419234567]]।
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.38` / `fail`
- **Flags:** `['domain_persona_mismatch', 'instruction_drift']`
- **Reasoning:** Male name Ramesh for female 48yo; Shimla hospital/district instead of Jammu J&K; otherwise Dogri prose + allowed tags
- **Preview:**

```
TPA claim — बीमा पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
[[PATIENT_NAME|रमेश कुमार]] [[AGE|48]] [[GENDER|Female]] [[MRN|GMCJ-2024-0456]] Aadhaar [[AADHAAR_NUMBER|203835321155]]
Hospital [[HOSPITAL_NAME|शिमला अस्पताल]] जिला [[DISTRICT|शिमला जिला]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|JK02AB1234]] (सिर्फ इक बारी)।
PAN [[PAN_NUMBER|JKPAB1234C]] IFSC [[IFSC_CODE|SBIN0005678]] खाता [[BANK_ACCOUNT_NUMBER|0078901234567]] [[BANK_ROUTING_NUMBER|123456789012]]

मरीज ने दस्सेआ जे 3 महीने तक्…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `lab_report` (`kok`).
- **Score / verdict:** `0.42` / `fail`
- **Flags:** `['domain_persona_mismatch', 'dialect_script_impurity']`
- **Reasoning:** Female patient described with masculine verbs/pronouns (तो, करतो, राहतो); clinical prose is Marathi not Konkani despite Devanagari script.
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

### S5 judge fail 9

- **What:** linguistic judge **fail** on `er_triage_notes` (`ks`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose is Urdu (not Kashmiri) despite Arabic script and valid tags; minor lexical attempts at ks do not salvage narrative language match.
- **Preview:**

```
ایمرجنسی ٹریاج — [[HOSPITAL_NAME|ہسپتال]] ملاقات [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|علی احمد]] [[AGE|28]] [[GENDER|Male]] وارڈ [[WARD_NUMBER|ER]] بستر [[BED_NUMBER|03]]
ایمبولینس ذٔریعہ ووت [[VEHICLE_REGISTRATION|JK01AB1234]] (صرف اکھ لٹہ)۔
رشتہ دار [[RELATIVE_NAME|عائشہ بیگم]] فون [[PHONE_NUMBER|9419234567]] ڈاکٹر [[DOCTOR_NAME|ڈاکٹر راشد]]
حیاتی علامات: BP 140/90، HR 110، RR 22، Temp 38.2°C، SpO2 94% کمرے کی ہوا پر۔ مریض کی شکایت ہے بتدریج سانس پھولنا، 3 مہینوں میں 8 کلوگرام وز…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `er_triage_notes` (`ks`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose mostly Urdu (e.g. 'رپورٹ نہیں کیا گیا', 'انکار کرتا ہے') rather than Kashmiri despite Arabic script and some lexical insertions; all entity tags valid and persona fit OK.
- **Preview:**

```
ایمرجنسی ٹریاج — [[HOSPITAL_NAME|SKIMS Soura]] ملاقات [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] وارڈ [[WARD_NUMBER|ER]] بید [[BED_NUMBER|07]]
ایمبولینس ذٔریعہ آمُت [[VEHICLE_REGISTRATION|JK01AB5678]]
رشتہ دار [[RELATIVE_NAME|Mohammad Yousuf]] فون [[PHONE_NUMBER|9419234567]] ڈاکٹر [[DOCTOR_NAME|Dr. Farooq Ahmad]]
وائٹلز / حالت: ہوشس منٛز تہٕ 3 طرفہٕ باخبر، BP 120/80، HR 78، RR 16، Temp 36.8°C، SpO2 98% کمرے کی ہوا پر۔ مریض چھُ پریشان نظر یوان نفسی…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity', 'cross_language_entity_shift']`
- **Reasoning:** Mixed English prose ('Dear colleague,', exam descriptions) violates Meitei requirement; DISTRICT tag uses Latin 'Thoubal' (wrong district + script) instead of Imphal East.
- **Preview:**

```
ꯔꯦꯐꯔꯦꯜ [[REFERRAL_ID|REF-2024-01]] ꯗꯒꯤ [[HOSPITAL_NAME|ꯑꯄꯣꯂꯣ ꯍꯣꯁꯄꯤꯇꯥꯜ]] / [[DOCTOR_NAME|ꯗꯣꯛꯇꯔ ꯁꯔꯃꯥ]]
Regarding: [[PATIENT_NAME|ꯁ꯭ꯔꯤꯃꯇꯤ ꯗꯦꯕꯤ]], [[AGE|79]] / [[GENDER|Female]], District [[DISTRICT|ꯏꯝꯐꯥꯜ ꯏꯁꯠ]]
ꯃꯔꯝ: ꯂꯦꯞꯇꯅ ꯂꯩꯕ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟ ꯃꯇꯝ ꯃꯇꯝꯒꯤ ꯑꯣꯏꯅ ꯀꯣꯛ ꯀꯣꯏꯕ ꯑꯃꯁꯨꯡ ꯀꯥꯎꯊꯣꯛꯄ

Dear colleague,

ꯑꯩꯈꯣꯏꯅ ꯔꯦꯐꯔ ꯇꯧꯔꯤ [[PATIENT_NAME|ꯁ꯭ꯔꯤꯃꯇꯤ ꯗꯦꯕꯤ]], ꯆꯍꯤ [[AGE|79]] ꯒꯤ [[GENDER|Female]] ꯅꯥꯕ ꯃꯤꯑꯣꯏ [[DISTRICT|Thoubal]] ꯗꯒꯤ ꯀꯟꯇ꯭ꯔꯣꯜ ꯇꯧꯕ ꯉꯝꯗꯕ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟ ꯃꯈꯥ ꯇꯥꯅ ꯊꯤꯖꯤꯟꯕ ꯑꯃꯁꯨꯡ ꯂꯥꯌꯦꯡꯕꯒꯤꯗꯃꯛ꯫ ꯅꯥꯕ ꯃꯤꯑꯣꯏ ꯑꯁꯤ ꯑꯩꯈꯣꯏꯒꯤ ꯌꯦꯡꯁꯤꯟꯕ…
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely English; expected Manipuri/Meitei script for clinical narrative.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Regional Medical Center Imphal]] / [[DOCTOR_NAME|Dr. Raj Kumar Singh]]
Re: [[PATIENT_NAME|Thokchom Sanjit]], [[AGE|38]] / [[GENDER|Male]], District [[DISTRICT|Imphal East]]
Reason: Persistent cough with weight loss and hypertension evaluation

Dear Colleague,

This is to refer [[PATIENT_NAME|Thokchom Sanjit]], a 38-year-old male ordained religious worker from Imphal East district, for further evaluation of suspected pulmonary tuberculo…
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `prescription` (`ne`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse', 'instruction_drift']`
- **Reasoning:** Kathmandu/Nepal location+ABHA vs West Bengal/Darjiling persona; male name for female patient; entity/context implausibility.
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

### S5 judge fail 14

- **What:** linguistic judge **fail** on `opd_slip` (`or`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** Male name 'Ramesh Chandra Patra' + Khordha district contradict female/59/Nabarangapur persona; clinical prose otherwise Odia and allowed tags used correctly.
- **Preview:**

```
ଆଉଟପେସେଣ୍ଟ ବିଭାଗ ସ୍ଲିପ୍ | [[HOSPITAL_NAME|ମେଟ୍ରୋ ହସ୍ପିଟାଲ୍]] | ID [[HOSPITAL_ID|DH-NAB-001]]
ରୋଗୀ: [[PATIENT_NAME|ରମେଶ ଚନ୍ଦ୍ର ପାତ୍ର]] | ଜନ୍ମ ତାରିଖ [[DOB|1965-03-15]] | ବୟସ: [[AGE|59]] | ଲିଙ୍ଗ: [[GENDER|Female]]
ଚାକିରି: [[OCCUPATION|ସରକାରୀ କର୍ମଚାରୀ]] | MRN: [[MRN|OPD-2024-0815-001]] | ଡାକ୍ତର: [[DOCTOR_NAME|ଡାକ୍ତର ପ୍ରଦୀପ କୁମାର]]
ସମ୍ପର୍କୀୟ: [[RELATIVE_NAME|ସୁନିତା ଦେବୀ]] | ଫୋନ୍: [[PHONE_NUMBER|9437812345]]
ରେଜିଷ୍ଟ୍ରାର EmpID: [[EMPLOYEE_ID|EMP-2024-001]] | ଜିଲ୍ଲା: [[DISTRICT|ଖୋର୍ଦ୍ଧା]]
ମୁଖ୍ୟ ଅଭିଯୋଗ:…
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `insurance_claim` (`sa`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; Sanskrit Devanagari required for narrative.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-UP-2024-9876]]
[[PATIENT_NAME|Aarav Khan]] [[AGE|19]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|233080913670]]
[[DISTRICT|Kanpur Nagar]]

Patient History and Clinical Summary:
The patient, a 19-year-old male student from Kanpur Nagar, presented with persistent fatigue, recurrent fevers, and unexplained bruising over the past three months. Initial blood work revealed pancytopenia. A subsequent bone marrow aspiration and biopsy confirmed a diagnosis…
```

### S5 judge fail 16

- **What:** linguistic judge **fail** on `automated_sms` (`sat`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in English; expected Santali Ol Chiki script for SMS body.
- **Preview:**

```
[[PATIENT_NAME|Purani Devi]]: Your appointment [[APPOINTMENT_ID|APT-240521-01]] with [[DOCTOR_NAME|Dr. Kumar]] at [[HOSPITAL_NAME|Dumka PHC]] on 21-May at 10:30 AM. Please bring your [[MRN|MRN-2024-0815-001]] card. Confirm on [[PHONE_NUMBER|9876512340]].
```

### S5 judge fail 17

- **What:** linguistic judge **fail** on `hospital_billing` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** All prose and item descriptions in English/Latin script; zero Santali Ol Chiki content despite explicit language requirement. Tags and maternal billing content otherwise mostly aligned with persona and allow-list.
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

### S5 judge fail 18

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English/Latin script; expected Santali Ol Chiki throughout narrative.
- **Preview:**

```
ASHA note — Village [[VILLAGE|Barjora]], District [[DISTRICT|Bankura]]
Beneficiary [[PATIENT_NAME|Ranjan Murmu]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Santi Tudu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presented with left forearm laceration after workplace accident. Wound cleaned and sutured at District Hospital. Patient advised to return for follow-up in 3 days.

Family details: Father [[RELATIVE_NAME|Sukhu Murmu]] contacted. BPL [[BPL_RATION_CARD|BPL-WB-…
```

### S5 judge fail 19

- **What:** linguistic judge **fail** on `automated_sms` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose language is Kashmiri (e.g. tuhund, chhu, manz) not Sindhi despite Arabic script; other elements (tags, length, persona fit) acceptable.
- **Preview:**

```
[[PATIENT_NAME|رَمیش کُمار]]: تُہُنٛد سائیکاٹری فالو اپ اپائنٹمنٹ کنفرم چھُ [[APPOINTMENT_ID|APT-240615-02]] پؠٹھ [[HOSPITAL_NAME|سایون ہسپتال]] منٛز ڈاکٹر [[DOCTOR_NAME|ڈاکٹر پٹیل]] سۭتۍ۔ MRN [[MRN|MRN-2024-0615-001]]۔ مہربانی کٔرِتھ 15 منٹ برونٛہہ وٲتِو۔ کنفرم کرنہٕ خٲطرٕ [[PHONE_NUMBER|9876543210]] کال کٔرِو۔
```

### S5 judge fail 20

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'cross_language_entity_shift']`
- **Reasoning:** Prose mixes Devanagari intrusions (labels, patient name value) into expected Sindhi Arabic script; PATIENT_NAME uses wrong script despite allow-list tag.
- **Preview:**

```
[[HOSPITAL_NAME|لليلاوتي اسپتال، بندرا اولهه، ممبئي]] [[DISTRICT|ممبئي سبوربن]]
پن [[PIN_CODE|400050]] مريز [[PATIENT_NAME|रमेश कुमार]] एम.आर.एन. [[MRN|MRN-MH-2024-0815-001]]
پتو [[RESIDENTIAL_ADDRESS|45، شِواجي پارڪ، دادا ر اولهه]] فون [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|ramesh.kumar@example.com]] پئن [[PAN_NUMBER|ABCDE1234F]]
लैंडलाइन [[TELEPHONE_LANDLINE|022-23456789]] گاڏي [[VEHICLE_REGISTRATION|MH01AB1234]] (امبوليانس جي پارڪنگ)
آڌار [[AADHAAR_NUMBER|206501253007]] پاليسي [[IN…
```

### S5 judge fail 21

- **What:** linguistic judge **fail** on `insurance_claim` (`sd`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose body uses Devanagari script with Hindi phrasing instead of required Sindhi Arabic script; only scattered tags and names use Arabic.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-7891]]
[[PATIENT_NAME|شيلپابن پٽيل]] [[AGE|75]] [[GENDER|عورت]] आधार [[AADHAAR_NUMBER|203835321155]]
अस्पताल [[HOSPITAL_NAME|وڊودرا مينٽل هيلٿ انسٽيٽيوٽ]] जिला [[DISTRICT|وڊودرا]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|GJ06AB1234]] (सिर्फ़ हिकु वारु).
पैन [[PAN_NUMBER|GHIJK5678L]] IFSC [[IFSC_CODE|SBIN0005678]] खातो [[BANK_ACCOUNT_NUMBER|6140200123456789]]
बैंक रूटिंग नंबर [[BANK_ROUTING_NUMBER|SBIN0005678]]
क्रेडिट कार्ड [[CREDIT_CARD_N…
```

### S5 judge fail 22

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.4` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Sindhi prose uses Devanagari script throughout instead of required Arabic script; all tags allowed, clinical content and persona fit otherwise plausible.
- **Preview:**

```
बिल — [[HOSPITAL_NAME|श्री सयाजी हॉस्पिटल]] ज़िलो [[DISTRICT|वडोदरा]]
पिन [[PIN_CODE|390001]] मरीज़ [[PATIENT_NAME|शिल्पाबेन वासावा]] एम.आर.एन. [[MRN|MRN-GJ-2024-0815]]
पतो [[RESIDENTIAL_ADDRESS|12, माधवपुरा सोसाइटी, सयाजी बाग़ जे भरसां]] फ़ोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|shilpaben.vasava@example.com]] पैन [[PAN_NUMBER|GJVAP1234C]]
लैंडलाइन [[TELEPHONE_LANDLINE|0265-2345678]] गाॾी [[VEHICLE_REGISTRATION|GJ06AB1234]] (हिकु भेरो)
आधार [[AADHAAR_NUMBER|206501253007]] पॉलिसी [[I…
```

### S5 judge fail 23

- **What:** linguistic judge **fail** on `hospital_billing` (`te`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['instruction_drift']`
- **Reasoning:** Prose mixes Telugu with embedded prompt instructions/meta-commentary on TYPE rules and missing line items; all required tags present and script mostly correct but output is contaminated.
- **Preview:**

```
ఇన్వాయిస్ — [[HOSPITAL_NAME|SCB Medical College and Hospital]] జిల్లా [[DISTRICT|Ganjam]]
PIN [[PIN_CODE|761001]] రోగి [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|SCB-2024-0815-001]]
చిరునామా [[RESIDENTIAL_ADDRESS|Plot No. 15, Ward 12, Berhampur]] ఫోన్ [[PHONE_NUMBER|9438765432]]
ఇమెయిల్ [[EMAIL_ADDRESS|ramesh.kumar.cleaner@example.com]] PAN [[PAN_NUMBER|ODHPK1234A]]
ల్యాండ్‌లైన్ [[TELEPHONE_LANDLINE|0674-2225678]] వాహనం [[VEHICLE_REGISTRATION|OD07AB1234]] (ఒకసారి మాత్రమే)
ఆధార్ [[AADHAAR_NUMBER|20…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `referral_letter` (`gu`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-TB-001]] થી [[HOSPITAL_NAME|Primary Health Center, Vadodara]] / [[DOCTOR_NAME|Dr. Rajesh Patel]]
વિષે: [[PATIENT_NAME|Jaymeenbhai Mehta]], [[AGE|48]] / [[GENDER|Male]], જિલ્લો [[DISTRICT|Vadodara]]

કારણ: સતત ઉધરસ સાથે શારીરિક લક્ષણો અને નવું નિદાન થયેલ Type 2 Diabetes Mellitus માટે વિશિષ્ટ મૂલ્યાંકન અને સંચાલન.

પ્રિય સહકર્મી,

હું [[PATIENT_NAME|Jaymeenbhai Mehta]], 48 વર્ષનો પુરુષ દુકાનદાર ગ્રામીણ વડોદરાથી, શંકાસ્પદ ફેફસાના ક્ષય રોગના મૂલ્યાંકન અને નવા નિદાન થયેલ…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `hospital_billing` (`gu`).
- **Errors:** `['span_alignment_failure', 'boundary_corruption_rate:0.05']`
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
આધાર નંબર: [[AADHAAR_NUMBER|206501253007]]
PAN નંબર: [[PAN_NUMBER|AAAPL1234C]]
વીમા પોલિસી નંબર: [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-7890]]
વાહન નોંધણી: [[VEHICLE_REGISTRA…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `insurance_claim` (`ta`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
TPA கோரிக்கை - பாலிசி [[INSURANCE_POLICY_NUMBER|POL-TN-2024-8901]]
நோயாளி விவரங்கள்:
பெயர்: [[PATIENT_NAME|லட்சுமி நாராயணன்]] வயது: [[AGE|40]] பாலினம்: [[GENDER|Female]] ஆதார்: [[AADHAAR_NUMBER|203835321155]]
மருத்துவமனை: [[HOSPITAL_NAME|Government Medical College Hospital Thiruvallur]] மாவட்டம்: [[DISTRICT|Thiruvallur]]

PAN: [[PAN_NUMBER|KLMNO5678P]] IFSC: [[IFSC_CODE|SBIN0005678]] கணக்கு: [[BANK_ACCOUNT_NUMBER|678901234567]]
வங்கி ரூட்டிங்: [[BANK_ROUTING_NUMBER|SBIN0005678]] கிரெடிட் கார்டு…
```


## Surviving curated set

- languages: `{'as': 6, 'bn': 4, 'brx': 4, 'doi': 2, 'en': 6, 'gu': 3, 'hi': 5, 'kn': 6, 'kok': 5, 'ks': 3, 'mai': 5, 'ml': 4, 'mni': 4, 'mr': 5, 'ne': 5, 'or': 4, 'pa': 5, 'sa': 5, 'sat': 3, 'sd': 2, 'ta': 5, 'te': 3, 'ur': 5}`
- doc_types: `{'asha_worker_note': 6, 'automated_sms': 6, 'discharge_summary': 9, 'er_triage_notes': 5, 'hospital_billing': 3, 'insurance_claim': 6, 'lab_report': 7, 'opd_slip': 11, 'phc_register': 4, 'prescription': 12, 'radiology_report': 8, 'referral_letter': 6, 'surgical_note': 12, 'telemedicine_transcript': 4}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
