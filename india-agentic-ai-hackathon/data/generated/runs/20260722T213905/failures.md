# Failures audit — `20260722T213905`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260722T213905/pipeline.resolved.yaml`
- **issue count:** **26** (hard=0, gen_soft=0, tr_soft=17, judge=9, auditor=0)
- **S4 entity_coverage_complete_rate:** `1.0`
- **S4b script_fail_count:** `0`
- **S5 pass_rate:** `0.8695652173913043`
- **S6 pass_rate / passed:** `1.0` / `60`
- **curated docs:** `58`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4b soft | `269a94e437d84643b728d5b86d5d08be` | `brx` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `269a94e437d84643b728d5b86d5d08be` | `brx` | `hospital_billing` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e6a759d47c084de984729dfaf40785e1` | `doi` | `hospital_billing` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e6a759d47c084de984729dfaf40785e1` | `doi` | `discharge_summary` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e6a759d47c084de984729dfaf40785e1` | `doi` | `referral_letter` | `tag_restore_or_translate_failed:None` |
| S4b soft | `1bd09fe5a4884629b02cbfd7660b402c` | `ks` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `1bd09fe5a4884629b02cbfd7660b402c` | `ks` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `1bd09fe5a4884629b02cbfd7660b402c` | `ks` | `insurance_claim` | `tag_restore_or_translate_failed:None` |
| S4b soft | `2f97625028784d7ab66673d76e697478` | `mni` | `phc_register` | `tag_restore_or_translate_failed:None` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S4b soft | `b5204bb0fe954a2cb47f1c994a300872` | `sat` | `er_triage_notes` | `tag_restore_or_translate_failed:None` |
| S4b soft | `b5204bb0fe954a2cb47f1c994a300872` | `sat` | `telemedicine_transcript` | `tag_restore_or_translate_failed:None` |
| S4b soft | `b5204bb0fe954a2cb47f1c994a300872` | `sat` | `opd_slip` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e9ec69ab351340d49920d8203b96c015` | `sd` | `asha_worker_note` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e9ec69ab351340d49920d8203b96c015` | `sd` | `phc_register` | `tag_restore_or_translate_failed:None` |
| S4b soft | `e9ec69ab351340d49920d8203b96c015` | `sd` | `automated_sms` | `tag_restore_or_translate_failed:None` |
| S5 fail | `269a94e437d84643b728d5b86d5d08be` | `brx` | `automated_sms` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `269a94e437d84643b728d5b86d5d08be` | `brx` | `hospital_billing` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `2f97625028784d7ab66673d76e697478` | `mni` | `phc_register` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `b5204bb0fe954a2cb47f1c994a300872` | `sat` | `er_triage_notes` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `b5204bb0fe954a2cb47f1c994a300872` | `sat` | `opd_slip` | score=0.28 flags=['dialect_script_impurity', 'length_violation', 'domain_persona_mismatch'] |
| S5 fail | `e9ec69ab351340d49920d8203b96c015` | `sd` | `asha_worker_note` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `e9ec69ab351340d49920d8203b96c015` | `sd` | `phc_register` | score=0.55 flags=['dialect_script_impurity'] |
| S5 fail | `e9ec69ab351340d49920d8203b96c015` | `sd` | `automated_sms` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `6feb104df37242faae24a67c95682734` | `ur` | `asha_worker_note` | score=0.55 flags=['cross_language_entity_shift', 'surrogate_plausibility_collapse'] |

## Per-failure audit

### S4b translation soft-fail 1

- **What:** translation soft-fail on `automated_sms` (`brx`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Bina Boro]]: Your ANC checkup is on 15-Oct at [[HOSPITAL_NAME|Kokrajhar PHC]] with [[DOCTOR_NAME|Dr. Priyanka Das]]. [[APPOINTMENT_ID|APT-241015-01]]. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Bina Boro]]: Your ANC checkup is on 15-Oct at [[HOSPITAL_NAME|Kokrajhar PHC]] with [[DOCTOR_NAME|Dr. Priyanka Das]]. [[APPOINTMENT_ID|APT-241015-01]]. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `hospital_billing` (`brx`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Bina Boro]]: Your ANC checkup is on 15-Oct at [[HOSPITAL_NAME|Kokrajhar PHC]] with [[DOCTOR_NAME|Dr. Priyanka Das]]. [[APPOINTMENT_ID|APT-241015-01]]. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Bina Boro]]: Your ANC checkup is on 15-Oct at [[HOSPITAL_NAME|Kokrajhar PHC]] with [[DOCTOR_NAME|Dr. Priyanka Das]]. [[APPOINTMENT_ID|APT-241015-01]]. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `hospital_billing` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```
- **Translated preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `discharge_summary` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```
- **Translated preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `referral_letter` (`doi`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```
- **Translated preview:**

```
SUB-DISTRICT HOSPITAL REASI
BILLING INVOICE

Patient Details:
[[PATIENT_NAME|Ramesh Kumar]]
[[AGE|26]]
[[GENDER|Male]]
[[RESIDENTIAL_ADDRESS|Village Pouni, Tehsil Reasi, Jammu & Kashmir]]
[[PIN_CODE|182212]]
[[PHONE_NUMBER|9419876543]]
[[TELEPHONE_LANDLINE|01996-222345]]
[[EMAIL_ADDRESS|ramesh.kumar.pj@example.com]]
[[AADHAAR_NUMBER|241587690123]]
[[PAN_NUMBER|JKPPR1234C]]
[[VEHICLE_REGISTRATION|…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `asha_worker_note` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `automated_sms` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `insurance_claim` (`ks`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Pulwama]], District [[DISTRICT|Pulwama]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|20]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Aisha Begum]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with anxiety symptoms and sleep disturbances. Reports feeling isolated and expresses concerns about future prospects. Family history significant …
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `phc_register` (`mni`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Dimapur Urban]], District [[DISTRICT|Dimapur]]
Beneficiary [[PATIENT_NAME|Lhingneichong Marak]], [[AGE|52]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Imli A. Sangtam]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased blood pressure readings at home. Complains of mild headaches and occasional dizziness. Blood pressure measured at 150/95…
```
- **Translated preview:**

```
ꯑꯥꯁꯥ ꯅꯣꯠ — ꯈꯨꯡꯒꯪ [[VILLAGE|Dimapur Urban]], ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|Dimapur]]
ꯕꯦꯅꯤꯐꯤꯁꯤꯌꯔꯤ [[PATIENT_NAME|Lhingneichong Marak]], [[AGE|52]] / [[GENDER|Female]]
ꯑꯥꯁꯥ: [[ASHA_WORKER_NAME|Imli A. Sangtam]] | ꯐꯣꯟ [[PHONE_NUMBER|9876543210]]
ꯐꯥꯏꯟꯗꯤꯡꯁꯤꯡ ꯌꯦꯡꯕꯤꯌꯨ: ꯄꯦꯁꯦꯟꯠꯅ ꯌꯨꯃꯗ ꯕ꯭ꯂꯗ ꯄ꯭ꯔꯦꯁꯔ ꯔꯤꯗꯤꯡ ꯍꯦꯟꯒꯠꯂꯛꯄꯒꯤ ꯔꯤꯄꯣꯔꯠ ꯄꯤꯈꯤ꯫ ꯈꯔ ꯀꯥꯡꯈꯠꯄ ꯑꯃꯁꯨꯡ ꯃꯔꯛ-ꯃꯔꯛꯇ ꯂꯥꯏꯅ ꯂꯥꯎꯕꯒꯤ ꯋꯥꯀꯠꯄ ꯄꯤꯈꯤ꯫ ꯕ꯭ꯂꯗ ꯄ꯭ꯔꯦꯁꯔ ꯑꯁꯤ 150/95 mmHg ꯗ ꯆꯦꯟꯈꯤ꯫ ꯑꯦꯟꯇꯤꯍ…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `asha_worker_note` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Shivpur]], District [[DISTRICT|Kanpur Nagar]]
Beneficiary [[PATIENT_NAME|Rohan Sharma]], [[AGE|19]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Yadav]] | Phone [[PHONE_NUMBER|9876512340]]
Visit findings: Patient presents with persistent fatigue and unexplained weight loss over past 3 weeks. Reports increased anxiety and difficulty concentrating on studies. Fami…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Shivpur]], District [[DISTRICT|Kanpur Nagar]]
Beneficiary [[PATIENT_NAME|Rohan Sharma]], [[AGE|19]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Yadav]] | Phone [[PHONE_NUMBER|9876512340]]
Visit findings: Patient presents with persistent fatigue and unexplained weight loss over past 3 weeks. Reports increased anxiety and difficulty concentrating on studies. Fami…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `automated_sms` (`sa`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Shivpur]], District [[DISTRICT|Kanpur Nagar]]
Beneficiary [[PATIENT_NAME|Rohan Sharma]], [[AGE|19]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Yadav]] | Phone [[PHONE_NUMBER|9876512340]]
Visit findings: Patient presents with persistent fatigue and unexplained weight loss over past 3 weeks. Reports increased anxiety and difficulty concentrating on studies. Fami…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Shivpur]], District [[DISTRICT|Kanpur Nagar]]
Beneficiary [[PATIENT_NAME|Rohan Sharma]], [[AGE|19]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Yadav]] | Phone [[PHONE_NUMBER|9876512340]]
Visit findings: Patient presents with persistent fatigue and unexplained weight loss over past 3 weeks. Reports increased anxiety and difficulty concentrating on studies. Fami…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `er_triage_notes` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```
- **Translated preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `telemedicine_transcript` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```
- **Translated preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `opd_slip` (`sat`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```
- **Translated preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. …
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `asha_worker_note` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `phc_register` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `automated_sms` (`sd`).
- **Error:** `tag_restore_or_translate_failed:None`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemoth…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `automated_sms` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Nepali/Hindi phrasing and grammar in Devanagari, not Bodo; all tags and IDs valid, persona/domain fit ok.
- **Preview:**

```
[[PATIENT_NAME|Bina Boro]]: नोंनि ANC चेकअप १५ अक्टोबरमा [[HOSPITAL_NAME|Kokrajhar PHC]] मा [[DOCTOR_NAME|Dr. Priyanka Das]] सँग छ। [[APPOINTMENT_ID|APT-241015-01]]। MRN [[MRN|MRN-2024-0815-001]]। पुष्टि गर्नका लागि [[PHONE_NUMBER|9876543210]] मा फोन गर्नुहोस्।
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `hospital_billing` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose and billing narrative written in Hindi instead of required Bodo (Devanagari); all other elements (persona fit, entity tags, plausibility) acceptable.
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|Kokrajhar Civil Hospital]] जिला [[DISTRICT|Kokrajhar]]
पिन [[PIN_CODE|783370]] मरीज [[PATIENT_NAME|Jolmil Boro]] MRN [[MRN|MRN-AS-2024-0815]]
पता [[RESIDENTIAL_ADDRESS|B.T. Road, Near Bodo Sahitya Sabha, Kokrajhar Town, Assam]] फोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|jolmil.boro@example.com]] पैन [[PAN_NUMBER|ABCDE1234F]]
लैंडलाइन [[TELEPHONE_LANDLINE|0364-2225678]] वाहन [[VEHICLE_REGISTRATION|AS-01-AB-1234]] (एक बार)
आधार [[AADHAAR_NUMBER|206501253007]] पॉलि…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `phc_register` (`mni`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Manipuri/Meitei script. All entity types allowed, persona/domain fit, no other violations.
- **Preview:**

```
PHC register — [[HOSPITAL_NAME|Dimapur PHC]] Village [[VILLAGE|Dimapur Colony]] District [[DISTRICT|Dimapur]]
[[PATIENT_NAME|Thokchom Ongbi Ibocha Devi]] [[AGE|52]] [[GENDER|Female]] | Chronic cough with fever
Patient is a 52-year-old female homemaker from Dimapur Colony, Dimapur, Nagaland. She presents with a history of productive cough for the past three weeks, associated with evening low-grade fever and significant weight loss of approximately 5 kg. She also reports loss of appetite and gene…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `er_triage_notes` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Santali Ol Chiki narrative absent.
- **Preview:**

```
ER triage — District Hospital Mayurbhanj Encounter [[ENCOUNTER_ID|ENC-2024-0512-001]]
[[HOSPITAL_NAME|District Hospital Mayurbhanj]] [[PATIENT_NAME|Bansidhar Ekka]] [[AGE|19]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|OD10A123456]]
Relative [[RELATIVE_NAME|Sushila Ekka]] Phone [[PHONE_NUMBER|9438765432]] Dr [[DOCTOR_NAME|Dr. Ramesh Kumar]]
Vitals / acuity: BP 120/80, HR 92, RR 18, Temp 98.4°F, SpO2 98% on room air. Patient …
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `opd_slip` (`sat`).
- **Score / verdict:** `0.28` / `fail`
- **Flags:** `['dialect_script_impurity', 'length_violation', 'domain_persona_mismatch']`
- **Reasoning:** Prose is English/Latin with sparse transliterated Santali words instead of Ol Chiki; OPD slip is multi-paragraph chart-length; 19yo male labeled homemaker mismatches persona.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Mayurbhanj District Hospital]] | ID [[HOSPITAL_ID|MDH-2024-01]]
Patient: [[PATIENT_NAME|Bansidhar Ekka]] | DOB [[DOB|2005-08-15]] | Age: [[AGE|19]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Homemaker]] | MRN: [[MRN|MDH-MRN-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Rina Soren]]
Attendant: [[RELATIVE_NAME|Sona Ekka]] | Phone: [[PHONE_NUMBER|9437891234]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-4501]] | District: [[DISTRICT|Mayurbhanj]]
Chief complaint: Tin hapta dh…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `asha_worker_note` (`sd`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose entirely in English Latin script instead of required Sindhi Arabic; all tags allowed and persona/domain otherwise plausible.
- **Preview:**

```
ASHA note — Village [[VILLAGE|Ghatkopar]], District [[DISTRICT|Mumbai Suburban]]
Beneficiary [[PATIENT_NAME|Dhaneshwar Patil]], [[AGE|18]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sunita Deshmukh]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent fatigue and mild abdominal discomfort. Blood work shows slight elevation in white blood cell count. Adherence to chemotherapy regimen is good. Family expresses concern about nutritional status.

[[RELATIVE_NAME|Ramesh Pa…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `phc_register` (`sd`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Sindhi Arabic-script prose contains repeated Devanagari intrusions (ॿ, मशवरो) and Latin fragments inside narrative, violating expected script purity despite valid tags.
- **Preview:**

```
پرائمري هيلٿ سينٽر ريڪارڊ — [[HOSPITAL_NAME|PHC Ghatkopar]] ڳوٺ [[VILLAGE|Ghatkopar Gaothan]] ضلعو [[DISTRICT|Mumbai Suburban]]
[[PATIENT_NAME|Ramesh Kumar]] [[AGE|18]] [[GENDER|Male]] | چِتا ۽ ننڊ نہ اچڻ

مريضو ॿن هفتن کان چِتا، چِڙچِڙاپڻي ۽ ننڊ نہ اچڻ جي شڪايتن سان آيو آهي. ॿڌائيندو آهي ته ڊپ محسوس ٿي سگهي ٿو ۽ پيشورانہ تربيت جي ڪلاسن ۾ ڌيان لڳائڻ ۾ تڪليف ٿي رهي آهي. هو 18 ساله، اڪلوتو، بے روزگار مرد [[VILLAGE|Ghatkopar Gaothan]]، [[DISTRICT|Mumbai Suburban]] ۾ رهندو آهي. ॿڌائيندو آهي ته خاند…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `automated_sms` (`sd`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Gurmukhi intrusion ('ਮਸ਼ورੀ') in otherwise Sindhi Arabic prose; not mostly wrong but violates script purity.
- **Preview:**

```
محترم [[PATIENT_NAME|Rohit Patil]], [[APPOINTMENT_ID|APT-240521-01]] [[DOCTOR_NAME|Dr. Mehta]] سان [[HOSPITAL_NAME|Sion Hospital]] تي 21-May تي صبح جو 10:30 جنرل ميڊيسن جي صلاح ਮਸ਼وري لاء آھي. مھرباني ڪري پنھنجو MRN [[MRN|MRN-2024-0815-001]] آڻيو. [[PHONE_NUMBER|9876543210]] تي تصديق ڪريو.
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `asha_worker_note` (`ur`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['cross_language_entity_shift', 'surrogate_plausibility_collapse']`
- **Reasoning:** Patient name Latin + South-Indian cultural mismatch for Bihar/Urdu persona; other prose/tags/domain fit ok.
- **Preview:**

```
آشا ورکر نوٹ — گاؤں [[VILLAGE|گلشن آباد]]، [[DISTRICT|Kishanganj]]
مریض [[PATIENT_NAME|Venkatesh Naidu]]، [[AGE|28]] / [[GENDER|Male]]
آشا: [[ASHA_WORKER_NAME|فاطمہ]] | فون [[PHONE_NUMBER|9876543210]]
معائنے کے نتائج: مریض نے تین ہفتوں سے مسلسل کھانسی اور ہلکے بخار کی شکایت کی۔
وہ کبھی کبھار رات کو پسینہ آنے اور وزن میں کمی کی اطلاع دیتا ہے۔
بلڈ پریشر 130/85 mmHg تھا۔
[[RELATIVE_NAME|عائشہ]]
[[BPL_RATION_CARD|BPL-BR-2024-001234]]
[[VOTER_ID|BR7890123456]]
[[RELIGION|اسلام]]
```


## Surviving curated set

- languages: `{'as': 3, 'bn': 3, 'brx': 1, 'doi': 3, 'en': 3, 'gu': 3, 'hi': 3, 'kn': 3, 'kok': 3, 'ks': 3, 'mai': 3, 'ml': 3, 'mni': 2, 'mr': 3, 'ne': 3, 'or': 2, 'pa': 3, 'sa': 3, 'ta': 3, 'te': 3, 'ur': 2}`
- doc_types: `{'asha_worker_note': 5, 'automated_sms': 8, 'discharge_summary': 3, 'er_triage_notes': 6, 'hospital_billing': 5, 'insurance_claim': 4, 'lab_report': 2, 'opd_slip': 3, 'phc_register': 3, 'prescription': 5, 'radiology_report': 5, 'referral_letter': 4, 'surgical_note': 2, 'telemedicine_transcript': 3}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
