# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- mean_chars: `888.3`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 2, 'opd_slip': 2, 'prescription': 1, 'radiology_report': 1, 'referral_letter': 1, 'surgical_note': 1}`

## Preview

### bn · surgical_note · psychiatry_behavioral

```
Operative note — [[HOSPITAL_NAME|Haora District Hospital]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-001]] Ward [[WARD_NUMBER|B2]]
[[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] Surgeon [[DOCTOR_NAME|Dr. Aparna Bose]]
Procedure / findings: The patient presented with acute psychotic episode with self-harm behavior. Pre-operative assessment revealed severe anxiety and disorganized thought patterns. Under general anesthesia, patient underwent electroconvulsive therapy (ECT) with bilateral electrode placement. Procedure completed in 15 minutes with successful seizure induction observed. Post-operative recovery was uneventful with vital signs stable. Patient transferred to post-anesthesia care unit for observation. Follow-up ECT sessions scheduled twice weekly for total of six treatments. Family counseled on treatment plan and potential side effects.
```

### en · radiology_report · tb_ncd

```
Imaging report — [[HOSPITAL_NAME|Sir J.J. Group of Hospitals]] | [[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Findings: Chest radiograph performed on 15 August 2024 demonstrates a right upper lobe cavitary lesion measuring approximately 2.5 cm with surrounding consolidation. No pleural effusion or pneumothorax identified. The heart size is normal, and the bony thorax is intact. Impression: Findings are suggestive of active pulmonary tuberculosis. Recommendation: Correlate clinically and consider sputum analysis for AFB. The study was interpreted by [[DOCTOR_NAME|Dr. Rohan Deshmukh]].
```

### gu · opd_slip · psychiatry_behavioral

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Multispecialty Hospital]]
Patient: [[PATIENT_NAME|Rameshbhai Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Shah]]
District: [[DISTRICT|Ahmedabad]] | Chief complaint: Persistent feelings of sadness and loss of interest in daily activities for the past two months.

History of Present Illness:
The patient, a 23-year-old male, presents with a two-month history of low mood, anhedonia, and decreased energy. He reports difficulty sleeping, waking up early in the morning, and a poor appetite with a 5 kg weight loss. He feels worthless and has difficulty concentrating on tasks. There are no reported psychotic symptoms. The patient denies any suicidal ideation or self-harm.

Past Psychiatric History:
No previous psychiatric diagnoses or treatments.

Personal History:
The patient is a 23-year-old male, currently married, and retired. He is illiterate and lives in an urban area of Ahmedabad. He speaks Gujarati as his first language. He has a history of attending local cultural events and enjoys street-food cuisine. He has no reported substance use.

Family History:
Father is alive an
```
