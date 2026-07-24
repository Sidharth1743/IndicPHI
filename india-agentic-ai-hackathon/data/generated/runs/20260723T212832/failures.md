# Failures audit — `20260723T212832`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260723T212832/pipeline.resolved.yaml`
- **issue count:** **53** (hard=0, gen_soft=1, tr_soft=33, judge=15, auditor=4)
- **S4 entity_coverage_complete_rate:** `0.9927536231884058`
- **S4b script_fail_count:** `2`
- **S5 pass_rate:** `0.8913043478260869`
- **S6 pass_rate / passed:** `0.967479674796748` / `119`
- **curated docs:** `100`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `25a8008cbebf4abda209c7d28427bb99` | `kok` | `asha_worker_note` | `['missing_required_entities:VOTER_ID']` |
| S4b soft | `3a14ecc1de8648689a3311540c7cdd2e` | `as` | `lab_report` | `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out…` |
| S4b soft | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `opd_slip` | `tag_restore_or_translate_failed:None` |
| S4b soft | `3ceb8b6e61ba4069980e557280aa9ba0` | `brx` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `opd_slip` | `tag_restore_or_translate_failed:None` |
| S4b soft | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `prescription` | `tag_restore_or_translate_failed:None` |
| S4b soft | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `60ff3470cf8340efaa474e13896d8568` | `ks` | `er_triage_notes` | `tag_restore_or_translate_failed:None` |
| S4b soft | `60ff3470cf8340efaa474e13896d8568` | `ks` | `telemedicine_transcript` | `tag_restore_or_translate_failed:None` |
| S4b soft | `60ff3470cf8340efaa474e13896d8568` | `ks` | `opd_slip` | `tag_restore_or_translate_failed:None` |
| S4b soft | `885a67d0071948ac8a8336b278e81003` | `ks` | `er_triage_notes` | `tag_restore_or_translate_failed:None` |
| S4b soft | `885a67d0071948ac8a8336b278e81003` | `ks` | `telemedicine_transcript` | `tag_restore_or_translate_failed:None` |
| S4b soft | `885a67d0071948ac8a8336b278e81003` | `ks` | `opd_slip` | `tag_restore_or_translate_failed:None` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `discharge_summary` | `tag_restore_or_translate_failed:None` |
| S4b soft | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | `tag_restore_or_translate_failed:None` |
| S4b soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:None` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `discharge_summary` | `tag_restore_or_translate_failed:None` |
| S4b soft | `57a29898a6944b899059fb674d16f990` | `te` | `hospital_billing` | `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_transla…` |
| S5 fail | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `insurance_claim` | score=0.35 flags=['dialect_script_impurity', 'surrogate_plausibility_collapse'] |
| S5 fail | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `insurance_claim` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `discharge_summary` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `asha_worker_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `automated_sms` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `0b19143502244d21a03f71ef838ab4ff` | `sat` | `hospital_billing` | score=0.55 flags=['instruction_drift', 'invented_entity_type'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `asha_worker_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `e899bd99966c4ac6b77d784bae3482f0` | `sat` | `insurance_claim` | score=0.2 flags=['dialect_script_impurity', 'instruction_drift'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `automated_sms` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `discharge_summary` | score=0.65 flags=['dialect_script_impurity'] |
| S5 fail | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `opd_slip` | score=0.55 flags=['domain_persona_mismatch'] |
| S6 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `referral_letter` | `['dics_below_threshold:0.7142857142857143']` |
| S6 fail | `5c5a472d66774bdc9e232a4893422f0c` | `mr` | `referral_letter` | `['dics_below_threshold:0.5']` |
| S6 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `['persona_age_mismatch']` |
| S6 fail | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `insurance_claim` | `['phi_residue:1']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `asha_worker_note` (`kok`).
- **Missing required tags:** `['VOTER_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:VOTER_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
वखतपत्र — [[HOSPITAL_NAME|Goa Medical College, Panaji]]
रुग्ण [[PATIENT_NAME|Natalina D'Souza]], [[AGE|46]] / [[GENDER|Female]], MRN [[MRN|MRN-GOA-2024-0156]]
डॉ. [[DOCTOR_NAME|Dr. Anjali Rao]]
Rx: टप्पा III ट्रिपल-नेगेटिव्ह ब्रेस्ट कॅन्सर, 6 पैकी चक्र 3 च्या व्यवस्थापना खातीर.
1. Paclitaxel 175 mg/m2 IV 3 वरांनी पयल्या दिसा.
2. Carboplatin AUC 5 IV 30 मिनटांनी पयल्या दिसा.
3. Ondansetron 8 mg PO दर 8 वरांनी मळमळपा खातीर PRN तोंडा वाटे.
4. Dexamethasone 8 mg PO मळमळ उणी करपाक पयल्या दिसा-3ऱ्या दिसा एक डोस.
5. G-CSF (Pegfilgrastim) 6 mg SC दुसऱ्या दिसा काती सकयल एक डोस.
कृपया जोर, थंडी आनी चड …
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `lab_report` (`as`).
- **Error:** `tag_restore_or_translate_failed:timed out:Sarvam timeout after 300.0s: The read operation timed out attempt=1`
- **script_ok:** `False`
- **EN pivot preview:**

```
Operative note — [[HOSPITAL_NAME|Tinsukia Civil Hospital]] Adm [[ADMISSION_NUMBER|ADM-2024-0912]] Ward [[WARD_NUMBER|OT-1]] Bed [[BED_NUMBER|15]]
[[PATIENT_NAME|Rina Gogoi]] [[AGE|22]] [[GENDER|Female]] Surgeon [[DOCTOR_NAME|Dr. Arun Sharma]]
[[PATIENT_ID|PID-TNS-7890]] [[MRN|MRN-TNS-2024-001]]

Procedure: Emergency Cesarean delivery.

Indication: Patient is a 22-year-old G1P0 at 38 weeks gestati…
```
- **Translated preview:**

```
অপাৰেটিভ টোকা — [[HOSPITAL_NAME|Tinsukia Civil Hospital]] এডমিট্ৰি [[ADMISSION_NUMBER|ADM-2024-0912]] ৱাৰ্ড [[WARD_NUMBER|OT-1]] বিচনা [[BED_NUMBER|15]]
[[PATIENT_NAME|Rina Gogoi]] [[AGE|22]] [[GENDER|Female]] চাৰ্জন [[DOCTOR_NAME|Dr. Arun Sharma]]
[[PATIENT_ID|PID-TNS-7890]] [[MRN|MRN-TNS-2024-001]]

প্ৰক্ৰিয়া: জৰুৰীকালীন চিজেৰিয়ান ডেলিভাৰী।

ইণ্ডিকেচন: ৰোগী এগৰাকী 22 বছৰীয়া G1P0, গৰ্ভধাৰণৰ 3…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `opd_slip` (`brx`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Baksa District Hospital]] | ID [[HOSPITAL_ID|BDH-001]]
Patient: [[PATIENT_NAME|Rina Boro]] | DOB [[DOB|1994-05-15]] | Age: [[AGE|30]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Hawker]] | MRN: [[MRN|OPD-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Sharma]]
Relative: [[RELATIVE_NAME|Jaya Boro]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Baksa District Hospital]] | ID [[HOSPITAL_ID|BDH-001]]
Patient: [[PATIENT_NAME|Rina Boro]] | DOB [[DOB|1994-05-15]] | Age: [[AGE|30]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Hawker]] | MRN: [[MRN|OPD-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Sharma]]
Relative: [[RELATIVE_NAME|Jaya Boro]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `insurance_claim` (`brx`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Baksa District Hospital]] | ID [[HOSPITAL_ID|BDH-001]]
Patient: [[PATIENT_NAME|Rina Boro]] | DOB [[DOB|1994-05-15]] | Age: [[AGE|30]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Hawker]] | MRN: [[MRN|OPD-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Sharma]]
Relative: [[RELATIVE_NAME|Jaya Boro]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Baksa District Hospital]] | ID [[HOSPITAL_ID|BDH-001]]
Patient: [[PATIENT_NAME|Rina Boro]] | DOB [[DOB|1994-05-15]] | Age: [[AGE|30]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Hawker]] | MRN: [[MRN|OPD-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Sharma]]
Relative: [[RELATIVE_NAME|Jaya Boro]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `opd_slip` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `prescription` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `insurance_claim` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Kathua]] | ID [[HOSPITAL_ID|DH-KTH-001]]
Patient: [[PATIENT_NAME|Anuradha Devi]] | DOB [[DOB|1986-05-15]] | Age: [[AGE|38]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Police Officer]] | MRN: [[MRN|OPD-2024-0456]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Kumar]] | Phone: [[PHONE_NUMBER|9419012345]]
Registrar …
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `asha_worker_note` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `automated_sms` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `insurance_claim` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Bahu]], District [[DISTRICT|Jammu]]
Beneficiary [[PATIENT_NAME|Sushma Devi]], [[AGE|48]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rajni Kumari]] | Phone [[PHONE_NUMBER|9419256783]]
Visit findings: Patient presents with increased anxiety symptoms, sleep disturbances, and reduced appetite for past three weeks. Reports feeling overwhelmed with household responsibili…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `er_triage_notes` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `telemedicine_transcript` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `opd_slip` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Shabir Ahmad]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity…
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `er_triage_notes` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `telemedicine_transcript` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `opd_slip` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|SMHS Hospital Srinagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Imran Ahmad]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK01AB1234]] (exactly once).
Relative [[RELATIVE_NAME|Mohammad Yousuf]] Phone [[PHONE_NUMBER|9419234567]] Dr [[DOCTOR_NAME|Dr. Naseer Ahmad]]
Vital…
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Laljit Singh]] DOB [[DOB|1986-05-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0521]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient underwent laparoscopic appendectomy on 21 May 2024 for acute appendicitis. Procedure completed succ…
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Laljit Singh]] DOB [[DOB|1986-05-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0521]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient underwent laparoscopic appendectomy on 21 May 2024 for acute appendicitis. Procedure completed succ…
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Laljit Singh]] DOB [[DOB|1986-05-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0521]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient underwent laparoscopic appendectomy on 21 May 2024 for acute appendicitis. Procedure completed succ…
```
- **Translated preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Laljit Singh]] DOB [[DOB|1986-05-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0521]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient underwent laparoscopic appendectomy on 21 May 2024 for acute appendicitis. Procedure completed succ…
```

### S4b translation soft-fail 18

- **What:** translation soft-fail on `insurance_claim` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Bundi District Hospital]]
Patient [[PATIENT_NAME|Ananya Sharma]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Rx: Isoniazid 300mg once daily, Rifampicin 450mg once daily, Pyrazinamide 1000mg once daily, Ethambutol 800mg once daily for 2 months, followed by Isoniazid 300mg and Rifampicin 450mg once daily for 4 mon…
```
- **Translated preview:**

```
चिकित्सापत्रम् — [[HOSPITAL_NAME|NM0]]
रोगिणी [[PATIENT_NAME|NM1]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
चिकित्सिका [[DOCTOR_NAME|NM2]]
चिकित्सापत्रम्: आइसोनियाज़िड 300 मि.ग्रा. प्रतिदिन एकवारम्, रिफाम्पिसिन 450 मि.ग्रा. प्रतिदिन एकवारम्, पाइराज़िनामाइड 1000 मि.ग्रा. प्रतिदिन एकवारम्, एथाम्बुटोल 800 मि.ग्रा. प्रतिदिन एकवारम्, द्वौ मासौ यावत्, ततः आइसोनियाज़िड 300 मि.ग्रा. …
```

### S4b translation soft-fail 19

- **What:** translation soft-fail on `asha_worker_note` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Bundi District Hospital]]
Patient [[PATIENT_NAME|Ananya Sharma]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Rx: Isoniazid 300mg once daily, Rifampicin 450mg once daily, Pyrazinamide 1000mg once daily, Ethambutol 800mg once daily for 2 months, followed by Isoniazid 300mg and Rifampicin 450mg once daily for 4 mon…
```
- **Translated preview:**

```
चिकित्सापत्रम् — [[HOSPITAL_NAME|NM0]]
रोगिणी [[PATIENT_NAME|NM1]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
चिकित्सिका [[DOCTOR_NAME|NM2]]
चिकित्सापत्रम्: आइसोनियाज़िड 300 मि.ग्रा. प्रतिदिन एकवारम्, रिफाम्पिसिन 450 मि.ग्रा. प्रतिदिन एकवारम्, पाइराज़िनामाइड 1000 मि.ग्रा. प्रतिदिन एकवारम्, एथाम्बुटोल 800 मि.ग्रा. प्रतिदिन एकवारम्, द्वौ मासौ यावत्, ततः आइसोनियाज़िड 300 मि.ग्रा. …
```

### S4b translation soft-fail 20

- **What:** translation soft-fail on `automated_sms` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Ramesh Kumar]], your TB follow-up appointment [[APPOINTMENT_ID|APT-240521-01]] is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] with [[DOCTOR_NAME|Dr. Sharma]] on 21-May at 10:30 AM. Please bring your [[MRN|MRN-2024-0815-001]] and continue your TB medications. Call [[PHONE_NUMBER|9876512340]] if you have questions.
```
- **Translated preview:**

```
Dear [[PATIENT_NAME|Ramesh Kumar]], your TB follow-up appointment [[APPOINTMENT_ID|APT-240521-01]] is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] with [[DOCTOR_NAME|Dr. Sharma]] on 21-May at 10:30 AM. Please bring your [[MRN|MRN-2024-0815-001]] and continue your TB medications. Call [[PHONE_NUMBER|9876512340]] if you have questions.
```

### S4b translation soft-fail 21

- **What:** translation soft-fail on `insurance_claim` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Ramesh Kumar]], your TB follow-up appointment [[APPOINTMENT_ID|APT-240521-01]] is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] with [[DOCTOR_NAME|Dr. Sharma]] on 21-May at 10:30 AM. Please bring your [[MRN|MRN-2024-0815-001]] and continue your TB medications. Call [[PHONE_NUMBER|9876512340]] if you have questions.
```
- **Translated preview:**

```
Dear [[PATIENT_NAME|Ramesh Kumar]], your TB follow-up appointment [[APPOINTMENT_ID|APT-240521-01]] is scheduled at [[HOSPITAL_NAME|District Hospital Kanpur]] with [[DOCTOR_NAME|Dr. Sharma]] on 21-May at 10:30 AM. Please bring your [[MRN|MRN-2024-0815-001]] and continue your TB medications. Call [[PHONE_NUMBER|9876512340]] if you have questions.
```

### S4b translation soft-fail 22

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```

### S4b translation soft-fail 23

- **What:** translation soft-fail on `automated_sms` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```

### S4b translation soft-fail 24

- **What:** translation soft-fail on `hospital_billing` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Baidpur]], District [[DISTRICT|Dumka]]
Beneficiary [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for 3 weeks with occasional fever. Blood pressure reading 140/90 mmHg. Referred to Dumka District Hospital for sputum examination and …
```

### S4b translation soft-fail 25

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Bankura Primary Health Centre]] Village [[VILLAGE|Chhatna]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Bikash Murmu]] [[AGE|18]] [[GENDER|Male]] | TB screening - cough for 3 weeks, weight loss 5kg

Patient presented with persistent cough, low-grade fever, and night sweats for past 3 weeks. Chest examination revealed decreased breath sounds in right upper zone. Spu…
```
- **Translated preview:**

```
ᱯᱤ ᱮᱪ ᱥᱤ ᱨᱮᱡᱤᱥᱴᱟᱨ — [[HOSPITAL_NAME|Bankura Primary Health Centre]] ᱟᱛᱳ [[VILLAGE|Chhatna]] ᱡᱤᱞᱟ [[DISTRICT|Bankura]]
[[PATIENT_NAME|Bikash Murmu]] [[AGE|18]] [[GENDER|Male]] | ᱴᱤ ᱵᱤ ᱥᱠᱨᱤᱱᱤᱝ - 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱠᱷᱩᱜ ᱟᱨ 5 ᱠᱤᱞᱚᱜᱨᱟᱢ ᱵᱚᱡᱚᱱ ᱠᱚᱢ ᱟᱠᱟᱱᱟ ᱾

ᱨᱩᱣᱟᱹᱜᱤ ᱫᱚ ᱢᱟᱲᱟᱝ 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱞᱟᱜᱟᱛᱟᱨ ᱠᱷᱩᱜ, ᱠᱚᱢ ᱞᱟᱛᱟᱨ ᱡᱚᱨᱚ ᱡᱚᱨᱚ ᱟᱨ ᱧᱤᱫᱟᱹ ᱨᱮ ᱦᱚᱭ ᱥᱟᱶᱛᱮ ᱦᱮᱡᱽ ᱟᱠᱟᱱᱟ ᱾ ᱪᱷᱟᱛᱤ ᱡᱚᱠᱷᱟ ᱫᱚ ᱡᱚᱡᱚᱢ ᱞᱟᱯᱷᱟᱝ ᱴᱚᱴᱷᱟ ᱨᱮ ᱥᱟᱦᱮᱫ ᱨᱮᱭᱟᱜ ᱥᱟᱰᱮ …
```

### S4b translation soft-fail 26

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Bankura Primary Health Centre]] Village [[VILLAGE|Chhatna]] District [[DISTRICT|Bankura]]
[[PATIENT_NAME|Bikash Murmu]] [[AGE|18]] [[GENDER|Male]] | TB screening - cough for 3 weeks, weight loss 5kg

Patient presented with persistent cough, low-grade fever, and night sweats for past 3 weeks. Chest examination revealed decreased breath sounds in right upper zone. Spu…
```
- **Translated preview:**

```
ᱯᱤ ᱮᱪ ᱥᱤ ᱨᱮᱡᱤᱥᱴᱟᱨ — [[HOSPITAL_NAME|Bankura Primary Health Centre]] ᱟᱛᱳ [[VILLAGE|Chhatna]] ᱡᱤᱞᱟ [[DISTRICT|Bankura]]
[[PATIENT_NAME|Bikash Murmu]] [[AGE|18]] [[GENDER|Male]] | ᱴᱤ ᱵᱤ ᱥᱠᱨᱤᱱᱤᱝ - 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱠᱷᱩᱜ ᱟᱨ 5 ᱠᱤᱞᱚᱜᱨᱟᱢ ᱵᱚᱡᱚᱱ ᱠᱚᱢ ᱟᱠᱟᱱᱟ ᱾

ᱨᱩᱣᱟᱹᱜᱤ ᱫᱚ ᱢᱟᱲᱟᱝ 3 ᱥᱟᱯᱛᱟᱦ ᱠᱷᱚᱱ ᱞᱟᱜᱟᱛᱟᱨ ᱠᱷᱩᱜ, ᱠᱚᱢ ᱞᱟᱛᱟᱨ ᱡᱚᱨᱚ ᱡᱚᱨᱚ ᱟᱨ ᱧᱤᱫᱟᱹ ᱨᱮ ᱦᱚᱭ ᱥᱟᱶᱛᱮ ᱦᱮᱡᱽ ᱟᱠᱟᱱᱟ ᱾ ᱪᱷᱟᱛᱤ ᱡᱚᱠᱷᱟ ᱫᱚ ᱡᱚᱡᱚᱢ ᱞᱟᱯᱷᱟᱝ ᱴᱚᱴᱷᱟ ᱨᱮ ᱥᱟᱦᱮᱫ ᱨᱮᱭᱟᱜ ᱥᱟᱰᱮ …
```

### S4b translation soft-fail 27

- **What:** translation soft-fail on `automated_sms` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```

### S4b translation soft-fail 28

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```

### S4b translation soft-fail 29

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry appointment [[APPOINTMENT_ID|APT-240521-01]] is confirmed at [[HOSPITAL_NAME|Sion Hospital]] on 21-May at 10:30 with [[DOCTOR_NAME|Dr. Mehta]]. Please confirm via [[PHONE_NUMBER|9876512340]]. MRN [[MRN|MRN-2024-0815-001]].
```

### S4b translation soft-fail 30

- **What:** translation soft-fail on `insurance_claim` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 31

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_script_purity_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 32

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|Vadodara Mental Health Institute]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GJPSV1234C]] IFSC [[IFSC_CODE|SBIN0005678]] account …
```

### S4b translation soft-fail 33

- **What:** translation soft-fail on `hospital_billing` (`te`).
- **Error:** `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Government Medical College Hospital]] District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|GMCH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|15 Shivaji Nagar, Nanded]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|ramesh.kumar@example.com]] PAN [[PAN_NUMBER|ABCPK1234F]]
Landline [[TELEPHONE_LANDLINE|02462-234567]…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Government Medical College Hospital]] District [[DISTRICT|Nanded]]
PIN [[PIN_CODE|431601]] Patient [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|GMCH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|15 Shivaji Nagar, Nanded]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|ramesh.kumar@example.com]] PAN [[PAN_NUMBER|ABCPK1234F]]
Landline [[TELEPHONE_LANDLINE|02462-234567]…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'surrogate_plausibility_collapse']`
- **Reasoning:** Hindi prose instead of Dogri; Bari Brahmana village mismatches Kathua district.
- **Preview:**

```
TPA क्लेम फॉर्म - पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
दावेदार विवरण:
[[PATIENT_NAME|Anuradha Devi]] [[AGE|38]] [[GENDER|Female]]
आधार: [[AADHAAR_NUMBER|203835321155]]
संपर्क: [[PHONE_NUMBER|9419876543]]
[[EMAIL_ADDRESS|anuradha.devi@example.com]]

अस्पताल विवरण:
[[HOSPITAL_NAME|District Hospital Kathua]]
[[HOSPITAL_ID|HSP-JK-001]]
[[DISTRICT|Kathua]]
[[VILLAGE|Bari Brahmana]]

बीमा पॉलिसी विवरण:
पॉलिसी संख्या: [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
पैन: [[PAN_NUMBER|JKPAB1…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `insurance_claim` (`doi`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose mixes English dates/numbers outside tags with Dogri Devanagari; not fully compliant with expected script/language for clinical content.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-JK-2024-4567]]

मरीज दी जानकारी:
[[PATIENT_NAME|Shanti Devi]] [[AGE|48]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|203835321155]]

हस्पताल दी जानकारी:
[[HOSPITAL_NAME|Government Medical College Jammu]] जिला [[DISTRICT|Jammu]]

मरीज दा संपर्क:
फोन [[PHONE_NUMBER|9419876543]] ईमेल [[EMAIL_ADDRESS|shanti.devi@example.com]]

वित्तीय जानकारी:
पैन [[PAN_NUMBER|JKPAB1234C]] आई ऐफ ऐस सी [[IFSC_CODE|SBIN0000123]] खाता [[BANK_ACCOUNT_NUMBER|123456789012]] रू…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English; expected Manipuri/Meitei script for narrative.
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Jawaharlal Nehru Hospital, Imphal]]
[[PATIENT_NAME|Laljit Singh]] DOB [[DOB|1986-05-15]] [[AGE|38]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0521]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]] | Course / advice: Patient underwent laparoscopic appendectomy on 21 May 2024 for acute appendicitis. Procedure completed successfully with no intraoperative complications. Postoperative recovery has been uneventful with norma…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose in Bengali script + English mix instead of required Meitei; all entity TYPEs allowed and persona/domain fit otherwise.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815-001]] দগী [[HOSPITAL_NAME|Imphal East District Hospital]] / [[DOCTOR_NAME|Dr. Kh. Ratan Singh]]
Patient: [[PATIENT_NAME|Lalremruata Khongsai]], [[AGE|38]] / [[GENDER|Male]], District [[DISTRICT|Imphal East]]
Reason: তিন সপ্তাহ ধরে কাশি, জ্বর আর ওজন কমে যাওয়া। রোগীর উচ্চ রক্তচাপের ইতিহাস আছে।
History of Present Illness: রোগী, ৩৮ বছরের ধর্মীয় কর্মী, তিন সপ্তাহ ধরে কাশি আছে। তিনি সন্ধ্যায় জ্বর অনুভব করেন এবং গত দুই মাসে প্রায় ৫ কেজি ওজন কমেছে। তিনি সামান্য …
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose entirely in Roman script with mixed Hindi/Santali transliteration; no Ol Chiki script used despite explicit Santali requirement.
- **Preview:**

```
ASHA-ag note — Gaon [[VILLAGE|Baidpur]], Jila [[DISTRICT|Dumka]]
Labharthi [[PATIENT_NAME|Purani Devi]], [[AGE|38]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Sita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Bhraman Findings: Rogi kare khas khas tin hapta lagid ar jwara. BP reading 140/90 mmHg. Dumka District Hospital lagid sputum test ar NCD evaluation lagid refer kiti.

[[RELATIVE_NAME|Ramesh Murmu]] visit lagid present. [[BPL_RATION_CARD|BPL-JH-2024-001234]] check kiti. [[VOTER_ID|JH123456…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `automated_sms` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** SMS prose entirely in English; expected Santali Ol Chiki narrative.
- **Preview:**

```
Dear [[PATIENT_NAME|Purani Devi]], your appointment [[APPOINTMENT_ID|APT-240521-01]] with [[DOCTOR_NAME|Dr. Kumar]] at [[HOSPITAL_NAME|Dumka PHC]] is confirmed for tomorrow. Please bring your [[MRN|MRN-2024-0815-001]] and arrive 15 minutes early. Call [[PHONE_NUMBER|9876543210]] for any queries.
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `hospital_billing` (`sat`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift', 'invented_entity_type']`
- **Reasoning:** Meta notes about untagged receipt/state fields and placeholder text indicate drift; receipt number invented outside allow-list despite soft billing rule.
- **Preview:**

```
ᱵᱤᱞ — [[HOSPITAL_NAME|Dumka District Hospital]] ᱦᱚᱱᱚᱛ [[DISTRICT|Dumka]]
ᱯᱤᱱ [[PIN_CODE|814101]] ᱨᱩᱜᱤ [[PATIENT_NAME|Purani Devi]] MRN [[MRN|DMH-2024-0815-001]]
ᱴᱷᱮᱱᱟ [[RESIDENTIAL_ADDRESS|Village: Bhangpahari, Post: Dumka]] ᱯᱷᱳᱱ [[PHONE_NUMBER|9431234567]]
ᱤᱢᱮᱞ [[EMAIL_ADDRESS|purani.devi@example.com]] ᱯᱮᱱ [[PAN_NUMBER|JHPPN1234F]]
ᱞᱮᱱᱰᱞᱟᱭᱤᱱ [[TELEPHONE_LANDLINE|03432-254678]] ᱜᱟᱹᱰᱤ [[VEHICLE_REGISTRATION|JH01AB1234]] (ᱮᱢᱵᱩᱞᱮᱱᱥ ᱯᱟᱨᱠᱤᱝ)
ᱟᱫᱷᱟᱨ [[AADHAAR_NUMBER|206501253007]] ᱯᱚᱞᱤᱥᱤ [[INSURANCE_P…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Roman script + English code-mixing instead of required Santali Ol Chiki; all other elements (entities, persona, domain) acceptable.
- **Preview:**

```
ASHA note — Village [[VILLAGE|Barjora]], District [[DISTRICT|Bankura]]
Beneficiary [[PATIENT_NAME|Ranjan Murmu]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sushila Hansda]] | Phone [[PHONE_NUMBER|9876543210]]
Visit reyag findings: Patient thenge pet dard ar jwor appendectomy surgery tayom. ghaw jayga mild redness ar discharge e dekhawa, dressing change lagid. Patient thenge bhukh kom ar mild discomfort walking okto. Advised emana antibiotics continue lagid ar immediately return lagi…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `insurance_claim` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** Clinical prose is English; expected Santali Ol Chiki. All tags/IDs/types/persona fit otherwise.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-WB-2024-4567]]
[[PATIENT_NAME|Babu Murmu]] [[AGE|18]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|203835321155]]
Hospital [[HOSPITAL_NAME|Bankura District Hospital]] District [[DISTRICT|Bankura]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|WB02J1234]] (exactly once).
PAN [[PAN_NUMBER|WBEPM1234F]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_ACCOUNT_NUMBER|123456789012]]

Patient presented with acute lower back pain and muscle strain following heavy …
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `automated_sms` (`sd`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Devanagari into expected Sindhi Arabic script; other entities/persona fit.
- **Preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: تُہُنٛد نفسیاتی اپائنٹمنٹ [[APPOINTMENT_ID|APT-240521-01]] تصدیق کَرنہٕ آمُت چھُ [[HOSPITAL_NAME|Sion Hospital]] پؠٹھ 21-May صُبح جو 10:30 بجہِ [[DOCTOR_NAME|Dr. Mehta]] سۭتۍ۔ مہرबानी کٔرتھ [[PHONE_NUMBER|9876512340]] ذٔریعہٕ تصدیق کٔرِو۔ MRN [[MRN|MRN-2024-0815-001]].
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English instead of required Sindhi Arabic script; all tags allowed and persona/domain fit otherwise.
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Lokmanya Tilak Municipal General Hospital]]
[[PATIENT_NAME|Ramesh Kumar]] DOB [[DOB|1992-08-15]] [[AGE|32]] [[GENDER|Male]]
Adm [[ADMISSION_NUMBER|ADM-2024-0815-004]] Ward [[WARD_NUMBER|B1]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Prakash Deshmukh]] | Course / advice: Patient admitted with pulmonary tuberculosis with associated hypertension. Sputum smear positive for AFB, culture confirmed Mycobacterium tuberculosis. Started on Category I DOTS regimen with…
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `insurance_claim` (`sd`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative entirely in Devanagari/Hindi-Urdu mix instead of required Sindhi Arabic script; language not Sindhi prose despite tags and IDs being allow-listed.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-GJ-2024-0892]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|987654321012]]
हस्पताल [[HOSPITAL_NAME|Vadodara Mental Health Institute]] ज़िलो [[DISTRICT|Vadodara]]
मोटर / आर टी ए गाड़ी [[VEHICLE_REGISTRATION|GJ06AB1234]] (सिर्फ़ हिकु वारु).
पैन [[PAN_NUMBER|GJPSV1234C]] आई एफ एस सी [[IFSC_CODE|SBIN0005678]] खातो [[BANK_ACCOUNT_NUMBER|50200012345678]]
[[CREDIT_CARD_NUMBER|4111111111111111]] [[CVV|456]] [[PIN|3…
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in Devanagari; expected Sindhi Arabic script. All TYPE tags allowed and IDs Latin; persona/domain fit ok.
- **Preview:**

```
इनवॉइस — [[HOSPITAL_NAME|Shri Sayaji Hospital]] ज़िलो [[DISTRICT|Vadodara]]
पिन [[PIN_CODE|390001]] मरीज़ [[PATIENT_NAME|Shilpaben Vasava]] एम.आर.एन. [[MRN|MRN-GJ-2024-0815-001]]
पतो [[RESIDENTIAL_ADDRESS|15, Manjalpur, Vadodara, Gujarat]] फ़ोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|shilpaben.vasava@example.com]] पैन [[PAN_NUMBER|ABCDE1234F]]
लैंडलाइन [[TELEPHONE_LANDLINE|0265-2345678]] गाॾी [[VEHICLE_REGISTRATION|GJ06AB1234]] (हिकु भेरो)
आधार [[AADHAAR_NUMBER|291512345678]] पॉलिसी [[INS…
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Devanagari 'डॉक्टर' intrudes into otherwise Arabic-script Sindhi prose; all tags allowed, persona/clinical fit and length OK.
- **Preview:**

```
خارجہ خلاصو — [[HOSPITAL_NAME|Shri Krishna Hospital]]
[[PATIENT_NAME|Shilpaben Vasava]] DOB [[DOB|1949-03-15]] [[AGE|75]] [[GENDER|Female]]
داخلو [[ADMISSION_NUMBER|ADM-2024-0815-042]] وارڊ [[WARD_NUMBER|B2]] بسترو [[BED_NUMBER|12]]
डॉक्टर [[DOCTOR_NAME|Dr. Rajesh Patel]] | طريقہ کار / صلاح: مريضه کي دل جي خرابي (heart failure) ۽ سخت خشڪي (dehydration) سبب داخل ڪيو ويو. شروعاتي وائٽلز ۾ بلڊ پريشر 85/50 mmHg، دل جي رفتار 110 bpm، ساهه جي رفتار 24/min، ۽ آڪسيجن جو سطح 92% کمر جي هوا ۾ نظر آيو. جس…
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `opd_slip` (`ta`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** Occupation 'News Paper Boy' conflicts with female/40yo persona; all other prose, tags, script and clinical content align.
- **Preview:**

```
சிகிச்சை அறிக்கை | [[HOSPITAL_NAME|District Hospital Thiruvallur]] | அடையாள எண் [[HOSPITAL_ID|DH-TVL-001]]
நோயாளி: [[PATIENT_NAME|Kalpana Verma]] | பிறந்த தேதி [[DOB|1984-07-15]] | வயது: [[AGE|40]] | பாலினம்: [[GENDER|Female]]
தொழில்: [[OCCUPATION|News Paper Boy]] | மருத்துவக் குறிப்பு எண்: [[MRN|OPD-2024-0892]] | மருத்துவர்: [[DOCTOR_NAME|Dr. Priya Natarajan]]
உறவினர்: [[RELATIVE_NAME|Ramesh Kumar]] | தொலைபேசி எண்: [[PHONE_NUMBER|9876543210]]
பதிவாளர் பணி எண்: [[EMPLOYEE_ID|EMP-4412]] | மாவட்ட…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `referral_letter` (`gu`).
- **Errors:** `['dics_below_threshold:0.7142857142857143']`
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-0891]] [[HOSPITAL_NAME|Primary Health Centre, Himmatnagar]] / [[DOCTOR_NAME|Dr. Rajesh Patel]] તરફથી
વિષે [[PATIENT_NAME|Dahiben Muchadiya]], [[AGE|58]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Sabar Kantha]]
કારણ: અનિયંત્રિત હાયપરટેન્શન અને નવા નિદાન થયેલ ટાઈપ 2 ડાયાબિટીસ મેલીટસનું મૂલ્યાંકન

પ્રિય સહકર્મી,

હું [[PATIENT_NAME|Dahiben Muchadiya]], 58 વર્ષની મહિલા ખેતીની દેખરેખ રાખનાર, ગ્રામીણ સાબરકાંઠાથી, તેની નવી નિદાન થયેલ મેટાબોલિક સ્થિતિઓના વ્યાપક મૂલ્યાંકન અને સ…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `referral_letter` (`mr`).
- **Errors:** `['dics_below_threshold:0.5']`
- **Preview:**

```
संदर्भ पत्र [[REFERRAL_ID|REF-2024-0847]] कडून [[HOSPITAL_NAME|Jalna District Civil Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Patil]]
विषय: [[PATIENT_NAME|Savitri Bai Shinde]], [[AGE|64]] / [[GENDER|Female]], जिल्हा [[DISTRICT|Jalna]]
कारण: सतत खोकला, वजन कमी होणे आणि अपुऱ्या नियंत्रणाखालील मधुमेह

आदरणीय फुफ्फुसशास्त्र विभाग,

मी [[PATIENT_NAME|Savitri Bai Shinde]] चे मूल्यमापन करण्यासाठी, जालना येथील एक 64 वर्षांची गृहिणी, दीर्घकालीन खोकला आणि संशयित फुफ्फुसाचा क्षयरोग यासाठी संदर्भ देत आहे. रुग्…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `hospital_billing` (`sd`).
- **Errors:** `['persona_age_mismatch']`
- **Preview:**

```
انوائيس — [[HOSPITAL_NAME|سر ج. ج. گروپ آف هاسپيٽلز]] [[DISTRICT|Mumbai Suburban]]
پن [[PIN_CODE|400001]] مريڊ [[PATIENT_NAME|Ramesh Patil]] ايم آر اين [[MRN|MH-MUM-2024-0815]]
پتو [[RESIDENTIAL_ADDRESS|45 Shivaji Park, Dadar West]] فون [[PHONE_NUMBER|9876543210]]
ايميل [[EMAIL_ADDRESS|ramesh.patil@example.com]] پن [[PAN_NUMBER|ABCDE1234F]]
لينڊ لائن [[TELEPHONE_LANDLINE|022-23456789]] گاڏي [[VEHICLE_REGISTRATION|MH01AB1234]] (هڪ ڀيرو)
آڌار [[AADHAAR_NUMBER|206501253007]] پاليسي [[INSURANCE_POL…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `insurance_claim` (`ta`).
- **Errors:** `['phi_residue:1']`
- **Preview:**

```
TPA கோரிக்கை படிவம் - பாலிசி [[INSURANCE_POLICY_NUMBER|POL-TN-2024-8901]]
[[PATIENT_NAME|Mahavir Jain]] [[AGE|34]] [[GENDER|Male]] ஆதார் எண் [[AADHAAR_NUMBER|236214820502]]
மருத்துவமனை [[HOSPITAL_NAME|Government Stanley Medical College Hospital]] மாவட்டம் [[DISTRICT|Chennai]]
வாகனம் / RTA வாகனம் [[VEHICLE_REGISTRATION|TN01AB1234]] (ஒருமுறை மட்டும்).
PAN [[PAN_NUMBER|TNJMV1234C]] IFSC [[IFSC_CODE|SBIN0000678]] கணக்கு [[BANK_ACCOUNT_NUMBER|678901234567]]

நோயாளி விவரங்கள்:
பெயர்: [[PATIENT_NAME|M…
```


## Surviving curated set

- languages: `{'as': 6, 'bn': 6, 'brx': 6, 'doi': 3, 'en': 5, 'gu': 5, 'hi': 6, 'kn': 4, 'kok': 6, 'ks': 2, 'mai': 4, 'ml': 4, 'mni': 4, 'mr': 4, 'ne': 5, 'or': 4, 'pa': 5, 'sa': 5, 'sat': 1, 'ta': 3, 'te': 6, 'ur': 6}`
- doc_types: `{'asha_worker_note': 5, 'automated_sms': 7, 'discharge_summary': 8, 'er_triage_notes': 6, 'hospital_billing': 7, 'insurance_claim': 5, 'lab_report': 9, 'opd_slip': 8, 'phc_register': 4, 'prescription': 13, 'radiology_report': 8, 'referral_letter': 7, 'surgical_note': 12, 'telemedicine_transcript': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
