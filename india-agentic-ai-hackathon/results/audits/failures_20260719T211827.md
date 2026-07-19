# Failures audit — `20260719T211827`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T211827/pipeline.resolved.yaml`
- **issue count:** **6** (hard=0, gen_soft=0, tr_soft=1, judge=3, auditor=2)
- **S4 entity_coverage_complete_rate:** `1.0`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.85`
- **S6 pass_rate / passed:** `0.8823529411764706` / `15`
- **curated docs:** `9`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4b soft | `bfcd0a5ac1664137a563f86f8f72d85a` | `ml` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S5 fail | `bfcd0a5ac1664137a563f86f8f72d85a` | `ml` | `insurance_claim` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `648f69965d61431083f8e5566b64f74d` | `pa` | `telemedicine_transcript` | score=0.65 flags=['domain_persona_mismatch'] |
| S5 fail | `66f87f0087064abda3938f2c4aba879e` | `pa` | `telemedicine_transcript` | score=0.65 flags=['domain_persona_mismatch'] |
| S6 fail | `9a1021f9af894a73808c2e1c1dc870b0` | `ta` | `insurance_claim` | `['format:AADHAAR_NUMBER:aadhaar_verhoeff']` |
| S6 fail | `01fef5fa094b4e0e83a555263004aa08` | `te` | `radiology_report` | `['unknown_entity_types:STATE']` |

## Per-failure audit

### S4b translation soft-fail 1

- **What:** translation soft-fail on `insurance_claim` (`ml`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-KR-2024-9876]]
[[PATIENT_NAME|Lakshmi Nair]] [[AGE|64]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Alappuzha Medical College Hospital]] District [[DISTRICT|Alappuzha]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KL04A1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNP5678Q]] IFSC [[IFSC_CODE|KKBK0001234]] account [[…
```
- **Translated preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-KR-2024-9876]]
[[PATIENT_NAME|Lakshmi Nair]] [[AGE|64]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Alappuzha Medical College Hospital]] District [[DISTRICT|Alappuzha]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KL04A1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNP5678Q]] IFSC [[IFSC_CODE|KKBK0001234]] account [[…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `insurance_claim` (`ml`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All prose and labels in English; expected Malayalam script for narrative in ml TPA form.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-KR-2024-9876]]
[[PATIENT_NAME|Lakshmi Nair]] [[AGE|64]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Alappuzha Medical College Hospital]] District [[DISTRICT|Alappuzha]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KL04A1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNP5678Q]] IFSC [[IFSC_CODE|KKBK0001234]] account [[BANK_ACCOUNT_NUMBER|678901234567]]
Bank Routing Number [[BANK_ROUTING_NUMBER|KKBK0001234]] Credit Ca…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`pa`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** Female doctor (Harpreet Kaur) uses masculine verb forms ('ਸਮਝਦਾ ਹਾਂ') and is addressed as 'ਸਰ'; all other elements (Gurmukhi prose, entity types, TB symptoms, persona anchors) align.
- **Preview:**

```
--- ਸੈਸ਼ਨ ---
ਅਪੌਇੰਟਮੈਂਟ [[APPOINTMENT_ID|APT-2024-0915-001]] ਪੋਰਟਲ [[URL|https://tele.example.in/visit]]
ਕਲਾਇੰਟ IP [[IP_ADDRESS|103.21.244.12]] ਡਿਵਾਈਸ IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- ਚੈਟ ---
ਮਰੀਜ਼ [[PATIENT_NAME|Balwinder Singh]] [[AGE|25]] [[GENDER|Male]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|balwinder.singh@example.com]]): ਸਰ, ਮੈਨੂੰ ਪਿਛਲੇ ਦੋ ਹਫ਼ਤਿਆਂ ਤੋਂ ਖੰਘ ਹੋ ਰਹੀ ਹੈ। ਇਹ ਠੀਕ ਨਹੀਂ ਹੋ ਰਹੀ। ਮੈਨੂੰ ਬਹੁਤ ਥਕਾਵਟ ਮਹਿਸੂਸ ਹੁੰਦੀ ਹੈ ਅਤੇ ਮੇਰਾ ਕੁਝ ਭਾਰ …
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `telemedicine_transcript` (`pa`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** Female persona uses repeated masculine verb forms (ਰਿਹਾ, ਖੰਘਦਾ, ਕਰਦਾ) in Punjabi prose; all entity tags and script otherwise valid.
- **Preview:**

```
--- ਸੈਸ਼ਨ ---
ਅਪੌਇੰਟਮੈਂਟ [[APPOINTMENT_ID|APT-240521-01]] ਪੋਰਟਲ [[URL|https://tele.example.in/visit]]
ਕਲਾਇੰਟ IP [[IP_ADDRESS|103.21.244.12]] ਡਿਵਾਈਸ IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- ਚੈਟ ---
ਮਰੀਜ਼ [[PATIENT_NAME|Jaswinder Kaur]] [[AGE|55]] [[GENDER|Female]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|jaswinder.kaur@example.com]]): ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਡਾਕਟਰ ਸਾਹਿਬ, ਮੈਂ ਪਿਛਲੇ ਦੋ ਦਿਨਾਂ ਤੋਂ ਆਪਣੇ ਸੱਜੇ ਪਾਸੇ ਦਰਦ ਮਹਿਸੂਸ ਕਰ ਰਿਹਾ ਹਾਂ। ਇਹ ਤੇਜ਼ ਦਰਦ ਹੈ, ਅਤੇ ਜਦੋਂ ਮੈਂ ਖੰ…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `insurance_claim` (`ta`).
- **Errors:** `['format:AADHAAR_NUMBER:aadhaar_verhoeff']`
- **Preview:**

```
TPA கோரிக்கை — பாலிசி [[INSURANCE_POLICY_NUMBER|POL-TN-2024-4589]]
[[PATIENT_NAME|Lakshmi]] [[AGE|45]] [[GENDER|Female]] ஆதார் [[AADHAAR_NUMBER|234567890123]]
மருத்துவமனை [[HOSPITAL_NAME|Government Medical College Hospital Erode]] மாவட்டம் [[DISTRICT|Erode]]
மோட்டார் / RTA வாகனம் [[VEHICLE_REGISTRATION|TN01AB1234]]
PAN [[PAN_NUMBER|FGHIJ5678K]] IFSC [[IFSC_CODE|CITI0000123]] கணக்கு [[BANK_ACCOUNT_NUMBER|678901234567]]
வங்கி வழித்தடம் [[BANK_ROUTING_NUMBER|CITI0000123]]
கிரெடிட் கார்டு [[CREDIT_…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `radiology_report` (`te`).
- **Errors:** `['unknown_entity_types:STATE']`
- **Preview:**

```
ఇమేజింగ్ రిపోర్ట్ — జిల్లా ఆసుపత్రి నెల్లూరు | [[PATIENT_NAME|Ravi Kumar]] [[AGE|32]] [[GENDER|Male]]
MRN [[MRN|MRN-2024-0815-001]] ఎన్‌కౌంటర్ [[ENCOUNTER_ID|ENC-55601]] | ఫలితాలు: రోగికి ఎడమ చేతి ఎక్స్-రే తీయబడింది. ఎక్స్-రేలో ఎడమ ఐదవ మెటాకార్పల్ షాఫ్ట్ యొక్క స్థానభ్రంశం లేని పగులు స్పష్టంగా కనిపిస్తుంది. కీళ్లలో ఎటువంటి ప్రమేయం లేదా అమరిక లోపం ఉన్నట్లు ఆధారాలు లేవు. మిగిలిన కార్పల్ ఎముకలు, ఫాలాంజెస్‌ మరియు డిస్టల్ రేడియస్/అల్నా సాధారణంగా ఉన్నాయి. పగులు ఉన్న ప్రదేశానికి సమీపంలో మృదు కణజాల వాపు…
```


## Surviving curated set

- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 1, 'discharge_summary': 1, 'er_triage_notes': 1, 'lab_report': 1, 'prescription': 1, 'radiology_report': 1, 'telemedicine_transcript': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
