# Failures audit — `20260720T180107`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260720T180107/pipeline.resolved.yaml`
- **issue count:** **13** (hard=0, gen_soft=5, tr_soft=0, judge=5, auditor=3)
- **S4 entity_coverage_complete_rate:** `0.8`
- **S4b script_fail_count:** `0`
- **S5 pass_rate:** `0.75`
- **S6 pass_rate / passed:** `0.8` / `12`
- **curated docs:** `8`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `12e31823de794a7ba4bbdd82d74370f3` | `bn` | `telemedicine_transcript` | `['entity_stuffing:AGE,GENDER,PHONE_NUMBER,EMAIL_ADDRESS,HOSPITAL_NAME']` |
| S4 soft | `6368e3f4fd8448f69e688a500e614e9a` | `bn` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `b2958cfe1a8946b88be2780178fdfa1a` | `hi` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `28085860cdbd4188a9769b9902f6890d` | `mr` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `92bfd5dd40004d968c6c58538433407c` | `ta` | `opd_slip` | `['missing_required_entities:HOSPITAL_NAME,EMPLOYEE_ID']` |
| S5 fail | `b2958cfe1a8946b88be2780178fdfa1a` | `hi` | `opd_slip` | score=0.55 flags=['instruction_drift'] |
| S5 fail | `315f86955b8745379f872ad0cf6fc38b` | `ml` | `discharge_summary` | score=0.55 flags=['instruction_drift', 'surrogate_plausibility_collapse'] |
| S5 fail | `588a02fac9ad4b8d82b655e6d190a312` | `ml` | `discharge_summary` | score=0.6 flags=['domain_persona_mismatch', 'surrogate_plausibility_collapse'] |
| S5 fail | `28085860cdbd4188a9769b9902f6890d` | `mr` | `opd_slip` | score=0.55 flags=['instruction_drift', 'domain_persona_mismatch'] |
| S5 fail | `2d4ff3d6af4a4c5dbf5bd49b6c47ed2a` | `pa` | `asha_worker_note` | score=0.72 flags=['surrogate_plausibility_collapse'] |
| S6 fail | `12e31823de794a7ba4bbdd82d74370f3` | `bn` | `telemedicine_transcript` | `['entity_stuffing_total_tags:30>24', 'entity_stuffing:AGE,EMAIL_ADDRESS,GENDER,HOSPITAL_NAME,PHONE_…` |
| S6 fail | `6368e3f4fd8448f69e688a500e614e9a` | `bn` | `opd_slip` | `['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITA…` |
| S6 fail | `92bfd5dd40004d968c6c58538433407c` | `ta` | `opd_slip` | `['missing_required:HOSPITAL_NAME,EMPLOYEE_ID', 'upstream_generation_soft_fail:missing_required_enti…` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `telemedicine_transcript` (`bn`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['AGE', 'GENDER', 'PHONE_NUMBER', 'EMAIL_ADDRESS', 'HOSPITAL_NAME']`
- **Raw reasons:** `['entity_stuffing:AGE,GENDER,PHONE_NUMBER,EMAIL_ADDRESS,HOSPITAL_NAME']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
--- সেশন ---
অ্যাপয়েন্টমেন্ট [[APPOINTMENT_ID|APT-240521-01]] পোর্টাল [[URL|https://tele.example.in/visit]]
ক্লায়েন্ট আই.পি [[IP_ADDRESS|103.21.244.12]] ডিভাইস আই.এম.ই.আই [[IMEI_NUMBER|356938035643809]]
ম্যাক [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- চ্যাট ---
রোগী [[PATIENT_NAME|Mohitosh Das]] [[AGE|37]] [[GENDER|Male]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|mohitosh.das.art@example.com]]): ডাক্তার, আমি সম্প্রতি খুব উদ্বিগ্ন বোধ করছি। আমার হৃদস্পন্দন বেড়ে যায় এবং আমি ভালোভাবে ঘুমাতে পারি না।
ডাক্তার [[DOCTOR_NAME|Dr. Ananya Roy]] ([[HOSPITAL_NAME|Tripura Institute of Psychiatry]]): মো…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `opd_slip` (`bn`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ও.পি.ডি স্লিপ | বীরভূম জেলা হাসপাতাল | আইডি [[HOSPITAL_ID|DH-WB-021]]
রোগী: [[PATIENT_NAME|Sanjay Kumar]] | জন্ম তারিখ [[DOB|1989-07-22]] | বয়স: [[AGE|35]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Labourer, Other]] | মেডিকেল রেকর্ড নম্বর: [[MRN|OPD-2024-087]] | ডাক্তার: [[DOCTOR_NAME|Dr. Amitava Chatterjee]]
জেলা: [[DISTRICT|Birbhum]] | প্রধান অভিযোগ: ৩ দিন ধরে জ্বর এবং ଦେହ ব্যথা।
বর্তমান অসুস্থতার ইতিহাস: রোগী গতকাল সন্ধ্যা থেকে উচ্চ জ্বরে আক্রান্ত বলে জানিয়েছেন, যার সাথে সারা শরীরে ব্যথা এবং মাথাব্যথা রয়েছে। তিনি বাড়িতে প্যারাসিটামল খেয়েছিলেন যার ফলে কিছুটা উপশম হয়েছে। কাশি বা গলা …
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `opd_slip` (`hi`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ओपीडी स्लिप | जिला अस्पताल झज्जर | आई डी [[HOSPITAL_ID|DH-JH-001]]
रोगी: [[PATIENT_NAME|Amit Kumar]] | जन्म तिथि [[DOB|1973-08-22]] | आयु: [[AGE|51]] | लिंग: [[GENDER|Male]]
व्यवसाय: [[OCCUPATION|Vending Machine Attendant]] | एम आर एन: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Verma]]
जिला: [[DISTRICT|Jhajjar]] | मुख्य शिकायत: पिछले 3 महीनों से लगातार खांसी और वजन कम होना।
वर्तमान बीमारी का इतिहास: रोगी ने शुरुआत में सूखी खांसी की सूचना दी, अब कभी-कभी रक्त-युक्त बलगम के साथ उत्पादक खांसी हो रही है। शाम को हल्का बुखार और लगभग 5 किलोग्राम वजन में क्रमिक कमी से जुड़ा है। आराम …
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `opd_slip` (`mr`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ओपीडी स्लिप | जिल्हा रुग्णालय, वर्धा | आयडी [[HOSPITAL_ID|DH-MH-023]]
रुग्ण: [[PATIENT_NAME|Meshram Chaudhary]] | जन्म तारीख [[DOB|1988-05-22]] | वय: [[AGE|36]] | लिंग: [[GENDER|Male]]
व्यवसाय: [[OCCUPATION|Motor Cycle Driver]] | एमआरएन: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Priya Deshmukh]]
जिल्हा: [[DISTRICT|Wardha]] | मुख्य तक्रार: ३ आठवड्यांपासून खोकला आणि खोकल्यातून रक्त येणे.
सध्याच्या आजाराचा इतिहास: रुग्णाने गेल्या तीन आठवड्यांपासून खोकल्याची तक्रार केली आहे, जो सुरुवातीला कोरडा होता आणि आता त्यात रक्ताच्या रेषा दिसत आहेत. त्याला संध्याकाळी हलका ताप येतो आणि गेल्या महि…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `opd_slip` (`ta`).
- **Missing required tags:** `['HOSPITAL_NAME', 'EMPLOYEE_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME,EMPLOYEE_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD சீட்டு | பெரம்பலூர் மாவட்ட மருத்துவமனை | அடையாள எண் [[HOSPITAL_ID|DH-PER-001]]
நோயாளி: [[PATIENT_NAME|Karthik]] | பிறந்த தேதி [[DOB|1991-08-22]] | வயது: [[AGE|33]] | பாலினம்: [[GENDER|Male]]
தொழில்: [[OCCUPATION|Driver, Car]] | மருத்துவ பதிவு எண்: [[MRN|OPD-2024-0815-001]] | மருத்துவர்: [[DOCTOR_NAME|Dr. S. Ramesh]]
மாவட்டம்: [[DISTRICT|Perambalur]] | முதன்மைப் புகார்: மூன்று வாரங்களாகத் தொடரும் இருமல் மற்றும் குறைந்த அளவிலான காய்ச்சல்.

தற்போதைய நோயின் வரலாறு:
பெரம்பலூரைச் சேர்ந்த 33 வயது ஆண் கார் ஓட்டுநர், மூன்று வாரங்களாக இருமல் மற்றும் சளியுடன் வருகிறார். ஆரம்பத்தில் வறட்டு இருமல் இரு…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `opd_slip` (`hi`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift']`
- **Reasoning:** Domain Oncology/Complex Chronic Care not followed; content is TB workup instead. Hindi prose and allowed entity tags otherwise correct.
- **Preview:**

```
ओपीडी स्लिप | जिला अस्पताल झज्जर | आई डी [[HOSPITAL_ID|DH-JH-001]]
रोगी: [[PATIENT_NAME|Amit Kumar]] | जन्म तिथि [[DOB|1973-08-22]] | आयु: [[AGE|51]] | लिंग: [[GENDER|Male]]
व्यवसाय: [[OCCUPATION|Vending Machine Attendant]] | एम आर एन: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Rajesh Verma]]
जिला: [[DISTRICT|Jhajjar]] | मुख्य शिकायत: पिछले 3 महीनों से लगातार खांसी और वजन कम होना।
वर्तमान बीमारी का इतिहास: रोगी ने शुरुआत में सूखी खांसी की सूचना दी, अब कभी-कभी रक्त-युक्त बलगम के साथ उ…
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `discharge_summary` (`ml`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift', 'surrogate_plausibility_collapse']`
- **Reasoning:** District Ernakulam mismatches persona Pathanamthitta; ABHA saritha.thomas inconsistent with Annamma/Mary Thomas names.
- **Preview:**

```
ഡിസ്ചാർജ് സമ്മറി — [[HOSPITAL_NAME|മരിയോ ഹോസ്പിറ്റൽ]]
[[PATIENT_NAME|അന്നമ്മ തോമസ്]] ജനനത്തീയതി [[DOB|1981-09-05]] [[AGE|43]] [[GENDER|Female]]
പ്രവേശനം [[ADMISSION_NUMBER|ADM-2024-0815-004]] വാർഡ് [[WARD_NUMBER|A1]] ബെഡ് [[BED_NUMBER|07]]
ഡോ. [[DOCTOR_NAME|ഡോ. രാജേഷ് കുമാർ]] | ചികിത്സാക്രമം / നിർദ്ദേശം: രോഗിയെ കമ്മ്യൂണിറ്റി-അക്വയേർഡ് ന്യൂമോണിയയും സെപ്സിസും ബാധിച്ച നിലയിൽ പ്രവേശിപ്പിച്ചു. രോഗിക്ക് ഇൻട്രാവീനസ് സെഫ്‌ട്രിയാക്സോൺ, അസിത്രോമൈസിൻ എന്നിവ നൽകി ആരംഭിച്ചു, പിന്നീട് ക്ലിനിക്കൽ പുരോഗതിയുടെ …
```

### S5 judge fail 3

- **What:** linguistic judge **fail** on `discharge_summary` (`ml`).
- **Score / verdict:** `0.6` / `fail`
- **Flags:** `['domain_persona_mismatch', 'surrogate_plausibility_collapse']`
- **Reasoning:** District set to Wayanad (not Thiruvananthapuram); ABHA address name 'gopalakrishnan' mismatches patient Ramesh Kumar
- **Preview:**

```
ഡിസ്ചാർജ് സമ്മറി — [[HOSPITAL_NAME|മരിയ ഹോസ്പിറ്റൽ]]
[[PATIENT_NAME|രമേശ് കുമാർ]] ജനനത്തീയതി [[DOB|1953-08-15]] [[AGE|71]] [[GENDER|Male]]
അഡ്മിഷൻ [[ADMISSION_NUMBER|ADM-2024-1028]] വാർഡ് [[WARD_NUMBER|A1]] ബെഡ് [[BED_NUMBER|05]]
ഡോ. [[DOCTOR_NAME|ഡോ. അനിത ശർമ്മ]] | ചികിത്സാ രീതി / നിർദ്ദേശങ്ങൾ: രോഗിയെ പൾമണറി ട്യൂബർകുലോസിസ് (Pulmonary tuberculosis) രോഗനിർണ്ണയത്തോടെ പ്രവേശിപ്പിച്ചു. ഇതിനോടൊപ്പം ടൈപ്പ് 2 ഡയബറ്റിസ് മെലിറ്റസും (type 2 diabetes mellitus) കണ്ടെത്തി. അദ്ദേഹം ലെവോഫ്ലോക്സാസിൻ (levofloxa…
```

### S5 judge fail 4

- **What:** linguistic judge **fail** on `opd_slip` (`mr`).
- **Score / verdict:** `0.55` / `fail`
- **Flags:** `['instruction_drift', 'domain_persona_mismatch']`
- **Reasoning:** Oncology domain specified but content is pulmonary TB diagnosis and RNTCP treatment; minor fit issues despite correct Marathi prose and valid entity tags.
- **Preview:**

```
ओपीडी स्लिप | जिल्हा रुग्णालय, वर्धा | आयडी [[HOSPITAL_ID|DH-MH-023]]
रुग्ण: [[PATIENT_NAME|Meshram Chaudhary]] | जन्म तारीख [[DOB|1988-05-22]] | वय: [[AGE|36]] | लिंग: [[GENDER|Male]]
व्यवसाय: [[OCCUPATION|Motor Cycle Driver]] | एमआरएन: [[MRN|OPD-2024-0815-001]] | डॉक्टर: [[DOCTOR_NAME|Dr. Priya Deshmukh]]
जिल्हा: [[DISTRICT|Wardha]] | मुख्य तक्रार: ३ आठवड्यांपासून खोकला आणि खोकल्यातून रक्त येणे.
सध्याच्या आजाराचा इतिहास: रुग्णाने गेल्या तीन आठवड्यांपासून खोकल्याची तक्रार केली आहे, जो सुरुवाती…
```

### S5 judge fail 5

- **What:** linguistic judge **fail** on `asha_worker_note` (`pa`).
- **Score / verdict:** `0.72` / `fail`
- **Flags:** `['surrogate_plausibility_collapse']`
- **Reasoning:** Village Kapurthala surrogate clashes with Faridkot district; all other language, entity types, persona and domain fit are correct.
- **Preview:**

```
ਆਸ਼ਾ ਨੋਟ — ਪਿੰਡ [[VILLAGE|Kapurthala]], ਜ਼ਿਲ੍ਹਾ [[DISTRICT|Faridkot]]
ਲਾਭਪਾਤਰੀ [[PATIENT_NAME|Harpreet Kaur]], [[AGE|38]] / [[GENDER|Female]]
ਆਸ਼ਾ: [[ASHA_WORKER_NAME|Jaswinder Kaur]] | ਫ਼ੋਨ [[PHONE_NUMBER|9876543210]]
ਮੁਲਾਕਾਤ ਦੇ ਨਤੀਜੇ: ਮਰੀਜ਼ ਪਿਛਲੇ ਦੋ ਮਹੀਨਿਆਂ ਤੋਂ ਲਗਾਤਾਰ ਘੱਟ ਮੂਡ ਅਤੇ ਚਿੰਤਾ ਦੀ ਰਿਪੋਰਟ ਕਰਦੀ ਹੈ। ਉਹ ਘਰੇਲੂ ਜ਼ਿੰਮੇਵਾਰੀਆਂ ਨਾਲ ਬਹੁਤ ਜ਼ਿਆਦਾ ਬੋਝ ਮਹਿਸੂਸ ਕਰਦੀ ਹੈ ਅਤੇ ਸੌਣ ਵਿੱਚ ਮੁਸ਼ਕਲ ਆਉਂਦੀ ਹੈ। ਉਹ ਇਸ ਸਮੇਂ PHC ਡਾਕਟਰ ਦੁਆਰਾ ਨਿਰਧਾਰਤ ਦਵਾਈ ਲੈ ਰਹੀ ਹੈ। ਉਸਦਾ ਪਤੀ [[RELATIVE_NAME|Balwinder Singh]] ਸਹਾਇਕ ਹੈ ਅ…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `telemedicine_transcript` (`bn`).
- **Errors:** `['entity_stuffing_total_tags:30>24', 'entity_stuffing:AGE,EMAIL_ADDRESS,GENDER,HOSPITAL_NAME,PHONE_NUMBER', 'upstream_generation_soft_fail:entity_stuffing:AGE,GENDER,PHONE_NUMBER,EMAIL_ADDRESS,HOSPITAL_NAME']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** tag dump / over-repetition of entity TYPEs.
- **Preview:**

```
--- সেশন ---
অ্যাপয়েন্টমেন্ট [[APPOINTMENT_ID|APT-240521-01]] পোর্টাল [[URL|https://tele.example.in/visit]]
ক্লায়েন্ট আই.পি [[IP_ADDRESS|103.21.244.12]] ডিভাইস আই.এম.ই.আই [[IMEI_NUMBER|356938035643809]]
ম্যাক [[MAC_ADDRESS|00:1A:2B:3C:4D:5E]]
--- চ্যাট ---
রোগী [[PATIENT_NAME|Mohitosh Das]] [[AGE|37]] [[GENDER|Male]] ([[PHONE_NUMBER|9876543210]], [[EMAIL_ADDRESS|mohitosh.das.art@example.com]]): ডাক্তার, আমি সম্প্রতি খুব উদ্বিগ্ন বোধ করছি। আমার হৃদস্পন্দন বেড়ে যায় এবং আমি ভালোভাবে ঘুমাতে পার…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `opd_slip` (`bn`).
- **Errors:** `['missing_required:HOSPITAL_NAME', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
ও.পি.ডি স্লিপ | বীরভূম জেলা হাসপাতাল | আইডি [[HOSPITAL_ID|DH-WB-021]]
রোগী: [[PATIENT_NAME|Sanjay Kumar]] | জন্ম তারিখ [[DOB|1989-07-22]] | বয়স: [[AGE|35]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Labourer, Other]] | মেডিকেল রেকর্ড নম্বর: [[MRN|OPD-2024-087]] | ডাক্তার: [[DOCTOR_NAME|Dr. Amitava Chatterjee]]
জেলা: [[DISTRICT|Birbhum]] | প্রধান অভিযোগ: ৩ দিন ধরে জ্বর এবং ଦେହ ব্যথা।
বর্তমান অসুস্থতার ইতিহাস: রোগী গতকাল সন্ধ্যা থেকে উচ্চ জ্বরে আক্রান্ত বলে জানিয়েছেন, যার সাথে সারা শরীরে ব্যথা…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `opd_slip` (`ta`).
- **Errors:** `['missing_required:HOSPITAL_NAME,EMPLOYEE_ID', 'upstream_generation_soft_fail:missing_required_entities:HOSPITAL_NAME,EMPLOYEE_ID']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
OPD சீட்டு | பெரம்பலூர் மாவட்ட மருத்துவமனை | அடையாள எண் [[HOSPITAL_ID|DH-PER-001]]
நோயாளி: [[PATIENT_NAME|Karthik]] | பிறந்த தேதி [[DOB|1991-08-22]] | வயது: [[AGE|33]] | பாலினம்: [[GENDER|Male]]
தொழில்: [[OCCUPATION|Driver, Car]] | மருத்துவ பதிவு எண்: [[MRN|OPD-2024-0815-001]] | மருத்துவர்: [[DOCTOR_NAME|Dr. S. Ramesh]]
மாவட்டம்: [[DISTRICT|Perambalur]] | முதன்மைப் புகார்: மூன்று வாரங்களாகத் தொடரும் இருமல் மற்றும் குறைந்த அளவிலான காய்ச்சல்.

தற்போதைய நோயின் வரலாறு:
பெரம்பலூரைச் சேர்ந்த 33 வயது …
```


## Surviving curated set

- languages: `{'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'automated_sms': 2, 'opd_slip': 1, 'prescription': 1, 'referral_letter': 1, 'surgical_note': 3}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
