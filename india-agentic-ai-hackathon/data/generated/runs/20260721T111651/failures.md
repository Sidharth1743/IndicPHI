# Failures audit — `20260721T111651`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260721T111651/pipeline.resolved.yaml`
- **issue count:** **69** (hard=0, gen_soft=9, tr_soft=22, judge=30, auditor=8)
- **S4 entity_coverage_complete_rate:** `0.9565217391304348`
- **S4b script_fail_count:** `22`
- **S5 pass_rate:** `0.782608695652174`
- **S6 pass_rate / passed:** `0.9259259259259259` / `100`
- **curated docs:** `22`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `5afdbf29e52249fc95146ec7db5e2023` | `as` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `a215dd216aff46e7add35a2cb913a177` | `en` | `referral_letter` | `['entity_stuffing:AGE,DISTRICT,GENDER,HOSPITAL_ID,HOSPITAL_NAME,MRN,PHONE_NUMBER,REFERRAL_ID,RELATI…` |
| S4 soft | `a215dd216aff46e7add35a2cb913a177` | `en` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `85cdb818ce5740ed85a9bfb29cf57098` | `gu` | `radiology_report` | `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S4 soft | `9b16854e981048c59b1bc1efd2685bdf` | `hi` | `insurance_claim` | `['entity_stuffing:TOTAL_TAGS>32']` |
| S4 soft | `911448710ce34ff686d217211c009ba8` | `kn` | `insurance_claim` | `['missing_required_entities:BANK_ROUTING_NUMBER']` |
| S4 soft | `99d8e2b0dd9e42e6b270e50cb12c26c5` | `ks` | `insurance_claim` | `['entity_stuffing:AADHAAR_NUMBER,AGE,BANK_ACCOUNT_NUMBER,BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV…` |
| S4 soft | `9fe1a2291cd5496b92e09e133ea65d85` | `mai` | `lab_report` | `['invalid_type_tags:রোগীর_নাম,এম.আর.এন']` |
| S4 soft | `64ccf4937c134083910a24e651a7f14c` | `te` | `asha_worker_note` | `['missing_required_entities:VILLAGE,DISTRICT,RELIGION']` |
| S4b soft | `85cdb818ce5740ed85a9bfb29cf57098` | `gu` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `8c410a2e98134e9a91f1d50d5811a470` | `gu` | `er_triage_notes` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `c03b2ff49ffa439380a254bb9f8972f7` | `kok` | `hospital_billing` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `18a30340943543c59236f8f4e9379b8d` | `ks` | `asha_worker_note` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:ok` |
| S4b soft | `18a30340943543c59236f8f4e9379b8d` | `ks` | `automated_sms` | `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:ok` |
| S4b soft | `99d8e2b0dd9e42e6b270e50cb12c26c5` | `ks` | `asha_worker_note` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `99d8e2b0dd9e42e6b270e50cb12c26c5` | `ks` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `hospital_billing` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `discharge_summary` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `referral_letter` | `script_purity_failed:target_script_ratio:0.328<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `hospital_billing` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `discharge_summary` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `referral_letter` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `6319018329714b92a0a64f8228dc39b6` | `ne` | `prescription` | `script_purity_failed:target_script_ratio:0.082<0.35 attempt=1;generator_repair_failed:ok` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `opd_slip` | `Missing NM placeholder restore for ⟦NM6⟧;generator_repair_failed:target_script_ratio:0.000<0.35` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `phc_register` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1` |
| S4b soft | `49e7eef3f6644cc689038f044f77f052` | `sat` | `prescription` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `automated_sms` | `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1;generator_repair_failed:wrong…` |
| S4b soft | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `insurance_claim` | `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script…` |
| S4b soft | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `discharge_summary` | `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_i…` |
| S4b soft | `e9f9b9a22bcb47f28198db61b9bd4966` | `sd` | `discharge_summary` | `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_i…` |
| S4b soft | `e9f9b9a22bcb47f28198db61b9bd4966` | `sd` | `referral_letter` | `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:target_…` |
| S5 fail | `8b77264c0f7747c59ec191e95202ff7f` | `brx` | `automated_sms` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `8b77264c0f7747c59ec191e95202ff7f` | `brx` | `hospital_billing` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `fac14bf3d91143958fc1e8190e25c390` | `brx` | `insurance_claim` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `0cb542c8c62e4d52ac1c51fcfb93a238` | `doi` | `er_triage_notes` | score=0.15 flags=['dialect_script_impurity'] |
| S5 fail | `85cdb818ce5740ed85a9bfb29cf57098` | `gu` | `er_triage_notes` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `8c410a2e98134e9a91f1d50d5811a470` | `gu` | `er_triage_notes` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `fc0833a3fd3a4916849cba96e415af4b` | `kok` | `hospital_billing` | score=0.6 flags=['domain_persona_mismatch'] |
| S5 fail | `99d8e2b0dd9e42e6b270e50cb12c26c5` | `ks` | `insurance_claim` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `9fe1a2291cd5496b92e09e133ea65d85` | `mai` | `lab_report` | score=0.35 flags=['dialect_script_impurity', 'cross_language_entity_shift'] |
| S5 fail | `17f9c3d0179e4aa5a9546ec050612896` | `ml` | `hospital_billing` | score=0.6 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `80435bdcef24479390d6e6ae0b2aeeb1` | `ml` | `hospital_billing` | score=0.55 flags=['surrogate_plausibility_collapse', 'instruction_drift'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `hospital_billing` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `discharge_summary` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `1e23bb4e93b0465fa42494aee52e02ef` | `mni` | `referral_letter` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `hospital_billing` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `discharge_summary` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `d15c31be6c8e40a393e6e6f4f9562ea3` | `mni` | `referral_letter` | score=0.25 flags=['dialect_script_impurity'] |
| S5 fail | `24405a884af14bcba6e9c3657baebf83` | `pa` | `radiology_report` | score=0.45 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse', 'instruction_drift'] |
| S5 fail | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `phc_register` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `6e943dc3578249e38b9e61705d0912a9` | `sa` | `phc_register` | score=0.35 flags=['dialect_script_impurity'] |
| S5 fail | `49e7eef3f6644cc689038f044f77f052` | `sat` | `opd_slip` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `49e7eef3f6644cc689038f044f77f052` | `sat` | `phc_register` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `49e7eef3f6644cc689038f044f77f052` | `sat` | `prescription` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `automated_sms` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `c98c2d51b4ea4d0c947d6dfc0ee57383` | `sat` | `insurance_claim` | score=0.2 flags=['dialect_script_impurity'] |
| S5 fail | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `hospital_billing` | score=0.55 flags=['instruction_drift', 'length_violation'] |
| S5 fail | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `discharge_summary` | score=0.35 flags=['dialect_script_impurity', 'domain_persona_mismatch'] |
| S5 fail | `5c09bf9c92bb4474a1a128379f250e86` | `sd` | `referral_letter` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `e9f9b9a22bcb47f28198db61b9bd4966` | `sd` | `discharge_summary` | score=0.45 flags=['dialect_script_impurity'] |
| S5 fail | `e9f9b9a22bcb47f28198db61b9bd4966` | `sd` | `referral_letter` | score=0.35 flags=['dialect_script_impurity'] |
| S6 fail | `fe2793cf648244fa8cc427adc569983a` | `as` | `hospital_billing` | `['unknown_entity_types:BANK_NAME']` |
| S6 fail | `a215dd216aff46e7add35a2cb913a177` | `en` | `referral_letter` | `['entity_stuffing:PHONE_NUMBER,RELATIVE_NAME', 'dics_below_threshold:0.625']` |
| S6 fail | `a215dd216aff46e7add35a2cb913a177` | `en` | `radiology_report` | `['missing_required:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']` |
| S6 fail | `d89930b893984d4b96fbd0b492413321` | `kn` | `insurance_claim` | `['entity_stuffing:DISTRICT', 'phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `18a30340943543c59236f8f4e9379b8d` | `ks` | `asha_worker_note` | `['phi_residue:1']` |
| S6 fail | `18a30340943543c59236f8f4e9379b8d` | `ks` | `automated_sms` | `['script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `efe93c7f20fc46b7aa8ef936a09c90c6` | `mr` | `insurance_claim` | `['format:PAN_NUMBER:pan_format']` |
| S6 fail | `6319018329714b92a0a64f8228dc39b6` | `ne` | `prescription` | `['missing_required:HOSPITAL_NAME']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `insurance_claim` (`as`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Kumar]]: আপোনাৰ টি বি ফলো-আপ [[APPOINTMENT_ID|APT-240521-01]] তাৰিখে [[HOSPITAL_NAME|Bangalore PHC]] ত ড° [[DOCTOR_NAME|Dr. Anjali Sharma]] ৰ সৈতে হ’ব। এম আৰ এন [[MRN|MRN-2024-0815-001]]। অনুগ্ৰহ কৰি [[PHONE_NUMBER|9876512340]] ত নিশ্চিত কৰক।
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `referral_letter` (`en`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['AGE', 'DISTRICT', 'GENDER', 'HOSPITAL_ID', 'HOSPITAL_NAME', 'MRN', 'PHONE_NUMBER', 'REFERRAL_ID', 'RELATIVE_NAME']`
- **Raw reasons:** `['entity_stuffing:AGE,DISTRICT,GENDER,HOSPITAL_ID,HOSPITAL_NAME,MRN,PHONE_NUMBER,REFERRAL_ID,RELATIVE_NAME']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0912]] from [[HOSPITAL_NAME|YSR District Government Hospital]] / [[DOCTOR_NAME|Dr. Srinivas Reddy]]
Re: [[PATIENT_NAME|Lakshmi]], [[AGE|38]] / [[GENDER|Female]], District [[DISTRICT|Y.S.R. District]]
Reason: Persistent left-sided breast mass with progressive enlargement and new-onset nipple discharge, requiring oncological evaluation and management.

Dear Sir/Madam,

We are referring [[PATIENT_NAME|Lakshmi]], a 38-year-old female resident of [[VILLAGE|Chiluvuru]], [[DISTRICT|Y.S.R. District]], for further evaluation and management of a complex breast condition.…
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `radiology_report` (`en`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0912]] from [[HOSPITAL_NAME|YSR District Government Hospital]] / [[DOCTOR_NAME|Dr. Srinivas Reddy]]
Re: [[PATIENT_NAME|Lakshmi]], [[AGE|38]] / [[GENDER|Female]], District [[DISTRICT|Y.S.R. District]]
Reason: Persistent left-sided breast mass with progressive enlargement and new-onset nipple discharge, requiring oncological evaluation and management.

Dear Sir/Madam,

We are referring [[PATIENT_NAME|Lakshmi]], a 38-year-old female resident of [[VILLAGE|Chiluvuru]], [[DISTRICT|Y.S.R. District]], for further evaluation and management of a complex breast condition.…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `radiology_report` (`gu`).
- **Missing required tags:** `['DISTRICT', 'PHONE_NUMBER', 'HOSPITAL_ID', 'ABHA_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Mahesana District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Patel]] તરફથી
વિષે: [[PATIENT_NAME|Champaben Bhagat]], [[AGE|59]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Mahesana]]
કારણ: પેટમાં સતત અસ્વસ્થતા અને અસ્પષ્ટ વજન ઘટાડો

પ્રિય સાહેબ/મેડમ,

અમે [[PATIENT_NAME|Champaben Bhagat]], એક 59 વર્ષની મહિલા, મહેસાણા જિલ્લામાંથી, તેના જટિલ લાંબા ગાળાના રોગના વધુ મૂલ્યાંકન અને સંચાલન માટે તમને મોકલી રહ્યા છીએ. દર્દી ત્રણ મહિનાથી પેટમાં વધતી જતી અસ્વસ્થતા અને નોંધપાત્ર વજન ઘટાડાની મુખ્ય ફરિયાદ સાથે આવે છે. તમારા સંદર્ભ માટે તેની [[MRN|MRN-2024-0815-001]]…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `insurance_claim` (`hi`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['TOTAL_TAGS>32']`
- **Raw reasons:** `['entity_stuffing:TOTAL_TAGS>32']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
TPA दावा — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Abdul Rahman]] [[AGE|28]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|244345834584]]
अस्पताल [[HOSPITAL_NAME|Nawada District Hospital]] जिला [[DISTRICT|Nawada]]
मोटर / RTA वाहन [[VEHICLE_REGISTRATION|BR01A1234]] (सटीक रूप से एक बार)।
पैन [[PAN_NUMBER|ABCDR1234F]] IFSC [[IFSC_CODE|SBIN0001234]] खाता [[BANK_ACCOUNT_NUMBER|30912345678901]]
[[BANK_ROUTING_NUMBER|SBIN0001234]]
[[CREDIT_CARD_NUMBER|4111111111111111]]
[[CVV|123]]
[[PIN|8120]]
[[PHONE_NUMBER|9431122334]]
मुख्य शिकायत: रोगी लगातार खांसी, हेमोप्टाइसिस (रक्त के साथ …
```

### S4 generation soft-fail 6

- **What:** generation soft-fail on `insurance_claim` (`kn`).
- **Missing required tags:** `['BANK_ROUTING_NUMBER']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:BANK_ROUTING_NUMBER']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
[[PATIENT_NAME|Ramesh Gowda]]: ನಿಮ್ಮ ಟಿಬಿ ಫಾಲೋ-ಅಪ್ [[APPOINTMENT_ID|APT-240521-01]] ಆಗಿದೆ 21-ಮೇ ರಂದು 10:30 ಕ್ಕೆ ಡಾ. [[DOCTOR_NAME|Dr. Manjunath]] ಅವರೊಂದಿಗೆ [[HOSPITAL_NAME|Haveri District Hospital]] ನಲ್ಲಿ. ದಯವಿಟ್ಟು [[PHONE_NUMBER|9876543210]] ನಲ್ಲಿ ದೃಢೀಕರಿಸಿ. MRN [[MRN|MRN-2024-0815-001]].
```

### S4 generation soft-fail 7

- **What:** generation soft-fail on `insurance_claim` (`ks`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['AADHAAR_NUMBER', 'AGE', 'BANK_ACCOUNT_NUMBER', 'BANK_ROUTING_NUMBER', 'CREDIT_CARD_NUMBER', 'CVV', 'DISTRICT', 'GENDER', 'HOSPITAL_NAME', 'IFSC_CODE', 'INSURANCE_POLICY_NUMBER', 'PAN_NUMBER', 'PHONE_NUMBER', 'PIN', 'VEHICLE_REGISTRATION']`
- **Raw reasons:** `['entity_stuffing:AADHAAR_NUMBER,AGE,BANK_ACCOUNT_NUMBER,BANK_ROUTING_NUMBER,CREDIT_CARD_NUMBER,CVV,DISTRICT,GENDER,HOSPITAL_NAME,IFSC_CODE,INSURANCE_POLICY_NUMBER,PAN_NUMBER,PHONE_NUMBER,PIN,VEHICLE_REGISTRATION']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
پی ایچ سی رجسٹر — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] گام [[VILLAGE|Lidder]] ضِلہ [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Shabnam Bano]] [[AGE|59]] [[GENDER|Female]] | ہارمونل تھراپی پؠٹھ سٹیج II بریسٹ کارسینوما خٲطرٕ فالو اپ۔

مریضہ چھےٚ اکھ 59 ؤری ہنٛز ناخواندہ زنانہٕ، یۄس لیدر گام، اننت ناگ پؠٹھ چھےٚ، تہٕ فی الحال چھےٚ خاندرِتھ۔ تس چھےٚ کھووِرہِ طرفہٕ چھاتہِ منٛز گٔٹھِ ہنٛز تٲریٖخ، یمیُک پتہٕ 8 رٮ۪تن برونٛہہ ڈسٹرکٹ ہسپتال اننت ناگس منٛز لۆگمُت اوس۔ بایوپسی سۭتۍ گوو انویزو ڈکٹل کارسینوما، گریڈ II ہنٛز تصدیٖق۔ تس منٛز لمپیکٹومی تہٕ ایکسلری کلیئرنس 6 رٮ۪تن برونٛہہ کرنہٕ آمژ چھےٚ تہٕ…
```

### S4 generation soft-fail 8

- **What:** generation soft-fail on `lab_report` (`mai`).
- **Missing required tags:** `—`
- **Stuffing flags:** `—`
- **Raw reasons:** `['invalid_type_tags:রোগীর_নাম,এম.আর.এন']`
- **Preview:**

```
प्रयोगशाला रिपोर्ट — [[HOSPITAL_NAME|Araria District Hospital]] जिला [[DISTRICT|Araria]]
एम आर एन [[MRN|MRN-BR-2024-0815]] पेशेंट आई डी [[PATIENT_ID|PID-BR-7781]]
[[PATIENT_NAME|Sita Devi]] [[AGE|22]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
[[DOCTOR_NAME|Dr. Rajiv Kumar]] द्वारा आदेशित
परिणाम तालिका (एनालाइट मान PHI संस्थाओं के रूप में टैग नहीं किए गए हैं)।
कभी भी [[রোগীর_নাম|…]] / [[এম.আর.এন|…]] न लिखें — केवल PATIENT_NAME, MRN, आदि।

प्रयोगशाला निष्कर्ष
संग्रह की तिथि: 15 अगस्त 2024
नमूना: परिधीय रक्त (EDTA)
परीक्षण: डिफरेंशियल के साथ पूर्ण रक्त गणना (CBC)
संदर्भ सीमाएँ: हीमोग्लोब…
```

### S4 generation soft-fail 9

- **What:** generation soft-fail on `asha_worker_note` (`te`).
- **Missing required tags:** `['VILLAGE', 'DISTRICT', 'RELIGION']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:VILLAGE,DISTRICT,RELIGION']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ప్రాథమిక ఆరోగ్య కేంద్రం రిజిస్టర్ — [[HOSPITAL_NAME|PHC Mahbubnagar]] గ్రామం [[VILLAGE|Kothur]] జిల్లా [[DISTRICT|Mahbubnagar]]
[[PATIENT_NAME|Ramesh Reddy]] [[AGE|60]] [[GENDER|Male]] | స్టేజ్ III కొలొరెక్టల్ క్యాన్సర్ ఫాలో-అప్

రోగి 60 ఏళ్ల వృద్ధుడు, రిటైర్డ్ గృహిణి, వివాహితుడు, రక్తపోటు మరియు టైప్ 2 డయాబెటిస్ మెల్లిటస్ చరిత్ర ఉంది. స్టేజ్ III కొలొరెక్టల్ క్యాన్సర్ కోసం అడ్జువెంట్ కీమోథెరపీని పూర్తి చేసిన తర్వాత 3 నెలల ఫాలో-అప్ కోసం వచ్చారు. అతని ఇటీవలి CEA స్థాయి 3.2 ng/mL, ఇది గతంలో 3.5 ng/mL గా ఉన్న విలువ నుండి స్థిరంగా ఉంది. అతను స్వల్ప అలసటను నివేదించాడు కానీ కొత్తగా కడుపు నొప్పి, మలవి…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `er_triage_notes` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Mahesana District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Patel]]
Re: [[PATIENT_NAME|Champaben Bhagat]], [[AGE|59]] / [[GENDER|Female]], District [[DISTRICT|Mahesana]]
Reason: Persistent abdominal discomfort and unexplained weight loss

Dear Sir/Madam,

We are referring [[PATIENT_NAME|Champaben Bhagat]], a 59-year-old female from Mahesana …
```
- **Translated preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Mahesana District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Patel]] તરફથી
વિષે: [[PATIENT_NAME|Champaben Bhagat]], [[AGE|59]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Mahesana]]
કારણ: પેટમાં સતત અસ્વસ્થતા અને અસ્પષ્ટ વજન ઘટાડો

પ્રિય સાહેબ/મેડમ,

અમે [[PATIENT_NAME|Champaben Bhagat]], એક 59 વર્ષની મહિલા, મહેસાણા જિલ્લામાંથી, તેના જટિલ લાંબા ગાળાના રોગ…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `er_triage_notes` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Vadodara General Hospital]] / [[DOCTOR_NAME|Dr. Priya Nair]]
Re: [[PATIENT_NAME|Kavita Patel]], [[AGE|25]] / [[GENDER|Female]], District [[DISTRICT|Vadodara]]
Reason: Chronic insomnia and anxiety symptoms with associated mood lability, requiring specialized psychiatric evaluation and management.

Patient is a 25-year-old female homemaker…
```
- **Translated preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Vadodara General Hospital]] / [[DOCTOR_NAME|Dr. Priya Nair]] તરફથી
વિષે: [[PATIENT_NAME|Kavita Patel]], [[AGE|25]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Vadodara]]
કારણ: લાંબા ગાળાની અનિદ્રા અને ચિંતાના લક્ષણો સાથે સંકળાયેલ મૂડ અસ્થિરતા, જે માટે વિશિષ્ટ મનોચિકિત્સા મૂલ્યાંકન અને વ્યવસ્થાપનની જરૂર છે.

દર્દી 25 વર્ષની મહિલા ગૃહિણી છે, જે વડોદરા,…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `hospital_billing` (`kok`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
[[PATIENT_NAME|Ramesh Naik]]: appt [[APPOINTMENT_ID|APT-240615-02]] at [[HOSPITAL_NAME|District Hospital Karwar]] on 15-Jun 14:00 with [[DOCTOR_NAME|Dr. Priya Shenoy]]. Confirm on [[PHONE_NUMBER|9876543210]]. MRN [[MRN|MRN-2024-0615-002]].
```
- **Translated preview:**

```
[[PATIENT_NAME|Ramesh Naik]]: 15-Jun 14:00 वरांक [[HOSPITAL_NAME|District Hospital Karwar]] हांगा [[DOCTOR_NAME|Dr. Priya Shenoy]] हांचे वांगडा [[APPOINTMENT_ID|APT-240615-02]] वेळार भेट (appt) आसा. [[PHONE_NUMBER|9876543210]] चेर खात्री (confirm) करात. MRN [[MRN|MRN-2024-0615-002]].
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `asha_worker_note` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:ok`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Zainakadal]], District [[DISTRICT|Srinagar]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|40]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Shabnam Bano]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: Patient reports persistent fatigue and intermittent chest discomfort for the past three weeks. He has a history of hypertension and was recently referred to …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|زینیکدل]], District [[DISTRICT|سرینگر]]
Beneficiary [[PATIENT_NAME|محمد یوسف]], [[AGE|40]] / [[GENDER|مرد]]
ASHA: [[ASHA_WORKER_NAME|شبنم بانو]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: مریٖض چھُ پچھلن ترٛیون ہفتن پٮ۪ٹھ مُستقل تھکاوٹ تہٕ وقفہٕ وقفہٕ سان سینس منٛز تکلیف محسوس کران۔ أمس چھُ ہایپر ٹینشنُک تٲریٖخ تہٕ حال ہی منٛز چھُ تٔمۍ سٕنٛدِ پھیپھڑن منٛز کُ…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `automated_sms` (`ks`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:ok`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Zainakadal]], District [[DISTRICT|Srinagar]]
Beneficiary [[PATIENT_NAME|Mohammad Yousuf]], [[AGE|40]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Shabnam Bano]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: Patient reports persistent fatigue and intermittent chest discomfort for the past three weeks. He has a history of hypertension and was recently referred to …
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|زینیکدل]], District [[DISTRICT|سرینگر]]
Beneficiary [[PATIENT_NAME|محمد یوسف]], [[AGE|40]] / [[GENDER|مرد]]
ASHA: [[ASHA_WORKER_NAME|شبنم بانو]] | Phone [[PHONE_NUMBER|9419012345]]
Visit findings: مریٖض چھُ پچھلن ترٛیون ہفتن پٮ۪ٹھ مُستقل تھکاوٹ تہٕ وقفہٕ وقفہٕ سان سینس منٛز تکلیف محسوس کران۔ أمس چھُ ہایپر ٹینشنُک تٲریٖخ تہٕ حال ہی منٛز چھُ تٔمۍ سٕنٛدِ پھیپھڑن منٛز کُ…
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `asha_worker_note` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] Village [[VILLAGE|Lidder]] District [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Shabnam Bano]] [[AGE|59]] [[GENDER|Female]] | Follow-up for Stage II breast carcinoma on hormonal therapy.

Patient is a 59-year-old illiterate female hand embroiderer from Lidder village, Anantnag, currently married. She presents with a history of left-sided br…
```
- **Translated preview:**

```
پی ایچ سی رجسٹر — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] گام [[VILLAGE|Lidder]] ضِلہ [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Shabnam Bano]] [[AGE|59]] [[GENDER|Female]] | ہارمونل تھراپی پؠٹھ سٹیج II بریسٹ کارسینوما خٲطرٕ فالو اپ۔

مریضہ چھےٚ اکھ 59 ؤری ہنٛز ناخواندہ زنانہٕ، یۄس لیدر گام، اننت ناگ پؠٹھ چھےٚ، تہٕ فی الحال چھےٚ خاندرِتھ۔ تس چھےٚ کھووِرہِ طرفہٕ چھاتہِ منٛز گٔٹھِ ہنٛز تٲریٖخ، ی…
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `insurance_claim` (`ks`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] Village [[VILLAGE|Lidder]] District [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Shabnam Bano]] [[AGE|59]] [[GENDER|Female]] | Follow-up for Stage II breast carcinoma on hormonal therapy.

Patient is a 59-year-old illiterate female hand embroiderer from Lidder village, Anantnag, currently married. She presents with a history of left-sided br…
```
- **Translated preview:**

```
پی ایچ سی رجسٹر — [[HOSPITAL_NAME|Primary Health Centre Anantnag]] گام [[VILLAGE|Lidder]] ضِلہ [[DISTRICT|Anantnag]]
[[PATIENT_NAME|Shabnam Bano]] [[AGE|59]] [[GENDER|Female]] | ہارمونل تھراپی پؠٹھ سٹیج II بریسٹ کارسینوما خٲطرٕ فالو اپ۔

مریضہ چھےٚ اکھ 59 ؤری ہنٛز ناخواندہ زنانہٕ، یۄس لیدر گام، اننت ناگ پؠٹھ چھےٚ، تہٕ فی الحال چھےٚ خاندرِتھ۔ تس چھےٚ کھووِرہِ طرفہٕ چھاتہِ منٛز گٔٹھِ ہنٛز تٲریٖخ، ی…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `hospital_billing` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 9

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 10

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.328<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 11

- **What:** translation soft-fail on `hospital_billing` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 12

- **What:** translation soft-fail on `discharge_summary` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 13

- **What:** translation soft-fail on `referral_letter` (`mni`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|234567890123]]
Pho…
```

### S4b translation soft-fail 14

- **What:** translation soft-fail on `prescription` (`ne`).
- **Error:** `script_purity_failed:target_script_ratio:0.082<0.35 attempt=1;generator_repair_failed:ok`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Darjiling District Hospital]] | ID [[HOSPITAL_ID|DDH-WB-001]]
Patient: [[PATIENT_NAME|Kumar Sharma]] | DOB [[DOB|1970-05-22]] | Age: [[AGE|54]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Stock Clerk]] | MRN: [[MRN|OPD-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Anirban Chatterjee]]
Relative: [[RELATIVE_NAME|Sunita Sharma]] | Phone: [[PHONE_NUMBER|9832145678]]
Re…
```
- **Translated preview:**

```
ओपिडी स्लिप | [[HOSPITAL_NAME|Darjiling District Hospital]] | आइडी [[HOSPITAL_ID|DDH-WB-001]]
बिरामी: [[PATIENT_NAME|Kumar Sharma]] | जन्ममिति [[DOB|1970-05-22]] | उमेर: [[AGE|54]] | लिङ्ग: [[GENDER|Male]]
व्यवसाय: [[OCCUPATION|Stock Clerk]] | एमआरएन: [[MRN|OPD-2024-0815-001]] | डाक्टर: [[DOCTOR_NAME|Dr. Anirban Chatterjee]]
सम्बन्धित: [[RELATIVE_NAME|Sunita Sharma]] | फोन: [[PHONE_NUMBER|9832145…
```

### S4b translation soft-fail 15

- **What:** translation soft-fail on `opd_slip` (`sat`).
- **Error:** `Missing NM placeholder restore for ⟦NM6⟧;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```

### S4b translation soft-fail 16

- **What:** translation soft-fail on `phc_register` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```

### S4b translation soft-fail 17

- **What:** translation soft-fail on `prescription` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210…
```

### S4b translation soft-fail 18

- **What:** translation soft-fail on `automated_sms` (`sat`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Ol Chiki attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Ol Chiki`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Kashipur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Bikash Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Mina Hansda]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough and weight loss for two months. He feels weak and has difficulty breathing. He is worried about his health and the cost of treatmen…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|ᱠᱟᱹᱥᱤᱯᱩᱨ]], District [[DISTRICT|ᱵᱤᱨᱵᱷᱩᱢ]]
Beneficiary [[PATIENT_NAME|ᱵᱤᱠᱟᱹᱥ ᱢᱩᱨᱢᱩ]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|ᱢᱤᱱᱟ ᱦᱟᱱᱥᱫᱟᱹ]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: ᱨᱩᱜᱤ ᱫᱚ ᱵᱟᱨ ᱪᱟᱸᱫᱚ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱷᱩᱜ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱠᱟᱛᱷᱟᱭ ᱞᱟᱹᱭᱮᱫᱟ ᱾ ᱩᱱᱤ ᱫᱚ ᱞᱟᱸᱜᱟ ᱜᱮᱭ ᱵᱩᱡᱷᱟᱹᱣᱮᱫᱟ ᱟᱨ ᱥᱟᱸᱦᱮᱫ ᱦᱟᱛᱟᱣ ᱨᱮ ᱟᱱᱟᱴ ᱦᱩᱭᱩᱜ ᱛᱟᱭᱟ ᱾ ᱟᱡᱟᱜ ᱦᱚᱲᱢᱚ ᱟᱨ ᱴᱨᱤᱴᱢᱮᱱᱴ ᱨᱮᱭ…
```

### S4b translation soft-fail 19

- **What:** translation soft-fail on `insurance_claim` (`sat`).
- **Error:** `script_purity_failed:target_script_ratio:0.000<0.35 attempt=1;generator_repair_failed:target_script_ratio:0.000<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|Kashipur]], District [[DISTRICT|Birbhum]]
Beneficiary [[PATIENT_NAME|Bikash Murmu]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Mina Hansda]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough and weight loss for two months. He feels weak and has difficulty breathing. He is worried about his health and the cost of treatmen…
```
- **Translated preview:**

```
ASHA note — Village [[VILLAGE|ᱠᱟᱹᱥᱤᱯᱩᱨ]], District [[DISTRICT|ᱵᱤᱨᱵᱷᱩᱢ]]
Beneficiary [[PATIENT_NAME|ᱵᱤᱠᱟᱹᱥ ᱢᱩᱨᱢᱩ]], [[AGE|56]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|ᱢᱤᱱᱟ ᱦᱟᱱᱥᱫᱟᱹ]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: ᱨᱩᱜᱤ ᱫᱚ ᱵᱟᱨ ᱪᱟᱸᱫᱚ ᱠᱷᱚᱱ ᱞᱮᱛᱟᱲ ᱠᱷᱩᱜ ᱟᱨ ᱦᱟᱢᱟᱞ ᱠᱚᱢᱚᱜ ᱨᱮᱭᱟᱜ ᱠᱟᱛᱷᱟᱭ ᱞᱟᱹᱭᱮᱫᱟ ᱾ ᱩᱱᱤ ᱫᱚ ᱞᱟᱸᱜᱟ ᱜᱮᱭ ᱵᱩᱡᱷᱟᱹᱣᱮᱫᱟ ᱟᱨ ᱥᱟᱸᱦᱮᱫ ᱦᱟᱛᱟᱣ ᱨᱮ ᱟᱱᱟᱴ ᱦᱩᱭᱩᱜ ᱛᱟᱭᱟ ᱾ ᱟᱡᱟᱜ ᱦᱚᱲᱢᱚ ᱟᱨ ᱴᱨᱤᱴᱢᱮᱱᱴ ᱨᱮᱭ…
```

### S4b translation soft-fail 20

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] | Patient [[PATIENT_NAME|Ujma Bano]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Bhilwara]] PIN [[PIN_CODE|311001]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|RJ14AB1234]] (exactly once).
Patient [[PATIENT_NAME|Ujma Bano]] was admitted on 15 August 2024 for evaluation of persistent fever and generalized weakness. Investig…
```
- **Translated preview:**

```
بل (Invoice) — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] | مريضو [[PATIENT_NAME|Ujma Bano]] | MRN [[MRN|MRN-2024-0815-001]]
پتھو ضلع [[DISTRICT|Bhilwara]] پن [[PIN_CODE|311001]]
ايمبولينس / پارڪنگ گاڏي [[VEHICLE_REGISTRATION|RJ14AB1234]] (بلڪل هڪ ڀيرو).
مريضو [[PATIENT_NAME|Ujma Bano]] 15 آگسٽ 2024 تي مسلسل تپش ۽ عام ڪمزوريءَ جي چڪاس (evaluation) لاء داخل ڪيو ويو. چڪاسن ۾ CBC, ESR, ۽ بلڊ ڪلچر شام…
```

### S4b translation soft-fail 21

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:wrong_indic_script:Devanagari>Arabic`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Bhavnagar Civil Hospital]] | Patient [[PATIENT_NAME|Ahmed Mustafa]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Bhavnagar]] PIN [[PIN_CODE|364001]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ02CD5678]]
[[PATIENT_NAME|Ahmed Mustafa]] presented with a persistent cough, low-grade fever, and weight loss. Investigations including sputum smear microscopy and Ge…
```
- **Translated preview:**

```
بلٽ — [[HOSPITAL_NAME|Bhavnagar Civil Hospital]] | مريض [[PATIENT_NAME|Ahmed Mustafa]] | MRN [[MRN|MRN-2024-0815-001]]
پتھو ضلعو [[DISTRICT|Bhavnagar]] پن [[PIN_CODE|364001]]
ايمبولينس گاڏي [[VEHICLE_REGISTRATION|GJ02CD5678]]
[[PATIENT_NAME|Ahmed Mustafa]] پيش ٿيو مستقل کنگھ، گھٽ درجي جو تپ، ۽ وزن گھٽجڻ سان. جاچون بشمول کنگھ جو اسமியر مائڪروسڪوپي ۽ GeneXpert MTB/RIF ايسائي پلمونري ٽيبرڪولوسس جي ت…
```

### S4b translation soft-fail 22

- **What:** translation soft-fail on `referral_letter` (`sd`).
- **Error:** `script_purity_failed:wrong_indic_script:Devanagari>Arabic attempt=1;generator_repair_failed:target_script_ratio:0.011<0.35`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Bhavnagar Civil Hospital]] | Patient [[PATIENT_NAME|Ahmed Mustafa]] | MRN [[MRN|MRN-2024-0815-001]]
Address district [[DISTRICT|Bhavnagar]] PIN [[PIN_CODE|364001]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ02CD5678]]
[[PATIENT_NAME|Ahmed Mustafa]] presented with a persistent cough, low-grade fever, and weight loss. Investigations including sputum smear microscopy and Ge…
```
- **Translated preview:**

```
بلٽ — [[HOSPITAL_NAME|Bhavnagar Civil Hospital]] | مريض [[PATIENT_NAME|Ahmed Mustafa]] | MRN [[MRN|MRN-2024-0815-001]]
پتھو ضلعو [[DISTRICT|Bhavnagar]] پن [[PIN_CODE|364001]]
ايمبولينس گاڏي [[VEHICLE_REGISTRATION|GJ02CD5678]]
[[PATIENT_NAME|Ahmed Mustafa]] پيش ٿيو مستقل کنگھ، گھٽ درجي جو تپ، ۽ وزن گھٽجڻ سان. جاچون بشمول کنگھ جو اسமியر مائڪروسڪوپي ۽ GeneXpert MTB/RIF ايسائي پلمونري ٽيبرڪولوسس جي ت…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `automated_sms` (`brx`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Eastern Nagari/Assamese script and phrasing instead of required Bodo Devanagari; language not Bodo.
- **Preview:**

```
[[PATIENT_NAME|Ramesh Boro]]: 15-Aug 10:30-ত [[HOSPITAL_NAME|Baksa PHC]]-ত [[DOCTOR_NAME|Dr. Anjali Sharma]]-ৰ সৈতে appt [[APPOINTMENT_ID|APT-240815-02]] আছে। [[PHONE_NUMBER|9876543210]]-ত confirm কৰক। MRN [[MRN|MRN-2024-0815-002]]।
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `hospital_billing` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose is Hindi, not Bodo; all other elements (persona, entities, length, domain) align.
- **Preview:**

```
इनवॉइस — [[HOSPITAL_NAME|Bongaigaon Civil Hospital]] | पेशेंट [[PATIENT_NAME|Jibon Boro]] | MRN [[MRN|MRN-2024-0815-001]]
पता जिला [[DISTRICT|Baksa]] पिन [[PIN_CODE|781314]]
एम्बुलेंस वाहन [[VEHICLE_REGISTRATION|AS-01-A-9876]]
[[PATIENT_NAME|Jibon Boro]] बाक्सा जिला, असम का 24 वर्षीय पुरुष है। उसे अपेंडिक्स के लिए भर्ती किया गया था। यह प्रक्रिया 15 अगस्त 2024 को डॉ. अंजलि शर्मा द्वारा की गई थी। पेशेंट को 17 अगस्त 2024 को छुट्टी दे दी गई। उसका [[AADHAAR_NUMBER|203835321155]] और [[PHONE_NUMBER|98…
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `insurance_claim` (`brx`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Hindi vocabulary in Devanagari; expected Bodo language despite correct script and allowed ID tags.
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-ASS-2024-001234]]
[[PATIENT_NAME|Rina Boro]] [[AGE|29]] [[GENDER|Female]] आधार [[AADHAAR_NUMBER|203835321155]]
हस्पताल [[HOSPITAL_NAME|Kokrajhar Civil Hospital]] जिला [[DISTRICT|Kokrajhar]]
[[VEHICLE_REGISTRATION|AS-14-F-5678]]
[[PAN_NUMBER|FGHIJ5678K]]
[[IFSC_CODE|SBIN0005678]]
[[BANK_ACCOUNT_NUMBER|30912345678901]]
[[BANK_ROUTING_NUMBER|SBIN0005678]]
[[CREDIT_CARD_NUMBER|5555555555554444]]
[[CVV|456]]
[[PIN|7890]]
[[PHONE_NUMBER|9876543210]]
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `er_triage_notes` (`doi`).
- **Score / verdict:** `0.15` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Dogri Devanagari narrative absent.
- **Preview:**

```
ER Triage & Nursing Notes
ER Triage & Nursing Notes
Sub-District Hospital Reasi Encounter ENC-2024-0815-001
Shabnam Begum AGE 37 GENDER Female Ward ER Bed 03
Arrived by ambulance vehicle JK02-1234567.
Relative Ghulam Rasool Phone 9419123456 Dr Dr. Anjali Sharma
Vitals / acuity: Alert, oriented, in mild distress. BP 140/90, HR 110, RR 22, SpO2 96% on room air. Abdominal tenderness suprapubic, uterine fundus firm but tender.

Nursing notes:
Patient reports sudden onset of severe lower abdominal p…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `er_triage_notes` (`gu`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Romanized English-Gujarati mix instead of required Gujarati script; all entity types valid and persona fit ok.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Mahesana District Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|Champaben Bhagat]] [[AGE|59]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|03]]
Ambulance vehicle [[VEHICLE_REGISTRATION|GJ01AB1234]] thi aavyu.
Relative [[RELATIVE_NAME|Rameshbhai Bhagat]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Priya Patel]]
Vitals / acuity: Patient ne acute shortness of breath, 3 days thi productive cough with hemoptysis, ane low-g…
```

### S5 judge fail 6

- **What:** linguistic judge **fail** on `er_triage_notes` (`gu`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose entirely in English instead of Gujarati script.
- **Preview:**

```
ER triage — [[HOSPITAL_NAME|Vadodara Civil Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0912-001]]
[[PATIENT_NAME|Kavita Patel]] [[AGE|25]] [[GENDER|Female]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|04]]
Arrived by ambulance [[VEHICLE_REGISTRATION|GJ-06-AB-1234]]
Relative [[RELATIVE_NAME|Rameshbhai Patel]] Phone [[PHONE_NUMBER|9876543210]] Dr [[DOCTOR_NAME|Dr. Rajesh Mehta]]
Vitals / acuity: Patient is conscious, alert, oriented. Vitals stable.

Nursing notes:
Patient presented with chief compl…
```

### S5 judge fail 7

- **What:** linguistic judge **fail** on `hospital_billing` (`kok`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['domain_persona_mismatch']`
- **Reasoning:** 49yo female with postpartum hemorrhage after normal delivery violates maternal-health persona anchors.
- **Preview:**

```
बील — [[HOSPITAL_NAME|Sion Hospital]] | रुग्ण [[PATIENT_NAME|Sunita Patil]] | MRN [[MRN|MRN-2024-0915-001]]
पत्ता जिल्हा [[DISTRICT|Mumbai Suburban]] पिन [[PIN_CODE|400022]]
अँब्युलन्स वाहन [[VEHICLE_REGISTRATION|MH01AB1234]]

रुग्णाची म्हायती:
[[PATIENT_NAME|Sunita Patil]]
[[AADHAAR_NUMBER|203835321155]]
[[PHONE_NUMBER|9876543210]]
[[GENDER|Female]]
[[AGE|49]]
[[OCCUPATION|Homemaker]]
[[RESIDENTIAL_ADDRESS|45, Shivaji Park, Dadar, Mumbai]]

विमो म्हायती:
[[INSURANCE_POLICY_NUMBER|POL-MH-2024-9…
```

### S5 judge fail 8

- **What:** linguistic judge **fail** on `insurance_claim` (`ks`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose and form narrative in English; expected Kashmiri (Arabic script).
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-JK-2024-8901]]
[[PATIENT_NAME|Aisha Bano]] [[AGE|59]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|244554266125]]
Hospital [[HOSPITAL_NAME|District Hospital Anantnag]] District [[DISTRICT|Anantnag]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|JK02A-5432]]
PAN [[PAN_NUMBER|ABCPB1234C]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_ACCOUNT_NUMBER|11234567890]]
Bank Routing Number [[BANK_ROUTING_NUMBER|SBIN0001234]]
Credit Card [[CREDIT_CARD_NUMBER|511…
```

### S5 judge fail 9

- **What:** linguistic judge **fail** on `lab_report` (`mai`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'cross_language_entity_shift']`
- **Reasoning:** Prose in Hindi not Maithili; entity values (HOSPITAL_NAME, PATIENT_NAME, DISTRICT) use Bengali script instead of Devanagari.
- **Preview:**

```
प्रयोगशाला रिपोर्ट — [[HOSPITAL_NAME|আরারিয়া জেলা হাসপাতাল]] जिला [[DISTRICT|আরারিয়া]]
एम आर एन [[MRN|MRN-BR-2024-0815]] पेशेंट आई डी [[PATIENT_ID|PID-BR-7781]]
[[PATIENT_NAME|সীতা দেবী]] [[AGE|22]] [[GENDER|Female]] फोन [[PHONE_NUMBER|9876543210]]
[[DOCTOR_NAME|Dr. Rajiv Kumar]] द्वारा आदेशित

परिणाम तालिका (एनालाइट मान PHI संस्थाओं के रूप में टैग नहीं किए गए हैं)।

प्रयोगशाला निष्कर्ष
संग्रह की तिथि: 15 अगस्त 2024
नमूना: परिधीय रक्त (EDTA)
परीक्षण: डिफरेंशियल के साथ पूर्ण रक्त गणना (CBC)
सं…
```

### S5 judge fail 10

- **What:** linguistic judge **fail** on `hospital_billing` (`ml`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** District set to Ernakulam (with Kozhikode PIN) violating persona anchor; minor internal location inconsistency.
- **Preview:**

```
ഇൻവോയ്സ് — [[HOSPITAL_NAME|മരിയ ഹോസ്പിറ്റൽ]] | രോഗി [[PATIENT_NAME|അന്നമ്മ തോമസ്]] | MRN [[MRN|KDH-2024-0815-004]]
വിലാസം ജില്ല [[DISTRICT|എറണാകുളം]] പിൻ [[PIN_CODE|673001]]
ആംബുലൻസ് വാഹനം [[VEHICLE_REGISTRATION|KL07AB1234]] (കൃത്യം ഒരു തവണ).
രോഗി [[PATIENT_NAME|അന്നമ്മ തോമസ്]] MRN [[MRN|KDH-2024-0815-004]] സാധാരണ പ്രസവത്തിനായി പ്രവേശിപ്പിച്ചു.
രോഗി [[PATIENT_NAME|അന്നമ്മ തോമസ്]] ജനിച്ചത് [[DOB|2006-04-10]], പ്രായം [[AGE|18]], [[GENDER|Female]], വിവാഹിതയല്ല, ഗൃഹലക്ഷ്മി.
ബന്ധപ്പെടുക [[PHONE_NUMB…
```

### S5 judge fail 11

- **What:** linguistic judge **fail** on `hospital_billing` (`ml`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['surrogate_plausibility_collapse', 'instruction_drift']`
- **Reasoning:** District/hospital/PIN/vehicle details conflict with persona (Thiruvananthapuram) and internally inconsistent; otherwise correct Malayalam script and allowed entity types.
- **Preview:**

```
ഇൻവോയ്സ് — [[HOSPITAL_NAME|മാവേലിക്കര ജനറൽ ഹോസ്പിറ്റൽ]] | രോഗി [[PATIENT_NAME|അന്നമ്മ തോമസ്]] | MRN [[MRN|GH-THIR-2024-0815-001]]
വിലാസം ജില്ല [[DISTRICT|ആലപ്പുഴ]] പിൻ [[PIN_CODE|695001]]
ആംബുലൻസ് / പാർക്കിംഗ് വാഹനം [[VEHICLE_REGISTRATION|KL01AB1234]] (കൃത്യം ഒരു തവണ).
[[PHONE_NUMBER|9876543210]]
[[AADHAAR_NUMBER|203835321155]]
[[INSURANCE_POLICY_NUMBER|POL-KL-2024-456789]]
[[TAX_ID|29AAAPM1234C1ZV]]
[[TELEPHONE_LANDLINE|0471-2345678]]
```

### S5 judge fail 12

- **What:** linguistic judge **fail** on `hospital_billing` (`mni`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All narrative labels, structure and prose in English/Latin script; expected Manipuri Meitei script for clinical billing document.
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Lilati Devi]] | MRN [[MRN|THD-2024-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795135]]
Ambulance / parking vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
PATIENT DETAILS
Name: [[PATIENT_NAME|Lilati Devi]]
Age: [[AGE|21]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|203835321155]]
Phone: [[PHONE_NUMBER|9876543210]]
Email: [[EMAIL_ADDRESS|lilati.devi@example.com]]
Insurance Policy: […
```

### S5 judge fail 13

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Manipuri/Meitei script for narrative.
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Thoubal District Hospital]]
[[PATIENT_NAME|Lilati Devi]] DOB [[DOB|2003-04-18]] [[AGE|21]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-0815-001]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|04]]
Dr [[DOCTOR_NAME|Dr. Renu Thokchom]] | Course / advice: Patient was admitted with complaints of high-grade fever, chills, and generalized body aches for three days. On examination, she was febrile with a temperature of 102.4°F, tachycardic with a heart rate of 110 …
```

### S5 judge fail 14

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English; expected Manipuri/Meitei script not used. All entity types allowed and persona/domain fit.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0815]] from [[HOSPITAL_NAME|Thoubal District Hospital]] / [[DOCTOR_NAME|Dr. L. Renu Devi]]
Re: [[PATIENT_NAME|M. Sanjita Devi]], [[AGE|21]] / [[GENDER|Female]], District [[DISTRICT|Thoubal]]
Reason: Antenatal check-up for high-risk pregnancy due to severe anemia and history of threatened miscarriage.

Dear Sir/Madam,

This is to refer [[PATIENT_NAME|M. Sanjita Devi]], a 21-year-old female from [[VILLAGE|Lamlong]], Thoubal district, for specialized antenatal care.…
```

### S5 judge fail 15

- **What:** linguistic judge **fail** on `hospital_billing` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose and invoice narrative in English; expected Manipuri Meitei script not used.
- **Preview:**

```
Invoice — [[HOSPITAL_NAME|Thoubal District Hospital]] | Patient [[PATIENT_NAME|Rani Thangjam]] | MRN [[MRN|THD-2024-0715-001]]
Address district [[DISTRICT|Thoubal]] PIN [[PIN_CODE|795138]]
Ambulance vehicle [[VEHICLE_REGISTRATION|MN01AB1234]] (exactly once).
Patient Details:
Name: [[PATIENT_NAME|Rani Thangjam]]
Age: [[AGE|26]]
Gender: [[GENDER|Female]]
Aadhaar: [[AADHAAR_NUMBER|203835321155]]
Phone: [[PHONE_NUMBER|9412345678]]
Landline: [[TELEPHONE_LANDLINE|03842-222555]]
Insurance Policy: [[IN…
```

### S5 judge fail 16

- **What:** linguistic judge **fail** on `discharge_summary` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose in English instead of required Manipuri Meitei script; all entity types allowed and persona fit intact.
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Thoubal District Hospital]]
[[PATIENT_NAME|Nongthombam Bimol]] DOB [[DOB|1998-04-12]] [[AGE|26]] [[GENDER|Female]]
Adm [[ADMISSION_NUMBER|ADM-2024-0815-004]] Ward [[WARD_NUMBER|M2]] Bed [[BED_NUMBER|08]]
Dr [[DOCTOR_NAME|Dr. Renu Sharma]] | Course / advice: 26-year-old female patient from Thoubal, Manipur, rural area, presented with postpartum hemorrhage after normal vaginal delivery. Diagnosed with uterine atony, treated with oxytocin infusion and uterine ma…
```

### S5 judge fail 17

- **What:** linguistic judge **fail** on `referral_letter` (`mni`).
- **Score / verdict:** `0.25` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose almost entirely English; only one Meitei token present despite mni/Meitei requirement.
- **Preview:**

```
[[HOSPITAL_NAME|Thoubal District Hospital]] / [[DOCTOR_NAME|Dr. L. Ibohal]] ꯗꯒꯤ Referral [[REFERRAL_ID|REF-2024-0815]]
Re: [[PATIENT_NAME|S. Sanjita]], [[AGE|26]] / [[GENDER|Female]], District [[DISTRICT|Thoubal]]
Reason: Chronic lower back pain with radiating right leg symptoms for the past three months, suspected lumbar disc prolapse.

Dear Sir/Madam,

This is to refer our patient, S. Sanjita, a 26-year-old female from Thoubal district, for further evaluation and management of her condition. …
```

### S5 judge fail 18

- **What:** linguistic judge **fail** on `radiology_report` (`pa`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse', 'instruction_drift']`
- **Reasoning:** Male-coded name (Singh) with Female gender; district=Amritsar vs Barnala persona; otherwise correct Gurmukhi prose and valid tags.
- **Preview:**

```
ਰੇਡੀਓਲੋਜੀ ਰਿਪੋਰਟ — [[HOSPITAL_NAME|ਗੁਰੂ ਨਾਨਕ ਦੇਵ ਹਸਪਤਾਲ]] | [[PATIENT_NAME|ਜਸਵਿੰਦਰ ਸਿੰਘ]] [[AGE|80]] [[GENDER|Female]]
MRN [[MRN|MRN-PB-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]] | ਰਿਪੋਰਟ ਕੀਤੀ ਗਈ ਡਾ. [[DOCTOR_NAME|ਡਾ. ਗੁਰਚਰਨ ਸਿੰਘ]] ਦੁਆਰਾ
ਨਤੀਜੇ: ਛਾਤੀ ਦਾ ਐਕਸ-ਰੇ PA ਵਿਊ ਦੋਵਾਂ ਉੱਪਰਲੇ ਲੋਬਸ ਵਿੱਚ ਕਈ ਸਪਸ਼ਟ ਗੋਲ ਓਪੈਸਿਟੀਜ਼ (opacities) ਨੂੰ ਦਰਸਾਉਂਦਾ ਹੈ, ਜੋ ਠੀਕ ਹੋਏ ਪਲਮਨਰੀ ਟਿਊਬਰਕਲੋਸਿਸ ਦੇ ਅਨੁਕੂਲ ਹੈ। ਕੋਈ ਸਰਗਰਮ ਕੈਵਿਟੇਸ਼ਨ ਜਾਂ ਪਲੂਰਲ ਇਫਿਊਜ਼ਨ ਨਹੀਂ ਦੇਖਿਆ ਗਿਆ। ਦਿਲ ਦੀ ਸ਼ਕਲ ਆਮ ਸੀਮਾਵਾਂ ਦੇ ਅੰਦਰ ਹੈ। ਫੇਫੜਿਆ…
```

### S5 judge fail 19

- **What:** linguistic judge **fail** on `phc_register` (`sa`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose language is Hindi (modern register) not Sanskrit despite Devanagari script and correct entity tags.
- **Preview:**

```
प्राथमिक स्वास्थ्य केंद्र रजिस्टर — [[HOSPITAL_NAME|PHC Bundi Urban]] ग्राम [[VILLAGE|Ramganj]] जिला [[DISTRICT|Bundi]]
[[PATIENT_NAME|Kavita Kumari]] [[AGE|19]] [[GENDER|Female]] | द्वितीय त्रैमासिक प्रसव-पूर्व जांच

रोगी कवित कुमारी, 19 वर्षीया अविवाहिता, रामगंज ग्राम की निवासी, नियमित प्रसव-पूर्व जांच के लिए प्रस्तुत हुई। उसकी अंतिम मासिक धर्म तिथि लगभग 16 सप्ताह पूर्व थी, और वह हाल ही में पहली बार गर्भस्थ शिशु की हलचल महसूस करने की सूचना देती है। उसे कोई ज्ञात दीर्घकालिक बीमारी नहीं है और व…
```

### S5 judge fail 20

- **What:** linguistic judge **fail** on `phc_register` (`sa`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose is Hindi (modern register) not Sanskrit; all other constraints met.
- **Preview:**

```
प्राथमिक स्वास्थ्य केंद्र रजिस्टर प्रविष्टि — [[HOSPITAL_NAME|प्राथमिक स्वास्थ्य केंद्र, कानपुर नगर]] शहरी वार्ड [[VILLAGE|शहरी वार्ड 4]] जिला [[DISTRICT|कानपुर नगर]]
[[PATIENT_NAME|रोहन शर्मा]] [[AGE|19]] [[GENDER|Male]] | रोगी ने निरंतर खांसी और अल्प ज्वर की शिकायत की।

रोगी का इतिहास:
रोगी 19 वर्षीय अविवाहित पुरुष है, जो कानपुर नगर जिले के शहरी वार्ड 4 में निवास करता है। वह वर्तमान में बेरोजगार है और उसने अपनी माध्यमिक शिक्षा पूर्ण की है। उसकी प्रथम भाषा संस्कृत है। वह कभी-कभी चिंता की रिपोर…
```

### S5 judge fail 21

- **What:** linguistic judge **fail** on `opd_slip` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English; expected Santali Ol Chiki script not used.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Ranchi District Hospital]] | ID [[HOSPITAL_ID|RCH-001]]
Patient: [[PATIENT_NAME|Phulo Murmu]] | DOB [[DOB|1992-08-22]] | Age: [[AGE|32]] | Gender: [[GENDER|Female]]
Occupation: [[OCCUPATION|Wireman, Light and Power]] | MRN: [[MRN|RCH-OPD-2024-0822-001]] | Doctor: [[DOCTOR_NAME|Dr. Sanjay Kumar]]
Relative: [[RELATIVE_NAME|Sanjay Murmu]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[EMPLOYEE_ID|EMP-RCH-045]] | District: [[DISTRICT|Ranchi]]
Chief complaint: Per…
```

### S5 judge fail 22

- **What:** linguistic judge **fail** on `phc_register` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose entirely in English instead of required Santali Ol Chiki; all other elements (tags, persona, content) acceptable.
- **Preview:**

```
PHC register — [[HOSPITAL_NAME|Primary Health Centre, Kanke]] Village [[VILLAGE|Kanke]] District [[DISTRICT|Ranchi]]
[[PATIENT_NAME|Phoolmani Murmu]] [[AGE|32]] [[GENDER|Female]] | Anxiety and competitive behavior

Patient presents with chief complaint of persistent worry and irritability for the past two months. She reports difficulty sleeping and feeling restless, especially when comparing her family's progress to neighbors. The patient's husband notes she often becomes argumentative over min…
```

### S5 judge fail 23

- **What:** linguistic judge **fail** on `prescription` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in English/Latin; no Santali Ol Chiki narrative as required for expected language.
- **Preview:**

```
Prescription — [[HOSPITAL_NAME|Ranchi District Hospital]]
Patient [[PATIENT_NAME|Santi Murmu]], [[AGE|32]] / [[GENDER|Female]], MRN [[MRN|RCH-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Priya Singh]]
Rx: Paracetamol 500mg one tablet orally every six hours as needed for fever.
[[PATIENT_ID|PID-RCH-2024-0815-001]]
[[ABHA_ID|12-3456-7890-1234]]
[[PHONE_NUMBER|9431056789]]
[[DISTRICT|Ranchi]]
[[RESIDENTIAL_ADDRESS|Village: Gurgutu, Post: Gurgutu, Ranchi, Jharkhand 834001]]
[[ABHA_ADDRESS|santi.murmu@abdm…
```

### S5 judge fail 24

- **What:** linguistic judge **fail** on `automated_sms` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Prose uses Bengali script instead of required Santali Ol Chiki; all other elements (entities, persona, length) acceptable.
- **Preview:**

```
[[PATIENT_NAME|Bikash Murmu]]: 21-May 10:30-এ [[HOSPITAL_NAME|Birbhum District Hospital]]-এ [[DOCTOR_NAME|Dr. S. K. Chatterjee]]-এর সাথে অ্যাপয়েন্টমেন্ট [[APPOINTMENT_ID|APT-240521-02]]। [[PHONE_NUMBER|9876543210]]-এ নিশ্চিত করুন। MRN [[MRN|MRN-2024-0815-002]]।
```

### S5 judge fail 25

- **What:** linguistic judge **fail** on `insurance_claim` (`sat`).
- **Score / verdict:** `0.2` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical narrative prose entirely in English; expected Santali Ol Chiki script for all body text.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-WB-2024-7781]]
Claimant [[PATIENT_NAME|Bikash Murmu]] [[AGE|56]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|229337586155]]
Hospital [[HOSPITAL_NAME|Birbhum District Hospital]] District [[DISTRICT|Birbhum]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|WB01AB1234]] (exactly once).
PAN [[PAN_NUMBER|ABCDE1234F]] IFSC [[IFSC_CODE|SBIN0001234]] account [[BANK_ACCOUNT_NUMBER|50200012345678]]
Bank Routing [[BANK_ROUTING_NUMBER|SBIN0001234]]
Credit Card [[CRE…
```

### S5 judge fail 26

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift', 'length_violation']`
- **Reasoning:** Sindhi Arabic-script prose matches expectation and persona fit is good, but content is a long clinical narrative rather than billing/invoice format; includes excess chart-style details without charges or itemization.
- **Preview:**

```
بلٽ — [[HOSPITAL_NAME|Mahatma Gandhi Hospital]] | مريض [[PATIENT_NAME|Ujma Bano]] | MRN [[MRN|MRN-2024-0815-001]]
پتھو ضلعو [[DISTRICT|Bhilwara]] پن [[PIN_CODE|311001]]
ايمبولينس / پارڪنگ گاڏي [[VEHICLE_REGISTRATION|RJ14AB1234]] (بلڪل ڀيرو).
مريض [[PATIENT_NAME|Ujma Bano]] 15 آگسٽ 2024 تي مستقل تپش ۽ عام ڪمزوريءَ جي چڪاس لاء داخل ڪيو ويو. چڪاسن ۾ CBC، ESR، ۽ بلڊ ڪلچر جو حڪم ڏنو ويو. مريض کي سخت ڪميونٽي-اڪوائرڊ نمونيا جي تشخيص ڪئي وئي ۽ انٽراوينيوس سيفتريڪسون ۽ ائزيٿرومائيسن شروع ڪيائون. هن علاج…
```

### S5 judge fail 27

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity', 'domain_persona_mismatch']`
- **Reasoning:** Narrative prose uses Devanagari instead of required Arabic script for Sindhi; age 47 with normal vaginal delivery and PPH is implausible geriatric maternal case.
- **Preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|Mahatma Gandhi Hospital, Bhilwara]]
[[PATIENT_NAME|Ujma Bano]] जन्म तारीख [[DOB|1977-09-15]] [[AGE|47]] [[GENDER|Female]]
भर्ती तारीख [[ADMISSION_NUMBER|ADM-2024-0815-001]] वार्ड [[WARD_NUMBER|B2]] खाट [[BED_NUMBER|12]]
डाक्टर [[DOCTOR_NAME|Dr. Anjali Sharma]] | इलाज / मशवरो: मरीज़ खे नॉर्मल योनि प्रसव खां पोइ रति जे वहाक (postpartum hemorrhage) जे इंतज़ाम लाइ भर्ती कयो वयो हो। खेस ज़रूरत मूजिबि गर्भाशय खे सिकोड़ण वारियूं दवायूं (uterotonics) ऐं रति जो चढ़ावो (b…
```

### S5 judge fail 28

- **What:** linguistic judge **fail** on `referral_letter` (`sd`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** All clinical prose in Devanagari; expected Sindhi Arabic script. No other mismatches.
- **Preview:**

```
रेफरल [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|District Hospital Bhilwara]] खां / [[DOCTOR_NAME|Dr. Rajesh Kumar]]
बारे में: [[PATIENT_NAME|Ujma Bano]], [[AGE|47]] / [[GENDER|Female]], ज़िलो [[DISTRICT|Bhilwara]]
सबब: मुस्तक़िल खोघ सां गॾु वज़नु घटि थियणु ऐं साहु खणण में तकलीफ़, शक थियल फेफड़नि जो तपेदिक (पल्मोनरी ट्यूबरकुलोसिस) ऐं गॾु मौजूद हाई ब्लड प्रेशर।

मरीज़ [[PATIENT_NAME|Ujma Bano]] हिक 47 सालन जी औरत आहे जेका भीलवाड़ा, राजस्थान खां आहे, वधीक जांच लाइ मोकली वई आहे, छो त खेस 3 हफ़्…
```

### S5 judge fail 29

- **What:** linguistic judge **fail** on `discharge_summary` (`sd`).
- **Score / verdict:** `0.45` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose uses Devanagari script instead of required Arabic script for Sindhi; all entity types allowed, persona/domain fit, length and content otherwise plausible.
- **Preview:**

```
डिस्चार्ज समरी — [[HOSPITAL_NAME|Bhavnagar Civil Hospital]]
[[PATIENT_NAME|Ahmed Mustafa]] जन्म तारीख [[DOB|2002-04-18]] [[AGE|22]] [[GENDER|Male]]
भर्ती तारीख [[ADMISSION_NUMBER|ADM-2024-0815-001]] वार्ड [[WARD_NUMBER|A1]] बेड [[BED_NUMBER|05]]
डॉक्टर [[DOCTOR_NAME|Dr. Rajesh Patel]] | इलाज / सलाह: मरीज़ हिकु 22 सालन जो मर्द बिल्डिंग इंसुलेटर आहे, जेको एक्यूट गैस्ट्रोएंटेराइटिस जे इतिहास सां भर्ती थियो हो। खेस 3 ॾींहुं खां पाणीअ वांॻुरि पाख़ानो, पेट में मरोड़ ऐं हलको बुख़ारु हो। जांच दौरान, खे…
```

### S5 judge fail 30

- **What:** linguistic judge **fail** on `referral_letter` (`sd`).
- **Score / verdict:** `0.35` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose uses Devanagari script with Hindi framing instead of required Sindhi Arabic script; all entities valid and persona/domain fit otherwise.
- **Preview:**

```
सिंधी (अरबी लिपि) में अनुवाद:

रेफरल [[REFERRAL_ID|REF-2024-0815]] [[HOSPITAL_NAME|Bhavnagar Civil Hospital]] खां / [[DOCTOR_NAME|Dr. Rajesh Patel]]
बारे में: [[PATIENT_NAME|Ahmed Mustafa]], [[AGE|22]] / [[GENDER|Male]], ज़िलो [[DISTRICT|Bhavnagar]]
वजह: एक्यूट अपेंडिसाइटिस सां गॾु पेरिटोनाइटिस, जहिं में इमरजेंसी सर्जिकल दख़लअंदाज़ीअ जी ज़रूरत आहे।

मरीज़ अहमद मुस्तफ़ा, 22 सालन जो मर्द, जेको बिल्डिंग इंसुलेटर आहे, इमरजेंसी डिपार्टमेंट में 24 कलाकन खां पेट जे हेठें साजे पासे में वधंदड़ दुख सां ग…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `hospital_billing` (`as`).
- **Errors:** `['unknown_entity_types:BANK_NAME']`
- **Preview:**

```
বিল — [[HOSPITAL_NAME|Sivasagar Cancer Care Centre]] | ৰোগী [[PATIENT_NAME|Ranjan Gogoi]] | MRN [[MRN|MRN-SC-2024-001]]
ঠিকনা জিলা [[DISTRICT|Sivasagar]] পিন [[PIN_CODE|785001]]
এম্বুলেন্স বাহন [[VEHICLE_REGISTRATION|AS-18-B-9876]] (ঠিক এবাৰ)।

ৰোগীৰ বিৱৰণ:
নাম: [[PATIENT_NAME|Ranjan Gogoi]]
বয়স: [[AGE|30]]
লিংগ: [[GENDER|Male]]
ঠিকনা: [[RESIDENTIAL_ADDRESS|House No. 15, Ward 3, Jorhat Road, Sivasagar]]
ফোন: [[PHONE_NUMBER|9876543210]]
লেণ্ডলাইন: [[TELEPHONE_LANDLINE|03776-222555]]
আধাৰ: [[AAD…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `referral_letter` (`en`).
- **Errors:** `['entity_stuffing:PHONE_NUMBER,RELATIVE_NAME', 'dics_below_threshold:0.625']`
- **Cause:** tag dump / over-repetition of entity TYPEs.
- **Preview:**

```
Referral [[REFERRAL_ID|REF-2024-0912]] from [[HOSPITAL_NAME|YSR District Government Hospital]] / [[DOCTOR_NAME|Dr. Srinivas Reddy]]
Re: [[PATIENT_NAME|Lakshmi]], [[AGE|38]] / [[GENDER|Female]], District [[DISTRICT|Y.S.R. District]]
Reason: Persistent left-sided breast mass with progressive enlargement and new-onset nipple discharge, requiring oncological evaluation and management.

Dear Sir/Madam,

We are referring [[PATIENT_NAME|Lakshmi]], a 38-year-old female resident of [[VILLAGE|Chiluvuru]]…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `radiology_report` (`en`).
- **Errors:** `['missing_required:DISTRICT,PHONE_NUMBER,HOSPITAL_ID,ABHA_ID']`
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
Imaging report — [[HOSPITAL_NAME|District Hospital Kadapa]] | [[PATIENT_NAME|Sujatha]] [[AGE|38]] [[GENDER|Female]]
MRN [[MRN|MRN-2024-0815-001]] Encounter [[ENCOUNTER_ID|ENC-55601]] | Reported by Dr [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Findings: Plain radiograph of the chest was performed on the patient. The lung fields are clear with no evidence of consolidation, effusion, or pneumothorax. The cardiac silhouette is within normal limits. The bony thorax, including the ribs and clavicles, appears u…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `insurance_claim` (`kn`).
- **Errors:** `['entity_stuffing:DISTRICT', 'phi_residue:1', 'script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Cause:** tag dump / over-repetition of entity TYPEs.
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Ramesh Kumar]] [[AGE|28]] [[GENDER|Male]] Aadhaar [[AADHAAR_NUMBER|248090102804]]
Hospital [[HOSPITAL_NAME|Chamarajanagar District Hospital]] District [[DISTRICT|Chamarajanagar]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|KA02H1234]]
PAN [[PAN_NUMBER|FGHIJ5678K]] IFSC [[IFSC_CODE|SBIN0000123]] account [[BANK_ACCOUNT_NUMBER|6050100123456789]]
Bank Routing [[BANK_ROUTING_NUMBER|SBIN0000123]]
Credit Card [[CREDIT_CARD_N…
```

### S6 auditor fail 5

- **What:** deterministic auditor **fail** on `asha_worker_note` (`ks`).
- **Errors:** `['phi_residue:1']`
- **Preview:**

```
ASHA Worker Note
Oncology / Complex Chronic Care
HOSPITAL_NAME: SKIMS, Srinagar
PATIENT_NAME: [[PATIENT_NAME|مۆحمّد یوسف]]
AGE: [[AGE|40]]
GENDER: [[GENDER|Male]]
ASHA_WORKER_NAME: [[ASHA_WORKER_NAME|شبنم بانو]]
VILLAGE: [[VILLAGE|زینیکدال]]
DISTRICT: [[DISTRICT|سرینگر]]
PHONE_NUMBER: [[PHONE_NUMBER|9419012345]]
RELATIVE_NAME: [[RELATIVE_NAME|عائشہ یوسف]]
BPL_RATION_CARD: [[BPL_RATION_CARD|BPL-JK-2021-004567]]
VOTER_ID: [[VOTER_ID|JK012345678]]
RELIGION: [[RELIGION|Muslim]]
Visit findings: مریٖ…
```

### S6 auditor fail 6

- **What:** deterministic auditor **fail** on `automated_sms` (`ks`).
- **Errors:** `['script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
[[PATIENT_NAME|محمد یوسف]], [[PHONE_NUMBER|9876543210]], [[APPOINTMENT_ID|APT-240521-02]] is with Dr. [[DOCTOR_NAME|ڈاکٹر عیجاز احمد]] at [[HOSPITAL_NAME|ایس ایم ایچ ایس ہسپتال]] on 21-May at 10:30 AM with MRN [[MRN|123456789]]. Please confirm this.
```

### S6 auditor fail 7

- **What:** deterministic auditor **fail** on `insurance_claim` (`mr`).
- **Errors:** `['format:PAN_NUMBER:pan_format']`
- **Preview:**

```
TPA क्लेम — पॉलिसी [[INSURANCE_POLICY_NUMBER|POL-MH-2024-8891]]
रुग्ण माहिती:
[[PATIENT_NAME|Ramesh Patil]] [[AGE|51]] [[GENDER|Male]] आधार [[AADHAAR_NUMBER|223339454317]]
[[HOSPITAL_NAME|Chhatrapati Pramilatai Raje Hospital]] जिल्हा [[DISTRICT|Kolhapur]]
वाहन / आरटीए [[VEHICLE_REGISTRATION|MH04AB1234]] (नेमके एकदा).
पॅन [[PAN_NUMBER|PATILR1234C]] आयएफएससी [[IFSC_CODE|SBIN0001234]] खाते [[BANK_ACCOUNT_NUMBER|50200012345678]]
[[BANK_ROUTING_NUMBER|SBIN0001234]]
[[CREDIT_CARD_NUMBER|4111111111111…
```

### S6 auditor fail 8

- **What:** deterministic auditor **fail** on `prescription` (`ne`).
- **Errors:** `['missing_required:HOSPITAL_NAME']`
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
नेपाल बङ्गला स्पाइनल एन्ड जनरल हस्पिटल
बिरामी [[PATIENT_NAME|रश्मी चन्द्र राय]], [[AGE|54]] / [[GENDER|Male]], MRN [[MRN|NB-2024-0815-001]]
डाक्टर [[DOCTOR_NAME|आनन्द शर्मा]]
[[PHONE_NUMBER|9832145678]]
[[DISTRICT|दार्चुला]]
[[RESIDENTIAL_ADDRESS|12, हिल भ्यु रोड, कुरसेङ, पश्चिम बङ्गाल 734301]]
[[PATIENT_ID|NB-PAT-2024-0815-001]]
[[ABHA_ID|ABHA-WB-1234-5678]]
Rx: मेटफर्मिन 500 mg दिनको दुई पटक खानासँगै, एटोरभास्टाटिन 20 mg सुत्ने बेलामा दिनको एक पटक, एस्पिरिन 75 mg दिनको एक पटक, टेलमिसार्टन 40 …
```


## Surviving curated set

- languages: `{'as': 1, 'bn': 1, 'brx': 1, 'doi': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'kok': 1, 'ks': 1, 'mai': 1, 'ml': 1, 'mr': 1, 'ne': 1, 'or': 1, 'pa': 1, 'sa': 1, 'sat': 1, 'sd': 1, 'ta': 1, 'te': 1, 'ur': 1}`
- doc_types: `{'asha_worker_note': 5, 'automated_sms': 4, 'er_triage_notes': 1, 'hospital_billing': 2, 'insurance_claim': 1, 'lab_report': 1, 'opd_slip': 3, 'phc_register': 1, 'prescription': 1, 'radiology_report': 1, 'referral_letter': 2}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
