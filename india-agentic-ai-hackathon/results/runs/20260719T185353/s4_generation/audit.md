# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- soft_fail_count: **1**
- entity_coverage_incomplete_count: `1`
- entity_stuffing_count: `1`
- entity_coverage_complete_rate: `0.900`
- mean_chars: `719.2`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 3, 'er_triage_notes': 1, 'radiology_report': 3, 'telemedicine_transcript': 1}`

## Soft failures (audited — not silent)

- `7568f8e67bea4c959a480fd295d29db7` · `telemedicine_transcript` · `en` · reasons=['missing_required_entities:AGE,GENDER', 'entity_stuffing:DOCTOR_NAME,PATIENT_NAME']

## Preview

### bn · asha_worker_note · tb_ncd

```
ASHA note — Village [[VILLAGE|Bally]], District [[DISTRICT|Haora]]
Beneficiary [[PATIENT_NAME|Anjali Das]], [[AGE|23]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Rita Chatterjee]] | Phone [[PHONE_NUMBER|9832145678]]
Visit findings: Patient reports persistent cough for three weeks and night sweats. She was advised to get a sputum test at the Haora District Hospital. Her husband [[RELATIVE_NAME|Sanjay Das]] will accompany her for the test.
[[BPL_RATION_CARD|BPL-WB-208001-5589]]
[[VOTER_ID|WB012345678]]
[[RELIGION|Hindu]]
```

### en · telemedicine_transcript · psychiatry_behavioral

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Anita Deshmukh]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|anita.deshmukh@email.com]]): Good morning doctor. I'm Anita Deshmukh, I have my appointment today. I've been feeling very low and anxious for the past few weeks. I find it hard to concentrate at work and I'm not sleeping well.
Dr [[DOCTOR_NAME|Dr. Priya Nair]] ([[HOSPITAL_NAME|Sion Hospital]]): Good morning Anita. I'm sorry to hear you're feeling this way. Can you tell me more about what's been on your mind? How long have these feelings been present?
Patient [[PATIENT_NAME|Anita Deshmukh]]: It's been about three weeks now. The anxiety is worst in the mornings before I go to the oil expeller. My mind just races with negative thoughts. I feel a heaviness in my chest and my hands sometimes shake. I'm 32 years old.
Dr [[DOCTOR_NAME|Dr. Priya Nair]]: Thank you for sharing that, Anita. It sounds very distressing. Based on what you've described, it sounds like you may be expe
```

### gu · er_triage_notes · tb_ncd

```
ER triage — [[HOSPITAL_NAME|Shri Krishna Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Rameshbhai Patel]] [[AGE|23]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|05]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|GJ-01-AB-9876]] (exactly once).
Relative [[RELATIVE_NAME|Savitaben Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Vikram Shah]]
Vitals / acuity: Patient presents with productive cough for 3 days, low-grade fever, and night sweats. Respiratory rate 24/min, SpO2 91% on room air. Acuity: High. Immediate chest X-ray and sputum for AFB requested. Patient appears anxious and is cooperative. Initial assessment suggests possible pulmonary tuberculosis. Monitoring vitals every 15 minutes. Oxygen supplementation via nasal cannula started. IV access established with 18G cannula in left forearm. Blood samples sent for CBC, ESR, and liver function tests. Patient counseled on infection control measures. Family informed about the condition and isolation protocol.
```
