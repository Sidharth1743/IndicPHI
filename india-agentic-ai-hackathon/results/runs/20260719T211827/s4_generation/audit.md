# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `12`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **20**
- soft_fail_count: **0**
- entity_coverage_incomplete_count: `0`
- entity_stuffing_count: `0`
- entity_coverage_complete_rate: `1.000`
- mean_chars: `1165.2`
- languages: `{'bn': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'ml': 2, 'mr': 2, 'pa': 2, 'ta': 2, 'te': 2}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 1, 'discharge_summary': 2, 'er_triage_notes': 2, 'insurance_claim': 2, 'lab_report': 1, 'phc_register': 2, 'prescription': 2, 'radiology_report': 2, 'surgical_note': 1, 'telemedicine_transcript': 3}`

## Preview

### bn · lab_report · surgical

```
Lab report — [[HOSPITAL_NAME|Haora Medical College and Hospital]] MRN [[MRN|MRN-2024-0815-001]]
[[PATIENT_NAME|Sathi Mandal]] [[AGE|23]] [[GENDER|Female]] Ordered by [[DOCTOR_NAME|Dr. Aparna Ghosh]]
Patient resides in [[DISTRICT|Haora]], West Bengal. Contact at [[PHONE_NUMBER|9876543210]].
Patient ID: [[PATIENT_ID|PID-WB-2024-0815-001]].
Student ID: [[STUDENT_ID|STU-WB-2024-0815-001]].

--------------------------------------------------------------------------------
LABORATORY FINDINGS
--------------------------------------------------------------------------------
Test Name                                 Result      Reference Range
--------------------------------------------------------------------------------
Complete Blood Count (CBC)
  Hemoglobin                                11.2 g/dL   12.0 - 15.5 g/dL
  White Blood Cell Count                    6,500/uL    4,500 - 11,000/uL
  Platelet Count                            2,50,000/uL 1,50,000 - 4,50,000/uL
--------------------------------------------------------------------------------
Biochemistry
  Total Bilirubin                           0.8 mg/dL    0.3 - 1.0 mg/dL
  Direct Bilirubin                          0.3 mg/dL    
```

### bn · prescription · surgical

```
Prescription — [[HOSPITAL_NAME|North 24 Parganas District Hospital]]
Patient [[PATIENT_NAME|Dulal Dolu]], [[AGE|61]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Subrata Chatterjee]]
Phone: [[PHONE_NUMBER|9830054321]]
Address: [[RESIDENTIAL_ADDRESS|Village: Shibpur, Post: Madhyamgram, PIN: 743432]]
District: [[DISTRICT|North Twenty Four Parganas]]
Patient ID: [[PATIENT_ID|PID-WB-N24P-001]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
Rx: Tablet Cefixime 400mg one tablet twice daily for 7 days.
Tablet Paracetamol 500mg one tablet four times daily as needed for pain.
Apply antiseptic solution on the wound twice daily.
Return for suture removal in 10 days.
Follow up with Dr. Chatterjee at the OPD.
```

### en · er_triage_notes · general_medicine

```
ER triage — [[HOSPITAL_NAME|Lilavati Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|MH01AB1234]]
Relative [[RELATIVE_NAME|Vikram Patil]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Sameer Deshmukh]]
Vitals / acuity: Patient conscious, oriented, vitals stable. Complaining of severe headache and dizziness for the past 2 hours. No fever. Blood pressure 140/90 mmHg. Pulse 98 bpm. Respiratory rate 18/min. SpO2 98% on room air.

Nursing Notes:
Patient is a 32-year-old female oil expeller from Mumbai Suburban, Maharashtra, currently married, with middle education. She speaks English and Marathi. She reports a sudden onset of throbbing headache, described as 8/10 in intensity, associated with nausea but no vomiting. Denies any visual changes, neck stiffness, or weakness in limbs. No history of similar episodes. Patient appears anxious and is repeatedly checking her pulse. She has a known history of hypertension, diagnosed 6 months ago. She reports compliance with her medications, which she keeps in her purse. No know
```
