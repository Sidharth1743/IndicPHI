# Failures audit — `20260719T191524`

- **run status:** `ok`
- **resolved config:** `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T191524/pipeline.resolved.yaml`
- **issue count:** **7** (hard=0, gen_soft=2, tr_soft=1, judge=2, auditor=2)
- **S4 entity_coverage_complete_rate:** `0.9`
- **S4b script_fail_count:** `1`
- **S5 pass_rate:** `0.9`
- **S6 pass_rate / passed:** `0.8888888888888888` / `16`
- **curated docs:** `9`

## Summary

| Stage | UUID | Lang | Doc type | Symptom |
| --- | --- | --- | --- | --- |
| S4 soft | `7568f8e67bea4c959a480fd295d29db7` | `en` | `discharge_summary` | `['missing_required_entities:DOB']` |
| S4 soft | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `opd_slip` | `['missing_required_entities:DOB,OCCUPATION,HOSPITAL_ID']` |
| S4b soft | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `opd_slip` | `script_purity_failed:target_script_ratio:0.241<0.35 attempt=1` |
| S5 fail | `396f437fcf6a45e6b7f38f4fe5cf5e48` | `gu` | `opd_slip` | score=0.3 flags=['dialect_script_impurity'] |
| S5 fail | `93bac4c7fd9e4e2bbdf66866e9203b8b` | `gu` | `surgical_note` | score=0.3 flags=['instruction_drift', 'surrogate_plausibility_collapse'] |
| S6 fail | `7568f8e67bea4c959a480fd295d29db7` | `en` | `discharge_summary` | `['missing_required:DOB', 'upstream_generation_soft_fail:missing_required_entities:DOB']` |
| S6 fail | `66f87f0087064abda3938f2c4aba879e` | `pa` | `insurance_claim` | `['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:3']` |

## Per-failure audit

### S4 generation soft-fail 1

- **What:** generation soft-fail on `discharge_summary` (`en`).
- **Missing required tags:** `['DOB']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DOB']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Lilavati Hospital]]
[[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-004]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Vikram Mehta]] | Course / advice: The patient is a 32-year-old female with a history of Stage III Triple-Negative Breast Cancer, admitted for management of chemotherapy-induced neutropenic sepsis. She has completed six cycles of adjuvant chemotherapy and was scheduled for the seventh cycle. On admission, she presented with fever, chills, and a neutrophil count of 0.2 x 10^…
```

### S4 generation soft-fail 2

- **What:** generation soft-fail on `opd_slip` (`gu`).
- **Missing required tags:** `['DOB', 'OCCUPATION', 'HOSPITAL_ID']`
- **Stuffing flags:** `—`
- **Raw reasons:** `['missing_required_entities:DOB,OCCUPATION,HOSPITAL_ID']`
- **Why likely:** model wrote clinical chat/prose without wrapping every mandatory TYPE (common on telemedicine when AGE/GENDER stay in narrative only).
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient: [[PATIENT_NAME|Ahmed Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0915-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Shah]]
District: [[DISTRICT|Ahmadabad]] | Chief complaint: સતત ઓછું mood અને anxiety છેલ્લા બે મહિનાથી.

History of Present Illness:
Patient, 23 વર્ષનો પુરુષ homemaker, low mood, anhedonia, અને generalized anxiety ની ફરિયાદ સાથે આવે છે. Symptoms લગભગ આઠ અઠવાડિયા પહેલા શરૂ થયા હતા અને ધીમે ધીમે વધ્યા છે. તે ઊંઘવામાં તકલીફ, ઓછું appetite, અને worthlessness ની લાગણી જણાવે છે. તે કોઈ suicidal ideation …
```

### S4b translation soft-fail 1

- **What:** translation soft-fail on `opd_slip` (`gu`).
- **Error:** `script_purity_failed:target_script_ratio:0.241<0.35 attempt=1`
- **script_ok:** `False`
- **Why:** output stayed Latin / Romanized instead of the target Indic script (ratio below threshold). Judge usually fails this too.
- **EN pivot preview:**

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient: [[PATIENT_NAME|Ahmed Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0915-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Shah]]
District: [[DISTRICT|Ahmadabad]] | Chief complaint: Persistent low mood and anxiety for the past two months.

History of Present Illness:
The patient, a 23-year-old male homemaker, presents with…
```
- **Translated preview:**

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient: [[PATIENT_NAME|Ahmed Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0915-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Shah]]
District: [[DISTRICT|Ahmadabad]] | Chief complaint: સતત ઓછું mood અને anxiety છેલ્લા બે મહિનાથી.

History of Present Illness:
Patient, 23 વર્ષનો પુરુષ homemaker, low mood, anhedonia, અને general…
```

### S5 judge fail 1

- **What:** linguistic judge **fail** on `opd_slip` (`gu`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['dialect_script_impurity']`
- **Reasoning:** Clinical prose is predominantly English with sporadic Gujarati insertions instead of full Gujarati narrative as required; code-mixing violates script/language rule despite allowed Latin tags.
- **Preview:**

```
OPD Slip | [[HOSPITAL_NAME|Shri Krishna Hospital]]
Patient: [[PATIENT_NAME|Ahmed Patel]] | Age: [[AGE|23]] | Gender: [[GENDER|Male]]
MRN: [[MRN|OPD-2024-0915-001]] | Doctor: [[DOCTOR_NAME|Dr. Priya Shah]]
District: [[DISTRICT|Ahmadabad]] | Chief complaint: સતત ઓછું mood અને anxiety છેલ્લા બે મહિનાથી.

History of Present Illness:
Patient, 23 વર્ષનો પુરુષ homemaker, low mood, anhedonia, અને generalized anxiety ની ફરિયાદ સાથે આવે છે. Symptoms લગભગ આઠ અઠવાડિયા પહેલા શરૂ થયા હતા અને ધીમે ધીમે વધ્યા …
```

### S5 judge fail 2

- **What:** linguistic judge **fail** on `surgical_note` (`gu`).
- **Score / verdict:** `0.3` / `fail`
- **Flags:** `['instruction_drift', 'surrogate_plausibility_collapse']`
- **Reasoning:** Operative note format with psych admission content only; no procedure/findings; relative name gender implausible (Ramesh Devi as husband).
- **Preview:**

```
ઓપરેટિવ નોટ — [[HOSPITAL_NAME|District Hospital Bharuch]] એડમિટ [[ADMISSION_NUMBER|ADM-2024-0515]] વોર્ડ [[WARD_NUMBER|B2]]
[[PATIENT_NAME|Meena Devi]] [[AGE|42]] [[GENDER|Female]] સર્જન [[DOCTOR_NAME|Dr. Rajesh Patel]]
પ્રક્રિયા / તારણો: દર્દી 42-વર્ષની સ્ત્રી છે જે ક્રોનિક એન્ઝાયટી અને ડિપ્રેસિવ એપિસોડ્સના ઇતિહાસ સાથે રજૂ થાય છે, જે ઘણા વર્ષોથી રૂઢિચુસ્ત રીતે સંચાલિત કરવામાં આવ્યા છે. તાજેતરમાં લક્ષણો વધવાને કારણે પેનિક એટેક અને અનિદ્રાને કારણે એડમિશન આપવામાં આવ્યું. વાઇટલ્સ સ્થિર છે. શારીરિક…
```

### S6 auditor fail 1

- **What:** deterministic auditor **fail** on `discharge_summary` (`en`).
- **Errors:** `['missing_required:DOB', 'upstream_generation_soft_fail:missing_required_entities:DOB']`
- **Cause chain:** inherited S4 generation soft-fail (not silent).
- **Cause:** profile-required entity TYPE(s) absent from text.
- **Preview:**

```
Discharge Summary — [[HOSPITAL_NAME|Lilavati Hospital]]
[[PATIENT_NAME|Anita Patil]] [[AGE|32]] [[GENDER|Female]] Adm [[ADMISSION_NUMBER|ADM-2024-0815-004]] Ward [[WARD_NUMBER|B2]] Bed [[BED_NUMBER|12]]
Dr [[DOCTOR_NAME|Dr. Vikram Mehta]] | Course / advice: The patient is a 32-year-old female with a history of Stage III Triple-Negative Breast Cancer, admitted for management of chemotherapy-induced neutropenic sepsis. She has completed six cycles of adjuvant chemotherapy and was scheduled for th…
```

### S6 auditor fail 2

- **What:** deterministic auditor **fail** on `insurance_claim` (`pa`).
- **Errors:** `['format:AADHAAR_NUMBER:aadhaar_verhoeff', 'phi_residue:3']`
- **Preview:**

```
TPA claim — Policy [[INSURANCE_POLICY_NUMBER|POL-PB-2024-7781]]
[[PATIENT_NAME|Jaswinder Kaur]] [[AGE|55]] [[GENDER|Female]] Aadhaar [[AADHAAR_NUMBER|589241673452]]
Hospital [[HOSPITAL_NAME|Civil Hospital Muktsar]] District [[DISTRICT|Muktsar]]
Motor / RTA vehicle [[VEHICLE_REGISTRATION|PB05AB1234]]
PAN [[PAN_NUMBER|FGHIJ5678K]] IFSC [[IFSC_CODE|PUNB0001234]] account [[BANK_ACCOUNT_NUMBER|50200012345678]]
Bank Routing Number [[BANK_ROUTING_NUMBER|PUNB0001234]]
Credit Card [[CREDIT_CARD_NUMBER|5…
```


## Surviving curated set

- languages: `{'bn': 1, 'en': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 1, 'automated_sms': 1, 'discharge_summary': 1, 'opd_slip': 2, 'prescription': 2, 'radiology_report': 1, 'surgical_note': 1}`

_Generated by `main.pipeline.failures_report`. Re-run: `python -m main.pipeline.failures_report --run-id <id>`._
