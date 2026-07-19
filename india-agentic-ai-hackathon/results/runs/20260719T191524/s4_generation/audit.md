# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `12`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **20**
- soft_fail_count: **2**
- entity_coverage_incomplete_count: `2`
- entity_stuffing_count: `0`
- entity_coverage_complete_rate: `0.900`
- mean_chars: `1368.9`
- languages: `{'bn': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'ml': 2, 'mr': 2, 'pa': 2, 'ta': 2, 'te': 2}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 1, 'discharge_summary': 2, 'insurance_claim': 1, 'lab_report': 2, 'opd_slip': 4, 'phc_register': 1, 'prescription': 2, 'radiology_report': 2, 'surgical_note': 4}`

## Soft failures (audited — not silent)

- `7568f8e67bea4c959a480fd295d29db7` · `discharge_summary` · `en` · reasons=['missing_required_entities:DOB']
- `396f437fcf6a45e6b7f38f4fe5cf5e48` · `opd_slip` · `gu` · reasons=['missing_required_entities:DOB,OCCUPATION,HOSPITAL_ID']

## Preview

### bn · opd_slip · maternal_health

```
OPD Slip | [[HOSPITAL_NAME|Haora District Hospital]]
Patient: [[PATIENT_NAME|Sathi Mandal]] | Age: [[AGE|23]] | Gender: [[GENDER|Female]]
MRN: [[MRN|OPD-2024-001]] | Doctor: [[DOCTOR_NAME|Dr. Ananya Chatterjee]]
District: [[DISTRICT|Haora]] | Chief complaint: Amenorrhea for 8 weeks, nausea, and mild lower abdominal discomfort.

History of Present Illness:
Sathi Mandal, a 23-year-old homemaker, presents with a history of secondary amenorrhea for the past two months. She reports associated symptoms of morning nausea and occasional vomiting. The patient also complains of a dull, aching pain in the lower abdomen, which she rates as 3/10 in severity. She denies any fever, chills, or vaginal bleeding apart from the amenorrhea. There is no history of dysuria or urinary frequency.

Obstetric History:
The patient is married and reports regular unprotected intercourse. Her last menstrual period was approximately 10 weeks ago. She denies any known prior pregnancies. She has not undergone any contraceptive procedures.

Past Medical History:
The patient has no known chronic illnesses such as hypertension, diabetes, or thyroid disorders. She has not had any major surgeries in the past. There is 
```

### bn · opd_slip · tb_ncd

```
OPD Slip | [[HOSPITAL_NAME|District Hospital North 24 Parganas]]
Patient: [[PATIENT_NAME|Dulal Dolu]] | Age: [[AGE|61]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Amitava Chatterjee]]
District: [[DISTRICT|North Twenty Four Parganas]] | Chief complaint: Persistent cough with hemoptysis for three weeks.
DOB: [[DOB|1963-05-22]] | Occupation: [[OCCUPATION|Bullock Cart Builder]]
Phone: [[PHONE_NUMBER|9433112244]] | Relative: [[RELATIVE_NAME|Smt. Rina Dolu]]
Employee ID: [[EMPLOYEE_ID|EMP-WB-0451]] | Hospital ID: [[HOSPITAL_ID|HSP-WB-N24-001]]

Examination:
General: Patient is conscious, oriented, and appears cachectic.
Respiratory: Bilateral crackles noted in the upper zones. No clubbing.
Chest X-ray: Suggestive of infiltrates in the right upper lobe.

Investigations:
Sputum for AFB: Positive (2+).
Mantoux test: 15mm induration.

Diagnosis:
Pulmonary Tuberculosis, Right Upper Lobe.

Treatment:
Started on Category I DOTS regimen.
Prescribed Isoniazid, Rifampicin, Pyrazinamide, and Ethambutol.
Counselled on treatment adherence and nutrition.

Follow-up:
Return in 1 month for review.
```

### en · discharge_summary · oncology_chronic

```
Discharge Summary — [[HOSPITAL_NAME|Lilavati Hospital]]
[[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-004]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Vikram Mehta]] | Course / advice: The patient is a 32-year-old female with a history of Stage III Triple-Negative Breast Cancer, admitted for management of chemotherapy-induced neutropenic sepsis. She has completed six cycles of adjuvant chemotherapy and was scheduled for the seventh cycle. On admission, she presented with fever, chills, and a neutrophil count of 0.2 x 10^9/L. Blood cultures grew E. coli, and she was started on IV Cefepime. Her fever resolved within 48 hours, and repeat blood cultures were negative. She has been afebrile for the last 72 hours and her neutrophil count has recovered to 1.5 x 10^9/L. She is being discharged on oral Ciprofloxacin and advised to continue her growth factor support. The patient and her husband have been counseled on infection prevention measures, including hand hygiene and avoiding crowded places. Her next oncology follow-up is scheduled in one week for further treatment planning. The patient is advised to report any f
```
