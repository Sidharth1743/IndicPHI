# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- mean_chars: `1028.5`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 2, 'opd_slip': 2, 'prescription': 1, 'radiology_report': 1, 'referral_letter': 1, 'surgical_note': 1}`

## Preview

### bn · surgical_note · psychiatry_behavioral

```
Operative note — [[HOSPITAL_NAME|Haora District Hospital]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-001]] Ward [[WARD_NUMBER|B2]]
[[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] Surgeon [[DOCTOR_NAME|Dr. Anirban Chatterjee]]
Procedure / findings: The patient presented with a history of acute psychotic episode with agitation and disorganized behavior. The decision was made for Electroconvulsive Therapy (ECT) after failure of conservative management with antipsychotic medication. The patient was evaluated pre-operatively and deemed fit for general anesthesia. The procedure was performed under standard ECT protocol with bilateral electrode placement. The first session was administered on the day of admission. Post-procedure, the patient was observed in the recovery area for 30 minutes and then transferred back to the ward. The patient tolerated the procedure well without any immediate adverse events. The treatment plan is for a total of 12 sessions, administered thrice weekly. The patient's husband, [[RELATIVE_NAME|Ratan Mandal]], was present for counseling and consent. The patient's [[MRN|MRN-2024-0815-001]] and [[PATIENT_ID|PID-WB-2024-0815-001]] have been updated in the syst
```

### en · radiology_report · tb_ncd

```
Imaging report — [[HOSPITAL_NAME|Lilavati Hospital]] | [[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0915-008]] Encounter [[ENCOUNTER_ID|ENC-88765]] | Findings: Chest X-ray performed on the patient reveals bilateral upper lobe infiltrates with cavitary lesions, highly suggestive of active pulmonary tuberculosis. No pleural effusion noted. Sputum sample sent for AFB smear and culture.

[[DOCTOR_NAME|Dr. Priya Nair]]
[[DISTRICT|Mumbai Suburban]]
[[PHONE_NUMBER|9876543210]]
[[HOSPITAL_ID|HSP-MH-005]]
[[ABHA_ID|12-3456-7890-1234]]
```

### gu · opd_slip · psychiatry_behavioral

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient: [[PATIENT_NAME|Rameshbhai Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Anjali Shah]]
District: [[DISTRICT|Ahmadabad]] | Chief complaint: Anxiety and sleep disturbance for the past two months.

History of Present Illness:
Patient is a 23-year-old male, married, and currently not employed, who presents with complaints of excessive worry, restlessness, and difficulty falling asleep. He reports feeling tense most of the day and experiencing palpitations on several occasions. Symptoms started approximately two months ago following a family dispute. He denies any suicidal ideation or self-harm.

Past Medical History:
No known chronic illnesses. No history of surgeries.

Medications:
No regular medications.

Allergies:
No known drug allergies.

Family History:
Father is alive and well. Mother has hypertension. No known family history of psychiatric illness.

Social History:
Patient is married and lives with his spouse and parents in a joint family setup in urban Ahmedabad. He is a fluent Gujarati speaker with limited literacy. He is currently not engaged in any occ
```
