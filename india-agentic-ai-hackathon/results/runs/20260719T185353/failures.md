# Failures audit — `20260719T185353`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T185353/pipeline.resolved.yaml`
- **issue count:** **4** (hard=0, gen_soft=1, tr_soft=1, judge=1, auditor=1)
- **S4 entity_coverage_complete_rate:** `0.9`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.9`
- **S6 pass_rate / passed:** `0.8888888888888888` / `8`
- **curated docs:** `8`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `7568f8e67bea4c959a480fd295d29db7` | `en` | `telemedicine_transcript` | `['missing_required_entities:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME']` |
| S4b soft | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S5 fail | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `er_triage_notes` | score=0.55 flags=['dialect_script_impurity'] |
| S6 fail | `7568f8e67bea4c959a480fd295d29db7` | `en` | `telemedicine_transcript` | `['missing_required:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME', 'upstream_generation_so…` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `telemedicine_transcript` (`en`).
- **Missing required tags:** `['AGE', 'GENDER']`
- **Stuffing flags:** `['DOCTOR_NAME', 'PATIENT_NAME']`
- **Raw reasons:** `['missing_required_entities:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Anita Deshmukh]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|anita.deshmukh@email.com]]): Good morning doctor. I'm Anita Deshmukh, I have my appointment today. I've been feeling very low and anxious for the past few weeks. I find it hard to concentrate at work and I'm not sleeping well.
Dr [[DOCTOR_NAME|Dr. Priya Nair]] ([[HOSPITAL_NAME|Si…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `er_triage_notes` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|Shri Krishna Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Rameshbhai Patel]] [[AGE|23]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|GJ-01-AB-9876]] (exactly once).
Relative [[RELATIVE_NAME|Savitaben Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Vikram Shah]]…
```
- **Translated preview:**

```
ER triage — [[HOSPITAL_NAME|Shri Krishna Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Rameshbhai Patel]] [[AGE|23]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ-01-AB-9876]] thi aavya.
Relative [[RELATIVE_NAME|Savitaben Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Vikram Shah]]
Vitals / acuity…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `er_triage_notes` (`gu`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is Romanized English-Gujarati mix instead of required Gujarati script; all other rubric dimensions (persona, entities, length, domain) pass.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Shri Krishna Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Rameshbhai Patel]] [[AGE|23]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ-01-AB-9876]] thi aavya.
Relative [[RELATIVE_NAME|Savitaben Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Vikram Shah]]
Vitals / acuity: Patient 3 divas thi productive cough, low-grade fever, ane night sweats sathe aavya chhe. Respirat…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `telemedicine_transcript` (`en`).
- **Errors:** `['missing_required:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME', 'upstream_generation_soft_fail:missing_required_entities:AGE,GENDER;entity_stuffing:DOCTOR_NAME,PATIENT_NAME']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** tag dump / over-repetition of entity TYPEs.
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Anita Deshmukh]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|anita.deshmukh@email.com]]): Good morning doctor. I'm Anita Deshmukh, I have my appointment today. I've been feeling very low and anxious for the past few weeks. I find it hard to …
```


## Surviving curated set

- languages: `{'bn': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 3, 'radiology_report': 3}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
