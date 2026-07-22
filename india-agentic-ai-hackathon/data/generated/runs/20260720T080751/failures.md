# Failures audit — `20260720T080751`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260720T080751/pipeline.resolved.yaml`
- **issue count:** **7** (hard=0, gen_soft=1, tr_soft=2, judge=2, auditor=2)
- **S4 entity_coverage_complete_rate:** `0.95`
- **S4b script_fail_count:** `2`
- **S5 pass_rate:** `0.9`
- **S6 pass_rate / passed:** `0.8888888888888888` / `16`
- **curated docs:** `10`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `81ed007d28a447e3952a9359d6e9e528` | `ta` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4b soft | `89d785f5c9f64f119b428efc6d0c259e` | `bn` | `telemedicine_transcript` | `script_purity_failed:target_script_ratio:0.136<0.35 attempt=1` |
| S4b soft | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `prescription` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S5 fail | `89d785f5c9f64f119b428efc6d0c259e` | `bn` | `telemedicine_transcript` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `prescription` | score=0.25 flags=['dialect_script_impurity', 'instruction_drift'] |
| S6 fail | `877a805cf7d24d64b693bbfb59bf4e58` | `kn` | `insurance_claim` | `['format:AADHAAR_NUMBER:aadhaar_verhoeff']` |
| S6 fail | `81ed007d28a447e3952a9359d6e9e528` | `ta` | `opd_slip` | `['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITA…` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `opd_slip` (`ta`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD சீட்டு | தோத்துகுகுடி மாவட்ட மருத்துவமனை | அடையாள எண் [[HOSPITAL_ID|DH-TN-027]]
நோயாளி: [[PATIENT_NAME|Lakshmi Devi]] | பிறந்த தேதி [[DOB|1986-08-22]] | வயது: [[AGE|38]] | பாலினம்: [[GENDER|Female]]
தொழில்: [[OCCUPATION|Slitting Machine Operator (Abrasive)]] | மருத்துவப் பதிவு எண்: [[MRN|OPD-2024-0815-002]] | மருத்துவர்: [[DOCTOR_NAME|Dr. K. Ananthan]]
மாவட்டம்: [[DISTRICT|Thoothukkudi]] | முதன்மைப் புகார்: கடந்த 3 வாரங்களாகத் தொடரும் இருமல் மற்றும் குறைந்த அளவிலான காய்ச்சல்.
தற்போதைய நோயின் வரலாறு: நோயாளிக்கு மஞ்சள் நிறச் சளியுடன் கூடிய இருமல், கடந்த மூன்று வாரங்களாக மாலை நேரங்களில் குறை…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `telemedicine_transcript` (`bn`).
- **Error:** `script_purity_failed:target_script_ratio:0.136<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|sathi.mandal.wb@example.com]]): doctor, ami khub bhal…
```
- **Translated preview:**

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|sathi.mandal.wb@example.com]]): ডাক্তার, আমি খুব ভালো…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `prescription` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient [[PATIENT_NAME|Karan Patel]], [[AGE|23]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0912-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Mehta]]
Rx: Isoniazid 300mg once daily, Rifampicin 600mg once daily, Pyrazinamide 1500mg once daily, Ethambutol 800mg once daily for 2 months. Then Isoniazid 300mg and Rifampicin 600mg once daily for 4 months. Take all…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient [[PATIENT_NAME|Karan Patel]], [[AGE|23]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0912-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Mehta]]
Rx: Isoniazid 300mg once daily, Rifampicin 600mg once daily, Pyrazinamide 1500mg once daily, Ethambutol 800mg once daily for 2 months. Then Isoniazid 300mg and Rifampicin 600mg once daily for 4 months. Take all…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`bn`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Chat prose mostly Romanized Latin script after opening lines; expected Bengali script for clinical narrative.
- **Preview:**

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|sathi.mandal.wb@example.com]]): ডাক্তার, আমি খুব ভালো নেই না। এখন থেকে একটা ভালো লাগছে না।
Dr [[DOCTOR_NAME|Dr. Aparna Roy]] ([[HOSPITAL_NAME|Howrah Dist…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `prescription` (`gu`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift']`
- **Reasoning:** All clinical prose in English; Gujarati script required for narrative.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient [[PATIENT_NAME|Karan Patel]], [[AGE|23]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0912-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Mehta]]
Rx: Isoniazid 300mg once daily, Rifampicin 600mg once daily, Pyrazinamide 1500mg once daily, Ethambutol 800mg once daily for 2 months. Then Isoniazid 300mg and Rifampicin 600mg once daily for 4 months. Take all medications on an empty stomach with water. Monitor for vision changes, jaundice, and numbness. Fol…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `insurance_claim` (`kn`).
- **Errors:** `['format:AADHAAR_NUMBER:aadhaar_verhoeff']`
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Ramesh Kumar]] [[AGE|46]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Shimoga District Hospital]] District [[DISTRICT|Shimoga]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KA05AB1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0005678]] account [[BANK_ACCOUNT_NUMBER|6050100123456789]]
Bank routing [[BANK_ROUTING_NUMBER|SBIN0005678]]
Credit card [[CREDIT_CAR…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `opd_slip` (`ta`).
- **Errors:** `['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
OPD சீட்டு | தோத்துகுகுடி மாவட்ட மருத்துவமனை | அடையாள எண் [[HOSPITAL_ID|DH-TN-027]]
நோயாளி: [[PATIENT_NAME|Lakshmi Devi]] | பிறந்த தேதி [[DOB|1986-08-22]] | வயது: [[AGE|38]] | பாலினம்: [[GENDER|Female]]
தொழில்: [[OCCUPATION|Slitting Machine Operator (Abrasive)]] | மருத்துவப் பதிவு எண்: [[MRN|OPD-2024-0815-002]] | மருத்துவர்: [[DOCTOR_NAME|Dr. K. Ananthan]]
மாவட்டம்: [[DISTRICT|Thoothukkudi]] | முதன்மைப் புகார்: கடந்த 3 வாரங்களாகத் தொடரும் இருமல் மற்றும் குறைந்த அளவிலான காய்ச்சல்.
தற்போதைய நோயின…
```


## Surviving curated set

- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 1, 'discharge_summary': 1, 'lab_report': 1, 'opd_slip': 4, 'phc_register': 1, 'referral_letter': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
