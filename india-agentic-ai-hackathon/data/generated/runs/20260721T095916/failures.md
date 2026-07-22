# Failures audit — `20260721T095916`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260721T095916/pipeline.resolved.yaml`
- **issue count:** **24** (hard=0, gen_soft=0, tr_soft=9, judge=11, auditor=4)
- **S4 entity_coverage_complete_rate:** `1.0`
- **S4b script_fail_count:** `9`
- **S5 pass_rate:** `0.8405797101449275`
- **S6 pass_rate / passed:** `0.9310344827586207` / `54`
- **curated docs:** `22`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4b soft | `a24958482d8b463ab3daeee28d5f5365` | `brx` | `automated_sms` | `script_purity_failed:wrong_indic_script:Bengali>Devanagari attempt=1;generator_repair_failed:wrong_…` |
| S4b soft | `217fa134e0d64da4962f287453b86c70` | `ks` | `prescription` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `217fa134e0d64da4962f287453b86c70` | `ks` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `217fa134e0d64da4962f287453b86c70` | `ks` | `asha_worker_note` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `telemedicine_transcript` | `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:wrong_i…` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `surgical_note` | `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:target_…` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `lab_report` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `7604eaf4ec554261b752518c0f8a656e` | `sat` | `referral_letter` | `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1` |
| S4b soft | `7604eaf4ec554261b752518c0f8a656e` | `sat` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S5 fail | `a24958482d8b463ab3daeee28d5f5365` | `brx` | `automated_sms` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `ecc5c42af9364fb79dfa7c3bc3b426f7` | `doi` | `telemedicine_transcript` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `ecc5c42af9364fb79dfa7c3bc3b426f7` | `doi` | `surgical_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `217fa134e0d64da4962f287453b86c70` | `ks` | `prescription` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `217fa134e0d64da4962f287453b86c70` | `ks` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity', 'invented_entity_type'] |
| S5 fail | `217fa134e0d64da4962f287453b86c70` | `ks` | `asha_worker_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `telemedicine_transcript` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `surgical_note` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `2308b919936944228c90a4864f352d14` | `pa` | `er_triage_notes` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `7604eaf4ec554261b752518c0f8a656e` | `sat` | `referral_letter` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `7604eaf4ec554261b752518c0f8a656e` | `sat` | `er_triage_notes` | score=0.2 flags=['dialect_script_impurity'] |
| S6 fail | `611b1570604d4b8b8d4b06736a0ea305` | `bn` | `referral_letter` | `['dics_below_threshold:0.5']` |
| S6 fail | `b244567803e34199a9bba1a5e6910e49` | `kok` | `insurance_claim` | `['format:PAN_NUMBER:pan_format', 'format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio…` |
| S6 fail | `c44c080bc5434b75800bf9f1d3a12729` | `mr` | `lab_report` | `['unknown_entity_types:DATE']` |
| S6 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `lab_report` | `['script_purity:target_script_ratio:0.000<0.35']` |

## Per-failure audit

### S4b translation soft-fail 1

- **What:** translation soft-fail on `automated_sms` (`brx`).
- **Error:** `script_purity_failed:wrong_indic_script:Bengali>Devanagari attempt=1;generator_repair_failed:wrong_indic_script:Bengali>Devanagari`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Bongaigaon]], District [[DISTRICT|Chirang]]
Beneficiary [[PATIENT_NAME|Ranjit Boro]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Jalina Boro]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presented with fever and body ache for two days. He reports mild cough and headache. No history of vomiting or diarrhea.

Chief complaint: Fever and body a…
```
- **Translated preview:**

```
एएसए नोट — गामि [[VILLAGE|Bongaigaon]], जिला [[DISTRICT|Chirang]]
लाभार्थी [[PATIENT_NAME|Ranjit Boro]], [[AGE|18]] / [[GENDER|Male]]
एएसए: [[ASHA_WORKER_NAME|Jalina Boro]] | फोन [[PHONE_NUMBER|9876543210]]
भेटको निष्कर्ष: रोगी 2 दिनसँ बुखार आ शरीरमे दर्दक संग आयल छथि। ओ हल्का खाँसी आ माथक दर्दक रिपोर्ट करैत छथि। वमन वा दस्त केर कोनो इतिहास नहि अछि।

मुख्य शिकायत: बुखार आ शरीरमे दर्द।
वर्तमान बीम…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `prescription` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `insurance_claim` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `asha_worker_note` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srina…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `telemedicine_transcript` (`mni`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Meitei`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```
- **Translated preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `surgical_note` (`mni`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Meitei attempt=1;generator_repair_failed:target_script_ratio:0.010<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```
- **Translated preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `lab_report` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```
- **Translated preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoub…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `referral_letter` (`sat`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-01]] from [[HOSPITAL_NAME|Mayurbhanj District Hospital]] / [[DOCTOR_NAME|Dr. S. K. Patra]]
Re: [[PATIENT_NAME|Bikash Murmu]], [[AGE|25]] / [[GENDER|Male]], District [[DISTRICT|Mayurbhanj]]
Reason: Patient presents with persistent cough, low-grade fever, and weight loss, requiring further evaluation for suspected pulmonary tuberculosis and assessment of comorbid non…
```
- **Translated preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-01]] [[HOSPITAL_NAME|Mayurbhanj District Hospital]] / [[DOCTOR_NAME|Dr. S. K. Patra]]
विषय: [[PATIENT_NAME|Bikash Murmu]], [[AGE|25]] / [[GENDER|Male]], जिला [[DISTRICT|Mayurbhanj]]
कारण: रोगी को लगातार खांसी, हल्का बुखार और वजन कम होने की समस्या है, जिसके लिए संदिग्ध फेफड़ों के तपेदिक (पल्मोनरी ट्यूबरकुलोसिस) के आगे के मूल्यांकन और सह-रुग्ण गैर-संचारी रोगों के आकलन क…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `er_triage_notes` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-01]] from [[HOSPITAL_NAME|Mayurbhanj District Hospital]] / [[DOCTOR_NAME|Dr. S. K. Patra]]
Re: [[PATIENT_NAME|Bikash Murmu]], [[AGE|25]] / [[GENDER|Male]], District [[DISTRICT|Mayurbhanj]]
Reason: Patient presents with persistent cough, low-grade fever, and weight loss, requiring further evaluation for suspected pulmonary tuberculosis and assessment of comorbid non…
```
- **Translated preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-01]] [[HOSPITAL_NAME|Mayurbhanj District Hospital]] / [[DOCTOR_NAME|Dr. S. K. Patra]]
विषय: [[PATIENT_NAME|Bikash Murmu]], [[AGE|25]] / [[GENDER|Male]], जिला [[DISTRICT|Mayurbhanj]]
कारण: रोगी को लगातार खांसी, हल्का बुखार और वजन कम होने की समस्या है, जिसके लिए संदिग्ध फेफड़ों के तपेदिक (पल्मोनरी ट्यूबरकुलोसिस) के आगे के मूल्यांकन और सह-रुग्ण गैर-संचारी रोगों के आकलन क…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `automated_sms` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Assamese/Bengali script and phrasing instead of required Bodo Devanagari.
- **Preview:**

```
[[PATIENT_NAME|Ranjan Boro]]: 21-May 14:00-ত [[HOSPITAL_NAME|Chirang District Hospital]]-ত [[DOCTOR_NAME|Dr. Anjali Sharma]]-ৰ সৈতে [[APPOINTMENT_ID|APT-240521-02]] এপইণ্টমেণ্ট আছে। [[PHONE_NUMBER|9876543210]]-ত নিশ্চিত কৰক। MRN [[MRN|MRN-2024-0815-002]]।
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`doi`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose in standard Hindi; expected Dogri language in Devanagari.
- **Preview:**

```
--- सत्र ---
मरीज [[PATIENT_NAME|Shanti Devi]] [[AGE|20]] [[GENDER|Female]]
अपॉइंटमेंट [[APPOINTMENT_ID|APT-240521-01]] पोर्टल [[URL|https://tele.example.in/visit]]
क्लाइंट IP [[IP_ADDRESS|103.21.244.12]] डिवाइस IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] फोन [[PHONE_NUMBER|9419123456]]
ईमेल [[EMAIL_ADDRESS|shanti.devi.reasi@example.com]] अस्पताल [[HOSPITAL_NAME|Sub-District Hospital Reasi]]
--- चैट ---
मरीज: नमस्ते डॉक्टर साहब, मैं [[PATIENT_NAME|Shanti Devi]] री…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `surgical_note` (`doi`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is standard Hindi; Dogri (Devanagari) required. All tags allowed, persona/domain fit, length ok.
- **Preview:**

```
[[PATIENT_NAME|Ritu Devi]] [[AGE|20]] [[GENDER|Female]] [[DOCTOR_NAME|Dr. Anjali Sharma]] [[HOSPITAL_NAME|Sub-District Hospital Reasi]] [[ADMISSION_NUMBER|ADM-2024-0915]] [[WARD_NUMBER|OT]] [[BED_NUMBER|05]] [[MRN|MRN-2024-0915-004]] [[RELATIVE_NAME|Sanjay Kumar]] [[PATIENT_ID|PID-99876]]
ऑपरेशन नोट
प्रक्रिया / निष्कर्ष: मरीज़ 10 हफ़्तों की गर्भधारण के दौरान पूर्ण गर्भपात के साथ आई, जिसमें भारी योनि रक्तस्राव और ऐंठन थी। जांच पर, वह हेमोडायनामिक रूप से अस्थिर थी, जिसकी नाड़ी 110 bpm और रक्तचाप …
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `prescription` (`ks`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English/Latin script; expected Kashmiri (Arabic script). All entity types allowed, persona/domain fit, no length or surrogate issues.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|SKIMS Soura]]
Patient [[PATIENT_NAME|Ayesha Bano]], [[AGE|25]] / [[GENDER|Female]], MRN [[MRN|SKMS-2024-0158]]
Dr. [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Phone: [[PHONE_NUMBER|9419123456]]
Patient ID: [[PATIENT_ID|PID-2024-0158]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Address: [[RESIDENTIAL_ADDRESS|House No. 14, Nigeen Colony, Rajbagh, Srinagar]]
District: [[DISTRICT|Srinagar]]
Rx: Paclitaxel 175 mg/m² IV over 3 hours on Day 1, every 21 days for 6 cycles.
Doxorubicin 60 …
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `insurance_claim` (`ks`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'invented_entity_type']`
- **Reasoning:** Clinical prose entirely in English instead of required Kashmiri Arabic script; multiple non-allowlist TYPEs (CHIEF_COMPLAINT, HOSPITAL_COURSE, DISCHARGE_PLAN, TREATMENT_SUMMARY, ADMITTING_PHYSICIAN).
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-JK-2024-9876]]
[[PATIENT_NAME|Ayesha Bano]] [[AGE|25]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|238461786046]]
Hospital [[HOSPITAL_NAME|SMHS Hospital]] District [[DISTRICT|Srinagar]]
[[MRN|SMHS-2024-001234]]
Admitted on May 15, 2024 and discharged on May 20, 2024.
[[ADMITTING_PHYSICIAN|Dr. Farooq Ahmad]]
[[CHIEF_COMPLAINT|Patient presents with symptoms of major depressive disorder, including persistent low mood, anhedonia, and suicidal ideation…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `asha_worker_note` (`ks`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose entirely in English instead of required Kashmiri Arabic script; minor district mismatch but language is primary failure.
- **Preview:**

```
ASHA note — Village [[VILLAGE|کۆتھہ]], District [[DISTRICT|بڈگام]]
Beneficiary [[PATIENT_NAME|Ayesha Begum]], [[AGE|25]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Shabnam Bano]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough with fever for three days. She feels weakness and body ache. No known allergies. Mother [[RELATIVE_NAME|Zainab Begum]] accompanies her. BPL card [[BPL_RATION_CARD|BPL-JK-2024-001234]] is presented. Voter ID [[VOTER_ID|JK1234567]] ver…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical chat prose in English; expected Manipuri/Meitei script. All entity tags valid and Latin IDs allowed.
- **Preview:**

```
--- session ---
Patient [[PATIENT_NAME|Phanjom Chanu]] [[AGE|21]] [[GENDER|Female]]
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|phan.chanu@example.com]] Hospital [[HOSPITAL_NAME|Thoubal District Hospital]]
--- chat ---
Patient: Hello doctor, I am Phanjom Chanu from Thoubal. I have a…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `surgical_note` (`mni`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose uses Bengali script/language instead of required Meitei; all entity types valid, persona/clinical fit plausible, no length or invented-type issues.
- **Preview:**

```
অপারেশন নোট — [[HOSPITAL_NAME|Thoubal District Hospital]] অ্যাডমিশন [[ADMISSION_NUMBER|ADM-2024-1025]] ওয়ার্ড [[WARD_NUMBER|OT]]
[[PATIENT_NAME|Leima Devi]] [[AGE|21]] [[GENDER|Female]] সার্জন [[DOCTOR_NAME|Dr. Khuman Singh]]
পদ্ধতি / ফলাফল: রোগী হলেন 21 বছর বয়সী এক মহিলা, যিনি গ্রামীণ থৌবাল, মণিপুরের বাসিন্দা। তাঁর বাঁ হাতের কনুইয়ে কাঠের কাজ করার সময় একটি আঘাতজনিত ক্ষত (laceration) হয়েছে। প্রাথমিক পরীক্ষায় দেখা গেছে যে, ক্ষতটি 4 সেমি গভীর এবং অনিয়মিত, যেখানে মাঝারি রক্তপাত এবং কাঠের গুঁ…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `er_triage_notes` (`pa`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose is predominantly English with only scattered Gurmukhi insertions; expected full Punjabi (Gurmukhi) for this document language.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Sirsa Civil Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|Jaswinder Kaur]] [[AGE|39]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Ambulance vehicle [[VEHICLE_REGISTRATION|HR23AB5678]] ਰਾਹੀਂ ਆਏ।
Relative [[RELATIVE_NAME|Gurpreet Singh]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Vikram Chawla]]
Vitals / acuity: ਮਰੀਜ਼ alert and oriented x3 ਹੈ, severe right upper quadrant abdominal pain ਦੀ ਸ਼ਿਕਾਇਤ ਹੈ ਜੋ back ਤੱਕ ਜ…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `referral_letter` (`sat`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in Hindi/Devanagari; expected Santali Ol Chiki script for narrative.
- **Preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-01]] [[HOSPITAL_NAME|Mayurbhanj District Hospital]] / [[DOCTOR_NAME|Dr. S. K. Patra]] से
विषय: [[PATIENT_NAME|Bikash Murmu]], [[AGE|25]] / [[GENDER|Male]], [[DISTRICT|Mayurbhanj]] जिला

प्रिय सहयोगी,

हम [[PATIENT_NAME|Bikash Murmu]] को विशेष मूल्यांकन के लिए रेफर कर रहे हैं। रोगी 25 वर्षीय पुरुष है, जो संथाल समुदाय से है और मयूरभंज जिले के ग्रामीण क्षेत्र में रहता है। वह बाजार में दुकान लगाने वाला विक्रेता है और अपने काम से संबंधित अत्यधिक चिंता की रिपोर्ट करता है,…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `er_triage_notes` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English; expected Santali Ol Chiki narrative absent.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Mayurbhanj District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Soren Murmu]] [[AGE|25]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A1234567]]
Relative [[RELATIVE_NAME|Bikram Murmu]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. Ranjit Patnaik]]
Vitals / acuity: Patient conscious, alert, oriented x3. Vitals stable. Pain score 6/10. Awaiting surgical assessme…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `referral_letter` (`bn`).
- **Errors:** `['dics_below_threshold:0.5']`
- **Preview:**

```
রেফারেল [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Katihar Sadar Hospital]] / [[DOCTOR_NAME|Dr. Rajiv Kumar]] থেকে
বিষয়: [[PATIENT_NAME|Satyendra Kumar]], [[AGE|25]] / [[GENDER|Male]], জেলা [[DISTRICT|Katihar]]

প্রিয় সহকর্মী,

আমরা [[PATIENT_NAME|Satyendra Kumar]]-কে, যিনি [[VILLAGE|Shivpur]], [[DISTRICT|Katihar]]-এর বাসিন্দা, 25 বছর বয়সী একজন পুরুষ, পরবর্তী মূল্যায়ন এবং চিকিৎসার জন্য আপনার কাছে পাঠাচ্ছি। রোগীর তিন সপ্তাহ ধরে কাশি হচ্ছে, যা শুরুতে শুকনো ছিল এবং এখন সামান্য সাদা কফসহ হচ্…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `insurance_claim` (`kok`).
- **Errors:** `['format:PAN_NUMBER:pan_format', 'format:PAN_NUMBER:pan_format', 'script_purity:target_script_ratio:0.033<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GOA-2024-9876]]
[[PATIENT_NAME|मोहम्मद शेख]] [[AGE|30]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|987654321012]]
Hospital [[HOSPITAL_NAME|दक्षिण गोवा जिल्हा रुग्णालय]] District [[DISTRICT|दक्षिण गोवा]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GA01AB1234]] (exactly once).
PAN [[PAN_NUMBER|SHFM1234C]] IFSC [[IFSC_CODE|SBIN0000123]] account [[BANK_ACCOUNT_NUMBER|30912345678901]]
Credit Card [[CREDIT_CARD_NUMBER|5555555555554444]] CVV [[CVV|456]] PI…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `lab_report` (`mr`).
- **Errors:** `['unknown_entity_types:DATE']`
- **Preview:**

```
प्रयोगशाळा अहवाल — [[HOSPITAL_NAME|सांगली जिल्हा रुग्णालय]] जिल्हा [[DISTRICT|सांगली]]
एमआरएन [[MRN|MRN-MH-2024-0815]] पेशंट_आयडी [[PATIENT_ID|PID-MH-7781]]
[[PATIENT_NAME|सविता पाटील]] [[AGE|54]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
[[DOCTOR_NAME|डॉ. राजेश देशमुखांनी]] यांनी तपासणीसाठी आदेश दिले आहेत.

निकाल तक्ता (विश्लेषकांचे मूल्य पीआयआय म्हणून टॅग केलेले नाही)
पेशंटचे नाव: [[PATIENT_NAME|सविता पाटील]]
वय: [[AGE|54]] वर्षे
लिंग: [[GENDER|Female]]
रुग्णालयाचे नाव: [[HOSPITAL_NAM…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `lab_report` (`sa`).
- **Errors:** `['script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
LAB REPORT — DISTRICT HOSPITAL KANPUR KANPUR NAGAR
MRN [[MRN|MRN-UP-2024-0815]] PATIENT_ID [[PATIENT_ID|PID-UP-7781]]
PATIENT_NAME [[PATIENT_NAME|Rohan Sharma]] AGE [[AGE|19]] GENDER [[GENDER|Male]] PHONE_NUMBER [[PHONE_NUMBER|9876543210]]
ORDERED_BY [[DOCTOR_NAME|Dr. Anjali Verma]]

RESULTS SUMMARY (ANALYTE VALUES NOT MARKED AS PHI ENTITIES).

PATIENT INFORMATION
NAME: [[PATIENT_NAME|Rohan Sharma]]
AGE: [[AGE|19]]
GENDER: [[GENDER|Male]]
ADDRESS: 12 Gandhi Nagar, Ward 4, Kanpur Nagar, Uttar Pr…
```


## Surviving curated set

- languages: `{'as': 1, 'bn': 1, 'brx': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'mai': 1, 'ml': 1, 'mni': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sat': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 3, 'hospital_billing': 2, 'lab_report': 2, 'opd_slip': 2, 'prescription': 6, 'radiology_report': 3, 'referral_letter': 2, 'telemedicine_transcript': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
