# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `180.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **30**
- judge_repaired_count: **20**
- pass_rate: **0.783**
- label_distribution: `{'fail': 0.21739130434782608, 'pass': 0.782608695652174}`
- positional_length_bias: `{'pearson_r': -0.030672033123976688, 'n': 138.0}`

## Failures (audited — not silent)

- `8b77264c0f7747c59ec191e95202ff7f` · `automated_sms` · `brx` · score=0.35 soft=False · Prose uses Eastern Nagari/Assamese script and phrasing instead of required Bodo Devanagari; language not Bodo.
- `8b77264c0f7747c59ec191e95202ff7f` · `hospital_billing` · `brx` · score=0.3 soft=False · Clinical narrative prose is Hindi, not Bodo; all other elements (persona, entities, length, domain) align.
- `fac14bf3d91143958fc1e8190e25c390` · `insurance_claim` · `brx` · score=0.3 soft=False · Prose uses Hindi vocabulary in Devanagari; expected Bodo language despite correct script and allowed ID tags.
- `0cb542c8c62e4d52ac1c51fcfb93a238` · `er_triage_notes` · `doi` · score=0.15 soft=False · All clinical prose in English; expected Dogri Devanagari narrative absent.
- `85cdb818ce5740ed85a9bfb29cf57098` · `er_triage_notes` · `gu` · score=0.45 soft=False · Prose uses Romanized English-Gujarati mix instead of required Gujarati script; all entity types valid and persona fit ok.
- `8c410a2e98134e9a91f1d50d5811a470` · `er_triage_notes` · `gu` · score=0.2 soft=False · Clinical narrative prose entirely in English instead of Gujarati script.
- `fc0833a3fd3a4916849cba96e415af4b` · `hospital_billing` · `kok` · score=0.6 soft=False · 49yo female with postpartum hemorrhage after normal delivery violates maternal-health persona anchors.
- `99d8e2b0dd9e42e6b270e50cb12c26c5` · `insurance_claim` · `ks` · score=0.25 soft=False · All clinical prose and form narrative in English; expected Kashmiri (Arabic script).
- `9fe1a2291cd5496b92e09e133ea65d85` · `lab_report` · `mai` · score=0.35 soft=False · Prose in Hindi not Maithili; entity values (HOSPITAL_NAME, PATIENT_NAME, DISTRICT) use Bengali script instead of Devanagari.
- `17f9c3d0179e4aa5a9546ec050612896` · `hospital_billing` · `ml` · score=0.6 soft=False · District set to Ernakulam (with Kozhikode PIN) violating persona anchor; minor internal location inconsistency.
- `80435bdcef24479390d6e6ae0b2aeeb1` · `hospital_billing` · `ml` · score=0.55 soft=False · District/hospital/PIN/vehicle details conflict with persona (Thiruvananthapuram) and internally inconsistent; otherwise correct Malayalam script and allowed entity types.
- `1e23bb4e93b0465fa42494aee52e02ef` · `hospital_billing` · `mni` · score=0.35 soft=False · All narrative labels, structure and prose in English/Latin script; expected Manipuri Meitei script for clinical billing document.
- `1e23bb4e93b0465fa42494aee52e02ef` · `discharge_summary` · `mni` · score=0.2 soft=False · All clinical prose in English; expected Manipuri/Meitei script for narrative.
- `1e23bb4e93b0465fa42494aee52e02ef` · `referral_letter` · `mni` · score=0.25 soft=False · All clinical prose in English; expected Manipuri/Meitei script not used. All entity types allowed and persona/domain fit.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `hospital_billing` · `mni` · score=0.25 soft=False · All clinical prose and invoice narrative in English; expected Manipuri Meitei script not used.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `discharge_summary` · `mni` · score=0.25 soft=False · Clinical prose in English instead of required Manipuri Meitei script; all entity types allowed and persona fit intact.
- `d15c31be6c8e40a393e6e6f4f9562ea3` · `referral_letter` · `mni` · score=0.25 soft=False · Prose almost entirely English; only one Meitei token present despite mni/Meitei requirement.
- `24405a884af14bcba6e9c3657baebf83` · `radiology_report` · `pa` · score=0.45 soft=False · Male-coded name (Singh) with Female gender; district=Amritsar vs Barnala persona; otherwise correct Gurmukhi prose and valid tags.
- `22ef884ce12247309d07fc3f601a3c59` · `phc_register` · `sa` · score=0.45 soft=False · Prose language is Hindi (modern register) not Sanskrit despite Devanagari script and correct entity tags.
- `6e943dc3578249e38b9e61705d0912a9` · `phc_register` · `sa` · score=0.35 soft=False · Prose is Hindi (modern register) not Sanskrit; all other constraints met.
- `49e7eef3f6644cc689038f044f77f052` · `opd_slip` · `sat` · score=0.2 soft=False · Clinical prose entirely in English; expected Santali Ol Chiki script not used.
- `49e7eef3f6644cc689038f044f77f052` · `phc_register` · `sat` · score=0.2 soft=False · Clinical prose entirely in English instead of required Santali Ol Chiki; all other elements (tags, persona, content) acceptable.
- `49e7eef3f6644cc689038f044f77f052` · `prescription` · `sat` · score=0.2 soft=False · All clinical prose in English/Latin; no Santali Ol Chiki narrative as required for expected language.
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `automated_sms` · `sat` · score=0.2 soft=False · Prose uses Bengali script instead of required Santali Ol Chiki; all other elements (entities, persona, length) acceptable.
- `c98c2d51b4ea4d0c947d6dfc0ee57383` · `insurance_claim` · `sat` · score=0.2 soft=False · Clinical narrative prose entirely in English; expected Santali Ol Chiki script for all body text.
- `5c09bf9c92bb4474a1a128379f250e86` · `hospital_billing` · `sd` · score=0.55 soft=False · Sindhi Arabic-script prose matches expectation and persona fit is good, but content is a long clinical narrative rather than billing/invoice format; includes excess chart-style details without charges or itemization.
- `5c09bf9c92bb4474a1a128379f250e86` · `discharge_summary` · `sd` · score=0.35 soft=False · Narrative prose uses Devanagari instead of required Arabic script for Sindhi; age 47 with normal vaginal delivery and PPH is implausible geriatric maternal case.
- `5c09bf9c92bb4474a1a128379f250e86` · `referral_letter` · `sd` · score=0.3 soft=False · All clinical prose in Devanagari; expected Sindhi Arabic script. No other mismatches.
- `e9f9b9a22bcb47f28198db61b9bd4966` · `discharge_summary` · `sd` · score=0.45 soft=False · Clinical prose uses Devanagari script instead of required Arabic script for Sindhi; all entity types allowed, persona/domain fit, length and content otherwise plausible.
- `e9f9b9a22bcb47f28198db61b9bd4966` · `referral_letter` · `sd` · score=0.35 soft=False · Clinical prose uses Devanagari script with Hindi framing instead of required Sindhi Arabic script; all entities valid and persona/domain fit otherwise.
