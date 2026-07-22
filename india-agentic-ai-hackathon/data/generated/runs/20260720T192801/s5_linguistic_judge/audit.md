# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `180.0`
- network_retries: `2`
- rows_judged: **69**
- soft_fail_count: **0**
- failure_count: **27**
- pass_rate: **0.609**
- label_distribution: `{'fail': 0.391304347826087, 'pass': 0.6086956521739131}`
- positional_length_bias: `{'pearson_r': -0.2123442196329464, 'n': 69.0}`

## Failures (audited — not silent)

- `2a0042e543f7400299209a84f31ceab7` · `er_triage_notes` · `brx` · score=0.25 soft=False · Clinical narrative prose entirely in English; expected Bodo Devanagari. All entity tags allowed and Latin IDs permitted; no persona or length mismatch.
- `2a0042e543f7400299209a84f31ceab7` · `telemedicine_transcript` · `brx` · score=0.25 soft=False · Clinical prose entirely in Hindi (Devanagari) instead of required Bodo; all entity tags valid and Latin IDs permitted.
- `2a0042e543f7400299209a84f31ceab7` · `surgical_note` · `brx` · score=0.35 soft=False · Clinical prose is Hindi (Indo-Aryan) instead of Bodo despite Devanagari script; all other elements (persona fit, entity tags, length, medical content) are acceptable.
- `f584cfd90471426ea809f549021f9a0f` · `referral_letter` · `en` · score=0.8 soft=False · Non-allowlisted TYPE MEDICAL_RECORD_NUMBER used; all other aspects compliant.
- `f584cfd90471426ea809f549021f9a0f` · `radiology_report` · `en` · score=0.65 soft=False · District mismatch (Udupi vs expected Dakshina Kannada) and weak maternal-health fit for post-menopausal screening.
- `c56b228238e847d393141f0a17d86444` · `er_triage_notes` · `hi` · score=0.4 soft=False · Implausible occupation phrase and illiterate-supervisor contradiction break surrogate fit; minor prose drift.
- `a90ec50b35a04cb3a09db6ca09ff1a37` · `lab_report` · `kn` · score=0.45 soft=False · STUDENT_ID on 55yo; meta PHI note + empty psych lab content; minor English abbr in Kannada prose
- `442b760204fb4430b6745545930228cd` · `opd_slip` · `ks` · score=0.55 soft=False · Clinical prose written in Urdu (not Kashmiri) despite Arabic script and expected ks language; all entity types allowed and persona fit otherwise.
- `442b760204fb4430b6745545930228cd` · `prescription` · `ks` · score=0.25 soft=False · All clinical prose in English; expected Kashmiri Arabic script not used.
- `72db01dc59584f27949df74b76c51edf` · `referral_letter` · `mai` · score=0.35 soft=False · 18yo male persona described as retired housewife (गृहणी); clear contradiction despite mostly correct Maithili prose and valid entity tags.
- `f3d9ad4909c345f99fadaafad821b3b0` · `opd_slip` · `ml` · score=0.7 soft=False · District value Kollam mismatches persona Thrissur; prose/script and entity types otherwise compliant.
- `f3d9ad4909c345f99fadaafad821b3b0` · `prescription` · `ml` · score=0.65 soft=False · District mismatch (Thrissur persona vs Ernakulam/Kochi in text); all other prose, script, and entity types adhere.
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `opd_slip` · `mni` · score=0.25 soft=False · All clinical prose in English; expected Manipuri/Meitei script for narrative.
- `51fc0c57ffcc40c6ae5d2fb055d07030` · `phc_register` · `mni` · score=0.1 soft=False · Massive tag repetition creates >>400-char dump with no Manipuri prose or maternal content; generation collapse evident.
- `01f011a8da4d401ca4ff9810f7a35a19` · `insurance_claim` · `or` · score=0.25 soft=False · All narrative prose in English; expected Odia script for clinical content per instructions.
- `edf29d2e2af24030992b0a4ccf114083` · `radiology_report` · `pa` · score=0.6 soft=False · Male-coded name (Jaswant Singh) + female gender tag; district Amritsar vs expected Rupnagar; minor domain fit issue for psych+radiology
- `edf29d2e2af24030992b0a4ccf114083` · `er_triage_notes` · `pa` · score=0.65 soft=False · Female persona with repeated masculine verb forms (ਰਿਹਾ ਹੈ) in Punjabi prose; minor English label mixing but narrative script mostly compliant and entities allowed.
- `6e943dc3578249e38b9e61705d0912a9` · `asha_worker_note` · `sa` · score=0.55 soft=False · Prose mixes Hindi terms with Sanskrit; expected pure Sanskrit clinical narrative in Devanagari.
- `6e943dc3578249e38b9e61705d0912a9` · `phc_register` · `sa` · score=0.25 soft=False · Prose is Hindi (Devanagari) not Sanskrit; language mismatch with expected sa script.
- `944cf9bf2c4d48b2974bb723f704bded` · `referral_letter` · `sat` · score=0.15 soft=False · All clinical prose in English; expected Santali Ol Chiki narrative absent.
- `944cf9bf2c4d48b2974bb723f704bded` · `radiology_report` · `sat` · score=0.25 soft=False · Narrative prose fully English; expected Santali Ol Chiki script.
- `944cf9bf2c4d48b2974bb723f704bded` · `er_triage_notes` · `sat` · score=0.25 soft=False · Prose is English with scattered Santali words in Latin script; expected full Santali narrative in Ol Chiki.
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `er_triage_notes` · `sd` · score=0.25 soft=False · Endless repetition of filler phrase creates >>400-char dump; clinical notes lack coherent Sindhi prose or psychiatric triage content despite correct script and allowed entity tags.
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `telemedicine_transcript` · `sd` · score=0.35 soft=False · Prose entirely in Devanagari instead of required Sindhi Arabic script; all entity types allowed and persona fit otherwise ok.
- `68da8d4342bc4e28a1a4cd69a55cc86f` · `surgical_note` · `sd` · score=0.3 soft=False · Prose mixes Meitei/Devanagari/English intrusions into expected Sindhi Arabic script; medical narrative implausibly garbled.
- `6dae1a15538348f3a3bc29a4111088bc` · `opd_slip` · `te` · score=0.55 soft=False · Domain oncology/chronic care specified but content is lumbar disc disease; prose mostly Telugu with acceptable Latin terms.
- `c8cbb5811e2a4a05bfe15b06b2be3a52` · `hospital_billing` · `ur` · score=0.45 soft=False · Extensive clinical narrative (SOAP-style) exceeds pure billing/invoice scope; Urdu-primary + Narayanan name in TN creates low plausibility; multi-paragraph length violates concise invoice expectation.
