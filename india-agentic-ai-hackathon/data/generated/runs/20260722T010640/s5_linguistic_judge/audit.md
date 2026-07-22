# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **8**
- judge_repaired_count: **9**
- pass_rate: **0.942**
- label_distribution: `{'fail': 0.057971014492753624, 'pass': 0.9420289855072463}`
- positional_length_bias: `{'pearson_r': 0.005619885694973533, 'n': 138.0}`

## Failures (audited — not silent)

- `8b77264c0f7747c59ec191e95202ff7f` · `insurance_claim` · `brx` · score=0.35 soft=False · Clinical prose entirely in Hindi (wrong language) despite Devanagari script and Bodo requirement; all entity tags valid and Latin IDs allowed.
- `fac14bf3d91143958fc1e8190e25c390` · `insurance_claim` · `brx` · score=0.25 soft=False · Clinical narrative in Nepali (not Bodo); district mismatches persona anchor (Kokrajhar vs Kamrup); extra billing entities soft but language fails requirement.
- `fac14bf3d91143958fc1e8190e25c390` · `asha_worker_note` · `brx` · score=0.35 soft=False · Clinical narrative prose is Nepali (e.g. 'बिरामीले आफ्नो', 'गर्छिन्', 'रगत चिनी') instead of Bodo; all entity tags and Latin medical terms are valid.
- `9b16854e981048c59b1bc1efd2685bdf` · `automated_sms` · `hi` · score=0.65 soft=False · Correct Hindi Devanagari prose and SMS length; fits psychiatry domain + male/28/Bihar persona; all TYPEs allow-listed and Latin IDs expected. Malformed nested MRN tag breaks formatting.
- `1e23bb4e93b0465fa42494aee52e02ef` · `referral_letter` · `mni` · score=0.2 soft=False · Clinical prose entirely English; expected Manipuri/Meitei script for narrative.
- `49e7eef3f6644cc689038f044f77f052` · `opd_slip` · `sat` · score=0.2 soft=False · Prose uses Romanized Hindi medical terms instead of Santali in Ol Chiki script; all other elements (tags, persona, length) acceptable.
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `insurance_claim` · `sat` · score=0.3 soft=False · Clinical prose entirely in Romanized mix/English instead of required Santali Ol Chiki script; RTA mention mildly drifts from TB/NCD domain.
- `5c09bf9c92bb4474a1a128379f250e86` · `discharge_summary` · `sd` · score=0.6 soft=False · Non-allowlist tags (CLINICAL_DIAGNOSIS, CLINICAL_HISTORY, HOSPITAL_COURSE, DISCHARGE_CONDITION, DISCHARGE_INSTRUCTIONS) used; prose/script, persona fit and IDs otherwise acceptable.
