# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `40.0`
- max_tokens: `4096`
- rows_generated: **10**
- mean_chars: `3016.1`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'automated_sms': 3, 'discharge_summary': 1, 'hospital_billing': 1, 'insurance_claim': 2, 'prescription': 2, 'referral_letter': 1}`

## Preview

### bn · hospital_billing · oncology_chronic

```
হাসপাতাল বিল / ইনভয়েস
হাসপাতালের নাম: [[HOSPITAL_NAME|গ্লোবাল হেলথ কেয়ার, হাওড়া]]
রোগীর নাম: [[PATIENT_NAME|সতী মণ্ডল]]
মেডিকেল রেকর্ড নম্বর: [[MRN|GHCH-2024-BNG-8901]]
জন্ম তারিখ: 15/08/2001
লিঙ্গ: মহিলা
ঠিকানা: [[DISTRICT|হাওড়া]] জেলা, [[PIN_CODE|711101]]
ফোন নম্বর: [[PHONE_NUMBER|9876543210]]
আধার নম্বর: [[AADHAAR_NUMBER|234567890123]]
বীমা পলিসি নম্বর: [[INSURANCE_POLICY_NUMBER|WB-INS-2023-456789]]

বিলিং তারিখ: 25/10/2024
বিল নম্বর: GHCH-INV-2024-1025-001

বিবরণ | পরিমাণ | ইউনিট মূল্য | মোট
---|---|---|---
প্রাথমিক পরামর্শ (অনকোলজি) | 1 | 1500.00 | 1500.00
ল্যাবরেটরি পরীক্ষা (সি.বি.সি, এল.এফ.টি, রেনাল প্রোফাইল) | 1 | 800.00 | 800.00
প্যাথলজি (বায়োপসি এবং হিস্টোপ্যাথলজি) | 1 | 2500.00 | 2500.00
ইমেজিং (সিটি স্ক্যান অ্যাবডোমেন এবং পেলভিস) | 1 | 3500.00 | 3500.00
ওষুধ (প্রথম পর্যায়ের কেমোথেরাপি - সাইক্লোফসফামাইড 500mg) | 1 | 1200.00 | 1200.00
ওষুধ (দ্বিতীয় পর্যায়ের কেমোথেরাপি - ডক্সোরুবিসিন 60mg) | 1 | 1800.00 | 1800.00
ওষুধ (সহায়ক ওষুধ - অ্যান্টি-এমেটিকস এবং জিঙ্ক) | 1 | 500.00 | 500.00
নার্সিং চার্জ (প্রতিদিন) | 5 | 750.00 | 3750.00
বেড চার্জ (আই.সি.ইউ) | 3 | 2000.00 | 6000.00
ডাক্তারদের ফি (অনকোলজিস্ট) | 1 | 2000.00 | 2000.00
ডাক্তারদের ফি (রেডিওলজিস্ট) | 1 | 1000.00 
```

### en · prescription · psychiatry_behavioral

```
PRESCRIPTION

Date: [[DATE|2024-05-21]]
Prescribing Physician: Dr. [[DOCTOR_NAME|Dr. Anjali Sharma]]
Hospital: [[HOSPITAL_NAME|Saraswati Wellness Clinic]]
Patient: [[PATIENT_NAME|Kaushalya Siddharth]]
Age: [[AGE|32]]
Gender: [[GENDER|Female]]
MRN: [[MRN|MH-MUM-987654]]

Diagnosis: Generalized Anxiety Disorder, F41.1

Instructions:
Take the following medication as directed.

Medication:
- Sertraline 50mg
  - One tablet orally once daily in the morning.
  - May be increased to 100mg after 2 weeks if tolerated.

- Clonazepam 0.5mg
  - One tablet orally twice daily as needed for acute anxiety.
  - Do not exceed 4 tablets in 24 hours.

Non-Pharmacological Recommendations:
1. Practice mindfulness meditation for 10 minutes daily.
2. Engage in regular physical activity, such as a 30-minute walk.
3. Maintain a consistent sleep schedule, aiming for 7-8 hours of sleep per night.
4. Avoid excessive caffeine and alcohol consumption.

Follow-up:
Please schedule a follow-up appointment in 4 weeks to assess response to treatment and medication tolerance.

For any urgent concerns, contact the clinic at [[PHONE_NUMBER|+91-22-2654-7890]].

[[RESIDENTIAL_ADDRESS|123, Shivaji Nagar, Andheri West, Mumba
```

### gu · prescription · tb_ncd

```
દવા પત્રક

દર્દીનું નામ: [[PATIENT_NAME|Bhai Shekh]]
ઉંમર: [[AGE|23]]
જાતિ: [[GENDER|Male]]
તબીબી રેકોર્ડ નંબર (MRN): [[MRN|MH-2024-GUJ-001234]]
તબીબી ઇતિહાસ: દર્દીને બે વર્ષથી ઉધરસ અને તાવની સમસ્યા છે. છાતીના એક્સ-રેમાં ઇન્ફેક્શન જોવા મળ્યું છે. દર્દીને ડાયાબિટીસ નથી.

તબીબી તપાસ: ડો. [[DOCTOR_NAME|Dr. Anjali Patel]] દ્વારા દર્દીની તપાસ કરવામાં આવી છે. દર્દીનું તાપમાન 38.5 ડિગ્રી સેલ્સિયસ છે.

દવા:
1. આઇસોનિયાઝિડ (Isoniazid) 300 mg - દિવસમાં એકવાર, 6 મહિના માટે.
2. રિફામ્પિસિન (Rifampicin) 600 mg - દિવસમાં એકવાર, 6 મહિના માટે.
3. પાયરાઝિનામાઇડ (Pyrazinamide) 1500 mg - દિવસમાં એકવાર, 2 મહિના માટે.
4. ઇથામ્બુટોલ (Ethambutol) 800 mg - દિવસમાં એકવાર, 2 મહિના માટે.

સૂચનાઓ:
- દવા દરરોજ ખાલી પેટે લેવી.
- દવા લેવાનું ભૂલી ન જવું.
- નિયમિતપણે ડો. [[DOCTOR_NAME|Dr. Anjali Patel]] ને મળવું.
- હોસ્પિટલ: [[HOSPITAL_NAME|Shri Krishna Multispecialty Hospital, Ahmedabad]].

ફોલો-અપ: 15 દિવસ પછી ફરીથી તપાસ માટે આવવું.

સરનામું: [[RESIDENTIAL_ADDRESS|Old City, Ahmedabad, Gujarat, 380001]]
ફોન: [[PHONE_NUMBER|+91-9876543210]]
જિલ્લો: [[DISTRICT|Ahmedabad]]
```
