# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- mean_chars: `713.5`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'automated_sms': 5, 'discharge_summary': 1, 'hospital_billing': 1, 'prescription': 2, 'referral_letter': 1}`

## Preview

### bn · hospital_billing · oncology_chronic

```
Invoice — [[HOSPITAL_NAME|Haora Cancer Care Centre]] | Patient [[PATIENT_NAME|Sathi Mandal]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Haora]] PIN [[PIN_CODE|711101]]
Phone: [[PHONE_NUMBER|9830123456]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Insurance Policy: [[INSURANCE_POLICY_NUMBER|POL-WB-2024-9876]]

Date: 15 August 2024

To,
The Insurance Department
[[INSURANCE_POLICY_NUMBER|POL-WB-2024-9876]]

Sub: Hospital Bill for [[PATIENT_NAME|Sathi Mandal]]

Dear Sir/Madam,

Please find enclosed the itemized bill for the treatment of [[PATIENT_NAME|Sathi Mandal]] admitted under Dr. Arun Ghosh.

Particulars                                   Charges (INR)
-----------------------------------------------------------------
Admission Fee                                      500
Bed Charges (General Ward, 5 days)                2500
Doctor's Consultation Fees (Dr. Arun Ghosh)       1500
Chemotherapy Session 1 (Cisplatin)                 8000
Chemotherapy Session 2 (Paclitaxel)                9500
Chemotherapy Session 3 (Carboplatin)               8500
Blood Tests (CBC, LFT, KFT)                        2000
CT Scan (Chest, Abdomen, Pelvis)                   4500
Pathology Biop
```

### en · prescription · psychiatry_behavioral

```
Prescription — [[HOSPITAL_NAME|Sir J.J. Group of Hospitals]]
Patient [[PATIENT_NAME|Anita Patil]], [[AGE|32]] / [[GENDER|Female]], MRN [[MRN|MH-MUM-2024-0042]]
Dr. [[DOCTOR_NAME|Dr. Rohan Mehta]]
Rx: Sertraline 50 mg once daily in the morning. Escitalopram 10 mg once daily in the evening.
Follow-up in 4 weeks. Please monitor for any changes in mood or sleep patterns.
[[PHONE_NUMBER|9876543210]]
[[DISTRICT|Mumbai Suburban]]
[[RESIDENTIAL_ADDRESS|45, Shivaji Park, Matunga]]
```

### gu · prescription · tb_ncd

```
Prescription — [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient [[PATIENT_NAME|Karan Patel]], [[AGE|23]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Shah]]
Rx: Isoniazid 300mg once daily, Rifampicin 450mg once daily, Pyrazinamide 1500mg once daily, Ethambutol 800mg once daily for two months, followed by Isoniazid 300mg and Rifampicin 450mg once daily for four months. Take all medications on an empty stomach with a full glass of water. Monitor for yellowing of skin or eyes and report immediately.
```
