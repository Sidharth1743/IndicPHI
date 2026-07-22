# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `180.0`
- network_retries: `2`
- rows_judged: **69**
- soft_fail_count: **0**
- failure_count: **19**
- judge_repaired_count: **9**
- pass_rate: **0.725**
- label_distribution: `{'fail': 0.2753623188405797, 'pass': 0.7246376811594203}`
- positional_length_bias: `{'pearson_r': -0.2601068650185871, 'n': 69.0}`

## Failures (audited — not silent)

- `3c0199017c7c4f00bbb3de4770ce25fc` · `hospital_billing` · `as` · score=0.35 soft=False · All content in English/Latin script instead of Assamese (Bengali); multiple non-allowlist types (ADMISSION_DATE, BILLING_CODE, DISCHARGE_DATE, etc.).
- `2a0042e543f7400299209a84f31ceab7` · `er_triage_notes` · `brx` · score=0.35 soft=False · Domain oncology/chronic care violated by acute appendicitis content; clinical prose mixes English medical phrases instead of consistent Bodo Devanagari narrative.
- `2a0042e543f7400299209a84f31ceab7` · `telemedicine_transcript` · `brx` · score=0.35 soft=False · All clinical prose is Hindi (not Bodo) despite Devanagari script and correct Latin-tagged entities.
- `2a0042e543f7400299209a84f31ceab7` · `surgical_note` · `brx` · score=0.3 soft=False · Clinical prose is Hindi, not Bodo, despite Devanagari script and valid tags.
- `8027a62865e6486cba6cb4978d8de433` · `radiology_report` · `doi` · score=0.18 soft=False · English prose instead of Dogri Devanagari; male patient with ovarian/uterine anatomy and adnexal mass.
- `c56b228238e847d393141f0a17d86444` · `er_triage_notes` · `hi` · score=0.0 soft=False · Pure English title repetition (no Devanagari prose); extreme length dump with zero clinical content or Hindi narrative.
- `442b760204fb4430b6745545930228cd` · `opd_slip` · `ks` · score=0.35 soft=False · Clinical prose is Urdu (not Kashmiri) despite Arabic script and correct persona/domain fit.
- `442b760204fb4430b6745545930228cd` · `prescription` · `ks` · score=0.3 soft=False · Clinical prose entirely in English; expected Kashmiri Arabic script.
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `lab_report` · `mni` · score=0.25 soft=False · Prose entirely in Bengali script/language instead of required Meitei script for Manipuri; all other elements (tags, content, persona fit) acceptable.
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `opd_slip` · `mni` · score=0.15 soft=False · OPD prose complaint is repetitive gibberish in Bengali script (not Meitei), massively exceeds length, and lacks clinical plausibility.
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `phc_register` · `mni` · score=0.35 soft=False · Prose mixes Bengali script with Tamil intrusion instead of Meitei; long multi-paragraph narrative also mismatches register-entry brevity.
- `edf29d2e2af24030992b0a4ccf114083` · `er_triage_notes` · `pa` · score=0.55 soft=False · Clinical narrative mixes substantial English prose sentences with Punjabi; expected full Gurmukhi body for Punjabi document.
- `6e943dc3578249e38b9e61705d0912a9` · `phc_register` · `sa` · score=0.55 soft=False · Prose is Hindi (with Sanskritized medical terms) in Devanagari rather than Sanskrit; minor English glosses outside tags but main narrative mismatches required language.
- `944cf9bf2c4d48b2974bb723f704bded` · `referral_letter` · `sat` · score=0.25 soft=False · All clinical prose in English; expected Santali Ol Chiki. No other violations (entities allowed, persona fit, length ok).
- `944cf9bf2c4d48b2974bb723f704bded` · `radiology_report` · `sat` · score=0.2 soft=False · Clinical prose entirely in English; expected Santali Ol Chiki narrative.
- `944cf9bf2c4d48b2974bb723f704bded` · `er_triage_notes` · `sat` · score=0.25 soft=False · Prose is English/Latin with scattered transliterated Santali words; expected full Santali narrative in Ol Chiki script.
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `er_triage_notes` · `sd` · score=0.4 soft=False · Narrative prose heavily code-mixed with English terms and contains Devanagari intrusions instead of consistent Sindhi (Arabic script).
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `telemedicine_transcript` · `sd` · score=0.25 soft=False · Prose mixes Devanagari/Thai/English heavily into Sindhi Arabic narrative; violates expected script despite valid entity tags.
- `6dae1a15538348f3a3bc29a4111088bc` · `opd_slip` · `te` · score=0.55 soft=False · Domain Oncology specified but content is TB workup/diagnosis; Telugu prose and allowed entities otherwise match.
