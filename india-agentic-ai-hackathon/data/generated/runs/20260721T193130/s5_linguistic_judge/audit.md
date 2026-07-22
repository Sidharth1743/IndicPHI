# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `300.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **11**
- judge_repaired_count: **32**
- pass_rate: **0.920**
- label_distribution: `{'fail': 0.07971014492753623, 'pass': 0.9202898550724637}`
- positional_length_bias: `{'pearson_r': 0.029272656439593796, 'n': 138.0}`

## Failures (audited — not silent)

- `8b77264c0f7747c59ec191e95202ff7f` · `automated_sms` · `brx` · score=0.45 soft=False · Prose mixes Nepali phrasing/verbs with partial Bodo terms; expected Bodo (Devanagari) narrative not met.
- `8b77264c0f7747c59ec191e95202ff7f` · `hospital_billing` · `brx` · score=0.3 soft=False · Narrative prose uses Assamese/Bengali script+lexicon instead of required Bodo Devanagari; entity values show mixed/wrong scripts.
- `fac14bf3d91143958fc1e8190e25c390` · `prescription` · `brx` · score=0.45 soft=False · Clinical prose uses Hindi/Nepali vocabulary and structure instead of Bodo; all entity tags and content otherwise valid and persona-plausible.
- `fac14bf3d91143958fc1e8190e25c390` · `insurance_claim` · `brx` · score=0.35 soft=False · Clinical narrative prose written mostly in Assamese/Bengali script with mixed Devanagari insertions instead of required Bodo Devanagari; language and script mismatch for expected brx document.
- `fc0833a3fd3a4916849cba96e415af4b` · `hospital_billing` · `kok` · score=0.35 soft=False · 49yo female as surrogate at 28 weeks gestation violates age-domain fit and surrogate plausibility; prose/script otherwise acceptable with valid entity tags.
- `1e23bb4e93b0465fa42494aee52e02ef` · `hospital_billing` · `mni` · score=0.25 soft=False · Narrative prose in Bengali script instead of required Meitei; all entity TYPEs valid and Latin IDs acceptable.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `hospital_billing` · `mni` · score=0.65 soft=False · Invalid STATE type (not in allow-list) + Bengali script for place name instead of Meitei.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `discharge_summary` · `mni` · score=0.25 soft=False · Narrative prose uses Burmese script instead of required Meitei; content incoherent with 'American citizen' reference and garbled delivery/Apgar details, breaking persona and plausibility.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `referral_letter` · `mni` · score=0.25 soft=False · Narrative prose uses Assamese/Bengali script throughout instead of required Meitei; female patient listed with wife (পত্নী) relative creates sex mismatch.
- `f64651bbe52e4c86b23c9a11c76682d9` · `opd_slip` · `or` · score=0.65 soft=False · Maternal health domain incompatible with 45yo postmenopausal/menopausal presentation and negative pregnancy test.
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `asha_worker_note` · `sat` · score=0.2 soft=False · Narrative prose entirely in Hindi/Devanagari; expected Santali in Ol Chiki script.
