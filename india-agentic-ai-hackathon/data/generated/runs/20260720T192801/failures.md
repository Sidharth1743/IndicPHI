# Failures audit — `20260720T192801`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260720T192801/pipeline.resolved.yaml`
- **issue count:** **46** (hard=0, gen_soft=5, tr_soft=9, judge=27, auditor=5)
- **S4 entity_coverage_complete_rate:** `0.927536231884058`
- **S4b script_fail_count:** `9`
- **S5 pass_rate:** `0.6086956521739131`
- **S6 pass_rate / passed:** `0.8809523809523809` / `37`
- **curated docs:** `20`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `8b08baf3bcbf412eaace2d648074de01` | `bn` | `surgical_note` | `['missing_required_entities:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER']` |
| S4 soft | `2a0042e543f7400299209a84f31ceab7` | `brx` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `72db01dc59584f27949df74b76c51edf` | `mai` | `radiology_report` | `['missing_required_entities:HOSPITAL_ID']` |
| S4 soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `er_triage_notes` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `6dae1a15538348f3a3bc29a4111088bc` | `te` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4b soft | `2a0042e543f7400299209a84f31ceab7` | `brx` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 5…` |
| S4b soft | `442b760204fb4430b6745545930228cd` | `ks` | `prescription` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `opd_slip` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_s…` |
| S4b soft | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `phc_register` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 5…` |
| S4b soft | `01f011a8da4d401ca4ff9810f7a35a19` | `or` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `referral_letter` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_s…` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `radiology_report` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `telemedicine_transcript` | `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_i…` |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `er_triage_notes` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `telemedicine_transcript` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `2a0042e543f7400299209a84f31ceab7` | `brx` | `surgical_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `referral_letter` | score=0.8 flags=['invented_entity_type'] |
| S5 fail | `f584cfd90471426ea809f549021f9a0f` | `en` | `radiology_report` | score=0.65 flags=['domain_persona_mismatch'] |
| S5 fail | `c56b228238e847d393141f0a17d86444` | `hi` | `er_triage_notes` | score=0.4 flags=['surrogate_plausibility_collapse', 'instruction_drift'] |
| S5 fail | `a90ec50b35a04cb3a09db6ca09ff1a37` | `kn` | `lab_report` | score=0.45 flags=['instruction_drift', 'surrogate_plausibility_collapse'] |
| S5 fail | `442b760204fb4430b6745545930228cd` | `ks` | `opd_slip` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `442b760204fb4430b6745545930228cd` | `ks` | `prescription` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `72db01dc59584f27949df74b76c51edf` | `mai` | `referral_letter` | score=0.35 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `f3d9ad4909c345f99fadaafad821b3b0` | `ml` | `opd_slip` | score=0.7 flags=['instruction_drift'] |
| S5 fail | `f3d9ad4909c345f99fadaafad821b3b0` | `ml` | `prescription` | score=0.65 flags=['domain_persona_mismatch'] |
| S5 fail | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `opd_slip` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `51fc0c57ffcc40c6ae5d2fb055d07030` | `mni` | `phc_register` | score=0.1 flags=['length_violation', 'instruction_drift', 'surrogate_plausibility_collapse'] |
| S5 fail | `01f011a8da4d401ca4ff9810f7a35a19` | `or` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity', 'instruction_drift'] |
| S5 fail | `edf29d2e2af24030992b0a4ccf114083` | `pa` | `radiology_report` | score=0.6 flags=['domain_persona_mismatch'] |
| S5 fail | `edf29d2e2af24030992b0a4ccf114083` | `pa` | `er_triage_notes` | score=0.65 flags=['surrogate_plausibility_collapse'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `asha_worker_note` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `phc_register` | score=0.25 flags=['dialect_script_impurity', 'instruction_drift'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `referral_letter` | score=0.15 flags=['dialect_script_impurity'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `radiology_report` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `944cf9bf2c4d48b2974bb723f704bded` | `sat` | `er_triage_notes` | score=0.25 flags=['dialect_script_impurity', 'instruction_drift'] |
| S5 fail | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `er_triage_notes` | score=0.25 flags=['length_violation', 'surrogate_plausibility_collapse'] |
| S5 fail | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `telemedicine_transcript` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `68da8d4342bc4e28a1a4cd69a55cc86f` | `sd` | `surgical_note` | score=0.3 flags=['dialect_script_impurity', 'surrogate_plausibility_collapse'] |
| S5 fail | `6dae1a15538348f3a3bc29a4111088bc` | `te` | `opd_slip` | score=0.55 flags=['instruction_drift', 'domain_persona_mismatch'] |
| S5 fail | `c8cbb5811e2a4a05bfe15b06b2be3a52` | `ur` | `hospital_billing` | score=0.45 flags=['instruction_drift', 'surrogate_plausibility_collapse', 'length_violation'] |
| S6 fail | `3c0199017c7c4f00bbb3de4770ce25fc` | `as` | `hospital_billing` | `['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:1']` |
| S6 fail | `8b08baf3bcbf412eaace2d648074de01` | `bn` | `surgical_note` | `['missing_required:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER', 'upstream_ge…` |
| S6 fail | `72db01dc59584f27949df74b76c51edf` | `mai` | `radiology_report` | `['missing_required:HOSPITAL_ID', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_…` |
| S6 fail | `259f783314be4a6ca9979240d0de82cd` | `ne` | `telemedicine_transcript` | `['format:PHONE_NUMBER:phone_format']` |
| S6 fail | `c8cbb5811e2a4a05bfe15b06b2be3a52` | `ur` | `insurance_claim` | `['format:AADHAAR_NUMBER:aadhaar_verhoeff']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `surgical_note` (`bn`).
- **Missing required tags:** `['DOCTOR_NAME', 'HOSPITAL_NAME', 'ADMISSION_NUMBER', 'WARD_NUMBER', 'BED_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
--- সেশন ---
রোগী [[PATIENT_NAME|Rina Mondal]] [[AGE|27]] [[GENDER|Female]]
অ্যাপয়েন্টমেন্ট [[APPOINTMENT_ID|APT-WB-2024-1123]] পোর্টাল [[URL|https://tele.wbhealth.in/visit]]
ক্লায়েন্ট আই.পি [[IP_ADDRESS|103.21.244.12]] ডিভাইস আই.এম.ই.আই [[IMEI_NUMBER|356938035643809]]
ম্যাক [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] ফোন [[PHONE_NUMBER|9876543210]]
ইমেল [[EMAIL_ADDRESS|rina.mondal.wb@example.com]] হাসপাতাল [[HOSPITAL_NAME|Sub-Divisional Hospital, Kalna]]
--- চ্যাট ---
রোগী: ডাক্তার, আমি রিনা মন্ডল। আমার বয়স 27 বছর এবং আমি গর্ভবতী। আমার 5 মাস চলছে। আমার পেটের নিচের দিকে কিছু ব্যথা হচ্ছে। এটি একটি ভো…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `er_triage_notes` (`brx`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ER triage — District Hospital Dimapur Encounter [[ENCOUNTER_ID|ENC-2024-1123]]
[[PATIENT_NAME|Lalita Ao]] [[AGE|28]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|NL01A1234]]
Relative [[RELATIVE_NAME|Temsula Ao]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Kevi Medom]]
Vitals / acuity: Patient presents with acute abdominal pain, nausea, and fatigue. Vitals stable, moderate distress.

Nursing Notes:
Patient Lalita Ao, a 28-year-old female cultivator from Dimapur, Nagaland, was brought to the ER by her spouse, Tems…
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `radiology_report` (`mai`).
- **Missing required tags:** `['HOSPITAL_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|District Hospital Purnia]]
[[PATIENT_NAME|Ramesh Kumar]] जन्म तिथि [[DOB|2006-04-15]] [[AGE|18]] [[GENDER|Male]]
भर्ती तिथि [[ADMISSION_NUMBER|ADM-2024-0815-001]] वार्ड [[WARD_NUMBER|A1]] बेड [[BED_NUMBER|05]]
डॉक्टर [[DOCTOR_NAME|Dr. Sanjay Prasad]] | उपचार / सलाह: रोगी 18 वर्षीय पुरुष छथि, जिनका ग्रामीण पृष्ठभूमि सँ छथि आ पूर्णिया जिला, बिहार सँ छथि। ओ तीन दिन सँ तेज बुखार, कंपकंपी आ शरीर मे दर्दक शिकायत कऽ रहल छलाह। परीक्षणक समय हुनका तेज बुखार (102.4°F), तीव्र हृदय गति (110 bpm) आ हल्का निर्जलीकरण (dehydration) छल। हुनकर रक्तचाप (blood pressure) 110/70 mmH…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `er_triage_notes` (`sat`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain, associated with fever and vomiting. On examination, she was tachycardic with a rigid abdomen and guarding in the right iliac fossa. Blood investigations showed a leukocytosis of 18,000 cells/mm3 with neu…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `opd_slip` (`te`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD Slip | జిల్లా జనరల్ హాస్పిటల్, ఒంగోలు | ID [[HOSPITAL_ID|DGH-AP-001]]
రోగి: [[PATIENT_NAME|రవి కుమార్]] | పుట్టిన తేదీ [[DOB|1992-05-20]] | వయస్సు: [[AGE|32]] | లింగం: [[GENDER|పురుషుడు]]
వృత్తి: [[OCCUPATION|Puncher, Metal]] | MRN: [[MRN|OPD-2024-0815-001]] | డాక్టర్: [[DOCTOR_NAME|డాక్టర్ శ్రీనివాస్ రెడ్డి]]
సంబంధీకులు: [[RELATIVE_NAME|లక్ష్మి]] | ఫోన్: [[PHONE_NUMBER|9440123456]]
రిజిస్ట్రార్ EmpID: [[EMPLOYEE_ID|EMP-4412]] | జిల్లా: [[DISTRICT|ప్రకాశం]]
ప్రధాన ఫిర్యాదు: గత మూడు నెలలుగా ఎడమ కాలు కిందకు తిమ్మిర్లు వస్తూ, నడుము నొప్పి ఉంది. ఎక్కువ సేపు నిలబడటం వల్ల నొప్పి పెరుగుతోంది.

ప…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `er_triage_notes` (`brx`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 500: {"error":{"message":"Model call failed: Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': \"Function id '267194f7-f0a1-43cc-814b-83e44d440f2c': DEGRADED function cannot be invoked\"}","code":"model_call_failed","request_id":"20260720_c32f2a23-00ee-4269-9470-76dbde8dce2c"}}`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ER triage — District Hospital Dimapur Encounter [[ENCOUNTER_ID|ENC-2024-1123]]
[[PATIENT_NAME|Lalita Ao]] [[AGE|28]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|NL01A1234]]
Relative [[RELATIVE_NAME|Temsula Ao]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Kevi Medom]]
Vitals / acuity: Patient presents with acute abd…
```
- **Translated preview:**

```
ER triage — District Hospital Dimapur Encounter [[ENCOUNTER_ID|ENC-2024-1123]]
[[PATIENT_NAME|Lalita Ao]] [[AGE|28]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|NL01A1234]]
Relative [[RELATIVE_NAME|Temsula Ao]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Kevi Medom]]
Vitals / acuity: Patient presents with acute abd…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `prescription` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Shupiyan]] | ID [[HOSPITAL_ID|DH-SJ-01]]
Patient: [[PATIENT_NAME|Zarifa Bibi]] | DOB [[DOB|1992-08-15]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Senior Officials of Political Party Organisations, Other]] | MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Ayesha Khan]]
Relative: [[RELATIVE_NAME|Mohammad Yousuf]] |…
```
- **Translated preview:**

```
آؤٹ پیشنٹ ڈیپارٹمنٹ سلپ | [[HOSPITAL_NAME|District Hospital Shupiyan]] | آئی ڈی [[HOSPITAL_ID|DH-SJ-01]]
مریض: [[PATIENT_NAME|Zarifa Bibi]] | تاریخ پیدائش [[DOB|1992-08-15]] | عمر: [[AGE|32]] | صنف: [[GENDER|Female]]
پیشہ: [[OCCUPATION|Senior Officials of Political Party Organisations, Other]] | میڈیکل ریکارڈ نمبر: [[MRN|OPD-2024-0815-001]] | ڈاکٹر: [[DOCTOR_NAME|Dr. Ayesha Khan]]
رشتہ دار: [[REL…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `opd_slip` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Lab report — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] MRN [[MRN|RC-2024-0815-001]]
[[PATIENT_NAME|Meena Devi]] [[AGE|33]] [[GENDER|Female]] Ordered by [[DOCTOR_NAME|Dr. L. Singh]]
[[PATIENT_ID|PID-77821]] [[STUDENT_ID|STU-2024-0912]] [[PHONE_NUMBER|9876512340]] [[DISTRICT|Bishnupur]]
Patient from rural Bishnupur, Manipur, presents with persistent fatigue and intermittent low-grade fevers. …
```
- **Translated preview:**

```
ꯂꯦꯕꯣꯔꯦꯇꯣꯔꯤ ꯔꯤꯄꯣꯔꯠ — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] MRN [[MRN|RC-2024-0815-001]]
[[PATIENT_NAME|Meena Devi]] [[AGE|33]] [[GENDER|Female]] [[DOCTOR_NAME|Dr. L. Singh]] ꯅ ꯑꯣꯔꯗꯔ ꯇꯧꯕ
[[PATIENT_ID|PID-77821]] [[STUDENT_ID|STU-2024-0912]] [[PHONE_NUMBER|9876512340]] [[DISTRICT|Bishnupur]]
ꯄꯦꯁꯦꯟꯠ ꯑꯁꯤ ꯃꯦꯅꯤꯄꯨꯔ ꯕꯤꯁꯅꯨꯄꯨꯔ ꯈꯨꯡꯒꯪꯒꯤ ꯃꯅꯨꯡꯗꯒꯤ ꯂꯥꯛꯄꯅꯤ, ꯂꯦꯞꯇꯅ ꯂꯥꯏꯅꯥ ꯅꯥꯕ ꯑꯃꯁꯨꯡ ꯃꯇꯝ ꯃꯇꯝꯒꯤ ꯑꯣꯏꯅ ꯅꯦꯝꯕ ꯂꯥꯏꯅꯥ…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `phc_register` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:Sarvam HTTP 500: {"error":{"message":"Model call failed: Error code: 400 - {'status': 400, 'title': 'Bad Request', 'detail': \"Function id '267194f7-f0a1-43cc-814b-83e44d440f2c': DEGRADED function cannot be invoked\"}","code":"model_call_failed","request_id":"20260720_9236bae5-964f-4d80-98b8-e617a994c551"}}`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Lab report — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] MRN [[MRN|RC-2024-0815-001]]
[[PATIENT_NAME|Meena Devi]] [[AGE|33]] [[GENDER|Female]] Ordered by [[DOCTOR_NAME|Dr. L. Singh]]
[[PATIENT_ID|PID-77821]] [[STUDENT_ID|STU-2024-0912]] [[PHONE_NUMBER|9876512340]] [[DISTRICT|Bishnupur]]
Patient from rural Bishnupur, Manipur, presents with persistent fatigue and intermittent low-grade fevers. …
```
- **Translated preview:**

```
ꯂꯦꯕꯣꯔꯦꯇꯣꯔꯤ ꯔꯤꯄꯣꯔꯠ — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] MRN [[MRN|RC-2024-0815-001]]
[[PATIENT_NAME|Meena Devi]] [[AGE|33]] [[GENDER|Female]] [[DOCTOR_NAME|Dr. L. Singh]] ꯅ ꯑꯣꯔꯗꯔ ꯇꯧꯕ
[[PATIENT_ID|PID-77821]] [[STUDENT_ID|STU-2024-0912]] [[PHONE_NUMBER|9876512340]] [[DISTRICT|Bishnupur]]
ꯄꯦꯁꯦꯟꯠ ꯑꯁꯤ ꯃꯦꯅꯤꯄꯨꯔ ꯕꯤꯁꯅꯨꯄꯨꯔ ꯈꯨꯡꯒꯪꯒꯤ ꯃꯅꯨꯡꯗꯒꯤ ꯂꯥꯛꯄꯅꯤ, ꯂꯦꯞꯇꯅ ꯂꯥꯏꯅꯥ ꯅꯥꯕ ꯑꯃꯁꯨꯡ ꯃꯇꯝ ꯃꯇꯝꯒꯤ ꯑꯣꯏꯅ ꯅꯦꯝꯕ ꯂꯥꯏꯅꯥ…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `insurance_claim` (`or`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.002<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|SCB Medical College Hospital]]
Patient [[PATIENT_NAME|Rashmi Pradhan]], [[AGE|20]] / [[GENDER|Female]], MRN [[MRN|SCB-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. S. K. Mishra]]
Phone: [[PHONE_NUMBER|9437981234]]
Address: [[RESIDENTIAL_ADDRESS|Village: Gobindpur, Post: Puri, District: Puri, Odisha]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Patient ID: [[PATIENT_ID|PID-SCB-20…
```
- **Translated preview:**

```
ପ୍ରେସକ୍ରିପସନ୍ — [[HOSPITAL_NAME|SCB Medical College Hospital]]
ରୋଗୀ [[PATIENT_NAME|Rashmi Pradhan]], [[AGE|20]] / [[GENDER|Female]], MRN [[MRN|SCB-2024-0815-001]]
ଡାକ୍ତର [[DOCTOR_NAME|Dr. S. K. Mishra]]
ଫୋନ୍: [[PHONE_NUMBER|9437981234]]
ଠିକଣା: [[RESIDENTIAL_ADDRESS|Village: Gobindpur, Post: Puri, District: Puri, Odisha]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
ରୋଗୀ ID: [[PATIENT_ID|PID-SCB-2024-08…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `referral_letter` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Ol Chiki`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain, ass…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `radiology_report` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.047<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain, ass…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `er_triage_notes` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.343<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain…
```
- **Translated preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain, ass…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `telemedicine_transcript` (`sd`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|District Hospital Jamnagar]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|Jashodaben Makvana]] [[AGE|46]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|GJ01AB1234]]
Relative [[RELATIVE_NAME|Rameshbhai Makvana]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Pratik Shah]]
Vitals…
```
- **Translated preview:**

```
ای آر ٹریاج اور نرسنگ نوٹس
کلینیکل ڈومین: نفسیات / رویے کی صحت
زبان: سندھی (sd, عربی)

ER triage — [[HOSPITAL_NAME|ڊسٽرڪٽ اسپتال جمن نگر]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|جشوڏي بين مڪوانا]] [[AGE|46]] [[GENDER|مادھو]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ01AB1234]] ذريعي آئي
Relative [[RELATIVE_NAME|رميش ڀائي مڪوانا]]…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `er_triage_notes` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose entirely in English; expected Bodo Devanagari. All entity tags allowed and Latin IDs permitted; no persona or length mismatch.
- **Preview:**

```
ER triage — District Hospital Dimapur Encounter [[ENCOUNTER_ID|ENC-2024-1123]]
[[PATIENT_NAME|Lalita Ao]] [[AGE|28]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|12]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|NL01A1234]]
Relative [[RELATIVE_NAME|Temsula Ao]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Kevi Medom]]
Vitals / acuity: Patient presents with acute abdominal pain, nausea, and fatigue. Vitals stable, moderate distress.

Nursing Notes:
Patient Lalita A…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in Hindi (Devanagari) instead of required Bodo; all entity tags valid and Latin IDs permitted.
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|Lalita Boro]] [[AGE|28]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240815-001]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|lalita.boro@example.com]] Hospital [[HOSPITAL_NAME|Dimapur District Hospital]]
--- chat ---
Patient: नमस्ते डाक्टर, मैं ललिता बोरो हूँ। मुझे पिछले तीन दिनों…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `surgical_note` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is Hindi (Indo-Aryan) instead of Bodo despite Devanagari script; all other elements (persona fit, entity tags, length, medical content) are acceptable.
- **Preview:**

```
शल्यक्रिया नोट — [[HOSPITAL_NAME|District Hospital Dimapur]] [[ADMISSION_NUMBER|ADM-2024-1025]] वार्ड [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Lalita Boro]] [[AGE|28]] [[GENDER|Female]] सर्जन [[DOCTOR_NAME|Dr. Kevi Angami]]
प्रक्रिया / निष्कर्ष: रोगी, डिमापुर, नागाल्यान्ड की 28 वर्षीय महिला किसान, प्रसव पीड़ा की लंबी अवधि और भ्रूण संकट के इतिहास के साथ आई थी। प्रसव पीड़ा प्रेरित करने के प्रयासों की विफलता के बाद, स्पाइनल एनेस्थीसिया के तहत आपातकालीन लोअर सेगमेंट सीजेरियन सेक्शन किया गया। ऑपरेशन के दौर…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `referral_letter` (`en`).
- **Score / verdict:** `0.8` / `fail`
- **Flags:** `['invented_entity_type']`
- **Reasoning:** Non-allowlisted TYPE MEDICAL_RECORD_NUMBER used; all other aspects compliant.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Kasturba Medical College Hospital]] / [[DOCTOR_NAME|Dr. Anjali Rao]]
Re: [[PATIENT_NAME|Shanthi Shetty]], [[AGE|45]] / [[GENDER|Female]], District [[DISTRICT|Dakshina Kannada]]
Reason: Evaluation for chronic anxiety and associated somatic symptoms.

Dear Colleague,

We are referring [[PATIENT_NAME|Shanthi Shetty]], a 45-year-old female tailor from Mangaluru, for your expert opinion on her persistent anxiety. Her [[MRN|MRN-2024-0815-001…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `radiology_report` (`en`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** District mismatch (Udupi vs expected Dakshina Kannada) and weak maternal-health fit for post-menopausal screening.
- **Preview:**

```
Imaging report — [[HOSPITAL_NAME|Kasturba Medical College Hospital]] | [[PATIENT_NAME|Shanthi Poojary]] [[AGE|45]] [[GENDER|Female]]
MRN [[MRN|KMC-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Anjali Menon]]
Findings: Ultrasound examination of the abdomen was performed on a 45-year-old female patient. The study was conducted to evaluate the uterus and adnexa. The endometrial stripe measures 8mm and appears homogeneous. The uterine cavity is unre…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `er_triage_notes` (`hi`).
- **Score / verdict:** `0.4` / `fail`
- **Flags:** `['surrogate_plausibility_collapse', 'instruction_drift']`
- **Reasoning:** Implausible occupation phrase and illiterate-supervisor contradiction break surrogate fit; minor prose drift.
- **Preview:**

```
ER ट्राइएज और नर्सिंग नोट्स
अस्पताल: [[HOSPITAL_NAME|जिला अस्पताल साहिबगंज]]
रोगी [[PATIENT_NAME|सुशीला मुर्मू]]
आयु [[AGE|23]]
लिंग [[GENDER|महिला]]
वार्ड [[WARD_NUMBER|ER]]
बेड [[BED_NUMBER|05]]
आगमन वाहन [[VEHICLE_REGISTRATION|JH10AB5678]]
एनकाउंटर [[ENCOUNTER_ID|ER20240521001]]

रोगी के संबंधी [[RELATIVE_NAME|राम प्रसाद मुर्मू]]
फोन [[PHONE_NUMBER|9431023456]]
चिकित्सक [[DOCTOR_NAME|डॉ. संजय कुमार]]

प्राथमिक जांच / गंभीरता: रोगी सचेत, सतर्क और मौखिक निर्देशों पर प्रतिक्रिया दे रही है। GCS …
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `lab_report` (`kn`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['instruction_drift', 'surrogate_plausibility_collapse']`
- **Reasoning:** STUDENT_ID on 55yo; meta PHI note + empty psych lab content; minor English abbr in Kannada prose
- **Preview:**

```
ಲ್ಯಾಬ್ ವರದಿ — ಜಿಲ್ಲಾ ಆಸ್ಪತ್ರೆ ರಾಮನಗರ MRN [[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Lakshmi Bai]] [[AGE|55]] [[GENDER|Female]] [[HOSPITAL_NAME|District Hospital Ramanagara]] [[DISTRICT|Ramanagara]] [[PHONE_NUMBER|+91-9876543210]] [[PATIENT_ID|P-2024-0815-001]] [[STUDENT_ID|S-2024-0815-001]] [[DOCTOR_NAME|Dr. Rajesh Kumar]] ಅವರಿಂದ ಆದೇಶಿಸಲಾಗಿದೆ
ಫಲಿತಾಂಶಗಳ ಕೋಷ್ಟಕ (ಅನಾಲೆ ಮೌಲ್ಯಗಳನ್ನು PHI ಘಟಕಗಳಾಗಿ ಟ್ಯಾಗ್ ಮಾಡಲಾಗಿಲ್ಲ)
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `opd_slip` (`ks`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose written in Urdu (not Kashmiri) despite Arabic script and expected ks language; all entity types allowed and persona fit otherwise.
- **Preview:**

```
آؤٹ پیشنٹ ڈیپارٹمنٹ سلپ | [[HOSPITAL_NAME|District Hospital Shupiyan]] | آئی ڈی [[HOSPITAL_ID|DH-SJ-01]]
مریض: [[PATIENT_NAME|Zarifa Bibi]] | تاریخ پیدائش [[DOB|1992-08-15]] | عمر: [[AGE|32]] | صنف: [[GENDER|Female]]
پیشہ: [[OCCUPATION|Senior Officials of Political Party Organisations, Other]] | میڈیکل ریکارڈ نمبر: [[MRN|OPD-2024-0815-001]] | ڈاکٹر: [[DOCTOR_NAME|Dr. Ayesha Khan]]
رشتہ دار: [[RELATIVE_NAME|Mohammad Yousuf]] | فون: [[PHONE_NUMBER|9419012345]]
رجسٹرار ایمپلائی آئی ڈی: [[EMPLOYEE_…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `prescription` (`ks`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Kashmiri Arabic script not used.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Zarifa Bibi]], [[AGE|32]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Ayesha Khan]]
Phone: [[PHONE_NUMBER|9419023456]]
Address: [[RESIDENTIAL_ADDRESS|Village Chrar, Post Shupiyan, District Shupiyan]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Patient ID: [[PATIENT_ID|PID-7890]]
District: [[DISTRICT|Shupiyan]]

Diagnosis: Acute Gastroenteritis

Rx:
1. ORS solution - 1 litre, sip as needed
2. Zinc tablets…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `referral_letter` (`mai`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** 18yo male persona described as retired housewife (गृहणी); clear contradiction despite mostly correct Maithili prose and valid entity tags.
- **Preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Primary Health Centre, Purnia]] सँ [[DOCTOR_NAME|Dr. Alok Kumar]]
विषय: [[PATIENT_NAME|Ram Prasad]], [[AGE|18]] / [[GENDER|Male]], जिला [[DISTRICT|Purnia]]
कारण: निरंतर खाँसी आ वजन कम होनाय।

रोगी [[PATIENT_NAME|Ram Prasad]], 18 वर्षक पुरुष, [[DISTRICT|Purnia]] सँ छथि, जे दू सप्ताहसँ उत्पादक खाँसी, हल्का बुखार आ वजनमे भारी कमीक शिकायत कऽ रहल छथि। ओ एकटा सेवानिवृत्त गृहणी छथि जिनका प्राथमिक शिक्षा अछि आ ओ एकटा ग्रामीण क्षेत्रमे रहैत छथि। हुनकर …
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `opd_slip` (`ml`).
- **Score / verdict:** `0.7` / `fail`
- **Flags:** `['instruction_drift']`
- **Reasoning:** District value Kollam mismatches persona Thrissur; prose/script and entity types otherwise compliant.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|മാതാ ആശുപത്രി]] | ID [[HOSPITAL_ID|DH-KL-01]]
രോഗി: [[PATIENT_NAME|അനിത ശർമ്മ]] | DOB [[DOB|1998-05-22]] | പ്രായം: [[AGE|26]] | ലിംഗം: [[GENDER|Female]]
തൊഴിൽ: [[OCCUPATION|അധ്യാപിക]] | MRN: [[MRN|OPD-2024-0815-001]] | ഡോക്ടർ: [[DOCTOR_NAME|ഡോ. രാജേഷ് കുമാർ]]
ബന്ധു: [[RELATIVE_NAME|പ്രവീൺ ശർമ്മ]] | ഫോൺ: [[PHONE_NUMBER|9876543210]]
രജിസ്ട്രാർ EmpID: [[EMPLOYEE_ID|EMP-8821]] | ജില്ല: [[DISTRICT|കൊല്ലം]]
പ്രധാന പരാതി: 3 ദിവസമായി വലതുവശത്തെ അടിവയറ്റിൽ വേദനയോടു കൂടിയ വീക്ക…
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `prescription` (`ml`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** District mismatch (Thrissur persona vs Ernakulam/Kochi in text); all other prose, script, and entity types adhere.
- **Preview:**

```
പ്രസ്ക്രിപ്ഷൻ — [[HOSPITAL_NAME|മാതാ ആശുപത്രി]]
രോഗി [[PATIENT_NAME|അന്ന മേരി]], [[AGE|26]] / [[GENDER|Female]], MRN [[MRN|GH-TR-2024-0087]]
ഡോ. [[DOCTOR_NAME|ഡോ. തോമസ് ഫിലിപ്പ്]]
ഫോൺ: [[PHONE_NUMBER|9876543210]]
[[PATIENT_ID|PID-TR-2024-0087]]
[[ABHA_ID|12-3456-7890-1234]]
[[RESIDENTIAL_ADDRESS|അന്ന മേരി, നാലുകവല, കൊച്ചി]]
[[DISTRICT|എറണാകുളം]]

പ്രധാന പരാതി:
രോഗിക്ക് 5 ദിവസമായി പനി, ശരീരവേദന, തലവേദന എന്നിവയുണ്ട്. അവർക്ക് 100.4°F കുറഞ്ഞ പനിയും, ശരീരത്തിലാകെ പേശിവേദനയും, ഉണങ്ങിയ ചുമയുമുണ്ട്. അവ…
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `opd_slip` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Manipuri/Meitei script for narrative.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|District Hospital Bishnupur]] | ID [[HOSPITAL_ID|DH-MN-001]]
Patient: [[PATIENT_NAME|Thokchom Sanjita Devi]] | DOB [[DOB|1991-08-22]] | Age: [[AGE|33]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Homemaker]] | MRN: [[MRN|OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. L. Renu Sharma]]
Relative: [[RELATIVE_NAME|Thokchom Sanjoy Singh]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-BHR-045]] | District: [[DISTRICT|Bishnupur]]
Chief comp…
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `phc_register` (`mni`).
- **Score / verdict:** `0.1` / `fail`
- **Flags:** `['length_violation', 'instruction_drift', 'surrogate_plausibility_collapse']`
- **Reasoning:** Massive tag repetition creates >>400-char dump with no Manipuri prose or maternal content; generation collapse evident.
- **Preview:**

```
[[PATIENT_NAME|ꯂꯥꯂꯤꯇꯥ ꯗꯦꯕꯤ]] [[AGE|꯳꯳]] [[GENDER|Female]] [[VILLAGE|ꯂꯥꯝꯂꯥꯏ]] [[DISTRICT|ꯕꯤꯁ꯭ꯅꯨꯄꯨꯔ]] [[HOSPITAL_NAME|Primary Health Centre, Bishnupur]] [[PHONE_NUMBER|9436512345]] [[ASHA_WORKER_NAME|Rani Devi]] [[BPL_RATION_CARD|BPL-MN-2021-0045]] [[VOTER_ID|MN20240012345]] [[ABHA_ID|12-3456-7890-1234]]
[[PATIENT_NAME|ꯂꯥꯂꯤꯇꯥ ꯗꯦꯕꯤ]] [[AGE|꯳꯳]] [[GENDER|Female]] [[VILLAGE|ꯂꯥꯝꯂꯥꯏ]] [[DISTRICT|ꯕꯤꯁ꯭ꯅꯨꯄꯨꯔ]] [[HOSPITAL_NAME|Primary Health Centre, Bishnupur]]
[[PATIENT_NAME|ꯂꯥꯂꯤꯇꯥ ꯗꯦꯕꯤ]] [[AGE|꯳꯳]] [[GE…
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `insurance_claim` (`or`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** All narrative prose in English; expected Odia script for clinical content per instructions.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Sushila Devi]] [[AGE|20]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Puri District Hospital]] District [[DISTRICT|Puri]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|OD12AB1234]] (exactly once).
PAN [[PAN_NUMBER|FGHIJ5678K]] IFSC [[IFSC_CODE|SBIN0005678]] account [[BANK_ACCOUNT_NUMBER|6030020000001234]]
Bank Routing [[BANK_ROUTING_NUMBER|SBIN0005678]] Credit Card [[CREDIT_CARD_NU…
```

### S5 judge fail 16

- **What:** linguistic judge **fail** on `radiology_report` (`pa`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** Male-coded name (Jaswant Singh) + female gender tag; district Amritsar vs expected Rupnagar; minor domain fit issue for psych+radiology
- **Preview:**

```
ਇਮੇਜਿੰਗ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਹਸਪਤਾਲ]] [[DISTRICT|ਅੰਮ੍ਰਿਤਸਰ]] | [[PATIENT_NAME|ਜਸਵੰਤ ਸਿੰਘ]] [[AGE|73]] [[GENDER|ਮਹਿਲਾ]]
MRN [[MRN|MRN-2024-0815-001]] [[ENCOUNTER_ID|ENC-55601]] | ਰਿਪੋਰਟ ਕੀਤੀ ਗਈ [[DOCTOR_NAME|ਡਾ. ਗੁਰਮੀਤ ਸਿੰਘ]] ਦੁਆਰਾ
ਫੋਨ [[PHONE_NUMBER|+91-9876543210]] | [[HOSPITAL_ID|DH-RGN-001]] | [[ABHA_ID|ABHA-1234-5678-9012]]
ਖੋਜਾਂ: ਖੋਪੜੀ ਦਾ ਸਧਾਰਨ ਰੇਡੀਓਗ੍ਰਾਫ ਕੋਈ ਗੰਭੀਰ ਇੰਟਰਾਕਰੇਨੀਅਲ ਹੈਮਰੇਜ, ਮਾਸ ਇਫੈਕਟ, ਜਾਂ ਖੋਪੜੀ ਦੇ ਫ੍ਰੈਕਚਰ ਨੂੰ ਨਹੀਂ ਦਰਸਾਉਂਦਾ। ਪੈਰਾਨਾਸਲ ਸਾਈਨਸ ਸਾਫ਼ ਹਨ। ਹੱਡੀਆਂ ਦੀਆਂ …
```

### S5 judge fail 17

- **What:** linguistic judge **fail** on `er_triage_notes` (`pa`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['surrogate_plausibility_collapse']`
- **Reasoning:** Female persona with repeated masculine verb forms (ਰਿਹਾ ਹੈ) in Punjabi prose; minor English label mixing but narrative script mostly compliant and entities allowed.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਹਸਪਤਾਲ]] Encounter [[ENCOUNTER_ID|ENC-2024-1123]]
[[PATIENT_NAME|ਗੁਰਮੀਤ ਕੌਰ]] [[AGE|73]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|PB10AB1234]] (exactly once).
Relative [[RELATIVE_NAME|ਬਲਵਿੰਦਰ ਸਿੰਘ]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|ਡਾ. ਰਮਨ ਸ਼ਰਮਾ]]
Vitals / acuity: ਮਰੀਜ਼ ਸੁਚੇਤ ਹੈ ਪਰ ਥਕਾਵਟ ਮਹਿਸੂਸ ਕਰ ਰਿਹਾ ਹੈ। BP 150/90 mmHg, HR 98 bpm, RR 20/min, SpO2 96% on room a…
```

### S5 judge fail 18

- **What:** linguistic judge **fail** on `asha_worker_note` (`sa`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Hindi terms with Sanskrit; expected pure Sanskrit clinical narrative in Devanagari.
- **Preview:**

```
ASHA टिप्पणी — ग्राम [[VILLAGE|Shivpur]], जनपद [[DISTRICT|Kanpur Nagar]]
लाभार्थी [[PATIENT_NAME|Abdul Rahim]], [[AGE|19]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Yadav]] | दूरभाष [[PHONE_NUMBER|9876512340]]
भ्रमण निष्कर्ष: रोगी त्रिसप्ताहं यावत् निरन्तरं कासं तथा अल्पज्वरं सूचयति। सः श्रान्तः अनुभवति तथा च अद्यतनकाले प्रायः द्विकिलोपरिमाणं भारं नष्टवान्। तस्य पिता [[RELATIVE_NAME|Mohammed Yusuf]], चिन्तितः अस्ति तथा च भ्रमणार्थं सह आगच्छति। रोगी [[BPL_RATION_CARD|BPL-UP-208001-4421]]…
```

### S5 judge fail 19

- **What:** linguistic judge **fail** on `phc_register` (`sa`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** Prose is Hindi (Devanagari) not Sanskrit; language mismatch with expected sa script.
- **Preview:**

```
प्राथमिक स्वास्थ्य केंद्र रजिस्टर प्रविष्टि — [[HOSPITAL_NAME|PHC Kanpur Nagar Urban]] ग्राम [[VILLAGE|Gandhi Nagar]] जिला [[DISTRICT|Kanpur Nagar]]
[[PATIENT_NAME|Abdul Rahim]] [[AGE|19]] [[GENDER|Male]] | तीव्र अपेंडिसाइटिस

मुख्य शिकायत:
रोगी के पास नाभि के चारों ओर दर्द का 2 दिन का इतिहास है जो दाहिने निचले चतुर्थांश में स्थानांतरित हो गया है, साथ ही मतली और हल्का बुखार है।

परीक्षण:
पेट नरम है जिसमें दाहिने इलियक फोसा में कोमलता और गार्डिंग है। रिबाउंड कोमलता मौजूद है। आंतों की ध्वनियाँ कम…
```

### S5 judge fail 20

- **What:** linguistic judge **fail** on `referral_letter` (`sat`).
- **Score / verdict:** `0.15` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Santali Ol Chiki narrative absent.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Dumka]] / [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Re: [[PATIENT_NAME|Meena Devi]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Dumka]]
Reason: Acute appendicitis with peritonitis

Patient Meena Devi, a 32-year-old female telemarketing sales person, presented with a 24-hour history of right lower quadrant abdominal pain, associated with fever and vomiting. On examination, she was tachycardic with a rigid abdomen and guardi…
```

### S5 judge fail 21

- **What:** linguistic judge **fail** on `radiology_report` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose fully English; expected Santali Ol Chiki script.
- **Preview:**

```
Imaging report — District Hospital Dumka | [[PATIENT_NAME|Meena Devi]] [[AGE|32]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Priya Singh]]
Findings: Plain radiograph of the chest PA view demonstrates clear lung fields bilaterally with no evidence of acute consolidation, effusion, or pneumothorax. The cardiac silhouette is within normal limits. Bony structures including the ribs, clavicles, and thoracic vertebrae are un…
```

### S5 judge fail 22

- **What:** linguistic judge **fail** on `er_triage_notes` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** Prose is English with scattered Santali words in Latin script; expected full Santali narrative in Ol Chiki.
- **Preview:**

```
ER triage — District Hospital Dumka Encounter [[ENCOUNTER_ID|ENC-2024-0815-004]]
[[PATIENT_NAME|Meena Devi]] [[AGE|32]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Ambulance vehicle [[VEHICLE_REGISTRATION|JH07C-1234]] (exactly once) te ayo.
Relative [[RELATIVE_NAME|Ramesh Devi]] Phone [[PHONE_NUMBER|9431023456]] Dr [[DOCTOR_NAME|Dr. Sunita Murmu]]
Vitals / acuity: GCS 15, BP 140/90, HR 110, RR 22, SpO2 98% room air re, Temp 37.8°C. Patient alert, oriented, menkhan anxious ne…
```

### S5 judge fail 23

- **What:** linguistic judge **fail** on `er_triage_notes` (`sd`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['length_violation', 'surrogate_plausibility_collapse']`
- **Reasoning:** Endless repetition of filler phrase creates >>400-char dump; clinical notes lack coherent Sindhi prose or psychiatric triage content despite correct script and allowed entity tags.
- **Preview:**

```
ای آر ٹریاج اور نرسنگ نوٹس
کلینیکل ڈومین: نفسیات / رویے کی صحت
زبان: سندھی (sd, عربی)

ER triage — [[HOSPITAL_NAME|ڊسٽرڪٽ اسپتال جمن نگر]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|جشوڏي بين مڪوانا]] [[AGE|46]] [[GENDER|مادھو]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ01AB1234]] ذريعي آئي
Relative [[RELATIVE_NAME|رميش ڀائي مڪوانا]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|ڊاڪٽر پراتڪ شاها]]

Vitals / acuity: مريضه تيز ت…
```

### S5 judge fail 24

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in Devanagari instead of required Sindhi Arabic script; all entity types allowed and persona fit otherwise ok.
- **Preview:**

```
--- session ---
मरीज़ [[PATIENT_NAME|Jashodaben Makvana]] [[AGE|46]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-GJ-2024-0815-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|jashodaben.makvana@email.com]] Hospital [[HOSPITAL_NAME|District Hospital Jamnagar]]
--- chat ---
मरीज़: डॉक्टर साहब, मूंखे गुज़रल ॿिनि ॾींहनि खां…
```

### S5 judge fail 25

- **What:** linguistic judge **fail** on `surgical_note` (`sd`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity', 'surrogate_plausibility_collapse']`
- **Reasoning:** Prose mixes Meitei/Devanagari/English intrusions into expected Sindhi Arabic script; medical narrative implausibly garbled.
- **Preview:**

```
آپريٽو نوٽ — [[HOSPITAL_NAME|Sardar Vallabhbhai Patel Medical College, Jamnagar]] داخلہ [[ADMISSION_NUMBER|ADM-2024-0815-001]] وارڊ [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Jashodaben Makvana]] [[AGE|46]] [[GENDER|Female]] سرجن [[DOCTOR_NAME|Dr. Rajesh Patel]]
طريقہ / مشاهدا: مريضہ 46 سالن جي گھريلو خاتون آهي، جيڪا جمن نگر، گجرات کان آئي آهي، جنهن کي حمل جو ॿيو مھينو پيچيده صورتحال پيش آئي. مريضہ کي سخت پيٽ جو سور ۽ ولائنل بلڊنگ جون شڪايتون آيون. معائنے دوران، مريضہ جو بلڊ پريشر گھٽ (hemodynamically u…
```

### S5 judge fail 26

- **What:** linguistic judge **fail** on `opd_slip` (`te`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift', 'domain_persona_mismatch']`
- **Reasoning:** Domain oncology/chronic care specified but content is lumbar disc disease; prose mostly Telugu with acceptable Latin terms.
- **Preview:**

```
OPD Slip | జిల్లా జనరల్ హాస్పిటల్, ఒంగోలు | ID [[HOSPITAL_ID|DGH-AP-001]]
రోగి: [[PATIENT_NAME|రవి కుమార్]] | పుట్టిన తేదీ [[DOB|1992-05-20]] | వయస్సు: [[AGE|32]] | లింగం: [[GENDER|పురుషుడు]]
వృత్తి: [[OCCUPATION|Puncher, Metal]] | MRN: [[MRN|OPD-2024-0815-001]] | డాక్టర్: [[DOCTOR_NAME|డాక్టర్ శ్రీనివాస్ రెడ్డి]]
సంబంధీకులు: [[RELATIVE_NAME|లక్ష్మి]] | ఫోన్: [[PHONE_NUMBER|9440123456]]
రిజిస్ట్రార్ EmpID: [[EMPLOYEE_ID|EMP-4412]] | జిల్లా: [[DISTRICT|ప్రకాశం]]
ప్రధాన ఫిర్యాదు: గత మూడు నెలలుగా …
```

### S5 judge fail 27

- **What:** linguistic judge **fail** on `hospital_billing` (`ur`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['instruction_drift', 'surrogate_plausibility_collapse', 'length_violation']`
- **Reasoning:** Extensive clinical narrative (SOAP-style) exceeds pure billing/invoice scope; Urdu-primary + Narayanan name in TN creates low plausibility; multi-paragraph length violates concise invoice expectation.
- **Preview:**

```
بل (انوائس) — [[HOSPITAL_NAME|Government Medical College Hospital]] | مریض [[PATIENT_NAME|Mohan Narayanan]] | MRN [[MRN|GMCH-2024-0815-001]]
پتہ ضلع [[DISTRICT|Salem]] پن کوڈ [[PIN_CODE|636007]]
ایمبولینس گاڑی [[VEHICLE_REGISTRATION|TN48-AB-1234]]
فون [[PHONE_NUMBER|9445012345]] | لینڈ لائن [[TELEPHONE_LANDLINE|0422-2541234]]
آدھار [[AADHAAR_NUMBER|234567890123]] | انشورنس [[INSURANCE_POLICY_NUMBER|POL-TN-2024-98765]]
ٹیکس آئی ڈی [[TAX_ID|29AAAPM1234C1ZV]]
تاریخ: 15 اگست 2024
مریض: جناب موہن نا…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `hospital_billing` (`as`).
- **Errors:** `['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:1']`
- **Preview:**

```
ইনভয়েচ — [[HOSPITAL_NAME|Dibrugarh Civil Hospital]] | রোগী [[PATIENT_NAME|Bikash Gogoi]] | MRN [[MRN|MRN-2024-0815-001]]
ঠিকনা জেলা [[DISTRICT|Dibrugarh]] পিন [[PIN_CODE|786001]]
অ্যাম্বুলেন্স যানবাহন [[VEHICLE_REGISTRATION|AS-01-AB-1234]] (ঠিক একবার)।

ভর্তির তারিখ: 15 আগস্ট 2024
ছাড়পত্রের তারিখ: 18 আগস্ট 2024
সময়কাল: 3 দিন

রোগীর বিবরণ:
নাম: [[PATIENT_NAME|Bikash Gogoi]]
বয়স: [[AGE|49]]
লিঙ্গ: [[GENDER|Male]]
আধার নম্বর: [[AADHAAR_NUMBER|234567890123]]
ফোন নম্বর: [[PHONE_NUMBER|9876543210…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `surgical_note` (`bn`).
- **Errors:** `['missing_required:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER', 'upstream_generation_soft_fail:missing_required_entities:DOCTOR_NAME,HOSPITAL_NAME,ADMISSION_NUMBER,WARD_NUMBER,BED_NUMBER']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
অপারেটিভ নোট — ডিস্ট্রিক্ট হাসপাতাল বর্ধমান অ্যাডমিশন ADM-2024-1123 ওয়ার্ড B2
[[PATIENT_NAME|মিতা চ্যাটার্জি]] [[AGE|27]] [[GENDER|Female]] সার্জন ডক্টর সুব্রত রায়
পদ্ধতি / ফলাফল: রোগী অ্যাকিউট অ্যাপেন্ডিসাইটিস নিয়ে উপস্থিত হয়েছিলেন। অস্ত্রোপচার-পূর্ব মূল্যায়নে মৃদু রক্তাল্পতা এবং 28.5 বি.এম.আই পাওয়া গেছে। সাধারণ অ্যানেস্থেশিয়ার অধীনে অস্ত্রোপচারটি সম্পন্ন করা হয়েছে। একটি স্ট্যান্ডার্ড ম্যাকবার্নি ইনসিশন করা হয়েছিল। অ্যাপেন্ডিক্সটি ডগায় প্রদাহযুক্ত এবং ছিদ্রযুক্ত অবস্থায় পাওয়া গেছে।…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `radiology_report` (`mai`).
- **Errors:** `['missing_required:HOSPITAL_ID', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_ID']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
इमेजिंग रिपोर्ट — [[HOSPITAL_NAME|जिला अस्पताल पूर्णिया]] | [[PATIENT_NAME|रमेस कुमार]] [[AGE|18]] [[GENDER|पुरुष]]
MRN [[MRN|MRN-2024-PUN-001]] Encounter [[ENCOUNTER_ID|ENC-2024-PUN-001]] | रिपोर्ट कयल गेल डॉ [[DOCTOR_NAME|डॉक्टर संजय कुमार]] द्वारा
निष्कर्ष: बाम पाखुरीक सामान्य रेडियोग्राफ बाम पाखुरीक निचुलका टिबिया आ फिबुलाक निचुलका हिस्साक एकटा जटिल फ्रैक्चरक खुलासा करैत अछि जतय महत्वपूर्ण विस्थापन अछि। फ्रैक्चरक रेखा टखनाक जोड़ धरि फैलल अछि, जे एकटा जटिल इंट्रा-आर्टिकुलर चोटक संकेत दैत अछि…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `telemedicine_transcript` (`ne`).
- **Errors:** `['format:PHONE_NUMBER:phone_format']`
- **Preview:**

```
--- सत्र ---
बिरामी [[PATIENT_NAME|Anita Sharma]] [[AGE|21]] [[GENDER|Female]]
अपोइन्टमेन्ट [[APPOINTMENT_ID|APT-240521-01]] पोर्टल [[URL|https://tele.example.in/visit]]
क्लाइन्ट IP [[IP_ADDRESS|103.21.244.12]] डिभाइस IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] फोन [[PHONE_NUMBER|91876543210]]
इमेल [[EMAIL_ADDRESS|anita.sharma.dib@example.com]] अस्पताल [[HOSPITAL_NAME|Dibrugarh Civil Hospital]]
--- च्याट ---
बिरामी: नमस्ते डाक्टर, मलाई पछिल्लो दुई दिनदेखि दाहिने त…
```

### S6 auditor fail 5

- **What:** deterministic auditor **fail** on `insurance_claim` (`ur`).
- **Errors:** `['format:AADHAAR_NUMBER:aadhaar_verhoeff']`
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
مریض کی تفصیلات: [[PATIENT_NAME|Mohan Narayanan]] [[AGE|48]] [[GENDER|Male]] آدھار [[AADHAAR_NUMBER|609815659387]]
ہسپتال [[HOSPITAL_NAME|Salem Government Medical College Hospital]] ضلع [[DISTRICT|Salem]]
موٹر / RTA گاڑی [[VEHICLE_REGISTRATION|TN48AB1234]] (صرف ایک بار)۔
PAN [[PAN_NUMBER|AABPN1234C]] IFSC [[IFSC_CODE|SBIN0001234]] اکاؤنٹ [[BANK_ACCOUNT_NUMBER|50200012345678]]
بینک روٹنگ [[BANK_ROUTING_NUMBER|SBIN0001234]]
کریڈٹ کار…
```


## Surviving curated set

- languages: `{'as': 1, 'bn': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mni': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- doc_types: `{'automated_sms': 3, 'discharge_summary': 3, 'lab_report': 1, 'opd_slip': 1, 'phc_register': 2, 'prescription': 2, 'referral_letter': 2, 'surgical_note': 3, 'telemedicine_transcript': 3}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
