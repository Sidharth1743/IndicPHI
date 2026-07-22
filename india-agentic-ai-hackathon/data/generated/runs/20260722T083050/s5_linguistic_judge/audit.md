# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **23**
- judge_repaired_count: **16**
- pass_rate: **0.833**
- label_distribution: `{'fail': 0.16666666666666666, 'pass': 0.8333333333333334}`
- positional_length_bias: `{'pearson_r': 0.022496294272354916, 'n': 138.0}`

## Failures (audited — not silent)

- `fdc875f657c1440c8e243a6845fb17a5` · `surgical_note` · `bn` · score=0.6 soft=False · Male name 'Rahul Sharma' assigned to female patient with husband; persona-gender mismatch despite Bengali prose and valid tags.
- `3ceb8b6e61ba4069980e557280aa9ba0` · `insurance_claim` · `brx` · score=0.25 soft=False · Narrative prose in Nepali/Hindi Devanagari, not Bodo; all other elements (tags, persona, domain) acceptable.
- `a0e6acd7770d41b5812edc8bbfbda7ee` · `lab_report` · `brx` · score=0.25 soft=False · Clinical prose entirely in Hindi (wrong language) despite Bodo/Devanagari requirement; all tags, IDs, persona fit, and lab content otherwise valid and plausible.
- `18473c8835b140ff8c0b5ed0d35a5271` · `opd_slip` · `doi` · score=0.55 soft=False · Prose uses standard Hindi vocabulary/grammar instead of Dogri; all entity tags, persona fit and clinical content otherwise valid.
- `18473c8835b140ff8c0b5ed0d35a5271` · `insurance_claim` · `doi` · score=0.65 soft=False · DATE_OF_ADMISSION and DATE_OF_DISCHARGE outside allow-list; prose in Devanagari with partial Dogri lexical flavor but mostly standard Hindi medical phrasing.
- `8116ee5699344b79a2c9c8d1e053dde5` · `automated_sms` · `doi` · score=0.45 soft=False · Male name 'रवि कुमार' for female persona; prose is Hindi not Dogri.
- `8116ee5699344b79a2c9c8d1e053dde5` · `insurance_claim` · `doi` · score=0.38 soft=False · Male name Ramesh for female 48yo; Shimla hospital/district instead of Jammu J&K; otherwise Dogri prose + allowed tags
- `25a8008cbebf4abda209c7d28427bb99` · `lab_report` · `kok` · score=0.42 soft=False · Female patient described with masculine verbs/pronouns (तो, करतो, राहतो); clinical prose is Marathi not Konkani despite Devanagari script.
- `60ff3470cf8340efaa474e13896d8568` · `er_triage_notes` · `ks` · score=0.45 soft=False · Prose is Urdu (not Kashmiri) despite Arabic script and valid tags; minor lexical attempts at ks do not salvage narrative language match.
- `885a67d0071948ac8a8336b278e81003` · `er_triage_notes` · `ks` · score=0.55 soft=False · Narrative prose mostly Urdu (e.g. 'رپورٹ نہیں کیا گیا', 'انکار کرتا ہے') rather than Kashmiri despite Arabic script and some lexical insertions; all entity tags valid and persona fit OK.
- `8a02e74c7f104c1fa9f00b8507bac016` · `referral_letter` · `mni` · score=0.45 soft=False · Mixed English prose ('Dear colleague,', exam descriptions) violates Meitei requirement; DISTRICT tag uses Latin 'Thoubal' (wrong district + script) instead of Imphal East.
- `df61060159844e75aeafcafe43b1bc0d` · `referral_letter` · `mni` · score=0.25 soft=False · Prose entirely English; expected Manipuri/Meitei script for clinical narrative.
- `8d7895d6831e4b31956f868182103764` · `prescription` · `ne` · score=0.3 soft=False · Kathmandu/Nepal location+ABHA vs West Bengal/Darjiling persona; male name for female patient; entity/context implausibility.
- `67bf2f4af82d452db4c95cd1c7f59330` · `opd_slip` · `or` · score=0.55 soft=False · Male name 'Ramesh Chandra Patra' + Khordha district contradict female/59/Nabarangapur persona; clinical prose otherwise Odia and allowed tags used correctly.
- `6e943dc3578249e38b9e61705d0912a9` · `insurance_claim` · `sa` · score=0.2 soft=False · All clinical prose in English; Sanskrit Devanagari required for narrative.
- `0b19143502244d21a03f71ef838ab4ff` · `automated_sms` · `sat` · score=0.3 soft=False · Prose entirely in English; expected Santali Ol Chiki script for SMS body.
- `0b19143502244d21a03f71ef838ab4ff` · `hospital_billing` · `sat` · score=0.25 soft=False · All prose and item descriptions in English/Latin script; zero Santali Ol Chiki content despite explicit language requirement. Tags and maternal billing content otherwise mostly aligned with persona and allow-list.
- `e899bd99966c4ac6b77d784bae3482f0` · `asha_worker_note` · `sat` · score=0.25 soft=False · All clinical prose in English/Latin script; expected Santali Ol Chiki throughout narrative.
- `825c4438c02440dc90d3ddec7ffec8ee` · `automated_sms` · `sd` · score=0.35 soft=False · Prose language is Kashmiri (e.g. tuhund, chhu, manz) not Sindhi despite Arabic script; other elements (tags, length, persona fit) acceptable.
- `825c4438c02440dc90d3ddec7ffec8ee` · `hospital_billing` · `sd` · score=0.35 soft=False · Prose mixes Devanagari intrusions (labels, patient name value) into expected Sindhi Arabic script; PATIENT_NAME uses wrong script despite allow-list tag.
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `insurance_claim` · `sd` · score=0.3 soft=False · Clinical prose body uses Devanagari script with Hindi phrasing instead of required Sindhi Arabic script; only scattered tags and names use Arabic.
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · score=0.4 soft=False · Sindhi prose uses Devanagari script throughout instead of required Arabic script; all tags allowed, clinical content and persona fit otherwise plausible.
- `f0e00cbdb5dd4d33a122229e4883c598` · `hospital_billing` · `te` · score=0.35 soft=False · Prose mixes Telugu with embedded prompt instructions/meta-commentary on TYPE rules and missing line items; all required tags present and script mostly correct but output is contaminated.
