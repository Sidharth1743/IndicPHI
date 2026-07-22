# Failures audit — `20260720T213322`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260720T213322/pipeline.resolved.yaml`
- **issue count:** **36** (hard=0, gen_soft=6, tr_soft=9, judge=19, auditor=2)
- **S4 entity_coverage_complete_rate:** `0.9130434782608695`
- **S4b script_fail_count:** `8`
- **S5 pass_rate:** `0.7246376811594203`
- **S6 pass_rate / passed:** `0.96` / `48`
- **curated docs:** `20`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `8b08baf3bcbf412eaace2d648074de01` | `bn` | `lab_report` | `['missing_required_entities:PATIENT_NAME,AGE,GENDER,HOSPITAL_NAME,MRN,DOCTOR_NAME,DISTRICT,PHONE_NU…` |
| S4 soft | `8027a62865e6486cba6cb4978d8de433` | `doi` | `radiology_report` | `['missing_required_entities:DISTRICT']` |
| S4 soft | `f584cfd90471426ea809f549021f9a0f` | `en` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `a90ec50b35a04cb3a09db6ca09ff1a37` | `kn` | `lab_report` | `['missing_required_entities:STUDENT_ID']` |
| S4 soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `referral_letter` | `['missing_required_entities:MRN']` |
| S4 soft | `6dae1a15538348f3a3bc29a4111088bc` | `te` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4b soft | `8b08baf3bcbf412eaace2d648074de01` | `bn` | `lab_report` | `no_valid_entity_tags_to_protect;invalid_type_tags:এম.আর.এন,রোগীর_নাম,বয়স,লিঙ্গ,ডক্টর_নাম,রোগী_আইডি…` |
| S4b soft | `c56b228238e847d393141f0a17d86444` | `hi` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.011<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `442b760204fb4430b6745545930228cd` | `ks` | `prescription` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `lab_report` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `opd_slip` | `script_purity_failed:wrong_indic_script:Bengali>Meitei attempt=1;generator_repair_failed:wrong_indi…` |
| S4b soft | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `phc_register` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_s…` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `referral_letter` | `Translation lost protected ID tag '[[AGE|32]]'` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `radiology_report` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S5 fail | `3c0199017c7c4f00bbb3de4770ce25fc` | `as` | `hospital_billing` | score=0.35 flags=['dialect_script_impurity', 'invented_entity_type'] |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `er_triage_notes` | score=0.35 flags=['instruction_drift', 'dialect_script_impurity'] |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `telemedicine_transcript` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `surgical_note` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `8027a62865e6486cba6cb4978d8de433` | `doi` | `radiology_report` | score=0.18 flags=['dialect_script_impurity', 'domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `c56b228238e847d393141f0a17d86444` | `hi` | `er_triage_notes` | score=0.0 flags=['instruction_drift', 'length_violation', 'dialect_script_impurity'] |
| S5 fail | `442b760204fb4430b6745545930228cd` | `ks` | `opd_slip` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `442b760204fb4430b6745545930228cd` | `ks` | `prescription` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `lab_report` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `opd_slip` | score=0.15 flags=['dialect_script_impurity', 'length_violation', 'surrogate_plausibility_collapse'] |
| S5 fail | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `phc_register` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `edf29d2e2af24030992b0a4ccf114083` | `pa` | `er_triage_notes` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `phc_register` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `referral_letter` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `radiology_report` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `er_triage_notes` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `er_triage_notes` | score=0.4 flags=['dialect_script_impurity'] |
| S5 fail | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `telemedicine_transcript` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `6dae1a15538348f3a3bc29a4111088bc` | `te` | `opd_slip` | score=0.55 flags=['instruction_drift'] |
| S6 fail | `8b08baf3bcbf412eaace2d648074de01` | `bn` | `telemedicine_transcript` | `['phi_residue:2']` |
| S6 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `radiology_report` | `['missing_required:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `lab_report` (`bn`).
- **Missing required tags:** `['PATIENT_NAME', 'AGE', 'GENDER', 'HOSPITAL_NAME', 'MRN', 'DOCTOR_NAME', 'DISTRICT', 'PHONE_NUMBER', 'PATIENT_ID', 'STUDENT_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:PATIENT_NAME,AGE,GENDER,HOSPITAL_NAME,MRN,DOCTOR_NAME,DISTRICT,PHONE_NUMBER,PATIENT_ID,STUDENT_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|Anjali Mondal]] [[AGE|27]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-WB-2024-0815-01]] Portal [[URL|https://tele.wbhealth.in/visit/APT-WB-2024-0815-01]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|anjali.mondal.wb@example.com]] Hospital [[HOSPITAL_NAME|Barddhaman District Hospital]]
--- chat ---
Patient: নমস্তে ডাক্তার। আমি অঞ্জলি, ২৭ বছরের। আমি ৩ মাসের অন্তঃসত্ত্বা। आजकल পেটে বেশি ব্যথা হচ্ছে, বিশেষ করে ডান দিকে। এটা কি …
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `radiology_report` (`doi`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|Civil Hospital Jalandhar]]
[[PATIENT_NAME|Baldev Singh]] जन्म तिथि [[DOB|1990-02-15]] [[AGE|34]] [[GENDER|Male]]
भर्ती तिथि [[ADMISSION_NUMBER|ADM-2024-0718]] वार्ड [[WARD_NUMBER|A1]] बेड [[BED_NUMBER|05]]
डाक्टर [[DOCTOR_NAME|Dr. Rajesh Kumar]] | कोर्स / सलाह: मरीज गी त्रै दिनें थमां तेज बुखार, कफ आह्‌ली खंघ, ते साऽ लैने च तकलीफ दी शिकायत कन्नै भर्ती कीता गेआ हा। जांच दे दौरान, उ’नें गी तेज बुखार हा जि’दे च तापमान 102.4°F, दिल दी धड़कन 110 bpm, साऽ दी रफ़्तार 24 साऽ/मिनट, ते ब्लड प्रेशर 130/85 mmHg हा। छाती दी जांच च दोनो पासे क्रैकल्स (crackles) सुनाई दित्ते…
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `radiology_report` (`en`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Kasturba Medical College Hospital]]
[[PATIENT_NAME|Shanthi Poojary]] DOB [[DOB|1979-11-05]] [[AGE|45]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-1028]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Rajesh Bhat]] | Course / advice: The patient is a 45-year-old female tailor from Dakshina Kannada, Karnataka, admitted with a diagnosis of pulmonary tuberculosis with associated hypertension. She was started on a standard four-drug anti-tubercular regimen of Isoniazid, Rifampicin, Pyrazinamide, and Ethambutol. Her blood pressure, whic…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `lab_report` (`kn`).
- **Missing required tags:** `['STUDENT_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:STUDENT_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ಪ್ರಿಸ್ಕ್ರಿಪ್ಷನ್ — [[HOSPITAL_NAME|Sri Sathya Sai Institute of Higher Medical Sciences, Ramanagara]]
ರೋಗಿ [[PATIENT_NAME|Savitri Bai]], [[AGE|55]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0815-001]]
ಡಾ. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
ಫೋನ್: [[PHONE_NUMBER|9886543210]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
ರೋಗಿ ID: [[PATIENT_ID|PID-88776]]
ವಿಳಾಸ: [[RESIDENTIAL_ADDRESS|15th Cross, Near KSRTC Bus Stand, Ramanagara Town, Karnataka - 562159]]
ಜಿಲ್ಲೆ: [[DISTRICT|Ramanagara]]

ರೋಗನಿರ್ಣಯ: ಮೂಳೆ ಮೆಟಾಸ್ಟಾಸಿಸ್‌ನೊಂದಿಗೆ ಮೆಟಾಸ್ಟಾಟಿಕ್ ಸ್ತನ ಕ್ಯಾನ್ಸರ್, ಎಡ ಮೊಣಕಾಲಿನ ದೀರ್ಘಕಾಲದ ಅಸ್ಥಿಸಂಧಿವಾತ.

Rx:
1.  ಪ್ಯಾಕ್ಲಿಟಾಕ್ಸೆ…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `referral_letter` (`sat`).
- **Missing required tags:** `['MRN']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:MRN']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales person from rural Dumka, was admitted to our facility following a road traffic accident. She reports that she was walking near her home in the village of [[VILLAGE|Shivpur]] when she was struck by a speedin…
```

### S4 generation soft-fail 6

- **What:** generation soft-fail on `opd_slip` (`te`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD Slip | డిస్ట్రిక్ట్ హాస్పిటల్ ఒంగోలు | ID [[HOSPITAL_ID|DH-AP-PO-001]]
Patient: [[PATIENT_NAME|రవి కుమార్]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|పురుషుడు]]
Occupation: [[OCCUPATION|Puncher, Metal]] | MRN: [[MRN|OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|డాక్టర్ శ్రీనివాస్ రెడ్డి]]
Relative: [[RELATIVE_NAME|లక్ష్మి]], Wife | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-4412]] | District: [[DISTRICT|ప్రకాశం]]
Chief complaint: మూడు వారాలుగా దగ్గుతో పాటు రక్తపు వాంతులు అవుతున్నాయి, బరువు తగ్గడం మరియు రాత్రిపూట చెమటలు పట్టడం.

History of prese…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `lab_report` (`bn`).
- **Error:** `no_valid_entity_tags_to_protect;invalid_type_tags:এম.আর.এন,রোগীর_নাম,বয়স,লিঙ্গ,ডক্টর_নাম,রোগী_আইডি,ফোন_নম্বর,জেলা,ছাত্র_আইডি`
- **script_ok:** `False`
- **EN pivot preview:**

```
--- session ---
Patient [[PATIENT_NAME|Anjali Mondal]] [[AGE|27]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-WB-2024-0815-01]] Portal [[URL|https://tele.wbhealth.in/visit/APT-WB-2024-0815-01]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|anjali.mondal.wb@example.com…
```
- **Translated preview:**

```
--- session ---
Patient [[PATIENT_NAME|Anjali Mondal]] [[AGE|27]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-WB-2024-0815-01]] Portal [[URL|https://tele.wbhealth.in/visit/APT-WB-2024-0815-01]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|anjali.mondal.wb@example.com…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `er_triage_notes` (`hi`).
- **Error:** `script_purity_failed:target_script_ratio:0.011<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|Sahibganj District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Sushila Murmu]] [[AGE|23]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JH04K-5678]] (exactly once).
Relative [[RELATIVE_NAME|Phoolmani Murmu]] Phone [[PHONE_NUMBER|9431023456]] Dr [[DOCTOR_NAME|Dr. Rajesh Kuma…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|Sahibganj District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Sushila Murmu]] [[AGE|23]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|JH04K-5678]] से आई (एक बार)।
Relative [[RELATIVE_NAME|Phoolmani Murmu]] Phone [[PHONE_NUMBER|9431023456]] Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Vitals …
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `prescription` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Shupiyan District Hospital]] | ID [[HOSPITAL_ID|SDH-SHU-001]]
Patient: [[PATIENT_NAME|Zarifa Bibi]] | DOB [[DOB|1992-08-15]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Senior Officials of Political Party Organisations, Other]] | MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Ayesha Malik]]
Relative: [[RELATIVE_NAME|Mohammed Yousuf…
```
- **Translated preview:**

```
آؤٹ پیشنٹ ڈیپارٹمنٹ سلپ | [[HOSPITAL_NAME|Shupiyan District Hospital]] | آئی ڈی [[HOSPITAL_ID|SDH-SHU-001]]
مریض: [[PATIENT_NAME|Zarifa Bibi]] | تاریخِ پیدائش [[DOB|1992-08-15]] | عمر: [[AGE|32]] | صنف: [[GENDER|Female]]
پیشہ: [[OCCUPATION|Senior Officials of Political Party Organisations, Other]] | میڈیکل ریکارڈ نمبر: [[MRN|OPD-2024-0815-001]] | ڈاکٹر: [[DOCTOR_NAME|Dr. Ayesha Malik]]
رشتہ دار: …
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `lab_report` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```
- **Translated preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `opd_slip` (`mni`).
- **Error:** `script_purity_failed:wrong_indic_script:Bengali>Meitei attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```
- **Translated preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `phc_register` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```
- **Translated preview:**

```
Laboratory Report
[[HOSPITAL_NAME|Bishnupur District Hospital]]
[[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Thokchom Ongbi Leima]]
[[AGE|33]]
[[GENDER|Female]]
Ordered by [[DOCTOR_NAME|Dr. R. K. Singh]]
[[DISTRICT|Bishnupur]]
[[PHONE_NUMBER|+91-9876543210]]
[[PATIENT_ID|PH-2024-MN-0815-001]]
[[STUDENT_ID|STU-2024-MN-0815-001]]
Test Results:
Hemoglobin: 11.2 g/dL
White Blood Cell Count: 7.5 x 10^9/L
…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `referral_letter` (`sat`).
- **Error:** `Translation lost protected ID tag '[[AGE|32]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] from [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales p…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales person…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `radiology_report` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] from [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales p…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales person…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `er_triage_notes` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] from [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales p…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales person…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `hospital_billing` (`as`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'invented_entity_type']`
- **Reasoning:** All content in English/Latin script instead of Assamese (Bengali); multiple non-allowlist types (ADMISSION_DATE, BILLING_CODE, DISCHARGE_DATE, etc.).
- **Preview:**

```
HOSPITAL BILLING INVOICE
HOSPITAL_NAME|Dibrugarh Civil Hospital
PATIENT_NAME|Ranjan Gogoi
MRN|MRN-2024-0912-001
PATIENT_ADDRESS|DISTRICT|Dibrugarh
PIN_CODE|786001
PHONE_NUMBER|9876543210
AADHAAR_NUMBER|203835321155
INSURANCE_POLICY_NUMBER|POL-AS-2024-5678
TAX_ID|18AAAPG1234C1ZV
TELEPHONE_LANDLINE|0373-2345678
VEHICLE_REGISTRATION|AS-01-AB-1234
ADMISSION_DATE|2024-09-15
DISCHARGE_DATE|2024-09-18
ADMISSION_TYPE|Emergency
DISCHARGE_STATUS|Discharged
BILLING_CODE|99284
BILLING_DESCRIPTION|Emergency…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `er_triage_notes` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['instruction_drift', 'dialect_script_impurity']`
- **Reasoning:** Domain oncology/chronic care violated by acute appendicitis content; clinical prose mixes English medical phrases instead of consistent Bodo Devanagari narrative.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|डिमापुर जिला अस्पताल]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|ललिता होरन]] [[AGE|28]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|NL01A1234]] नि जोहै फैदों।
Relative [[RELATIVE_NAME|बिरन होरन]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. केवि आंगामी]]
Vitals / acuity: Patient आ मोननै साननिफ्राय उदै सानाय, बान्दैनाय आरो उदै गाज्रि जानायजों फैदों। बिथाङा hemodynamically stable,…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose is Hindi (not Bodo) despite Devanagari script and correct Latin-tagged entities.
- **Preview:**

```
--- सत्र ---
रोगी [[PATIENT_NAME|Rina Boro]] [[AGE|28]] [[GENDER|Female]]
अपॉइंटमेंट [[APPOINTMENT_ID|APT-240521-01]] पोर्टल [[URL|https://tele.example.in/visit]]
क्लाइंट IP [[IP_ADDRESS|103.21.244.12]] डिवाइस IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|A1:B2:C3:D4:E5:F6]] फोन [[PHONE_NUMBER|9876512340]]
ईमेल [[EMAIL_ADDRESS|rina.boro@example.com]] अस्पताल [[HOSPITAL_NAME|Dimapur District Hospital]]
--- चैट ---
रोगी: नमस्कार डॉक्टर साहब, मैं [[PATIENT_NAME|Rina Boro]] डिमापुर से हूँ।…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `surgical_note` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is Hindi, not Bodo, despite Devanagari script and valid tags.
- **Preview:**

```
ऑपरेटिव नोट — [[HOSPITAL_NAME|जिला अस्पताल डिमापुर]] [[ADMISSION_NUMBER|ADM-2024-0912]] वार्ड [[WARD_NUMBER|OT]]
[[PATIENT_NAME|हेमा बोरो]] [[AGE|28]] [[GENDER|Female]] सर्जन [[DOCTOR_NAME|डॉ. के. जामीर]]
प्रक्रिया / निष्कर्ष: रोगी डिमापुर, नागालैंड की 28 वर्षीय महिला किसान है, जिसे 38 सप्ताह के गर्भ में भ्रूण संकट के कारण आपातकालीन सी-सेक्शन के लिए भर्ती किया गया था। रोगी विवाहित है और उसका एक पिछला सामान्य योनि प्रसव हुआ है। परीक्षण पर, उसके महत्वपूर्ण लक्षण स्थिर थे, रक्तचाप 110/70 mmHg और ह…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `radiology_report` (`doi`).
- **Score / verdict:** `0.18` / `fail`
- **Flags:** `['dialect_script_impurity', 'domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** English prose instead of Dogri Devanagari; male patient with ovarian/uterine anatomy and adnexal mass.
- **Preview:**

```
Radiology Report — [[HOSPITAL_NAME|Civil Hospital Jalandhar]] | [[PATIENT_NAME|Jaswinder Singh]] [[AGE|34]] [[GENDER|Male]]
MRN [[MRN|MRN-PB-2024-0891]] [[ENCOUNTER_ID|ENC-2024-08-15-001]] | Report by [[DOCTOR_NAME|Dr. Rajinder Kumar]]
Findings: 34-year-old male patient is a shopkeeper from Jalandhar, Punjab, presenting with acute right lower quadrant abdominal pain. Abdominal ultrasound was performed. Liver and spleen are normal in size and echotexture. Gallbladder is unremarkable without ston…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `er_triage_notes` (`hi`).
- **Score / verdict:** `0.0` / `fail`
- **Flags:** `['instruction_drift', 'length_violation', 'dialect_script_impurity']`
- **Reasoning:** Pure English title repetition (no Devanagari prose); extreme length dump with zero clinical content or Hindi narrative.
- **Preview:**

```
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Triage & Nursing Notes
ER Tr…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `opd_slip` (`ks`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is Urdu (not Kashmiri) despite Arabic script and correct persona/domain fit.
- **Preview:**

```
آؤٹ پیشنٹ ڈیپارٹمنٹ سلپ | [[HOSPITAL_NAME|شُپیاں ڈسٹرکٹ ہسپتال]] | آئی ڈی [[HOSPITAL_ID|SDH-SHU-001]]
مریض: [[PATIENT_NAME|زَرِفہ بی بی]] | تاریخِ پیدائش [[DOB|1992-08-15]] | عمر: [[AGE|32]] | صنف: [[GENDER|Female]]
پیشہ: [[OCCUPATION|سینیئر آفیسرز آف پولیٹیکل پارٹی آرگنائزیشنز، ادر]] | میڈیکل ریکارڈ نمبر: [[MRN|OPD-2024-0815-001]] | ڈاکٹر: [[DOCTOR_NAME|ڈاکٹر عائشہ ملک]]
رشتہ دار: [[RELATIVE_NAME|محمد یوسف]] | فون: [[PHONE_NUMBER|9419012345]]
رجسٹرار ایمپلائی آئی ڈی: [[EMPLOYEE_ID|EMP-SDH-045]…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `prescription` (`ks`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English; expected Kashmiri Arabic script.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|District Hospital Shupiyan]]
Patient [[PATIENT_NAME|زاريفا بيبي]], [[AGE|32]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0912-001]]
Dr. [[DOCTOR_NAME|Dr. Aijaz Ahmad]]
Rx: Tab. Paracetamol 500mg one tablet twice daily for fever and body ache. Tab. Azithromycin 250mg one tablet once daily for five days for respiratory infection. Tab. Pantoprazole 40mg one tablet once daily before breakfast for acidity. Apply Mupirocin 2% ointment on affected skin areas twice daily for …
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `lab_report` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in Bengali script/language instead of required Meitei script for Manipuri; all other elements (tags, content, persona fit) acceptable.
- **Preview:**

```
[[PATIENT_NAME|থোকচম ওংবি লেইমা]] [[AGE|33]] [[GENDER|Female]] [[HOSPITAL_NAME|বিষ্ণুপুর জেলা হাসপাতাল]] [[MRN|MRN-2024-0815-001]] [[DOCTOR_NAME|ডাঃ আর. কে. সিং]] [[DISTRICT|বিষ্ণুপুর]] [[PHONE_NUMBER|+91-9876543210]] [[PATIENT_ID|PH-2024-MN-0815-001]] [[STUDENT_ID|STU-2024-MN-0815-001]]
লাব রিপোর্ট
তারিখ: 15 আগস্ট 2024
রোগীর নাম: থোকচম ওংবি লেইমা
বয়স: 33
লিঙ্গ: মহিলা
এম.আর.এন: MRN-2024-0815-001
হাসপাতালের নাম: বিষ্ণুপুর জেলা হাসপাতাল
চিকিৎসকের নাম: ডাঃ আর. কে. সিং
জেলা: বিষ্ণুপুর
ফোন নম্বর: +…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `opd_slip` (`mni`).
- **Score / verdict:** `0.15` / `fail`
- **Flags:** `['dialect_script_impurity', 'length_violation', 'surrogate_plausibility_collapse']`
- **Reasoning:** OPD prose complaint is repetitive gibberish in Bengali script (not Meitei), massively exceeds length, and lacks clinical plausibility.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Bishnupur District Hospital]] | ID [[HOSPITAL_ID|BDH-01]]
Patient: [[PATIENT_NAME|Thokchom Sanjita Devi]] | DOB [[DOB|1991-07-22]] | Age: [[AGE|33]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Homemaker]] | MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. L. Renu]]
Relative: [[RELATIVE_NAME|Thokchom Sanjoy Singh]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-BDH-042]] | District: [[DISTRICT|Bishnupur]]
Chief complaint: 10 …
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `phc_register` (`mni`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Bengali script with Tamil intrusion instead of Meitei; long multi-paragraph narrative also mismatches register-entry brevity.
- **Preview:**

```
নংথোমবাম বিমল ৩০৩ [[GENDER|Female]] | [[VILLAGE|লামলাই]] [[DISTRICT|বিষ্ণুপুর]] [[HOSPITAL_NAME|Primary Health Centre, Bishnupur]] [[PHONE_NUMBER|9876543210]] [[ASHA_WORKER_NAME|থোকচম সঞ্জিতা]] [[BPL_RATION_CARD|BPL-MN-2023-0045]] [[VOTER_ID|VM20230456789]] [[ABHA_ID|12-3456-7890-1234]]
নংথোমবাম বিমল ৩০৩ [[GENDER|Female]] | ২৮ সপ্তাহ গর্ভকালীন সময়ের জন্য প্রসবপূর্ব পরীক্ষা

প্রধান অভিযোগ: রোগী নিয়মিত প্রসবপূর্ব পরীক্ষার জন্য এসেছেন। ২ দিন ধরে পেটের নিচের অংশে সামান্য অস্বস্তি হচ্ছে, জ্বর বা র…
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `er_triage_notes` (`pa`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative mixes substantial English prose sentences with Punjabi; expected full Gurmukhi body for Punjabi document.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|ਗੁਰੂਨਾਨਕ ਹਸਪਤਾਲ]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|ਜਸਵਿੰਦਰ ਕੌਰ]] [[AGE|73]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|PB10AB1234]] (exactly once).
Relative [[RELATIVE_NAME|ਬਲਵੰਤ ਕੌਰ]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Amarinder Singh]]
Vitals / acuity: ਮਰੀਜ਼ ਹੋਸ਼ ਵਿੱਚ ਹੈ ਪਰ ਪਰੇਸ਼ਾਨ ਪ੍ਰਤੀਤ ਹੋ ਰਹੀ ਹੈ। Blood pressure 160/95 mmHg, heart rate 110 bpm, …
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `phc_register` (`sa`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose is Hindi (with Sanskritized medical terms) in Devanagari rather than Sanskrit; minor English glosses outside tags but main narrative mismatches required language.
- **Preview:**

```
प्राथमिक स्वास्थ्य केंद्र रजिस्टर प्रविष्टि — [[HOSPITAL_NAME|प्राथमिक स्वास्थ्य केंद्र, बिल्हौर]] ग्राम [[VILLAGE|बिल्हौर]] जिला [[DISTRICT|कानपुर नगर]]
[[PATIENT_NAME|आरोह शर्मा]] [[AGE|19]] [[GENDER|पुरुष]] | [[ASHA_WORKER_NAME|सुनीता यादव]] ने [[PHONE_NUMBER|9876512340]] पर [[BPL_RATION_CARD|BPL-UP-208001-4421]] और [[VOTER_ID|ABC1234567]] के साथ [[ABHA_ID|12-3456-7890-1234]] रोगी [[PATIENT_NAME|आरोह शर्मा]] के लिए रिपोर्ट किया।
मुख्य शिकायत: रोगी 24 घंटों से तीव्र दक्षिण-अधो-उदर (राइट लोअर …
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `referral_letter` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Santali Ol Chiki. No other violations (entities allowed, persona fit, length ok).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0918]] [[HOSPITAL_NAME|Shri Krishna Medical College & Hospital]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Patient presents with a traumatic injury to the right lower limb requiring surgical intervention.

Patient Meena Devi, a 32-year-old female telemarketing sales person from rural Dumka, was admitted to our facility following a road traffic accident. She reports that …
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `radiology_report` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English; expected Santali Ol Chiki narrative.
- **Preview:**

```
Imaging report — [[HOSPITAL_NAME|Dumka District Hospital]] | [[PATIENT_NAME|Meena Devi]] [[AGE|32]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Findings: Plain radiograph of the chest was performed. The lungs are clear without any consolidations, effusions, or pneumothorax. The heart size is normal. The bony thorax is intact without any acute fractures. The diaphragm and costophrenic angles are sharp. No …
```

### S5 judge fail 16

- **What:** linguistic judge **fail** on `er_triage_notes` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose is English/Latin with scattered transliterated Santali words; expected full Santali narrative in Ol Chiki script.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|District Hospital Dumka]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Meena Devi]] [[AGE|32]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|JH10C-123456]] te ayo.
Relative [[RELATIVE_NAME|Ramesh Devi]] Phone [[PHONE_NUMBER|9431056789]] Dr [[DOCTOR_NAME|Dr. Sunita Murmu]]
Vitals / acuity: Patient conscious, alert, mild distress re. BP 140/90, Pulse 110/min, RR 22/min, Temp 37.8°C. SpO2 98% room…
```

### S5 judge fail 17

- **What:** linguistic judge **fail** on `er_triage_notes` (`sd`).
- **Score / verdict:** `0.4` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose heavily code-mixed with English terms and contains Devanagari intrusions instead of consistent Sindhi (Arabic script).
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Jamnagar District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Jashodaben Makvana]] [[AGE|46]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
آسپتال جي ambulance [[VEHICLE_REGISTRATION|GJ01AB1234]] (صرفه هڪ ڀيرو).
[[RELATIVE_NAME|Rameshbhai Makvana]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Anjali Patel]]
Vitals / acuity: مريضو تيز anxiety، restlessness، ۽ tearfulness سان گڏ اچي پيو. Blood pressure 140/90 mmHg،…
```

### S5 judge fail 18

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`sd`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Devanagari/Thai/English heavily into Sindhi Arabic narrative; violates expected script despite valid entity tags.
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|جاشوڏابن]] [[AGE|46]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|A1:B2:C3:D4:E5:F6]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|jashodaben.makvana@email.com]] Hospital [[HOSPITAL_NAME|جمنا نگر ڊسٽرڪٽ اسپتال]]
--- chat ---
Patient:سلام ڊاڪٽر، مون کي پچھل ٽن هفتن کان مُستقل کنگھ آھي. اھا ت…
```

### S5 judge fail 19

- **What:** linguistic judge **fail** on `opd_slip` (`te`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift']`
- **Reasoning:** Domain Oncology specified but content is TB workup/diagnosis; Telugu prose and allowed entities otherwise match.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|జిల్లా ఆసుపత్రి ఒంగోలు]] | ID [[HOSPITAL_ID|DH-AP-PO-001]]
Patient: [[PATIENT_NAME|రవికుమార్]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Puncher, Metal]] | MRN: [[MRN|OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|డాక్టర్ శ్రీనివాస్ రెడ్డి]]
Relative: [[RELATIVE_NAME|లక్ష్మి]], భార్య | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-4412]] | District: [[DISTRICT|ప్రకాశం]]
Chief complaint: మూడు వారా…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `telemedicine_transcript` (`bn`).
- **Errors:** `['phi_residue:2']`
- **Preview:**

```
--- সেশন ---
রোগী [[PATIENT_NAME|Anjali Mondal]] [[AGE|27]] [[GENDER|Female]]
অ্যাপয়েন্টমেন্ট [[APPOINTMENT_ID|APT-WB-2024-0815-01]] পোর্টাল [[URL|https://tele.wbhealth.in/visit/APT-WB-2024-0815-01]]
ক্লায়েন্ট আই.পি [[IP_ADDRESS|103.21.244.12]] ডিভাইস আই.এম.ই.আই [[IMEI_NUMBER|356938035643809]]
ম্যাক [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] ফোন [[PHONE_NUMBER|9876543210]]
ইমেল [[EMAIL_ADDRESS|anjali.mondal.wb@example.com]] হাসপাতাল [[HOSPITAL_NAME|Barddhaman District Hospital]]
--- চ্যাট ---
রোগী: नम…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `radiology_report` (`en`).
- **Errors:** `['missing_required:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
Radiology report — [[HOSPITAL_NAME|KMC Manipal Hospital]] | [[PATIENT_NAME|Shanthi Poojary]] [[AGE|45]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Priya Nair]]
Findings: Ultrasound examination of the abdomen was performed on [[PATIENT_NAME|Shanthi Poojary]], a 45-year-old female. The study was conducted to evaluate the uterus and adnexa. The uterus is anteverted and anteflexed, measuring 8.2 x 5.5 x 4.0 cm. The endomet…
```


## Surviving curated set

- languages: `{'as': 1, 'bn': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 2, 'discharge_summary': 3, 'opd_slip': 2, 'phc_register': 1, 'prescription': 2, 'radiology_report': 2, 'referral_letter': 1, 'surgical_note': 4, 'telemedicine_transcript': 2}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
