# Failures audit — `20260720T140451`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260720T140451/pipeline.resolved.yaml`
- **issue count:** **6** (hard=0, gen_soft=2, tr_soft=1, judge=2, auditor=1)
- **S4 entity_coverage_complete_rate:** `0.8`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.8`
- **S6 pass_rate / passed:** `0.875` / `7`
- **curated docs:** `7`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `e7e83d4610764345b6bfc1814beba784` | `mr` | `radiology_report` | `['missing_required_entities:DOCTOR_NAME']` |
| S4 soft | `f6d9e443342646fdb70285e45d2a3a48` | `te` | `automated_sms` | `['missing_required_entities:DOCTOR_NAME']` |
| S4b soft | `6549c3143bf44b4d81915ab4b5eea4ef` | `gu` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.032<0.35 attempt=1` |
| S5 fail | `6549c3143bf44b4d81915ab4b5eea4ef` | `gu` | `er_triage_notes` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `f6d9e443342646fdb70285e45d2a3a48` | `te` | `automated_sms` | score=0.6 flags=['cross_language_entity_shift'] |
| S6 fail | `e7e83d4610764345b6bfc1814beba784` | `mr` | `radiology_report` | `['missing_required:DOCTOR_NAME', 'upstream_generation_soft_fail:missing_required_entities:DOCTOR_NA…` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `radiology_report` (`mr`).
- **Missing required tags:** `['DOCTOR_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DOCTOR_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
इमेजिंग अहवाल — [[HOSPITAL_NAME|District Hospital Ahmadnagar]] | [[PATIENT_NAME|Rajaram Agand]] [[AGE|31]] [[GENDER|Male]]
एमआरएन [[MRN|MRN-2024-0915-001]] एन्काउंटर [[ENCOUNTER_ID|ENC-2024-0915-001]] | निष्कर्ष: रुग्णावर केलेल्या चेस्ट एक्स-रे मध्ये द्विपक्षीय वरच्या लोबमध्ये इन्फिल्ट्रेट्ससह कॅव्हिटेशन दिसून येते, जे सक्रिय फुफ्फुसीय क्षयरोगाशी सुसंगत आहे. प्लुरल इफ्यूजन नोंदवले गेले नाही. पृष्ठीय मणक्यामध्ये स्क्लेरोटिक जखमा दिसतात, जे पॉट्स आजाराचे सूचक आहेत. रुग्णाला क्षयरोगविरोधी उपचार सुरू करण्याचा सल्ला देण्यात आला. हा अहवाल डॉ. प्रकाश देशमुखांनी लिहून घेतला आहे. रुग्णाचा एबीएचए आयडी …
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `automated_sms` (`te`).
- **Missing required tags:** `['DOCTOR_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DOCTOR_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Chaitanya]]: మీ టిబి అపాయింట్‌మెంట్ [[APPOINTMENT_ID|APT-240521-01]] 21-మే నెల 10:30 గంటలకు డాక్టర్ శర్మతో [[HOSPITAL_NAME|PHC Visakhapatnam]] లో ఉంది. మీ MRN [[MRN|MRN-2024-0815-001]]. దయచేసి [[PHONE_NUMBER|9876512340]] లో నిర్ధారించండి.
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `er_triage_notes` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.032<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|District Hospital Vadodara]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Kavita Patel]] [[AGE|40]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]]
Relative [[RELATIVE_NAME|Rameshbhai Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Sunita Shah]]
Vitals / acuit…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|ગુજરાત મેડિકલ કોલેજ]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Kavita Patel]] [[AGE|40]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] દ્વારા આવ્યા
Relative [[RELATIVE_NAME|Rameshbhai Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Sunita Shah]]
Vitals / acuity: Pa…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `er_triage_notes` (`gu`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose body is English-dominant; only isolated Gujarati fragments present despite gu/Gujarati requirement.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|ગુજરાત મેડિકલ કોલેજ]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Kavita Patel]] [[AGE|40]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] દ્વારા આવ્યા
Relative [[RELATIVE_NAME|Rameshbhai Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Sunita Shah]]
Vitals / acuity: Patient conscious, alert, oriented. BP 140/90 mmHg, HR 100 bpm, RR 20/min, SpO2 98% on room air. Compl…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `automated_sms` (`te`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['cross_language_entity_shift']`
- **Reasoning:** PATIENT_NAME value in Latin script; prose otherwise Telugu but entity shift violates script expectation for document.
- **Preview:**

```
[[PATIENT_NAME|Chaitanya]]: మీ టిబి అపాయింట్‌మెంట్ [[APPOINTMENT_ID|APT-240521-01]] 21-మే నెల 10:30 గంటలకు డాక్టర్ శర్మతో [[HOSPITAL_NAME|PHC Visakhapatnam]] లో ఉంది. మీ MRN [[MRN|MRN-2024-0815-001]]. దయచేసి [[PHONE_NUMBER|9876512340]] లో నిర్ధారించండి.
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `radiology_report` (`mr`).
- **Errors:** `['missing_required:DOCTOR_NAME', 'upstream_generation_soft_fail:missing_required_entities:DOCTOR_NAME']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
इमेजिंग अहवाल — [[HOSPITAL_NAME|District Hospital Ahmadnagar]] | [[PATIENT_NAME|Rajaram Agand]] [[AGE|31]] [[GENDER|Male]]
एमआरएन [[MRN|MRN-2024-0915-001]] एन्काउंटर [[ENCOUNTER_ID|ENC-2024-0915-001]] | निष्कर्ष: रुग्णावर केलेल्या चेस्ट एक्स-रे मध्ये द्विपक्षीय वरच्या लोबमध्ये इन्फिल्ट्रेट्ससह कॅव्हिटेशन दिसून येते, जे सक्रिय फुफ्फुसीय क्षयरोगाशी सुसंगत आहे. प्लुरल इफ्यूजन नोंदवले गेले नाही. पृष्ठीय मणक्यामध्ये स्क्लेरोटिक जखमा दिसतात, जे पॉट्स आजाराचे सूचक आहेत. रुग्णाला क्षयरोगविरोधी उपचार सु…
```


## Surviving curated set

- languages: `{'bn': 1, 'en': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'pa': 1, 'ta': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 2, 'radiology_report': 2, 'telemedicine_transcript': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
