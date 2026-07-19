# Stage 4 — Generation Audit

- provider: `sarvam`
- model: `sarvam-105b`
- reasoning_effort: `None` (null = OFF)
- requests_per_minute: `110.0`
- max_workers: `8`
- max_tokens: `16384`
- reject_truncated: `True`
- rows_generated: **10**
- mean_chars: `1233.2`
- languages: `{'bn': 1, 'en': 1, 'gu': 1, 'hi': 1, 'kn': 1, 'ml': 1, 'mr': 1, 'pa': 1, 'ta': 1, 'te': 1}`
- doc_types: `{'asha_worker_note': 2, 'automated_sms': 3, 'er_triage_notes': 1, 'radiology_report': 3, 'telemedicine_transcript': 1}`

## Preview

### bn · asha_worker_note · tb_ncd

```
ASHA note — Village [[VILLAGE|Howrah]], District [[DISTRICT|Haora]]
Beneficiary [[PATIENT_NAME|Sathi Mandal]], [[AGE|23]] / [[GENDER|Female]]
ASHA: [[ASHA_WORKER_NAME|Anita Roy]] | Phone [[PHONE_NUMBER|9876543210]]
Visit findings: Patient reports persistent cough for three weeks with occasional fever. She was advised to get a sputum test done at the nearest health center. [[RELATIVE_NAME|Ranjan Mandal]] was informed about the importance of completing the full course of treatment. Patient holds a [[BPL_RATION_CARD|BPL-WB-2023-456789]] and her [[VOTER_ID|WBV20234567890]] was verified for follow-up. Patient is [[RELIGION|Hindu]].
```

### en · telemedicine_transcript · psychiatry_behavioral

```
Patient [[PATIENT_NAME|Anita Patil]] ([[PHONE_NUMBER|9876543210]]): Hello doctor, I'm feeling very anxious lately. I have a telemedicine appointment today.
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] ([[HOSPITAL_NAME|Jaslok Hospital Mumbai]]): Hello [[PATIENT_NAME|Anita Patil]], I see you for your scheduled appointment. Can you tell me more about your anxiety?
Patient [[PATIENT_NAME|Anita Patil]] ([[PHONE_NUMBER|9876543210]]): It's mostly work-related. I am an oil expeller and the pressure is high. I feel my heart racing sometimes.
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] ([[HOSPITAL_NAME|Jaslok Hospital Mumbai]]): I understand. [[AGE|32]] and [[GENDER|Female]], you are experiencing palpitations. When did this start?
Patient [[PATIENT_NAME|Anita Patil]] ([[PHONE_NUMBER|9876543210]]): About two weeks ago. I also have trouble sleeping.
Dr [[DOCTOR_NAME|Dr. Priya Deshmukh]] ([[HOSPITAL_NAME|Jaslok Hospital Mumbai]]): Let's schedule a follow-up. Your [[APPOINTMENT_ID|APT-MH-2024-0815-001]] is confirmed. Please be ready at [[TIME|7 PM]].
Patient [[PATIENT_NAME|Anita Patil]] ([[PHONE_NUMBER|9876543210]]): Okay. What is the [[IP_ADDRESS|192.168.1.100]] for the video call?
Dr [[DOCTOR_NAME|Dr. Priy
```

### gu · er_triage_notes · tb_ncd

```
ER triage — [[HOSPITAL_NAME|Shri Krishna Hospital]] Encounter [[ENCOUNTER_ID|ENC-2024-0815-001]]
[[PATIENT_NAME|Ahmed Khan]] [[AGE|23]] [[GENDER|Male]] Ward [[WARD_NUMBER|ER]] Dr [[DOCTOR_NAME|Dr. Rajesh Patel]]
Vitals / acuity: Patient presents with persistent cough for 3 weeks, low-grade fever, and weight loss. Acuity: High. Requires immediate chest X-ray and sputum analysis.

Nursing Notes:
Patient admitted to [[BED_NUMBER|05]] in the Emergency ward. Initial assessment completed by [[DOCTOR_NAME|Dr. Rajesh Patel]]. Patient is alert and oriented x3. Reports feeling weak and fatigued. Respiratory rate is 22 breaths per minute, heart rate 105 bpm, temperature 37.8°C, blood pressure 120/80 mmHg, SpO2 94% on room air. Patient reports a productive cough with yellowish sputum. No known drug allergies. Family history significant for tuberculosis. Patient's father, [[RELATIVE_NAME|Mohammad Khan]], is available for contact and has been informed of the patient's condition. Patient's [[PHONE_NUMBER|9876543210]] is on file for follow-up. Patient's [[VEHICLE_REGISTRATION|GJ-01-AB-1234]] was noted at the hospital entrance. Patient is a non-smoker and consumes alcohol socially. Diet ordered: so
```
