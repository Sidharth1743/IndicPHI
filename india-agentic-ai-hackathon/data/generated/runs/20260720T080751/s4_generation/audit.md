# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `12`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **20**
- soft_fail_count: **1**
- entity_coverage_incomplete_count: `1`
- entity_stuffing_count: `0`
- entity_coverage_complete_rate: `0.950`
- mean_chars: `1297.0`
- languages: `{'bn': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'ml': 2, 'mr': 2, 'pa': 2, 'ta': 2, 'te': 2}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 1, 'discharge_summary': 2, 'insurance_claim': 1, 'lab_report': 1, 'opd_slip': 5, 'phc_register': 2, 'prescription': 1, 'referral_letter': 2, 'surgical_note': 3, 'telemedicine_transcript': 1}`

## Soft failures (audited — not silent)

- `81ed007d28a447e3952a9359d6e9e528` · `opd_slip` · `ta` · reasons=['missing_required_entities:HOSPITAL_NAME']

## Preview

### bn · telemedicine_transcript · psychiatry_behavioral

```
--- session ---
Appt [[APPOINTMENT_ID|APT-240521-01]] Portal [[URL|https://tele.example.in/visit]]
Client IP [[IP_ADDRESS|103.21.244.12]] Device IMEI [[IMEI_NUMBER|356938035643809]]
MAC [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- chat ---
Patient [[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|sathi.mandal.wb@example.com]]): doctor, ami khub bhalo nei na. Ekhon theke ekta bhalo lagchhe na.
Dr [[DOCTOR_NAME|Dr. Aparna Roy]] ([[HOSPITAL_NAME|Howrah District Hospital]]): ami shunte pachchi Sathi. Ektu bolte paro ki bhabe bhalo lagchhe na?
Patient [[PATIENT_NAME|Sathi Mandal]]: amar mon ta khub kharap lagchhe. Raate ghum asche na. Shokale uthe dekhi shokale shokale shokale.
Dr [[DOCTOR_NAME|Dr. Aparna Roy]]: eta ki onek din dhore cholchhe? Kono oushod khachho ki?
Patient [[PATIENT_NAME|Sathi Mandal]]: haan, ekta doctor er kachhe oushod khachhilam, kintu ota kheye o bhalo lagchhe na. Ekhon ota bondho korechi.
Dr [[DOCTOR_NAME|Dr. Aparna Roy]]: bujhte parchhi. Eta ekta common problem. Ami tomake ekta notun oushod debo. Eta onek bhalo kaaj kore. Tumi ki ekta appointment korte paro?
Patient [[PATIENT_NAME|Sathi Mandal]]: haan, ami appointm
```

### bn · opd_slip · general_medicine

```
OPD Slip | [[HOSPITAL_NAME|North 24 Parganas District Hospital]] | ID [[HOSPITAL_ID|N24P-DH-001]]
Patient: [[PATIENT_NAME|Dulal Dolu]] | DOB [[DOB|1963-08-22]] | Age: [[AGE|61]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Bullock Cart Builder]] | MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Amitava Sen]]
District: [[DISTRICT|North Twenty Four Parganas]] | Chief complaint: Persistent cough and breathlessness for the past two weeks.
History of present illness: Patient reports a dry cough initially, which has become productive with white sputum over the last week. He also complains of mild shortness of breath on exertion, which is progressively worsening. He denies fever, chest pain, or hemoptysis. He attributes the symptoms to exposure to dust while working in his workshop.
Past medical history: No known chronic illnesses. No history of hypertension, diabetes, or tuberculosis.
Examination: General condition is average build, conscious and oriented. Vital signs: BP 130/80 mmHg, Pulse 92/min, Respiratory rate 20/min, Temperature 37.2°C, SpO2 94% on room air. Chest examination reveals decreased breath sounds in the right lower zone with occasional rhonchi.
Investiga
```

### en · referral_letter · oncology_chronic

```
Referral [[REFERRAL_ID|REF-2024-0912]] from [[HOSPITAL_NAME|Lilavati Hospital]] / [[DOCTOR_NAME|Dr. Priya Nair]]
Re: [[PATIENT_NAME|Anita Deshmukh]], [[AGE|32]] / [[GENDER|Female]], District [[DISTRICT|Mumbai Suburban]]
Reason: Persistent right-sided flank pain with hematuria and unexplained weight loss over the past six weeks, requiring oncological evaluation and imaging.

Patient is a 32-year-old female, married, working as an oil expeller in Mumbai. She reports a dull, constant ache in her right flank, radiating to the lower abdomen, which worsens at night. She has noticed intermittent pink-tinged urine for the last month and has lost approximately 4 kilograms without any change in diet or activity. She denies fever, chills, or nausea. Her past medical history is unremarkable. She has no known allergies.

On examination, she is alert and oriented, with a BMI of 21.5. Abdominal examination reveals tenderness in the right costovertebral angle. No palpable masses were detected. Vital signs are stable.

Initial investigations at our facility include a complete blood count, which shows mild normocytic anemia. A urine routine confirms microscopic hematuria. An ultrasound of the abdome
```
