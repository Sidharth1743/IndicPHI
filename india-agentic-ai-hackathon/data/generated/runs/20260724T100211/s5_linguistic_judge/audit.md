# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `120.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **506**
- soft_fail_count: **0**
- failure_count: **14**
- judge_repaired_count: **49**
- pass_rate: **0.972**
- label_distribution: `{'fail': 0.02766798418972332, 'pass': 0.9723320158102767}`
- positional_length_bias: `{'pearson_r': -0.021587677953490467, 'n': 506.0}`

## Failures (audited — not silent)

- `f619d5abd8244e93aab697fe1a8241a8` · `lab_report` · `brx` · score=0.25 soft=False · Clinical prose uses Bengali-Assamese script and Assamese phrasing instead of required Bodo Devanagari; LABORATORY_TECHNICIAN_NAME and LAB_TECH_ID outside allow-list.
- `f619d5abd8244e93aab697fe1a8241a8` · `asha_worker_note` · `brx` · score=0.35 soft=False · Bodo prose polluted with Hindi phrases; patient name culturally implausible and in wrong script for Devanagari Bodo note.
- `fee4de17dbbf4d15b95ef10f6a01c60c` · `referral_letter` · `brx` · score=0.65 soft=False · REFERRAL_ID outside allow-list; Bodo Devanagari prose and persona fit otherwise acceptable.
- `e90c7788a683415497f7cf0718f7966b` · `telemedicine_transcript` · `ks` · score=0.55 soft=False · Name clash: PATIENT_NAME=Manoj Yadav vs. doctor addressing patient as غلام رسول + ghulam.rasool email; Kashmiri prose and clinical fit otherwise acceptable.
- `75419f1fe22f409c8108d2a13f2e677f` · `referral_letter` · `mni` · score=0.2 soft=False · All clinical prose in English; expected Manipuri/Meitei script per instructions.
- `6e943dc3578249e38b9e61705d0912a9` · `insurance_claim` · `sa` · score=0.45 soft=False · Prose mixes Hindi/English (TPA, RTA, PAN, IFSC, दावा) instead of Sanskrit; Devanagari present but language not matching expected sa.
- `3bc580120add4e55b09a0e1ac85b643f` · `hospital_billing` · `sat` · score=0.2 soft=False · All narrative prose in English/Latin; expected Santali Ol Chiki script absent despite correct allow-listed tags and persona fit.
- `3bc580120add4e55b09a0e1ac85b643f` · `discharge_summary` · `sat` · score=0.55 soft=False · Female patient described with 'patni' (wife) relative + male name Bijoy; gender/spouse mismatch breaks persona and surrogate plausibility.
- `3bc580120add4e55b09a0e1ac85b643f` · `er_triage_notes` · `sat` · score=0.2 soft=False · Prose entirely English; expected Santali Ol Chiki clinical narrative.
- `228cb6f1c22941279fc07428487acd05` · `radiology_report` · `sd` · score=0.55 soft=False · Clinical narrative prose mixes Gujarati characters into Sindhi Arabic script; other elements (tags, persona, length, entity types) compliant.
- `228cb6f1c22941279fc07428487acd05` · `telemedicine_transcript` · `sd` · score=0.35 soft=False · Sindhi prose rendered in Devanagari (with Hindi intrusions like 'नमस्ते') instead of required Arabic script; all tags/IDs valid and persona fit ok.
- `6227e1809b0743be8c7473f02961d290` · `automated_sms` · `sd` · score=0.3 soft=False · Sindhi Arabic prose polluted by Gujarati script intrusion (માટે) and English transliterations; other aspects (persona, entities, length) acceptable.
- `6227e1809b0743be8c7473f02961d290` · `discharge_summary` · `sd` · score=0.55 soft=False · Patient name Latin + South-Indian (Karthik Krishnan) mismatches Sindhi/Arabic-script prose, Memon relative/caste, and Ramesh ABHA; other elements (prose script, domain, tags, length) acceptable.
- `043f5fb0c78c482298663bcaa05618fe` · `insurance_claim` · `te` · score=0.62 soft=False · ZONE outside allow-list; duplicate/misplaced RESIDENTIAL_ADDRESS + PIN reuse create minor admin inconsistency; Telugu clinical prose and persona/domain fit otherwise acceptable.
