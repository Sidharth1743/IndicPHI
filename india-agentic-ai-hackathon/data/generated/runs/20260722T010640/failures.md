# Failures audit — `20260722T010640`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260722T010640/pipeline.resolved.yaml`
- **issue count:** **38** (hard=0, gen_soft=6, tr_soft=20, judge=8, auditor=4)
- **S4 entity_coverage_complete_rate:** `0.9637681159420289`
- **S4b script_fail_count:** `2`
- **S5 pass_rate:** `0.9420289855072463`
- **S6 pass_rate / passed:** `0.9692307692307692` / `126`
- **curated docs:** `126`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `fc0833a3fd3a4916849cba96e415af4b` | `kok` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER']` |
| S4 soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `referral_letter` | `['entity_stuffing:HOSPITAL_NAME']` |
| S4 soft | `22eae34bd622448286f2f69f2f795893` | `pa` | `er_triage_notes` | `['missing_required_entities:PATIENT_NAME,AGE,GENDER,DOCTOR_NAME,HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUM…` |
| S4 soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `asha_worker_note` | `['missing_required_entities:RELIGION']` |
| S4 soft | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `discharge_summary` | `['missing_required_entities:DISTRICT']` |
| S4b soft | `d89930b893984d4b96fbd0b492413321` | `kn` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `c03b2ff49ffa439380a254bb9f8972f7` | `kok` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `fc0833a3fd3a4916849cba96e415af4b` | `kok` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `fc0833a3fd3a4916849cba96e415af4b` | `kok` | `discharge_summary` | `row_exception:The read operation timed out` |
| S4b soft | `18a30340943543c59236f8f4e9379b8d` | `ks` | `asha_worker_note` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered n…` |
| S4b soft | `99d8e2b0dd9e42e6b270e50cb12c26c5` | `ks` | `phc_register` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered n…` |
| S4b soft | `80435bdcef24479390d6e6ae0b2aeeb1` | `ml` | `hospital_billing` | `row_exception:The read operation timed out` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `referral_letter` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID…` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `discharge_summary` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID…` |
| S4b soft | `22eae34bd622448286f2f69f2f795893` | `pa` | `er_triage_notes` | `row_exception:The read operation timed out` |
| S4b soft | `22eae34bd622448286f2f69f2f795893` | `pa` | `telemedicine_transcript` | `row_exception:The read operation timed out` |
| S4b soft | `24405a884af14bcba6e9c3657baebf83` | `pa` | `er_triage_notes` | `row_exception:The read operation timed out` |
| S4b soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `lab_report` | `row_exception:The read operation timed out` |
| S4b soft | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `prescription` | `row_exception:The read operation timed out` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `opd_slip` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered n…` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `prescription` | `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID…` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `asha_worker_note` | `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `discharge_summary` | `row_exception:The read operation timed out` |
| S4b soft | `200f6b68373b4d389065d55262ec7847` | `te` | `automated_sms` | `tag_restore_or_translate_failed:Translation lost or altered name/place TYPE 'DOCTOR_NAME' (placehol…` |
| S5 fail | `8b77264c0f7747c59ec191e95202ff7f` | `brx` | `insurance_claim` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `fac14bf3d91143958fc1e8190e25c390` | `brx` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity', 'other'] |
| S5 fail | `fac14bf3d91143958fc1e8190e25c390` | `brx` | `asha_worker_note` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `9b16854e981048c59b1bc1efd2685bdf` | `hi` | `automated_sms` | score=0.65 flags=['other'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `referral_letter` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `49e7eef3f6644cc689038f044f77f052` | `sat` | `opd_slip` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `insurance_claim` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `discharge_summary` | score=0.6 flags=['invented_entity_type'] |
| S6 fail | `5afdbf29e52249fc95146ec7db5e2023` | `as` | `insurance_claim` | `['phi_residue:1']` |
| S6 fail | `9b16854e981048c59b1bc1efd2685bdf` | `hi` | `hospital_billing` | `['dics_below_threshold:0.0']` |
| S6 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `hospital_billing` | `['span_alignment_failure', 'boundary_corruption_rate:0.2857142857142857']` |
| S6 fail | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `hospital_billing` | `['missing_required:PATIENT_NAME,HOSPITAL_NAME,MRN,DISTRICT,PIN_CODE,PHONE_NUMBER,AADHAAR_NUMBER,INS…` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `insurance_claim` (`kok`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER', 'CREDIT_CARD_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
TPA दावो — धोरण [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
[[PATIENT_NAME|Sunita Kulkarni]] [[AGE|49]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|234567890123]]
हॉस्पिटल [[HOSPITAL_NAME|Lilavati Hospital]] जिल्हा [[DISTRICT|Mumbai Suburban]]
मोटार / RTA वाहन [[VEHICLE_REGISTRATION|MH01AB1234]] (फक्त एकदां).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0001234]] खाते [[BANK_ACCOUNT_NUMBER|60601234567890]]

रुग्णान मुखेल तक्रार केली की फाटल्या 6 म्हयन्यांपासून सतत चिंता, पैनिक अटॅक आनी डिप्रेशिव्ह लक्षणं आसात. इतिहासांत न्हिदपाक त्रास, दिसाच्या कामांत रस उणो जावप आनी निरुपयोगीपणाची भावना द…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `referral_letter` (`mni`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['HOSPITAL_NAME']`
- **Raw reasons:** `['entity_stuffing:HOSPITAL_NAME']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
ꯏꯟꯚꯣꯏꯁ — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|Thoubal]]
PIN [[PIN_CODE|795001]] ꯄꯦꯁꯦꯟꯠ [[PATIENT_NAME|Nongthombam Bimol]] MRN [[MRN|RC-2024-0815-001]]
ꯑꯦꯗ꯭ꯔꯦꯁ [[RESIDENTIAL_ADDRESS|Leimakhong Thoubal, Manipur]] ꯐꯣꯟ [[PHONE_NUMBER|9876543210]]
ꯏꯃꯦꯜ [[EMAIL_ADDRESS|nongthombam.bimol@example.com]] PAN [[PAN_NUMBER|MANB1234F]]
ꯂꯦꯟꯗꯂꯥꯏꯟ [[TELEPHONE_LANDLINE|0385-2345678]] ꯚꯦꯍꯤꯀꯜ [[VEHICLE_REGISTRATION|MN01AB1234]] (ꯑꯃꯨꯛꯇꯗ)
ꯑꯥꯙꯥꯔ [[AADHAAR_NUMBER|291512345678]] ꯄꯣꯂꯤꯁꯤ [[INSURANCE_POLICY_NUMBER|POL-MAN-2024-7781]] GSTIN [[TAX_ID|19ABCDE1234F1Z5]]
ꯔꯤꯁꯤꯠ ꯅꯝꯕꯔ INV-2024-08…
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `er_triage_notes` (`pa`).
- **Missing required tags:** `['PATIENT_NAME', 'AGE', 'GENDER', 'DOCTOR_NAME', 'HOSPITAL_NAME', 'ENCOUNTER_ID', 'WARD_NUMBER', 'RELATIVE_NAME', 'PHONE_NUMBER', 'BED_NUMBER', 'VEHICLE_REGISTRATION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:PATIENT_NAME,AGE,GENDER,DOCTOR_NAME,HOSPITAL_NAME,ENCOUNTER_ID,WARD_NUMBER,RELATIVE_NAME,PHONE_NUMBER,BED_NUMBER,VEHICLE_REGISTRATION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ਰੇਡੀਓਲੋਜੀ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|Guru Nanak Dev Hospital]] | [[PATIENT_NAME|Gurmel Rani]] [[AGE|40]] [[GENDER|Female]]
ਮੈਡੀਕਲ ਰਿਕਾਰਡ ਨੰਬਰ [[MRN|MRN-PUN-2024-0892]] ਐਨਕਾਊਂਟਰ [[ENCOUNTER_ID|ENC-2024-0892-001]] | ਡਾ. [[DOCTOR_NAME|Dr. Harpreet Singh]] ਦੁਆਰਾ ਰਿਪੋਰਟ ਕੀਤਾ ਗਿਆ
ਕਲੀਨਿਕਲ ਸੰਕੇਤ: 2 ਦਿਨਾਂ ਤੋਂ ਬੁਖਾਰ ਦੇ ਨਾਲ ਸੱਜੇ ਉੱਪਰਲੇ ਹਿੱਸੇ ਵਿੱਚ ਪੇਟ ਦਰਦ

ਤਕਨੀਕ: [[DATE|August 15, 2024]] 'ਤੇ ਕਰਵੀਲੀਨੀਅਰ ਟ੍ਰਾਂਸਡਿਊਸਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪੇਟ ਦਾ ਅਲਟਰਾਸਾਊਂਡ ਕੀਤਾ ਗਿਆ

ਨਤੀਜੇ: ਗਾਲਬਲੈਡਰ ਦੀ ਕੰਧ 4mm ਤੱਕ ਮੋਟੀ ਹੋ ਗਈ ਹੈ ਅਤੇ ਪੈਰੀਕੋਲੇਸਿਸਟਿਕ ਤਰਲ ਮੌਜੂਦ ਹੈ। ਕੋਈ ਪੱਥਰੀ ਨਹੀਂ ਦਿਖਾਈ ਦਿੱਤੀ। ਜਿਗਰ ਸਮਾਨ ਰੂਪ ਵਿੱਚ ਦਿਖਾਈ ਦੇ ਰਿਹਾ ਹੈ ਅਤੇ ਇਸਦੀ ਈਕ…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `opd_slip` (`sa`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Lab report — [[HOSPITAL_NAME|Bundi District Hospital]] District [[DISTRICT|Bundi]]
MRN [[MRN|RJ-BDH-2024-0815]] Patient ID [[PATIENT_ID|PID-RJ-7781]]
[[PATIENT_NAME|Devi Kumari]] [[AGE|19]] [[GENDER|Female]] Phone [[PHONE_NUMBER|9876543210]]
Ordered by [[DOCTOR_NAME|Dr. Rajesh Sharma]]
Date of collection: 15 August 2024

TEST RESULTS:
Thyroid Function Tests:
- TSH: 2.45 mIU/L (Reference: 0.4-4.0)
- Free T4: 1.2 ng/dL (Reference: 0.8-1.8)
- Free T3: 3.8 pg/mL (Reference: 2.3-4.2)

Vitamin Panel:
- Vitamin D: 18 ng/mL (Reference: 30-100)
- Vitamin B12: 285 pg/mL (Reference: 200-900)
- Folate: 6…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `asha_worker_note` (`sat`).
- **Missing required tags:** `['RELIGION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:RELIGION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ASHA नोटां — गाँव [[VILLAGE|Chak Pathar]], ज़िला [[DISTRICT|Birbhum]]
लाभार्थी [[PATIENT_NAME|Lal Mohan Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sabitri Hansda]] | फोन [[PHONE_NUMBER|9876543210]]
भेटे के निष्कर्ष: मरीज़ बताता है लगातार दर्द गले में और निगलने में मुश्किल पिछले एक हफ़्ते से। वह बताता है एक नया, सख्त गाँठ उसके बाएं जबड़े के पास। मरीज़ थका हुआ लग रहा है और मुँह के छाले हैं। वह अभी ले रहा है दिए गए analgesics और पोषण पूरक।
योजना: ASHA कार्यकर्ता ने मरीज़ को सलाह दी अपनी दवा जारी रखने और नरम आहार पर परामर्श दिया। उसने तीन दिनों में अगली मुलाकात तय की है और onc…
```

### S4 generation soft-fail 6

- **What:** generation soft-fail on `discharge_summary` (`sd`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
بل — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] ضلع [[DISTRICT|Bhilwara]]
پِن [[PIN_CODE|311001]] مريضو [[PATIENT_NAME|Ujma Bano]] MRN [[MRN|MGH-RJ-2024-0815]]
پتھو [[RESIDENTIAL_ADDRESS|15 Shivaji Colony, Ward 12]] فون [[PHONE_NUMBER|9876543210]]
اي ميل [[EMAIL_ADDRESS|ujma.bano@example.com]] PAN [[PAN_NUMBER|RJUPA1234F]]
لئنڊ لائن [[TELEPHONE_LANDLINE|01482-234567]] گاڏي [[VEHICLE_REGISTRATION|RJ14AB1234]] (امبوليئنس)
آڌار [[AADHAAR_NUMBER|291512345678]] پاليسي [[INSURANCE_POLICY_NUMBER|POL-RJ-2024-7781]] GSTIN [[TAX_ID|29ABCDE1234F1Z5]]
رسيپٽ نمبر INV-2024-0815 راجستھان اسٽيٽ لائن پليئن پرو…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `hospital_billing` (`kn`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-KA-2024-0892]]
[[PATIENT_NAME|Ramesh Kumar]] [[AGE|28]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|298745612345]]
Hospital [[HOSPITAL_NAME|Chamarajanagar District Hospital]] District [[DISTRICT|Chamarajanagar]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KA02AB1234]] (exactly once).
PAN [[PAN_NUMBER|ABCDR1234E]] IFSC [[IFSC_CODE|SBIN0001234]] account …
```
- **Translated preview:**

```
TPA ಕ್ಲೈಮ್ — ಪಾಲಿಸಿ [[INSURANCE_POLICY_NUMBER|POL-KA-2024-0892]]
[[PATIENT_NAME|ಶ್ರೀ ಶಂಕರ್]] [[AGE|28]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|298745612345]]
ಆಸ್ಪತ್ರೆ [[HOSPITAL_NAME|ಮಣಿಪಾಲ್ ಆಸ್ಪತ್ರೆ]] ಜಿಲ್ಲೆ [[DISTRICT|ಬೆಂಗಳೂರು]]
ಮೋಟಾರ್ / RTA ವಾಹನ [[VEHICLE_REGISTRATION|KA02AB1234]] (ಒಮ್ಮೆ ಮಾತ್ರ).
PAN [[PAN_NUMBER|ABCDR1234E]] IFSC [[IFSC_CODE|SBIN0001234]] ಖಾತೆ [[BANK_ACCOUNT_NUMBER|502000123…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `hospital_billing` (`kok`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: Your psychiatry follow-up for anxiety management is [[APPOINTMENT_ID|APT-241120-03]] on 20-Nov at 11:00 with [[DOCTOR_NAME|Dr. Anjali Rao]] at [[HOSPITAL_NAME|District Hospital Karwar]]. MRN [[MRN|MRN-2024-0815-001]]. Call [[PHONE_NUMBER|9876543210]] to confirm.
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Patil]]: तुमचो मानसोपचार पाठपुरावा चिंता व्यवस्थापना खातीर आसा. [[APPOINTMENT_ID|APT-241120-03]] 20-नोव्हेंबर क 11:00 वेळार [[DOCTOR_NAME|Dr. Anjali Rao]] [[HOSPITAL_NAME|District Hospital Karwar]] हांचे वांगडा. MRN [[MRN|MRN-2024-0815-001]]. खात्री करपा खातीर [[PHONE_NUMBER|9876543210]] फोन करात.
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `hospital_billing` (`kok`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
[[PATIENT_NAME|Sunita Kulkarni]] [[AGE|49]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Lilavati Hospital]] District [[DISTRICT|Mumbai Suburban]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|MH01AB1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_AC…
```
- **Translated preview:**

```
TPA दावो — धोरण [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
[[PATIENT_NAME|Sunita Kulkarni]] [[AGE|49]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|234567890123]]
हॉस्पिटल [[HOSPITAL_NAME|Lilavati Hospital]] जिल्हा [[DISTRICT|Mumbai Suburban]]
मोटार / RTA वाहन [[VEHICLE_REGISTRATION|MH01AB1234]] (फक्त एकदां).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0001234]] खाते [[BANK_ACCOUNT_NUMBER|606…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `discharge_summary` (`kok`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
[[PATIENT_NAME|Sunita Kulkarni]] [[AGE|49]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|234567890123]]
Hospital [[HOSPITAL_NAME|Lilavati Hospital]] District [[DISTRICT|Mumbai Suburban]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|MH01AB1234]] (exactly once).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_AC…
```
- **Translated preview:**

```
TPA दावो — धोरण [[INSURANCE_POLICY_NUMBER|POL-MH-2024-9876]]
[[PATIENT_NAME|Sunita Kulkarni]] [[AGE|49]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|234567890123]]
हॉस्पिटल [[HOSPITAL_NAME|Lilavati Hospital]] जिल्हा [[DISTRICT|Mumbai Suburban]]
मोटार / RTA वाहन [[VEHICLE_REGISTRATION|MH01AB1234]] (फक्त एकदां).
PAN [[PAN_NUMBER|KLMNO5678P]] IFSC [[IFSC_CODE|SBIN0001234]] खाते [[BANK_ACCOUNT_NUMBER|606…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `asha_worker_note` (`ks`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'RELIGION' (placeholder ⟦NM5⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Nigeen]], District [[DISTRICT|Srinagar]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|40]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Amina Begum]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: Patient presents with persistent cough and weight loss over 3 months. Reports intermittent fever and night sweats. Family history significant for lung cancer. Ref…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|Nigeen]], District [[DISTRICT|Srinagar]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|40]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Amina Begum]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: Patient presents with persistent cough and weight loss over 3 months. Reports intermittent fever and night sweats. Family history significant for lung cancer. Ref…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `phc_register` (`ks`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] Village [[VILLAGE|Kokernag]] District [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Amina Begum]] [[AGE|59]] [[GENDER|Female]] | Follow-up for Stage II Breast Cancer, post-chemotherapy

Patient presents with persistent fatigue and mild peripheral neuropathy secondary to chemotherapy. Reports intermittent chest discomfort on exertion. Current …
```
- **Translated preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] Village [[VILLAGE|Kokernag]] District [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Amina Begum]] [[AGE|59]] [[GENDER|Female]] | Follow-up for Stage II Breast Cancer, post-chemotherapy

Patient presents with persistent fatigue and mild peripheral neuropathy secondary to chemotherapy. Reports intermittent chest discomfort on exertion. Current …
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `hospital_billing` (`ml`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Karamcode]], District [[DISTRICT|Thiruvananthapuram]]
Beneficiary [[PATIENT_NAME|Megha John]], [[AGE|32]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Latha Nair]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased anxiety symptoms and sleep disturbances for past two weeks. She mentions difficulty concentrating at work and occasional panic …
```
- **Translated preview:**

```
ആശ വർക്കർ കുറിപ്പ് — ഗ്രാമം [[VILLAGE|Karamcode]], ജില്ല [[DISTRICT|Thiruvananthapuram]]
ഗുണഭോക്താവ് [[PATIENT_NAME|Megha John]], [[AGE|32]] / [[GENDER|Female]]
ആശ: [[ASHA_WORKER_NAME|Latha Nair]] | ഫോൺ [[PHONE_NUMBER|9876543210]]
സന്ദർശന കണ്ടെത്തലുകൾ: കഴിഞ്ഞ രണ്ട് ആഴ്ചയായി രോഗി വർദ്ധിച്ച ഉത്കണ്ഠാ ലക്ഷണങ്ങളും ഉറക്കത്തിലെ അസ്വസ്ഥതകളും റിപ്പോർട്ട് ചെയ്യുന്നു. ജോലിയിൽ ശ്രദ്ധ കേന്ദ്രീകരിക്കാൻ പ്രയാസമ…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-THB-2024-001]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
INVOICE — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] District [[DISTRICT|Thoubal]]
PIN [[PIN_CODE|795001]] Patient [[PATIENT_NAME|Nongthombam Bimol]] MRN [[MRN|RC-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Leimakhong Thoubal, Manipur]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|nongthombam.bimol@example.com]] PAN [[PAN_NUMBER|MANB1234F]]
Landline [[TELEPHONE_LANDLINE|0385-234…
```
- **Translated preview:**

```
ꯏꯟꯚꯣꯏꯁ — [[HOSPITAL_NAME|Regional Cancer Centre Imphal]] ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|Thoubal]]
PIN [[PIN_CODE|795001]] ꯄꯦꯁꯦꯟꯠ [[PATIENT_NAME|Nongthombam Bimol]] MRN [[MRN|RC-2024-0815-001]]
ꯑꯦꯗ꯭ꯔꯦꯁ [[RESIDENTIAL_ADDRESS|Leimakhong Thoubal, Manipur]] ꯐꯣꯟ [[PHONE_NUMBER|9876543210]]
ꯏꯃꯦꯜ [[EMAIL_ADDRESS|nongthombam.bimol@example.com]] PAN [[PAN_NUMBER|MANB1234F]]
ꯂꯦꯟꯗꯂꯥꯏꯟ [[TELEPHONE_LANDLINE|0385-2345678]…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PHONE_NUMBER|9876543210]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Hospital Billing Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] District [[DISTRICT|Thoubal]]
PIN [[PIN_CODE|795105]] Patient [[PATIENT_NAME|Lalita Devi]] MRN [[MRN|THD-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Vill. Hiyanglam, Thoubal]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|lalita.devi@example.com]] PAN [[PAN_NUMBER|MNPAB1234C]]
Landline [[TELEPHONE_LANDLINE|0385-234…
```
- **Translated preview:**

```
ꯍꯣꯁꯄꯤꯇꯥꯜ ꯕꯤꯜꯂꯤꯡ ꯏꯟꯚꯣꯏꯁ — [[HOSPITAL_NAME|[[NM0]]]] ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|[[NM1]]]]
ꯄꯤꯟ [[PIN_CODE|795105]] ꯄꯦꯁꯦꯟꯇ [[PATIENT_NAME|[[NM2]]]] ꯑꯦꯝ.ꯑꯥꯔ.ꯑꯦꯟ. [[MRN|THD-2024-0815-001]]
ꯑꯦꯗ꯭ꯔꯦꯁ [[RESIDENTIAL_ADDRESS|[[NM3]]]] ꯐꯣꯟ [[PHONE_NUMBER|9876543210]]
ꯏꯃꯦꯜ [[EMAIL_ADDRESS|lalita.devi@example.com]] ꯄꯦꯟ [[PAN_NUMBER|MNPAB1234C]]
ꯂꯦꯟꯗꯂꯥꯏꯟ [[TELEPHONE_LANDLINE|0385-2345678]] ꯚꯦꯍꯤꯀꯜ [[VEHICLE_REGISTRATION…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `er_triage_notes` (`pa`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Radiology Report — [[HOSPITAL_NAME|Guru Nanak Dev Hospital]] | [[PATIENT_NAME|Gurmel Rani]] [[AGE|40]] [[GENDER|Female]]
MRN [[MRN|MRN-PUN-2024-0892]] Encounter [[ENCOUNTER_ID|ENC-2024-0892-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Harpreet Singh]]
Clinical Indication: Acute right upper quadrant abdominal pain for 2 days with fever

Technique: Abdominal ultrasound performed on [[DATE|August 15, 20…
```
- **Translated preview:**

```
ਰੇਡੀਓਲੋਜੀ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|Guru Nanak Dev Hospital]] | [[PATIENT_NAME|Gurmel Rani]] [[AGE|40]] [[GENDER|Female]]
ਮੈਡੀਕਲ ਰਿਕਾਰਡ ਨੰਬਰ [[MRN|MRN-PUN-2024-0892]] ਐਨਕਾਊਂਟਰ [[ENCOUNTER_ID|ENC-2024-0892-001]] | ਡਾ. [[DOCTOR_NAME|Dr. Harpreet Singh]] ਦੁਆਰਾ ਰਿਪੋਰਟ ਕੀਤਾ ਗਿਆ
ਕਲੀਨਿਕਲ ਸੰਕੇਤ: 2 ਦਿਨਾਂ ਤੋਂ ਬੁਖਾਰ ਦੇ ਨਾਲ ਸੱਜੇ ਉੱਪਰਲੇ ਹਿੱਸੇ ਵਿੱਚ ਪੇਟ ਦਰਦ

ਤਕਨੀਕ: [[DATE|August 15, 2024]] 'ਤੇ ਕਰਵੀਲੀਨੀਅਰ ਟ੍ਰਾਂਸਡ…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `telemedicine_transcript` (`pa`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Radiology Report — [[HOSPITAL_NAME|Guru Nanak Dev Hospital]] | [[PATIENT_NAME|Gurmel Rani]] [[AGE|40]] [[GENDER|Female]]
MRN [[MRN|MRN-PUN-2024-0892]] Encounter [[ENCOUNTER_ID|ENC-2024-0892-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Harpreet Singh]]
Clinical Indication: Acute right upper quadrant abdominal pain for 2 days with fever

Technique: Abdominal ultrasound performed on [[DATE|August 15, 20…
```
- **Translated preview:**

```
ਰੇਡੀਓਲੋਜੀ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|Guru Nanak Dev Hospital]] | [[PATIENT_NAME|Gurmel Rani]] [[AGE|40]] [[GENDER|Female]]
ਮੈਡੀਕਲ ਰਿਕਾਰਡ ਨੰਬਰ [[MRN|MRN-PUN-2024-0892]] ਐਨਕਾਊਂਟਰ [[ENCOUNTER_ID|ENC-2024-0892-001]] | ਡਾ. [[DOCTOR_NAME|Dr. Harpreet Singh]] ਦੁਆਰਾ ਰਿਪੋਰਟ ਕੀਤਾ ਗਿਆ
ਕਲੀਨਿਕਲ ਸੰਕੇਤ: 2 ਦਿਨਾਂ ਤੋਂ ਬੁਖਾਰ ਦੇ ਨਾਲ ਸੱਜੇ ਉੱਪਰਲੇ ਹਿੱਸੇ ਵਿੱਚ ਪੇਟ ਦਰਦ

ਤਕਨੀਕ: [[DATE|August 15, 2024]] 'ਤੇ ਕਰਵੀਲੀਨੀਅਰ ਟ੍ਰਾਂਸਡ…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `er_triage_notes` (`pa`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Radiology Report — [[HOSPITAL_NAME|Civil Hospital Barnala]] | [[PATIENT_NAME|Gurdeep Kaur]] [[AGE|80]] [[GENDER|Female]]
MRN [[MRN|MRN-PB-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]] | Reported by Dr [[DOCTOR_NAME|Dr. Rajinder Singh]]
Patient from [[DISTRICT|Barnala]] district, Punjab, presents with chronic cough and weight loss.

CHEST X-RAY FINDINGS:
- Bilateral upper lobe infil…
```
- **Translated preview:**

```
ਰੇਡੀਓਲੋਜੀ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|ਸਰਵੈਂਟ ਹਸਪਤਾਲ]] | [[PATIENT_NAME|ਜਸਵੀਰ ਸਿੰਘ]] [[AGE|80]] [[GENDER|Female]]
ਮੈਡੀਕਲ ਰਿਕਾਰਡ ਨੰਬਰ [[MRN|MRN-PB-2024-0815-001]] ਮੁਲਾਕਾਤ [[ENCOUNTER_ID|ENC-2024-0815-001]] | ਦੁਆਰਾ ਰਿਪੋਰਟ ਕੀਤਾ ਗਿਆ ਡਾ. [[DOCTOR_NAME|ਡਾ. ਗੁਰਪ੍ਰੀਤ ਕੌਰ]]
ਮਰੀਜ਼ [[DISTRICT|ਅੰਮ੍ਰਿਤਸਰ]] ਜ਼ਿਲ੍ਹੇ, ਪੰਜਾਬ ਤੋਂ ਹੈ, ਪੁਰਾਣੀ ਖੰਘ ਅਤੇ ਭਾਰ ਘਟਣ ਦੇ ਲੱਛਣ ਹਨ।

ਛਾਤੀ ਦੇ ਐਕਸ-ਰੇ ਦੀਆਂ ਰਿਪੋਰਟਾਂ:
- ਸੱਜੇ ਪਾਸੇ ਦੇ ਉੱਪਰ…
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `lab_report` (`sa`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Lab report — [[HOSPITAL_NAME|Bundi District Hospital]] District [[DISTRICT|Bundi]]
MRN [[MRN|RJ-BDH-2024-0815]] Patient ID [[PATIENT_ID|PID-RJ-7781]]
[[PATIENT_NAME|Devi Kumari]] [[AGE|19]] [[GENDER|Female]] Phone [[PHONE_NUMBER|9876543210]]
Ordered by [[DOCTOR_NAME|Dr. Rajesh Sharma]]
Date of collection: 15 August 2024

TEST RESULTS:
Thyroid Function Tests:
- TSH: 2.45 mIU/L (Reference: 0.4-4.0)…
```
- **Translated preview:**

```
Lab report — [[HOSPITAL_NAME|Bundi District Hospital]] District [[DISTRICT|Bundi]]
MRN [[MRN|RJ-BDH-2024-0815]] Patient ID [[PATIENT_ID|PID-RJ-7781]]
[[PATIENT_NAME|Devi Kumari]] [[AGE|19]] [[GENDER|Female]] Phone [[PHONE_NUMBER|9876543210]]
Ordered by [[DOCTOR_NAME|Dr. Rajesh Sharma]]
Date of collection: 15 August 2024

TEST RESULTS:
Thyroid Function Tests:
- TSH: 2.45 mIU/L (Reference: 0.4-4.0)…
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `prescription` (`sa`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|District Hospital Kanpur]]
Patient [[PATIENT_NAME|Ahmed Khan]], [[AGE|19]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0915-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Phone: [[PHONE_NUMBER|9876543210]]
Address: [[RESIDENTIAL_ADDRESS|15/26 Civil Lines, Ward 12]]
District: [[DISTRICT|Kanpur Nagar]]
Patient ID: [[PATIENT_ID|PID-2024-0915-001]]
ABHA ID: [[ABHA_ID|12-3456-7890-…
```
- **Translated preview:**

```
Prescription — [[HOSPITAL_NAME|District Hospital Kanpur]]
Patient [[PATIENT_NAME|Ahmed Khan]], [[AGE|19]] / [[GENDER|Male]], MRN [[MRN|RX-2024-0915-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Phone: [[PHONE_NUMBER|9876543210]]
Address: [[RESIDENTIAL_ADDRESS|15/26 Civil Lines, Ward 12]]
District: [[DISTRICT|Kanpur Nagar]]
Patient ID: [[PATIENT_ID|PID-2024-0915-001]]
ABHA ID: [[ABHA_ID|12-3456-7890-…
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `opd_slip` (`sat`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Cancer Institute]] | ID [[HOSPITAL_ID|RCI-2024-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCI-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Singh]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Cancer Institute]] | ID [[HOSPITAL_ID|RCI-2024-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCI-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Singh]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]…
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `prescription` (`sat`).
- **Error:** `row_exception:The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[AGE|32]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Cancer Institute]] | ID [[HOSPITAL_ID|RCI-2024-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCI-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Singh]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi Cancer Institute]] | ID [[HOSPITAL_ID|RCI-2024-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCI-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Singh]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]…
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `asha_worker_note` (`sat`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Chak Pathar]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Lal Mohan Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sabitri Hansda]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent pain in the throat and difficulty swallowing for the past week. He mentions a new, hard lump near his left jawline. The patient …
```
- **Translated preview:**

```
ASHA नोटां — गाँव [[VILLAGE|Chak Pathar]], ज़िला [[DISTRICT|Birbhum]]
लाभार्थी [[PATIENT_NAME|Lal Mohan Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sabitri Hansda]] | फोन [[PHONE_NUMBER|9876543210]]
भेटे के निष्कर्ष: मरीज़ बताता है लगातार दर्द गले में और निगलने में मुश्किल पिछले एक हफ़्ते से। वह बताता है एक नया, सख्त गाँठ उसके बाएं जबड़े के पास। मरीज़ थका हुआ लग रहा है और मुँह …
```

### S4b translation soft-fail 18

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Chak Pathar]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Lal Mohan Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sabitri Hansda]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent pain in the throat and difficulty swallowing for the past week. He mentions a new, hard lump near his left jawline. The patient …
```
- **Translated preview:**

```
ASHA नोटां — गाँव [[VILLAGE|Chak Pathar]], ज़िला [[DISTRICT|Birbhum]]
लाभार्थी [[PATIENT_NAME|Lal Mohan Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Sabitri Hansda]] | फोन [[PHONE_NUMBER|9876543210]]
भेटे के निष्कर्ष: मरीज़ बताता है लगातार दर्द गले में और निगलने में मुश्किल पिछले एक हफ़्ते से। वह बताता है एक नया, सख्त गाँठ उसके बाएं जबड़े के पास। मरीज़ थका हुआ लग रहा है और मुँह …
```

### S4b translation soft-fail 19

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `row_exception:The read operation timed out`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] District [[DISTRICT|Bhilwara]]
PIN [[PIN_CODE|311001]] Patient [[PATIENT_NAME|Ujma Bano]] MRN [[MRN|MGH-RJ-2024-0815]]
Address [[RESIDENTIAL_ADDRESS|15 Shivaji Colony, Ward 12]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|ujma.bano@example.com]] PAN [[PAN_NUMBER|RJUPA1234F]]
Landline [[TELEPHONE_LANDLINE|01482-234567]] Vehicle [[VEHI…
```
- **Translated preview:**

```
بل — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] ضلع [[DISTRICT|Bhilwara]]
پِن [[PIN_CODE|311001]] مريضو [[PATIENT_NAME|Ujma Bano]] MRN [[MRN|MGH-RJ-2024-0815]]
پتھو [[RESIDENTIAL_ADDRESS|15 Shivaji Colony, Ward 12]] فون [[PHONE_NUMBER|9876543210]]
اي ميل [[EMAIL_ADDRESS|ujma.bano@example.com]] PAN [[PAN_NUMBER|RJUPA1234F]]
لئنڊ لائن [[TELEPHONE_LANDLINE|01482-234567]] گاڏي [[VEHICLE_REGISTRATION|R…
```

### S4b translation soft-fail 20

- **What:** translation soft-fail on `automated_sms` (`te`).
- **Error:** `tag_restore_or_translate_failed:Translation lost or altered name/place TYPE 'DOCTOR_NAME' (placeholder ⟦NM1⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Kaggadasapura]], District [[DISTRICT|Bangalore]]
Beneficiary [[PATIENT_NAME|Ramesh Chandra]], [[AGE|61]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Bai]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent pain in the right cheek, difficulty chewing, and new-onset numbness on the right side of his face. He is on oral chemotherapy an…
```
- **Translated preview:**

```
ASHA గమనిక — గ్రామం [[VILLAGE|Kaggadasapura]], జిల్లా [[DISTRICT|Bangalore]]
లబ్ధిదారుడు [[PATIENT_NAME|Ramesh Chandra]], [[AGE|61]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Bai]] | ఫోన్ [[PHONE_NUMBER|9876543210]]
సందర్శన ఫలితాలు: రోగి నివేదించారు కుడి బుగ్గలో నిరంతర నొప్పి, నమలడంలో ఇబ్బంది, మరియు అతని ముఖం కుడి వైపున కొత్తగా వచ్చిన తిమ్మిరి. అతను నోటి ద్వారా కీమోథెరపీ మరియు రేడియోథెరప…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in Hindi (wrong language) despite Devanagari script and Bodo requirement; all entity tags valid and Latin IDs allowed.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-AS-2024-001234]]
[[PATIENT_NAME|Ranjan Boro]] [[AGE|24]] [[GENDER|Male]] Assam [[DISTRICT|Baksa]] [[MRN|MRN-BAKSA-2024-001]] आधार [[AADHAAR_NUMBER|203835321155]]
हस्पताल [[HOSPITAL_NAME|Baksa District Hospital]] जिला [[DISTRICT|Baksa]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|AS01AB1234]] (एक बार मात्र)।
पॅन [[PAN_NUMBER|ABCPB1234C]] IFSC [[IFSC_CODE|SBIN0000123]] खाता [[BANK_ACCOUNT_NUMBER|30912345678901]]
क्रेडिट कार्ड [[CREDIT_CARD_NUMBER|411111…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity', 'other']`
- **Reasoning:** Clinical narrative in Nepali (not Bodo); district mismatches persona anchor (Kokrajhar vs Kamrup); extra billing entities soft but language fails requirement.
- **Preview:**

```
बीमा क्लेम / TPA फॉर्म
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|रश्मी बरुआ]] [[AGE|29]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|228767324243]]
अस्पताल [[HOSPITAL_NAME|गुवाहाटी मेडिकल कॉलेज एंड हॉस्पिटल]] जिला [[DISTRICT|कामरूप मेट्रोपॉलिटन]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|AS01M1234]] (प्रसव के लिए इस्तेमाल किया गया एम्बुलेंस)
PAN [[PAN_NUMBER|BOKPA1234C]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30200012345678]]
[[BANK_ROUTING_NUMBE…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `asha_worker_note` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose is Nepali (e.g. 'बिरामीले आफ्नो', 'गर्छिन्', 'रगत चिनी') instead of Bodo; all entity tags and Latin medical terms are valid.
- **Preview:**

```
आशा कार्यकर्तीको टिपोट — गाम [[VILLAGE|Bwisagu Gaon]], जिल्ला [[DISTRICT|Kokrajhar]]
बिरामी [[PATIENT_NAME|बिना बोरो]], [[AGE|29]] / [[GENDER|महिला]], जीवनसाथी [[RELATIVE_NAME|हिरण बोरो]]. आशा: [[ASHA_WORKER_NAME|जसिमोनी बोरो]] | फोन [[PHONE_NUMBER|9876543210]]. BPL: [[BPL_RATION_CARD|BPL-AS-KJR-2024-0012]]. मतदाता परिचय पत्र: [[VOTER_ID|ASV1234567]]. धर्म: [[RELIGION|Hindu]].
भेटको निष्कर्ष: बिरामीले आफ्नो anti-tubercular medication दैनिक लिइरहेकी रिपोर्ट गर्छिन्। उनीलाई राम्रो लागेको छ तर हल्…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `automated_sms` (`hi`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['other']`
- **Reasoning:** Correct Hindi Devanagari prose and SMS length; fits psychiatry domain + male/28/Bihar persona; all TYPEs allow-listed and Latin IDs expected. Malformed nested MRN tag breaks formatting.
- **Preview:**

```
प्रिय [[PATIENT_NAME|Rahim Ansari]], आपका मनोरोग परामर्श [[APPOINTMENT_ID|APT-240521-01]] के लिए [[HOSPITAL_NAME|Nawada Civil Hospital]] पर डॉ. [[DOCTOR_NAME|Dr. Amit Kumar]] के साथ पुष्टि हो गया है। कृपया अपना [[MRN|[[MRN|MRN-2024-0815-001]]]] साथ लाएं और 15 मिनट पहले पहुंचें। किसी भी बदलाव के लिए [[PHONE_NUMBER|9876543210]] पर संपर्क करें।
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely English; expected Manipuri/Meitei script for narrative.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-01]] from [[HOSPITAL_NAME|Thoubal District Hospital]] / [[DOCTOR_NAME|Dr. L. Sanatombi]]
Re: [[PATIENT_NAME|Ngangom Ongbi Leima]], [[AGE|21]] / [[GENDER|Female]], District [[DISTRICT|Thoubal]]

Reason: Routine Antenatal Care with mild anemia and elevated blood pressure

Patient presents for first trimester ANC at 10 weeks gestation. Patient is primigravida, never married, residing in [[VILLAGE|Lamphelpat]]. Patient reports mild fatigue and occasional headaches. V…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `opd_slip` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Romanized Hindi medical terms instead of Santali in Ol Chiki script; all other elements (tags, persona, length) acceptable.
- **Preview:**

```
Bahar Chikitsa Patra | [[HOSPITAL_NAME|Ranchi Cancer Institute]] | ID [[HOSPITAL_ID|RCI-2024-001]]
Rogi: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-03-14]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCI-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Singh]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-4412]] | District: [[DISTRICT|Ranchi]]
Mukhya Shikayat…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `insurance_claim` (`sat`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in Romanized mix/English instead of required Santali Ol Chiki script; RTA mention mildly drifts from TB/NCD domain.
- **Preview:**

```
TPA dabi — Policy [[INSURANCE_POLICY_NUMBER|POL-WB-2024-8765]]
[[PATIENT_NAME|Ramesh Murmu]] [[AGE|56]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|203835321155]]
Hospital [[HOSPITAL_NAME|Birbhum District Hospital]] District [[DISTRICT|Birbhum]]
Motor / RTA gadi [[VEHICLE_REGISTRATION|WB01AB1234]] (ekbar).
PAN [[PAN_NUMBER|WBMUR1234C]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_ACCOUNT_NUMBER|345678901234]]
Bank routing [[BANK_ROUTING_NUMBER|SBIN0001234]] Credit card [[CREDIT_CARD_NUMBER|411111…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['invented_entity_type']`
- **Reasoning:** Non-allowlist tags (CLINICAL_DIAGNOSIS, CLINICAL_HISTORY, HOSPITAL_COURSE, DISCHARGE_CONDITION, DISCHARGE_INSTRUCTIONS) used; prose/script, persona fit and IDs otherwise acceptable.
- **Preview:**

```
ڊسچارج خلاصو [[HOSPITAL_NAME|مھاتما گانڌي اسپتال]] [[DISTRICT|Bhilwara]]
[[PATIENT_NAME|عظما بانو]] [[DOB|1977-05-10]] [[AGE|47]] [[GENDER|Female]]
داخلو [[ADMISSION_NUMBER|ADM-2024-0815-001]] وارڊ [[WARD_NUMBER|B2]] بسترو [[BED_NUMBER|12]]
ڊاڪٽر [[DOCTOR_NAME|ڊاڪٽر راجيش ڪمار]]
[[CLINICAL_DIAGNOSIS|پلمونري ٽيوبرسڪلوسس (RNTCP ڪيٽيگري I) سان گڏ ٽائپ 2 ڊائيبٽيز میلیٽس]]
[[CLINICAL_HISTORY|مريضه 47 ساله عورت آهي، جنهن جو تعلق ڀيلواڙا، راجسٿان سان آهي. هن کي 2 مهينا اڳ کان کنگھ، گهٽ درجي جو بُخار، …
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `insurance_claim` (`as`).
- **Errors:** `['phi_residue:1']`
- **Preview:**

```
TPA CLAIM FORM
দাবীদাৰৰ বিৱৰণ
ৰোগীৰ নাম: [[PATIENT_NAME|Ranjan Sharma]] [[AGE|36]] [[GENDER|Male]] [[AADHAAR_NUMBER|203835321155]]
বৃত্তি: স্ব-নিয়োজিত ব্যৱসায়ী, পাইকাৰী বাণিজ্য
ঠিকনা: ১২ গান্ধী নগৰ, ৱাৰ্ড ৪, [[DISTRICT|Bangalore Urban]]
যোগাযোগ নম্বৰ: [[PHONE_NUMBER|9876543210]]
ইমেইল ঠিকনা: ranjan.sharma@example.com

হাস্পতালৰ বিৱৰণ
হাস্পতালৰ নাম: [[HOSPITAL_NAME|Apollo Hospital, Bangalore]]
ভৰ্তিৰ তাৰিখ: ১৬ মে’ ২০২৪
মুক্তিৰ তাৰিখ: ১৭ মে’ ২০২৪
চিকিৎসক: ড° প্ৰিয়া নায়াৰ

ক্লিনিকেল সাৰাংশ
ৰোগ…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `hospital_billing` (`hi`).
- **Errors:** `['dics_below_threshold:0.0']`
- **Preview:**

```
नवादा जिला अस्पताल, जिला [[DISTRICT|Nawada]]
पिन [[PIN_CODE|805130]] रोगी [[PATIENT_NAME|Ramesh Kumar]] MRN [[MRN|MRN-BR-2024-0815-001]]
पता [[RESIDENTIAL_ADDRESS|Bhadauni, Post Office, Nawada, Bihar 805130]] फोन [[PHONE_NUMBER|9876543210]]
ईमेल [[EMAIL_ADDRESS|ramesh.kumar.nawada@example.com]] पैन [[PAN_NUMBER|ABCDE1234F]]
लैंडलाइन [[TELEPHONE_LANDLINE|06322-222555]] वाहन [[VEHICLE_REGISTRATION|BR01AB1234]] (एक बार)
आधार [[AADHAAR_NUMBER|206501253007]] पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-BR-2…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `hospital_billing` (`mni`).
- **Errors:** `['span_alignment_failure', 'boundary_corruption_rate:0.2857142857142857']`
- **Preview:**

```
ꯍꯣꯁꯄꯤꯇꯥꯜ ꯕꯤꯜꯂꯤꯡ ꯏꯟꯚꯣꯏꯁ — [[HOSPITAL_NAME|[[NM0]]]] ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|[[NM1]]]]
ꯄꯤꯟ [[PIN_CODE|795105]] ꯄꯦꯁꯦꯟꯇ [[PATIENT_NAME|[[NM2]]]] ꯑꯦꯝ.ꯑꯥꯔ.ꯑꯦꯟ. [[MRN|THD-2024-0815-001]]
ꯑꯦꯗ꯭ꯔꯦꯁ [[RESIDENTIAL_ADDRESS|[[NM3]]]] ꯐꯣꯟ [[PHONE_NUMBER|9876543210]]
ꯏꯃꯦꯜ [[EMAIL_ADDRESS|lalita.devi@example.com]] ꯄꯦꯟ [[PAN_NUMBER|MNPAB1234C]]
ꯂꯦꯟꯗꯂꯥꯏꯟ [[TELEPHONE_LANDLINE|0385-2345678]] ꯚꯦꯍꯤꯀꯜ [[VEHICLE_REGISTRATION|MN01AB1234]] (ꯑꯃꯨꯛ)
ꯑꯥꯙꯥꯔ [[AADHAAR_NUMBER|206501253007]] ꯄꯣꯂꯤꯁꯤ [[INSURANCE_POLICY_NUMBER|POL-MH-2…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `hospital_billing` (`sd`).
- **Errors:** `['missing_required:PATIENT_NAME,HOSPITAL_NAME,MRN,DISTRICT,PIN_CODE,PHONE_NUMBER,AADHAAR_NUMBER,INSURANCE_POLICY_NUMBER,TAX_ID,TELEPHONE_LANDLINE,VEHICLE_REGISTRATION,EMAIL_ADDRESS,RESIDENTIAL_ADDRESS,PAN_NUMBER', 'phi_residue:14']`
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
بيلنگ / انوائس
مهاتما گانڌي اسپتال, بھيلواڙا
311001
عجمہ بانو
MGH-RJ-2024-0815
15 Shivaji Colony, Ward 12
9876543210
ujma.bano@example.com
RJUPA1234F
01482-234567
RJ14AB1234
206501253007
POL-RJ-2024-7781
29ABCDE1234F1Z5
بل جو تفصيل:
مشاورت فیس: ₹800
خون جا ٽيسٽ: ₹1,200
X-Ray Chest: ₹600
ECG: ₹400
دوائن جا چارجز: ₹1,500
روم چارجز (2 ڏينهن): ₹3,000
ڊاڪٽر جو فیس: ₹1,000
نرسنگ چارجز: ₹500
ٻيا خرچ: ₹300
سبٽوٽل: ₹9,300
GST (18%): ₹1,674
ٽوٽل رقم: ₹10,974
پيمنٽ موڊ: نقد
پيمنٽ اسٽيٽس: ادا ٿيل
مريضو جو …
```


## Surviving curated set

- languages: `{'as': 5, 'bn': 6, 'brx': 3, 'doi': 6, 'en': 6, 'gu': 6, 'hi': 4, 'kn': 6, 'kok': 6, 'ks': 6, 'mai': 6, 'ml': 6, 'mni': 4, 'mr': 6, 'ne': 6, 'or': 6, 'pa': 6, 'sa': 6, 'sat': 4, 'sd': 4, 'ta': 6, 'te': 6, 'ur': 6}`
- doc_types: `{'asha_worker_note': 13, 'automated_sms': 14, 'discharge_summary': 8, 'er_triage_notes': 8, 'hospital_billing': 14, 'insurance_claim': 9, 'lab_report': 7, 'opd_slip': 7, 'phc_register': 12, 'prescription': 8, 'radiology_report': 8, 'referral_letter': 11, 'surgical_note': 5, 'telemedicine_transcript': 2}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
