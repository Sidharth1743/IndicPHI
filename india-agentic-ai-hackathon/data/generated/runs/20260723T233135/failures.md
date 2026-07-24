# Failures audit — `20260723T233135`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/india-agentic-ai-hackathon/data/generated/runs/20260723T233135/pipeline.resolved.yaml`
- **issue count:** **19** (hard=0, gen_soft=5, tr_soft=8, judge=1, auditor=5)
- **S4 entity_coverage_complete_rate:** `0.9782608695652174`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.9927536231884058`
- **S6 pass_rate / passed:** `0.9635036496350365` / `132`
- **curated docs:** `114`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `7cf3cf4f60be4edabe12ffd948079164` | `bn` | `surgical_note` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `18473c8835b140ff8c0b5ed0d35a5271` | `doi` | `prescription` | `['missing_required_entities:DISTRICT']` |
| S4 soft | `8116ee5699344b79a2c9c8d1e053dde5` | `doi` | `insurance_claim` | `['entity_stuffing:AGE,DISTRICT,GENDER,INSURANCE_POLICY_NUMBER,PIN,VILLAGE']` |
| S4 soft | `67bf2f4af82d452db4c95cd1c7f59330` | `or` | `surgical_note` | `['missing_required_entities:HOSPITAL_NAME']` |
| S4 soft | `829db9fbfeda404d89ff9b8a405b5e4d` | `ta` | `insurance_claim` | `['entity_stuffing:TOTAL_TAGS>32']` |
| S4b soft | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `hospital_billing` | `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_transla…` |
| S4b soft | `59e7e12eb3d44dfbacf8755ef02f52c7` | `kn` | `opd_slip` | `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place T…` |
| S4b soft | `60ff3470cf8340efaa474e13896d8568` | `ks` | `opd_slip` | `prefer_chat_1:Translation lost protected ID tag '[[GENDER|Male]]';dedicated_translate_failed:Transl…` |
| S4b soft | `22ef884ce12247309d07fc3f601a3c59` | `sa` | `asha_worker_note` | `dedicated_translate_failed:Translation lost protected ID tag '[[AGE|19]]';rare_recovery_1:Sarvam ti…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-2024-0815-001]]';rare_recov…` |
| S4b soft | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `discharge_summary` | `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder…` |
| S4b soft | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | `dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|390001]]';rare_recovery_1:…` |
| S4b soft | `ce942a5fb5644181ac0db94b6c9c1314` | `ta` | `automated_sms` | `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place T…` |
| S5 fail | `fe3a6e05b50a4eb1b679f5fba0c5440b` | `sd` | `hospital_billing` | score=0.65 flags=['instruction_drift'] |
| S6 fail | `57e0ccc76318480b91dca7f2d464c122` | `gu` | `referral_letter` | `['dics_below_threshold:0.7142857142857143']` |
| S6 fail | `7e1fefa3b81344778d2739efd7575c6c` | `hi` | `insurance_claim` | `['phi_residue:1', 'dics_below_threshold:0.0', 'script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `df61060159844e75aeafcafe43b1bc0d` | `mni` | `referral_letter` | `['dics_below_threshold:0.6666666666666666']` |
| S6 fail | `825c4438c02440dc90d3ddec7ffec8ee` | `sd` | `hospital_billing` | `['script_purity:target_script_ratio:0.000<0.35']` |
| S6 fail | `6b15543bcd6545f5803d6887e2a48820` | `ur` | `referral_letter` | `['dics_below_threshold:0.5']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `surgical_note` (`bn`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
বহির্বিভাগ স্লিপ | [[HOSPITAL_NAME|Karimganj District Hospital]] | আইডি [[HOSPITAL_ID|KDH-2024-001]]
রোগী: [[PATIENT_NAME|Hanik Haq]] | জন্ম তারিখ [[DOB|1973-06-15]] | বয়স: [[AGE|51]] | লিঙ্গ: [[GENDER|Male]]
পেশা: [[OCCUPATION|Mica Screener]] | মেডিকেল রেকর্ড নম্বর: [[MRN|KDH-2024-0815-001]] | ডাক্তার: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
আত্মীয়: [[RELATIVE_NAME|Fatema Haq]] | ফোন: [[PHONE_NUMBER|9876543210]]
রেজিস্ট্রার এম্পিআইডি: [[EMPLOYEE_ID|EMP-KDH-023]] | জেলা: [[DISTRICT|Karimganj]]
প্রধান অভিযোগ: 5 দিন ধরে হালকা জ্বরসহ দীর্ঘস্থায়ী কাশি, বুকের অস্বস্তি এবং ক্লান্তি।

পরীক্ষার ফলাফল: তা…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `prescription` (`doi`).
- **Missing required tags:** `['DISTRICT']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DISTRICT']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ओपीडी स्लिप | [[HOSPITAL_NAME|District Hospital Kathua]] | आई डी [[HOSPITAL_ID|DH-JK-001]]
मरीज: [[PATIENT_NAME|Anuradha Devi]] | जन्म तिथि [[DOB|1986-05-22]] | उम्र: [[AGE|38]] | लिंग: [[GENDER|Female]]
पेशा: [[OCCUPATION|Police Officer]] | एम आर एन: [[MRN|OPD-2024-0815-001]] | डाक्टर: [[DOCTOR_NAME|Dr. Rajesh Kumar]]
रिश्तेदार: [[RELATIVE_NAME|Ramesh Kumar]] | फोन: [[PHONE_NUMBER|9419012345]]
रजिस्ट्रार कर्मचारी आई डी: [[EMPLOYEE_ID|EMP-2024-0815]] | जिला: [[DISTRICT|Kathua]]

मुख्य शिकायत: मरीज पिछले 3 महीने थमां लगातार चिंता, सोने च मुश्किल, ते मन च फालतू ख्याल आने दी शिकायत करदा ऐ। कम्म …
```

### S4 generation soft-fail 3

- **What:** generation soft-fail on `insurance_claim` (`doi`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['AGE', 'DISTRICT', 'GENDER', 'INSURANCE_POLICY_NUMBER', 'PIN', 'VILLAGE']`
- **Raw reasons:** `['entity_stuffing:AGE,DISTRICT,GENDER,INSURANCE_POLICY_NUMBER,PIN,VILLAGE']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
आशा वर्कर नोट — गांव [[VILLAGE|Bahu]], जिला [[DISTRICT|Jammu]]
लाभार्थी [[PATIENT_NAME|Fatima Begum]], [[AGE|48]] / [[GENDER|Female]]
आशा वर्कर: [[ASHA_WORKER_NAME|Shabnam Begum]] | फोन [[PHONE_NUMBER|9419876543]]
भेंट दे नतीजे: मरीज दस्सदे न पिछले महीने शा बधदी चिंता ते नींद च खलल। गल्लबात दे दौरान ओह्‌ अलग-थलग लभदी ऐ ते निराशा दे अहसास दस्सदी ऐ। पारिवारिक इतिहास दस्सदा ऐ मां गी बी एह्‌ जेहे लक्षण हे।

[[RELATIVE_NAME|Mohammed Iqbal]] (पति) भेंट दे दौरान मजूद हे। मरीज दस्सी दी एंटीडिप्रेसेंट दवाईयां ठीक चाल्ली लैंदे न। दस्सदे न जे हल्के योग करने कन्नै जोड़ें दी अकड़न च आराम मिलदा ऐ पर मूड दे…
```

### S4 generation soft-fail 4

- **What:** generation soft-fail on `surgical_note` (`or`).
- **Missing required tags:** `['HOSPITAL_NAME']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:HOSPITAL_NAME']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
ଆଉଟପେସେଣ୍ଟ ବିଭାଗ ସ୍ଲିପ୍ | ଜିଲ୍ଲା ଡାକ୍ତରଖାନା ନବରଙ୍ଗପୁର | ID DH-NAB-001
ରୋଗୀ: ମଲତି | ଜନ୍ମ ତାରିଖ 1965-06-15 | ବୟସ: 59 | ଲିଙ୍ଗ: ମହିଳା
ବୃତ୍ତି: ଗୃହିଣୀ | MRN: OPD-2024-001 | ଡାକ୍ତର: ଡାକ୍ତର ପ୍ରିୟା ପଟ୍ଟନାୟକ
ସମ୍ପର୍କୀୟ: ସୁନିତା ପଟ୍ଟନାୟକ | ଫୋନ୍: 9437891234
ରେଜିଷ୍ଟ୍ରାର କର୍ମଚାରୀ ID: EMP-2024-045 | ଜିଲ୍ଲା: ନବରଙ୍ଗପୁର
ମୁଖ୍ୟ ଅଭିଯୋଗ: 5 ଦିନ ହେବ ଜ୍ୱର ସହିତ କାଶ

ବର୍ତ୍ତମାନର ଅସୁସ୍ଥତାର ଇତିହାସ: ରୋଗୀଙ୍କର 5 ଦିନ ହେବ ଶୁଖିଲା କାଶରୁ ଆରମ୍ଭ ହୋଇ ହଳଦିଆ କଫ ସହିତ କାଶ, କମ୍ ଜ୍ୱର ଏବଂ ଶରୀରରେ ସାମାନ୍ୟ ଯନ୍ତ୍ରଣା ହେଉଛି। ପୂର୍ବରୁ ଏପରି କିଛି ହୋଇଥିବାର ଇତିହାସ ନାହିଁ।

ପରୀକ୍ଷା:
- ତାପମାତ୍ରା: 100.8°F
- ନାଡ଼ି: 88/min
- ରକ୍ତଚାପ: 130/80 mmHg
- ଶ୍ୱାସକ୍ରିୟା…
```

### S4 generation soft-fail 5

- **What:** generation soft-fail on `insurance_claim` (`ta`).
- **Missing required tags:** `—`
- **Stuffing flags:** `['TOTAL_TAGS>32']`
- **Raw reasons:** `['entity_stuffing:TOTAL_TAGS>32']`
- **Note:** repeated speaker names in multi-turn chat can look like stuffing; device/vehicle IDs should still appear once only.
- **Preview:**

```
சிகிச்சை அறிக்கை | [[HOSPITAL_NAME|Thiruvallur District Medical College Hospital]] | அடையாள எண் [[HOSPITAL_ID|TDMCH-001]]
நோயாளி: [[PATIENT_NAME|Lakshmi]] | பிறந்த தேதி [[DOB|1984-07-22]] | வயது: [[AGE|40]] | பாலினம்: [[GENDER|Female]]
தொழில்: [[OCCUPATION|Newspaper Boy]] | மருத்துவக் குறிப்பு எண்: [[MRN|OPD-2024-0842]] | மருத்துவர்: [[DOCTOR_NAME|Dr. Priya Natarajan]]
உறவினர்: [[RELATIVE_NAME|Ramesh]] | தொலைபேசி எண்: [[PHONE_NUMBER|9876543210]]
பதிவாளர் பணி எண்: [[EMPLOYEE_ID|EMP-2024-015]] | மாவட்டம்: [[DISTRICT|Thiruvallur]]
முக்கிய குறைபாடு: நோயாளி கடந்த 3 மாதங்களாக பதட்டம் மற்றும் தூக்கம…
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `hospital_billing` (`gu`).
- **Error:** `tag_restore_or_translate_failed:Translation lost protected ID tag '[[STATE|…]]';post_repair_translate:Translation lost protected ID tag '[[STATE|…]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Invoice — [[HOSPITAL_NAME|Shri Krishna Hospital]] District [[DISTRICT|Sabar Kantha]]
PIN [[PIN_CODE|383550]] Patient [[PATIENT_NAME|Dahiben Muchadiya]] MRN [[MRN|SKH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Village: Ranipura, Taluka: Himmatnagar]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|dahiben.muchadiya@example.com]] PAN [[PAN_NUMBER|GJPMD1234F]]
Landline [[TELEPHONE_LANDLIN…
```
- **Translated preview:**

```
Invoice — [[HOSPITAL_NAME|Shri Krishna Hospital]] District [[DISTRICT|Sabar Kantha]]
PIN [[PIN_CODE|383550]] Patient [[PATIENT_NAME|Dahiben Muchadiya]] MRN [[MRN|SKH-2024-0815-001]]
Address [[RESIDENTIAL_ADDRESS|Village: Ranipura, Taluka: Himmatnagar]] Phone [[PHONE_NUMBER|9876543210]]
Email [[EMAIL_ADDRESS|dahiben.muchadiya@example.com]] PAN [[PAN_NUMBER|GJPMD1234F]]
Landline [[TELEPHONE_LANDLIN…
```

### S4b translation soft-fail 2

- **What:** translation soft-fail on `opd_slip` (`kn`).
- **Error:** `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Gadag District Hospital]] | ID [[HOSPITAL_ID|GDS-2024-001]]
Patient: [[PATIENT_NAME|Basavaraj]] | DOB [[DOB|1975-07-22]] | Age: [[AGE|49]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Farmer]] | MRN: [[MRN|MRN-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Ramesh Hegde]]
Attendant: [[RELATIVE_NAME|Shakuntala]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[E…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Gadag District Hospital]] | ID [[HOSPITAL_ID|GDS-2024-001]]
Patient: [[PATIENT_NAME|Basavaraj]] | DOB [[DOB|1975-07-22]] | Age: [[AGE|49]] | Gender: [[GENDER|Male]]
Occupation: [[OCCUPATION|Farmer]] | MRN: [[MRN|MRN-2024-0815-001]] | Doctor: [[DOCTOR_NAME|Dr. Ramesh Hegde]]
Attendant: [[RELATIVE_NAME|Shakuntala]] | Phone: [[PHONE_NUMBER|9876543210]]
Registrar EmpID: [[E…
```

### S4b translation soft-fail 3

- **What:** translation soft-fail on `opd_slip` (`ks`).
- **Error:** `prefer_chat_1:Translation lost protected ID tag '[[GENDER|Male]]';dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ER triage — [[HOSPITAL_NAME|SKIMS Soura]] Encounter [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Bed [[BED_NUMBER|07]]
Arrived by ambulance vehicle [[VEHICLE_REGISTRATION|JK02AB1234]]
Relative [[RELATIVE_NAME|Amina Shamar]] Phone [[PHONE_NUMBER|9419212345]] Dr [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
Vitals / acuity: BP 140/90, HR 110…
```
- **Translated preview:**

```
ایمرجنسی ٹریاج — [[HOSPITAL_NAME|SKIMS Soura]] ملاقات [[ENCOUNTER_ID|ENC-2024-0915-001]]
[[PATIENT_NAME|Jammer Shamar]] [[AGE|28]] [[GENDER|Male]] وارڈ [[WARD_NUMBER|ER]] بستر [[BED_NUMBER|07]]
ایمبولینس گاڑی [[VEHICLE_REGISTRATION|JK02AB1234]] ذٔریعہٕ پہنچی
رشتہ دار [[RELATIVE_NAME|Amina Shamar]] فون [[PHONE_NUMBER|9419212345]] ڈاکٹر [[DOCTOR_NAME|Dr. Riyaz Ahmad]]
وائٹلز / شدت: BP 140/90, HR 11…
```

### S4b translation soft-fail 4

- **What:** translation soft-fail on `asha_worker_note` (`sa`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[AGE|19]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[AGE|19]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Prescription — [[HOSPITAL_NAME|Bundi District Hospital]]
Patient [[PATIENT_NAME|Ananya Sharma]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-0815-001]]
Dr. [[DOCTOR_NAME|Dr. Rajesh Kumar]]
Phone: [[PHONE_NUMBER|9876543210]]
Address: [[RESIDENTIAL_ADDRESS|12 Gandhi Nagar, Ward 4, Bundi]]
District: [[DISTRICT|Bundi]], Rajasthan
Patient ID: [[PATIENT_ID|PID-2024-0815-001]]
ABHA ID: [[ABHA_ID|…
```
- **Translated preview:**

```
अनुदेशः — [[HOSPITAL_NAME|NM0]]
रोगिणी [[PATIENT_NAME|NM1]], [[AGE|19]] / [[GENDER|Female]], MRN [[MRN|MRN-2024-0815-001]]
चिकित्सिका [[DOCTOR_NAME|NM2⟧]]
दूरवाणी: [[PHONE_NUMBER|9876543210]]
सङ्केतः: [[RESIDENTIAL_ADDRESS|NM3⟧]]
मण्डलम्: [[DISTRICT|NM4]], राजस्थानम्
रोगिणी परिचयपत्रम्: [[PATIENT_ID|PID-2024-0815-001]]
आभा परिचयपत्रम्: [[ABHA_ID|12-3456-7890-1234]]

निदानम्: फुफ्फुसीय क्षयरोगः, प…
```

### S4b translation soft-fail 5

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[MRN|MRN-2024-0815-001]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|400022]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Ramesh Patil]], your follow-up for behavioral health counseling is scheduled at [[HOSPITAL_NAME|Sion Hospital]] on 15-Dec at 11:30 AM with [[DOCTOR_NAME|Dr. Priya Nair]]. Please bring your [[MRN|MRN-MH-2024-0892]]. Confirm on [[PHONE_NUMBER|9876543210]]. [[APPOINTMENT_ID|APT-MH-2024-1215-001]].
```
- **Translated preview:**

```
محترم [[PATIENT_NAME|سنڌو]],
توهان جي برتاؤ صحت مشاورت جي پیروی [[HOSPITAL_NAME|سندھ گورنمنٹ اسپتال]] تي 15-ڊسمبر تي 11:30 صبح [[DOCTOR_NAME|ڊاڪٽر علي]] سان مقرر آهي۔
مહેરباني ڪري پنهنجو [[MRN|MRN-MH-2024-0892]] آڻيو۔
تصديق [[PHONE_NUMBER|9876543210]] تي۔
[[APPOINTMENT_ID|APT-MH-2024-1215-001]]۔
```

### S4b translation soft-fail 6

- **What:** translation soft-fail on `discharge_summary` (`sd`).
- **Error:** `dedicated_translate_failed:Translation lost or altered name/place TYPE 'HOSPITAL_NAME' (placeholder ⟦NM0⟧);script_purity_failed:wrong_indic_script:Devanagari>Arabic;dedicated_translate_failed:Translation lost protected ID tag '[[DOB|1992-06-15]]'`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
Dear [[PATIENT_NAME|Ramesh Patil]], your follow-up for behavioral health counseling is scheduled at [[HOSPITAL_NAME|Sion Hospital]] on 15-Dec at 11:30 AM with [[DOCTOR_NAME|Dr. Priya Nair]]. Please bring your [[MRN|MRN-MH-2024-0892]]. Confirm on [[PHONE_NUMBER|9876543210]]. [[APPOINTMENT_ID|APT-MH-2024-1215-001]].
```
- **Translated preview:**

```
محترم [[PATIENT_NAME|سنڌو]],
توهان جي برتاؤ صحت مشاورت جي پیروی [[HOSPITAL_NAME|سندھ گورنمنٹ اسپتال]] تي 15-ڊسمبر تي 11:30 صبح [[DOCTOR_NAME|ڊاڪٽر علي]] سان مقرر آهي۔
مહેરباني ڪري پنهنجو [[MRN|MRN-MH-2024-0892]] آڻيو۔
تصديق [[PHONE_NUMBER|9876543210]] تي۔
[[APPOINTMENT_ID|APT-MH-2024-1215-001]]۔
```

### S4b translation soft-fail 7

- **What:** translation soft-fail on `hospital_billing` (`sd`).
- **Error:** `dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|390001]]';rare_recovery_1:Sarvam timeout after 180.0s: The read operation timed out;dedicated_translate_failed:Translation lost protected ID tag '[[PIN_CODE|390001]]'`
- **script_ok:** `False`
- **EN pivot preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-9876]]
[[PATIENT_NAME|Shilpaben Vasava]] [[AGE|75]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|203835321155]]
Hospital [[HOSPITAL_NAME|Shri Krishna Hospital]] District [[DISTRICT|Vadodara]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|GJ06AB1234]] (exactly once).
PAN [[PAN_NUMBER|GHTPS1234C]] IFSC [[IFSC_CODE|SBIN0000123]] account [[BANK_ACC…
```
- **Translated preview:**

```
مريض: [[PATIENT_NAME|فاطمہ ميمڻ]] [[AGE|45]] [[GENDER|Female]].
اسپتال: [[HOSPITAL_NAME|سویل اسپتال]]۔ ضلعو: [[DISTRICT|حيدرآباد]].
شڪايت: کنگهه ۽ بخار۔ ڊاڪٽر: [[DOCTOR_NAME|علي شاه]].

TPA دعويٰ — پاليسي [[INSURANCE_POLICY_NUMBER|POL-GUJ-2024-9876]]
[[PATIENT_NAME|علي اڪبر]] [[AGE|75]] [[GENDER|Female]] آدھار [[AADHAAR_NUMBER|203835321155]]
هسپتال [[HOSPITAL_NAME|سول اسپتال]] ضلعو [[DISTRICT|حيد…
```

### S4b translation soft-fail 8

- **What:** translation soft-fail on `automated_sms` (`ta`).
- **Error:** `tag_restore_or_translate_failed:dedicated_translate_failed:Translation lost or altered name/place TYPE 'PATIENT_NAME' (placeholder ⟦NM0⟧)`
- **script_ok:** `False`
- **EN pivot preview:**

```
ASHA note — Village [[VILLAGE|T. Nagar]], District [[DISTRICT|Chennai]]
Beneficiary [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ASHA: [[ASHA_WORKER_NAME|Lakshmi Devi]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports increased irritability and sleep disturbances over past 3 weeks. Expresses work-related stress and financial concerns affecting daily functioning.
…
```
- **Translated preview:**

```
ஆஷா குறிப்பு — கிராமம் [[VILLAGE|T. Nagar]], மாவட்டம் [[DISTRICT|Chennai]]
பயனாளி [[PATIENT_NAME|Mahavir Jain]], [[AGE|34]] / [[GENDER|Male]]
ஆஷா: [[ASHA_WORKER_NAME|Lakshmi Devi]] | தொலைபேசி [[PHONE_NUMBER|9876543210]]
பரிசோதனை முடிவுகள்: நோயாளி கடந்த 3 வாரங்களாக அதிகமான எரிச்சல் மற்றும் தூக்கக் கோளாறுகளைக் கூறுகிறார். வேலை சார்ந்த மன அழுத்தம் மற்றும் நிதி சார்ந்த கவலைகள் தினசரி செயல்பாடுகளைப் ப…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `hospital_billing` (`sd`).
- **Score / verdict:** `0.65` / `fail`
- **Flags:** `['instruction_drift']`
- **Reasoning:** Sindhi Arabic-script prose and allow-listed tags are correct with plausible 75F TB+NCD billing content; meta leakage '(سادو نثر — قسم ناهي)' indicates instruction_drift.
- **Preview:**

```
انوائس — [[HOSPITAL_NAME|Vadodara Civil Hospital]] ضلعو [[DISTRICT|Vadodara]]
پن [[PIN_CODE|390001]] مريض [[PATIENT_NAME|Shilpaben Vasava]] MRN [[MRN|VCH-2024-0815-001]]
[[RESIDENTIAL_ADDRESS|12, Madhavpura Society, Near Alkapuri Circle]] فون [[PHONE_NUMBER|9876543210]]
[[EMAIL_ADDRESS|shilpaben.vasava@example.com]] PAN [[PAN_NUMBER|GJVAP1234C]]
لئنڊ لائن [[TELEPHONE_LANDLINE|0265-2345678]] گاڏي [[VEHICLE_REGISTRATION|GJ06AB1234]] (هڪ دفعو)
آڌار [[AADHAAR_NUMBER|206501253007]] پاليسي [[INSURANC…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `referral_letter` (`gu`).
- **Errors:** `['dics_below_threshold:0.7142857142857143']`
- **Preview:**

```
રેફરલ [[REFERRAL_ID|REF-2024-01]] [[HOSPITAL_NAME|Sabar Kantha District Hospital]] / [[DOCTOR_NAME|Dr. Rajesh Patel]] તરફથી
વિષે: [[PATIENT_NAME|Dahiben Muchadiya]], [[AGE|58]] / [[GENDER|Female]], જિલ્લો [[DISTRICT|Sabar Kantha]]
કારણ: અનિયંત્રિત હાઈપરટેન્શન અને ટાઈપ 2 ડાયાબિટીસ મેલીટસના મૂલ્યાંકન અને સંચાલન માટે

પ્રિય સહકર્મી,

હું [[PATIENT_NAME|Dahiben Muchadiya]], 58 વર્ષની મહિલા ખેતીની દેખરેખ રાખનાર, [[VILLAGE|Ranipura]] ગામની, [[DISTRICT|Sabar Kantha]] જિલ્લામાં, તેણીની લાંબા ગાળાની તબી…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `insurance_claim` (`hi`).
- **Errors:** `['phi_residue:1', 'dics_below_threshold:0.0', 'script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
Insurance Claim / TPA Application Form
Policy [[INSURANCE_POLICY_NUMBER|POL-MP-2024-9876]]
Patient Details:
Patient Name: [[PATIENT_NAME|Rohit Kapoor]] Age: [[AGE|42]] Gender: [[GENDER|Male]] Aadhaar Number: [[AADHAAR_NUMBER|203835321155]]
Phone Number: [[PHONE_NUMBER|9425098765]]
PIN: [[PIN|458001]] District: [[DISTRICT|Mandsaur]]
PAN Number: [[PAN_NUMBER|ABCDE1234F]]
Credit Card Number: [[CREDIT_CARD_NUMBER|4111111111111111]]
CVV: [[CVV|123]]
Vehicle Registration Number: [[VEHICLE_REGISTRATIO…
```

### S6 auditor fail 3

- **What:** deterministic auditor **fail** on `referral_letter` (`mni`).
- **Errors:** `['dics_below_threshold:0.6666666666666666']`
- **Preview:**

```
ꯔꯦꯐꯔꯦꯜ [[REFERRAL_ID|REF-2024-IMPH-001]] [[HOSPITAL_NAME|Regional Institute of Medical Sciences, Imphal]] ꯗꯒꯤ / [[DOCTOR_NAME|Dr. L. Singh]]
Regarding [[PATIENT_NAME|Thokchom Sanjit Singh]], [[AGE|38]] / [[GENDER|Male]], ꯗꯤꯁꯇ꯭ꯔꯤꯛ [[DISTRICT|Imphal East]]
ꯃꯔꯝ: ꯂꯦꯞꯇꯅ ꯈꯣꯡꯕ ꯑꯃꯁꯨꯡ ꯍꯛꯆꯥꯡꯒꯤ ꯑꯣꯏꯕ ꯂꯥꯏꯑꯣꯡꯁꯤꯡ ꯑꯃꯁꯨꯡ ꯃꯁꯤꯒ ꯂꯣꯏꯅꯅ ꯍꯥꯏꯄꯔꯇꯦꯟꯁꯟ ꯂꯩꯕꯅ ꯑꯈꯟꯅꯕ ꯊꯤꯖꯤꯟꯕ ꯃꯊꯧ ꯇꯥꯏ꯫

Dear Colleague,

ꯃꯁꯤ [[PATIENT_NAME|Thokchom Sanjit Singh]] ꯕꯨ ꯃꯈꯥ ꯇꯥꯅ ꯊꯤꯖꯤꯟꯕ ꯑꯃꯁꯨꯡ ꯂꯥꯌꯦꯡꯅꯕ ꯔꯦꯐꯔ ꯇꯧꯅꯕꯅꯤ, ꯃꯍꯥꯛ ꯏꯝꯐꯥꯜ ꯅꯣꯡꯄꯣꯛꯇ ꯂꯩꯕ ꯆꯍꯤ 38 ꯁꯨꯔꯕ ꯅꯨꯄ…
```

### S6 auditor fail 4

- **What:** deterministic auditor **fail** on `hospital_billing` (`sd`).
- **Errors:** `['script_purity:target_script_ratio:0.000<0.35']`
- **Cause chain:** translation/script purity issue.
- **Preview:**

```
Hospital Billing Invoice
Patient: [[PATIENT_NAME|Ramesh Patel]], Age: 32 years, Sex: Male
Attending Doctor: [[DOCTOR_NAME|Dr. Anjali Sharma]]
Medical Record Number: [[MRN|MH-2024-0912-001]]

Medical Services:
- Consultation with General Physician: 1500 INR
- Blood Pressure Check: 200 INR
- Blood Sugar Test (Fasting): 300 INR
- ECG: 400 INR
- Medicines (Prescription): 800 INR

Total Amount: 3200 INR
GST (18%): 576 INR
Final Amount: 3776 INR

Payment Method: [[INSURANCE_POLICY_NUMBER|POL-MH-2024-…
```

### S6 auditor fail 5

- **What:** deterministic auditor **fail** on `referral_letter` (`ur`).
- **Errors:** `['dics_below_threshold:0.5']`
- **Preview:**

```
رجوع [[REFERRAL_ID|REF-2024-01]] از [[HOSPITAL_NAME|District Hospital Amravati]] / [[DOCTOR_NAME|Dr. Priya Deshmukh]]
بابت [[PATIENT_NAME|Fatimah Begum]]، [[AGE|56]] / [[GENDER|Female]]، [[DISTRICT|Amravati]]
وجہ: غیر کنٹرول شدہ ہائی بلڈ پریشر اور ٹائپ 2 ذیابیطس میلیٹس جس کے لیے ماہر سے مشورہ اور ادویات میں تبدیلی درکار ہے۔

محترم ڈاکٹر شرما،

میں آپ کے مریضہ، [[PATIENT_NAME|Fatimah Begum]]، ایک 56 سالہ خاتون، امرتیا سے، اس کی دائمی طبی حالتوں کی تشخیص اور انتظام کے لیے رجوع کر رہی ہوں۔ مریضہ گ…
```


## Surviving curated set

- languages: `{'as': 6, 'bn': 5, 'brx': 6, 'doi': 6, 'en': 6, 'gu': 5, 'hi': 5, 'kn': 4, 'kok': 6, 'ks': 3, 'mai': 4, 'ml': 3, 'mni': 5, 'mr': 5, 'ne': 6, 'or': 4, 'pa': 5, 'sa': 6, 'sat': 6, 'sd': 3, 'ta': 5, 'te': 6, 'ur': 4}`
- doc_types: `{'asha_worker_note': 7, 'automated_sms': 9, 'discharge_summary': 11, 'er_triage_notes': 7, 'hospital_billing': 9, 'insurance_claim': 10, 'lab_report': 8, 'opd_slip': 9, 'phc_register': 4, 'prescription': 13, 'radiology_report': 8, 'referral_letter': 5, 'surgical_note': 11, 'telemedicine_transcript': 3}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
