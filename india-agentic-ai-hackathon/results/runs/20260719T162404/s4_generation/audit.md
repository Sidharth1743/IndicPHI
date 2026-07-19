# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- mean_chars: `476.8`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'automated_sms': 5, 'discharge_summary': 1, 'hospital_billing': 1, 'prescription': 2, 'referral_letter': 1}`

## Preview

### bn · hospital_billing · oncology_chronic

```
Invoice — [[HOSPITAL_NAME|Haora Oncology Care Centre]] | Patient [[PATIENT_NAME|Rashmi Chatterjee]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Haora]] PIN [[PIN_CODE|711101]]
[[PHONE_NUMBER|9832547890]]
[[AADHAAR_NUMBER|234567890123]]
[[INSURANCE_POLICY_NUMBER|POL-WB-2024-9876]]

Bill No: HB-2024-0815-001
Date: 15/08/2024

Particulars | Quantity | Rate (₹) | Amount (₹)
---|---|---|---
Consultation Fee - Dr. S. Banerjee | 1 | 1500 | 1500
CT Scan (Abdomen & Pelvis) | 1 | 4500 | 4500
Biopsy - Fine Needle Aspiration | 1 | 2500 | 2500
Chemotherapy Session - Cyclophosphamide | 1 | 3500 | 3500
Chemotherapy Session - Doxorubicin | 1 | 4000 | 4000
Chemotherapy Session - Paclitaxel | 1 | 5000 | 5000
Anti-emetic Medication (Oral) | 1 | 500 | 500
IV Fluids (Normal Saline) | 1 | 300 | 300
Bed Charges - ICU (Day) | 3 | 2000 | 6000
Doctor's Round Fee | 3 | 500 | 1500
Nursing Care Charges | 3 | 800 | 2400
Pathology Lab Charges | 1 | 1200 | 1200
Total Amount | | | 29100
GST (18%) | | | 5238
Grand Total | | | 34338

Payment Mode: Cash / Insurance Claim
Due Date: 20/08/2024

Note: All charges are as per the hospital tariff. Any subsequent investigations or procedures will be billed s
```

### en · prescription · psychiatry_behavioral

```
Prescription — [[HOSPITAL_NAME|Lilavati Hospital]]
Patient [[PATIENT_NAME|Priya Deshmukh]], [[AGE|32]] / [[GENDER|Female]], MRN [[MRN|RX-2024-0891]]
Dr. [[DOCTOR_NAME|Dr. Sameer Joshi]]
Rx: Sertraline 50 mg once daily in the morning. Escitalopram 10 mg once daily in the evening.
Follow-up in 4 weeks.
[[PHONE_NUMBER|919876543210]]
[[DISTRICT|Mumbai Suburban]]
[[RESIDENTIAL_ADDRESS|45, SV Road, Andheri West, Mumbai - 400058]]
```

### gu · prescription · tb_ncd

```
Prescription — [[HOSPITAL_NAME|Ahmedabad Civil Hospital]]
Patient [[PATIENT_NAME|Rameshbhai Patel]], [[AGE|23]] / [[GENDER|Male]], MRN [[MRN|RX-1001]]
Dr. [[DOCTOR_NAME|Dr. Vikram Shah]]
Rx: Isoniazid 300mg once daily, Rifampicin 450mg once daily, Pyrazinamide 1500mg once daily, Ethambutol 800mg once daily for 2 months, followed by Isoniazid 300mg and Rifampicin 450mg once daily for 4 months. [[PHONE_NUMBER|9876543210]]
[[DISTRICT|Ahmedabad]]
```
