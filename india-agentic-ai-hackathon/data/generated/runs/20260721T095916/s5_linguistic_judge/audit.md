# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `180.0`
- network_retries: `2`
- rows_judged: **69**
- soft_fail_count: **0**
- failure_count: **11**
- judge_repaired_count: **12**
- pass_rate: **0.841**
- label_distribution: `{'fail': 0.15942028985507245, 'pass': 0.8405797101449275}`
- positional_length_bias: `{'pearson_r': 0.010457970467638323, 'n': 69.0}`

## Failures (audited — not silent)

- `a24958482d8b463ab3daeee28d5f5365` · `automated_sms` · `brx` · score=0.3 soft=False · Prose uses Assamese/Bengali script and phrasing instead of required Bodo Devanagari.
- `ecc5c42af9364fb79dfa7c3bc3b426f7` · `telemedicine_transcript` · `doi` · score=0.45 soft=False · Prose in standard Hindi; expected Dogri language in Devanagari.
- `ecc5c42af9364fb79dfa7c3bc3b426f7` · `surgical_note` · `doi` · score=0.35 soft=False · Clinical prose is standard Hindi; Dogri (Devanagari) required. All tags allowed, persona/domain fit, length ok.
- `217fa134e0d64da4962f287453b86c70` · `prescription` · `ks` · score=0.25 soft=False · Clinical prose entirely in English/Latin script; expected Kashmiri (Arabic script). All entity types allowed, persona/domain fit, no length or surrogate issues.
- `217fa134e0d64da4962f287453b86c70` · `insurance_claim` · `ks` · score=0.25 soft=False · Clinical prose entirely in English instead of required Kashmiri Arabic script; multiple non-allowlist TYPEs (CHIEF_COMPLAINT, HOSPITAL_COURSE, DISCHARGE_PLAN, TREATMENT_SUMMARY, ADMITTING_PHYSICIAN).
- `217fa134e0d64da4962f287453b86c70` · `asha_worker_note` · `ks` · score=0.35 soft=False · Narrative prose entirely in English instead of required Kashmiri Arabic script; minor district mismatch but language is primary failure.
- `1e23bb4e93b0465fa42494aee52e02ef` · `telemedicine_transcript` · `mni` · score=0.25 soft=False · All clinical chat prose in English; expected Manipuri/Meitei script. All entity tags valid and Latin IDs allowed.
- `1e23bb4e93b0465fa42494aee52e02ef` · `surgical_note` · `mni` · score=0.45 soft=False · Narrative prose uses Bengali script/language instead of required Meitei; all entity types valid, persona/clinical fit plausible, no length or invented-type issues.
- `2308b919936944228c90a4864f352d14` · `er_triage_notes` · `pa` · score=0.3 soft=False · Clinical narrative prose is predominantly English with only scattered Gurmukhi insertions; expected full Punjabi (Gurmukhi) for this document language.
- `7604eaf4ec554261b752518c0f8a656e` · `referral_letter` · `sat` · score=0.25 soft=False · Prose entirely in Hindi/Devanagari; expected Santali Ol Chiki script for narrative.
- `7604eaf4ec554261b752518c0f8a656e` · `er_triage_notes` · `sat` · score=0.2 soft=False · Clinical prose entirely in English; expected Santali Ol Chiki narrative absent.
