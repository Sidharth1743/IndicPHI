# Failures audit — `20260721T193130`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260721T193130/pipeline.resolved.yaml`
- **issue count:** **26** (hard=0, gen_soft=2, tr_soft=8, judge=11, auditor=5)
- **S4 entity_coverage_complete_rate:** `0.9855072463768116`
- **S4b script_fail_count:** `0`
- **S5 pass_rate:** `0.9202898550724637`
- **S6 pass_rate / passed:** `0.9606299212598425` / `122`
- **curated docs:** `46`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `d89930b893984d4b96fbd0b492413321` | `kn` | `automated_sms` | `['missing_required_entities:APPOINTMENT_ID']` |
| S4 soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `hospital_billing` | `['missing_required_entities:HOSPITAL_NAME,DISTRICT,PIN_CODE']` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `discharge_summary` | `row_exception:The read operation timed out` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `referral_letter` | `row_exception:The read operation timed out` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `opd_slip` | `row_exception:The read operation timed out` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `asha_worker_note` | `row_exception:The read operation timed out` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `insurance_claim` | `row_exception:The read operation timed out` |
| S4b soft | `9952571815ae4558a362507fc4a9539f` | `ur` | `surgical_note` | `row_exception:The read operation timed out` |
| S5 fail | `8b77264c0f7747c59ec191e95202ff7f` | `brx` | `automated_sms` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `8b77264c0f7747c59ec191e95202ff7f` | `brx` | `hospital_billing` | score=0.3 flags=['dialect_script_impurity', 'instruction_drift', 'cross_language_entity_shift'] |
| S5 fail | `fac14bf3d91143958fc1e8190e25c390` | `brx` | `prescription` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `fac14bf3d91143958fc1e8190e25c390` | `brx` | `insurance_claim` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `fc0833a3fd3a4916849cba96e415af4b` | `kok` | `hospital_billing` | score=0.35 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `hospital_billing` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `hospital_billing` | score=0.65 flags=['invented_entity_type', 'cross_language_entity_shift'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `discharge_summary` | score=0.25 flags=['dialect_script_impurity', 'surrogate_plausibility_collapse'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `referral_letter` | score=0.25 flags=['dialect_script_impurity', 'domain_persona_mismatch'] |
| S5 fail | `f64651bbe52e4c86b23c9a11c76682d9` | `or` | `opd_slip` | score=0.65 flags=['domain_persona_mismatch'] |
| S5 fail | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `asha_worker_note` | score=0.2 flags=['dialect_script_impurity'] |
| S6 fail | `fe2793cf648244fa8cc427adc569983a` | `as` | `hospital_billing` | `['unknown_entity_types:ADDRESS_NUMBER', 'phi_residue:2']` |
| S6 fail | `e2083507b6fc4542853ff740cac47edf` | `bn` | `hospital_billing` | `['unknown_entity_types:RECEIPT_NUMBER']` |
| S6 fail | `62bbda52de29443287ee799e3f265919` | `hi` | `hospital_billing` | `['phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `efe93c7f20fc46b7aa8ef936a09c90c6` | `mr` | `insurance_claim` | `['format:PAN_NUMBER:pan_format']` |
| S6 fail | `e9f9b9a22bcb47f28198db61b9bd4966` | `sd` | `hospital_billing` | `['unknown_entity_types:CONTACT_EMAIL,EMAIL']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `automated_sms` (`kn`).
- **Missing required tags:** `['APPOINTMENT_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:APPOINTMENT_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
TPA ಕ್ಲೈಮ್ — ಪಾಲಿಸಿ [[INSURANCE_POLICY_NUMBER|POL-KA-2024-4567]]
[[PATIENT_NAME|Ramesh Kumar]] [[AGE|28]] [[GENDER|Male]] ಆಧಾರ [[AADHAAR_NUMBER|291512345678]]
ಆಸ್ಪತ್ರೆ [[HOSPITAL_NAME|Chamarajanagar District Hospital]] ಜಿಲ್ಲೆ [[DISTRICT|Chamarajanagar]]
ಮೋಟಾರ್ / RTA ವಾಹನ [[VEHICLE_REGISTRATION|KA01AB1234]] (ಒಮ್ಮೆ ಮಾತ್ರ).
PAN [[PAN_NUMBER|KAAPR1234C]] IFSC [[IFSC_CODE|SBIN0001234]] ಖಾತೆ [[BANK_ACCOUNT_NUMBER|50200012345678]]
ಬ್ಯಾಂಕ್ ರೂಟಿಂಗ್ [[BANK_ROUTING_NUMBER|SBIN0001234]] ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ [[CREDIT_CARD_NUMBER|4111111111111111]] CVV [[CVV|123]] PIN [[PIN|571101]]
ಸಂಪರ್ಕ [[PHONE_NUMBER|987654…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `hospital_billing` (`mni`).
- **Missing required tags:** `['HOSPITAL_NAME', 'DISTRICT', 'PIN_CODE']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME,DISTRICT,PIN_CODE']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Thoubal District Hospital
Thoubal, Manipur - 795138
Phone: [[TELEPHONE_LANDLINE|03842-254567]]

---
INVOICE
---
Patient: [[PATIENT_NAME|Ngangom Sanjita]]
MRN: [[MRN|THD-2024-0815-001]]

Admission Details
Admission Date: 15 August 2024
Discharge Date: 22 August 2024
Reason for Admission: Management of complex chronic care related to oncology treatment.

Bill Details
Room Charges: Rs. 5000 per day for 7 days = Rs. 35000
Doctor Consultation Fees: Rs. 3000
Chemotherapy Session 1: Rs. 15000
Chemotherapy Session 2: Rs. 15000
Chemotherapy Session 3: Rs. 15000
Blood Tests and Pathology: Rs. 8000
Imag…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `hospital_billing` (`mni`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Thoubal District Hospital
Thoubal, Manipur - 795138
Phone: [[TELEPHONE_LANDLINE|03842-254567]]

---
INVOICE
---
Patient: [[PATIENT_NAME|Ngangom Sanjita]]
MRN: [[MRN|THD-2024-0815-001]]

Admission Details
Admission Date: 15 August 2024
Discharge Date: 22 August 2024
Reason for Admission: Management of complex chronic care related to oncology treatment.

Bill Details
Room Charges: Rs. 5000 per day …
```
- **Translated preview:**

```
Thoubal District Hospital
Thoubal, Manipur - 795138
Phone: [[TELEPHONE_LANDLINE|03842-254567]]

---
INVOICE
---
Patient: [[PATIENT_NAME|Ngangom Sanjita]]
MRN: [[MRN|THD-2024-0815-001]]

Admission Details
Admission Date: 15 August 2024
Discharge Date: 22 August 2024
Reason for Admission: Management of complex chronic care related to oncology treatment.

Bill Details
Room Charges: Rs. 5000 per day …
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `hospital_billing` (`mni`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).

Date: 15 August 2024

Bill No: BD-2024-0815-001

Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Fem…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `opd_slip` (`sat`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Medical College and Hospital]] | ID [[HOSPITAL_ID|RMC-H-001]]
Patient: [[PATIENT_NAME|Santi Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RMC-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Rajiv Kumar]]
Relative: [[RELATIVE_NAME|Jugal Murmu]] | Phone: [[PHONE_NUMBER|9876543…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Medical College and Hospital]] | ID [[HOSPITAL_ID|RMC-H-001]]
Patient: [[PATIENT_NAME|Santi Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RMC-2024-0156]] | Doctor: [[DOCTOR_NAME|Dr. Rajiv Kumar]]
Relative: [[RELATIVE_NAME|Jugal Murmu]] | Phone: [[PHONE_NUMBER|9876543…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Madhabpur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Jibon Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Anita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough and chest pain for 3 months. Reports difficulty breathing during salt production work. Referred to District Hospital for furt…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Madhabpur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Jibon Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Anita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough and chest pain for 3 months. Reports difficulty breathing during salt production work. Referred to District Hospital for furt…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Madhabpur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Jibon Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Anita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough and chest pain for 3 months. Reports difficulty breathing during salt production work. Referred to District Hospital for furt…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Madhabpur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Jibon Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Anita Murmu]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient presents with persistent cough and chest pain for 3 months. Reports difficulty breathing during salt production work. Referred to District Hospital for furt…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `surgical_note` (`ur`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Sheikhpura District Hospital]] | ID [[HOSPITAL_ID|SDH-SB-001]]
Patient: [[PATIENT_NAME|Amina Khatoon]] | DOB [[DOB|1960-07-22]] | Age: [[AGE|64]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Homemaker]] | MRN: [[MRN|OPD-2024-0891]] | Doctor: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Relative: [[RELATIVE_NAME|Zainab Khatoon]] | Phone: [[PHONE_NUMBER|9431234567]]
Registrar…
```
- **Translated preview:**

```
آؤٹ پیشنٹ ڈیپارٹمنٹ سلپ | [[HOSPITAL_NAME|Sheikhpura District Hospital]] | آئی ڈی [[HOSPITAL_ID|SDH-SB-001]]
مریض: [[PATIENT_NAME|Amina Khatoon]] | تاریخِ پیدائش [[DOB|1960-07-22]] | عمر: [[AGE|64]] | صنف: [[GENDER|Female]]
پیشہ: [[OCCUPATION|Homemaker]] | میڈیکل ریکارڈ نمبر: [[MRN|OPD-2024-0891]] | ڈاکٹر: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
رشتہ دار: [[RELATIVE_NAME|Zainab Khatoon]] | فون: [[PHONE_…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `automated_sms` (`brx`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose mixes Nepali phrasing/verbs with partial Bodo terms; expected Bodo (Devanagari) narrative not met.
- **Preview:**

```
[[PATIENT_NAME|रमेश]] नोंनि अपोइन्टमेन्ट ID [[APPOINTMENT_ID|APT-240521-02]] [[HOSPITAL_NAME|बाकस जिलानि हास्पिटल]] आव 21-05-2024 बेला 11:00 [[DOCTOR_NAME|डा. ब्रह्म]] सँग हुनेछ। कृपया [[PHONE_NUMBER|9876543210]] आव कन्फर्म गर्नुहोस्। MRN [[MRN|MRN-2024-0815-002]]।
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `hospital_billing` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity', 'instruction_drift', 'cross_language_entity_shift']`
- **Reasoning:** Narrative prose uses Assamese/Bengali script+lexicon instead of required Bodo Devanagari; entity values show mixed/wrong scripts.
- **Preview:**

```
বিৱৰণ — [[HOSPITAL_NAME|বংগাইগাঁও सिविल अस्पताल]] | ৰোগী [[PATIENT_NAME|ৰণজিৎ বৰো]] | MRN [[MRN|MRN-2024-0815-001]]
ঠিকনা জিলা [[DISTRICT|বাক্সা]] PIN [[PIN_CODE|781310]]
এম্বুলেন্স বাহন [[VEHICLE_REGISTRATION|AS-01-AB-1234]] (এবাৰৰ বাবে)।

তাৰিখ: ১৫ আগষ্ট ২০২৪

ৰোগীৰ বিৱৰণ:
নাম: [[PATIENT_NAME|ৰণজিৎ বৰো]]
বয়স: ২৪ বছৰ
লিংগ: পুৰুষ
আধাৰ: [[AADHAAR_NUMBER|203835321155]]
ফোন: [[PHONE_NUMBER|9876543210]]
বীমা পলিচী: [[INSURANCE_POLICY_NUMBER|POL-AS-2024-001234]]
কৰ পৰিচয়: [[TAX_ID|27AAAPL1234C1ZV]…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `prescription` (`brx`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose uses Hindi/Nepali vocabulary and structure instead of Bodo; all entity tags and content otherwise valid and persona-plausible.
- **Preview:**

```
नुस्खा — [[HOSPITAL_NAME|कोकराझार जिल्ला अस्पताल]]
रोगी [[PATIENT_NAME|बिना बोरो]], [[AGE|29]] / [[GENDER|Female]], [[MRN|MRN-2024-0815-001]]
डाक्टर [[DOCTOR_NAME|डाक्टर राजेश कुमार]]
फोन: [[PHONE_NUMBER|9876543210]]
ABHA ID: [[ABHA_ID|12-3456-7890-1234]]
रोगी पहिचान: [[PATIENT_ID|PID-2024-0815-001]]
पता: [[RESIDENTIAL_ADDRESS|गाउँ: चापागुरी, पोस्ट: कोकराझार, जिल्ला: कोकराझार, आसाम - 783370]]
जिल्ला: [[DISTRICT|कोकराझार]]
तारीख: 15 अगस्त 2024

मुख्य शिकायत:
रोगी 3 दिनदेखि बुखार, शरीर दुखाइ र कम…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose written mostly in Assamese/Bengali script with mixed Devanagari insertions instead of required Bodo Devanagari; language and script mismatch for expected brx document.
- **Preview:**

```
TPA দাবী — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-AS-2024-0892]]
ৰোগীৰ নাম: [[PATIENT_NAME|रीনা बोरो]] [[AGE|29]] [[GENDER|Female]] আধাৰ [[AADHAAR_NUMBER|273321102157]]
হাস্পতাল [[HOSPITAL_NAME|कोकराझार सरकारी अस्पताल]] জিলা [[DISTRICT|कोकराझार]]
মোটৰ / RTA গাড়ী [[VEHICLE_REGISTRATION|AS01M1234]] (এবাৰহে)।
PAN [[PAN_NUMBER|ABCPB1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|50200012345678]]
[[BANK_ROUTING_NUMBER|SBIN0001234]] [[CREDIT_CARD_NUMBER|4111111111111111]] [[CVV|123]]…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `hospital_billing` (`kok`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** 49yo female as surrogate at 28 weeks gestation violates age-domain fit and surrogate plausibility; prose/script otherwise acceptable with valid entity tags.
- **Preview:**

```
बीजक — [[HOSPITAL_NAME|Lilavati Hospital and Research Centre]] | रुग्ण [[PATIENT_NAME|Anjali Kulkarni]] | MRN [[MRN|LH-2024-0815-004]]
पत्ता जिल्हा [[DISTRICT|Mumbai Suburban]] पिन [[PIN_CODE|400050]]
ॲम्ब्युलन्स वाहन [[VEHICLE_REGISTRATION|MH01AB1234]]
रुग्ण [[PATIENT_NAME|Anjali Kulkarni]] MRN [[MRN|LH-2024-0815-004]] ही सरोगेट आवय म्हणून गर्भावस्थेच्या 28 व्या सप्तकांत नियमित तपासणी खातीर आयली.
सेवा:
1. गर्भावस्थेची तपासणी: ₹1,500
2. अल्ट्रासाऊंड (भ्रूण देखरेख): ₹2,000
3. रक्त तपासणी (CBC, स…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `hospital_billing` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose in Bengali script instead of required Meitei; all entity TYPEs valid and Latin IDs acceptable.
- **Preview:**

```
[[HOSPITAL_NAME|Thoubal District Hospital]]
[[DISTRICT|Thoubal]], Manipur - [[PIN_CODE|795138]]
ফোন: [[TELEPHONE_LANDLINE|03842-254567]]

---
ইনভয়েস
---
রোগী: [[PATIENT_NAME|Ngangom Sanjita]]
MRN: [[MRN|THD-2024-0815-001]]

ভর্তি সংক্রান্ত বিবরণ
ভর্তির তারিখ: 15 August 2024
ছাড়পত্রের তারিখ: 22 August 2024
ভর্তির কারণ: Oncology treatment-এর জন্য complex chronic care management.

বিল সংক্রান্ত বিবরণ
কক্ষের ভাড়া: 7 দিনের জন্য প্রতিদিন Rs. 5000 = Rs. 35000
ডাক্তারের পরামর্শ ফি: Rs. 3000
কেমোথেরা…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `hospital_billing` (`mni`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['invented_entity_type', 'cross_language_entity_shift']`
- **Reasoning:** Invalid STATE type (not in allow-list) + Bengali script for place name instead of Meitei.
- **Preview:**

```
ꯕꯤꯜ — [[HOSPITAL_NAME|Thoubal District Hospital]] | ꯄꯦꯁꯦꯟꯠ [[PATIENT_NAME|ꯔꯥꯅꯤ ꯊꯥꯡꯒꯖꯝ]] | MRN [[MRN|MRN-2024-0815-001]]
ꯑꯦꯗ꯭ꯔꯦꯁ ꯗꯤꯁꯇ꯭ꯔꯤꯛꯠ [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
ꯑꯦꯝꯕꯨꯂꯦꯟꯁ ꯚꯦꯍꯤꯀꯜ [[VEHICLE_REGISTRATION|MN01AB1234]] (ꯑꯆꯨꯝꯕ ꯑꯃꯨꯛꯇ)꯫

ꯇꯥꯡ: 15 August 2024

ꯕꯤꯜ ꯅꯝꯕꯔ: BD-2024-0815-001

ꯄꯦꯁꯦꯟꯠ ꯃꯔꯣꯜꯁꯤꯡ:
ꯃꯃꯤꯡ: [[PATIENT_NAME|ꯔꯥꯅꯤ ꯊꯥꯡꯒꯖꯝ]]
ꯑꯥꯙꯥꯔ: [[AADHAAR_NUMBER|203835321155]]
ꯐꯣꯟ: [[PHONE_NUMBER|9412345678]]
ꯏꯃꯦꯜ: rani.thangjam@email.com
ꯑꯦꯗ꯭ꯔꯦꯁ: ꯗꯤꯁꯇ꯭ꯔꯤꯛꯠ: [[DISTRICT|Thoubal]] ꯁ꯭ꯇꯦ…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'surrogate_plausibility_collapse']`
- **Reasoning:** Narrative prose uses Burmese script instead of required Meitei; content incoherent with 'American citizen' reference and garbled delivery/Apgar details, breaking persona and plausibility.
- **Preview:**

```
တိုက်ကိုက်ချက်ပုံ — [[HOSPITAL_NAME|Thoubal District Hospital]]
[[PATIENT_NAME|Leima Devi]] DOB [[DOB|1998-04-15]] [[AGE|26]] [[GENDER|မိခိုး]]
Adm [[ADMISSION_NUMBER|ADM-2024-0815-001]] Ward [[WARD_NUMBER|A1]] Bed [[BED_NUMBER|05]]
Dr [[DOCTOR_NAME|Dr. Rina Thokchom]] | အရေးပါ့မှု / အချက်အလက်ချက်ပုံ: အားသားသည် 26 နှစ်ရှိသော အမေရိကာကွယ်လူတိုင်းသည်။ ကို 15 ဦးရောင် 2024 ခုနှစ် 08:30 အချိန်တွင် အခက်ချိုက်တိုက်ခဲ့သည်။ ကိုယ်လေယာဉ်ကို အခက်ချိုက်တိုက်ခဲ့သည်။ အပိုင်ဂါရေးခြင်းကို 1 မိနစ်တွင် 8 နှစ်နဲ့ 5…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'domain_persona_mismatch']`
- **Reasoning:** Narrative prose uses Assamese/Bengali script throughout instead of required Meitei; female patient listed with wife (পত্নী) relative creates sex mismatch.
- **Preview:**

```
পৰামৰ্শ [[REFERRAL_ID|REF-2024-THB-087]] [[HOSPITAL_NAME|Thoubal District Hospital]] / [[DOCTOR_NAME|ꯗꯣꯛꯇꯔ ꯑꯦꯜ. ꯁꯤꯡꯍ]]
ৰোগী: [[PATIENT_NAME|ꯂꯥꯂꯤꯇꯥ ꯗꯦꯕꯤ]], [[AGE|26]] / [[GENDER|Female]], জিলা [[DISTRICT|Thoubal]]
কাৰণ: [[AGE|26]] বছৰীয়া Thoubal জিলাৰ এগৰাকী মহিলা ৰোগীৰ ৩ সপ্তাহ ধৰি জ্বৰ আৰু ভাগৰ দেখা গৈছে।

প্ৰিয় সহকৰ্মী,

আমি এজন ৰোগীক আপোনাৰ ওচৰলৈ পঠিয়াইছোঁ [[PATIENT_NAME|ꯂꯥꯂꯤꯇꯥ ꯗꯦꯕꯤ]], Thoubal জিলাৰ ২৬ বছৰীয়া এগৰাকী মহিলা, যি যোৱা ৩ সপ্তাহ ধৰি দীৰ্ঘদিনীয়া জ্বৰ, অসুস্থতা আৰু গোটেই শৰীৰৰ …
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `opd_slip` (`or`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** Maternal health domain incompatible with 45yo postmenopausal/menopausal presentation and negative pregnancy test.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|ସାଧାରଣ ଡାକ୍ତରଖାନା]] | ID [[HOSPITAL_ID|BMC-H-001]]
ରୋଗୀ: [[PATIENT_NAME|ଶ୍ରୀମତୀ [ନାମ]]] | ଜନ୍ମ ତାରିଖ [[DOB|1979-07-22]] | ବୟସ: [[AGE|45]] | ଲିଙ୍ଗ: [[GENDER|Female]]
ବୃତ୍ତି: [[OCCUPATION|ଗୃହିଣୀ]] | ଚିକିତ୍ସା ରେକର୍ଡ ନମ୍ବର: [[MRN|BMC-2024-0815-004]] | ଡାକ୍ତର: [[DOCTOR_NAME|ଡାକ୍ତର [ନାମ]]]
ସମ୍ପର୍କୀୟ: [[RELATIVE_NAME|ପୁତ୍ର/କନ୍ୟା]] | ଫୋନ୍: [[PHONE_NUMBER|9438156723]]
ପଞ୍ଜିକରଣ କର୍ମଚାରୀ ID: [[EMPLOYEE_ID|REG-2024-012]] | ଜିଲ୍ଲା: [[DISTRICT|ଗଞ୍ଜାମ]]
ମୁଖ୍ୟ ଅଭିଯୋଗ: ଗତ 3 ମାସ ଧରି ଅନ…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `asha_worker_note` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Narrative prose entirely in Hindi/Devanagari; expected Santali in Ol Chiki script.
- **Preview:**

```
ASHA णोते — गाँव [[VILLAGE|मधुपुर]], जिला [[DISTRICT|बीरभूम]]
लाभार्थी [[PATIENT_NAME|जिबोन मुर्मु]], [[AGE|56]] / [[GENDER|मर्द]]
ASHA: [[ASHA_WORKER_NAME|अनिता मुर्मु]] | फोन [[PHONE_NUMBER|9876543210]]
भेट निष्कर्ष: रोगी को ३ मास से लगातार खाँसी आउर सीने में दर्द है। नमक बनाब के काम में सांस लेब में तकलीफ बताइया। आगे जांच के लिए जिला अस्पताल भेजा गया है।
पारिवारिक इतिहास: रोगी के पिता [[RELATIVE_NAME|संजय मुर्मु]] पिछले साल मरब से पहिले अइसे ही लक्षण से पीड़ित थे। रोगी के पास BPL राशन कार्ड …
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `hospital_billing` (`as`).
- **Errors:** `['unknown_entity_types:ADDRESS_NUMBER', 'phi_residue:2']`
- **Preview:**

```
বিল — [[HOSPITAL_NAME|কেন্সাৰ হাস্পতাল]] | ৰোগী [[PATIENT_NAME|ৰঞ্জিত বৰা]] | MRN [[MRN|MRN-2024-0815-001]]
ঠিকনা জিলা [[DISTRICT|শিৱসাগৰ]] পিন [[PIN_CODE|785001]]
এম্বুলেন্স বাহন [[VEHICLE_REGISTRATION|AS-01-AB-1234]]

ৰোগীৰ বিৱৰণ:
নাম: [[PATIENT_NAME|ৰঞ্জিত বৰা]]
বয়স: [[AGE|30]] বছৰ
লিংগ: পুৰুষ
বৃত্তি: জ্যেষ্ঠ মাধ্যমিক আৰু জ্যেষ্ঠ বিদ্যালয়ৰ শিক্ষক, বাণিজ্য
ঠিকনা: [[ADDRESS_NUMBER|12]] গান্ধী নগৰ, ৱাৰ্ড [[WARD_NUMBER|4]], [[DISTRICT|শিৱসাগৰ]], অসম 785001
ফোন: [[PHONE_NUMBER|9876543210]]
লেণ্…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `hospital_billing` (`bn`).
- **Errors:** `['unknown_entity_types:RECEIPT_NUMBER']`
- **Preview:**

```
বিল — [[HOSPITAL_NAME|South 24 Parganas District Hospital]] | [[PATIENT_NAME|Ranjan Kumar Mondal]] | [[MRN|MRN-WB-2024-0089]]
ঠিকানা জেলা [[DISTRICT|South Twenty Four Parganas]] পিন [[PIN_CODE|743347]]
অ্যাম্বুলেন্স যানবাহন [[VEHICLE_REGISTRATION|WB01AB1234]].

রোগীর বিবরণ:
নাম: [[PATIENT_NAME|Ranjan Kumar Mondal]]
বয়স: 30 বছর
লিঙ্গ: পুরুষ
এম.আর.এন: [[MRN|MRN-WB-2024-0089]]
আধার: [[AADHAAR_NUMBER|203835321155]]
ফোন: [[PHONE_NUMBER|9832045678]]
বিমা: [[INSURANCE_POLICY_NUMBER|POL-WB-2024-5678]]…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `hospital_billing` (`hi`).
- **Errors:** `['phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
Invoice - [[HOSPITAL_NAME|Indore District Hospital]] | Patient: [[PATIENT_NAME|सुनीता बाई]] | MRN [[MRN|MRN-2024-0815-001]]
Address District [[DISTRICT|इंदौर]] PIN [[PIN_CODE|452001]]
Ambulance / Parking Vehicle [[VEHICLE_REGISTRATION|MP01AB1234]] (only once).
Patient Details:
Name: [[PATIENT_NAME|सुनीता बाई]]
Age: [[AGE|33]]
Gender: [[GENDER|महिला]]
Aadhaar: [[AADHAAR_NUMBER|203835321155]]
Phone: [[PHONE_NUMBER|9876543210]]
Insurance: [[INSURANCE_POLICY_NUMBER|POL-MP-2024-5678]]
Tax ID: [[TAX_…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `insurance_claim` (`mr`).
- **Errors:** `['format:PAN_NUMBER:pan_format']`
- **Preview:**

```
टीपीए दावा — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-MH-2024-8921]]
[[PATIENT_NAME|Ramesh Patil]] [[AGE|51]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|278945612345]]
रुग्णालय [[HOSPITAL_NAME|Chhatrapati Pramilatai Hospital]] जिल्हा [[DISTRICT|Kolhapur]]
मोटार / आरटीए वाहन [[VEHICLE_REGISTRATION|MH02AB1234]] (एकदाच वापरले आहे).
पॅन [[PAN_NUMBER|PATILR1234C]] आयएफएससी [[IFSC_CODE|SBIN0001234]] खाते [[BANK_ACCOUNT_NUMBER|50200012345678]]

रुग्ण आपत्कालीन विभागात छातीत दुखणे डाव्या हाताकडे जाणारे, धाप लाग…
```

### S6 auditor fail 5

- **What:** deterministic auditor **fail** on `hospital_billing` (`sd`).
- **Errors:** `['unknown_entity_types:CONTACT_EMAIL,EMAIL']`
- **Preview:**

```
اسپتال — [[HOSPITAL_NAME|ڀونگر ميونسپل اسپتال]] | مريضو [[PATIENT_NAME|احمد مصطفیٰ]] | MRN [[MRN|BMH-2024-0815-001]]
پتو ضلعو [[DISTRICT|ڀونگر]] پن [[PIN_CODE|364001]]
امبوليئنس گاڏي [[VEHICLE_REGISTRATION|GJ01AB1234]] (بلڪل هڪ ڀيرو).

مريضو جو تفصيل:
نالو: [[PATIENT_NAME|احمد مصطفیٰ]]
عمر: 22 سال
صنف: مرد
آدھار: [[AADHAAR_NUMBER|203835321155]]
موبائل: [[PHONE_NUMBER|9876543210]]
ايميل: [[EMAIL|ahmed.mustafa@email.com]]
انشورنس پاليسي: [[INSURANCE_POLICY_NUMBER|INS-GUJ-2024-5678]]
ٽيڪس آئي ڊي: …
```


## Surviving curated set

- languages: `{'as': 2, 'bn': 2, 'brx': 2, 'doi': 2, 'en': 2, 'gu': 2, 'hi': 2, 'kn': 2, 'kok': 2, 'ks': 2, 'mai': 2, 'ml': 2, 'mni': 2, 'mr': 2, 'ne': 2, 'or': 2, 'pa': 2, 'sa': 2, 'sat': 2, 'sd': 2, 'ta': 2, 'te': 2, 'ur': 2}`
- doc_types: `{'asha_worker_note': 6, 'automated_sms': 5, 'discharge_summary': 4, 'er_triage_notes': 1, 'hospital_billing': 3, 'insurance_claim': 3, 'lab_report': 2, 'opd_slip': 5, 'phc_register': 5, 'prescription': 2, 'radiology_report': 4, 'referral_letter': 4, 'surgical_note': 2}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
