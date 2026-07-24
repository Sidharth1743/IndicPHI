# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `2`
- rows_judged: **69**
- soft_fail_count: **0**
- failure_count: **9**
- judge_repaired_count: **14**
- pass_rate: **0.870**
- label_distribution: `{'fail': 0.13043478260869565, 'pass': 0.8695652173913043}`
- positional_length_bias: `{'pearson_r': 0.029069432469053167, 'n': 69.0}`

## Failures (audited — not silent)

- `269a94e437d84643b728d5b86d5d08be` · `automated_sms` · `brx` · score=0.3 soft=False · Prose uses Nepali/Hindi phrasing and grammar in Devanagari, not Bodo; all tags and IDs valid, persona/domain fit ok.
- `269a94e437d84643b728d5b86d5d08be` · `hospital_billing` · `brx` · score=0.35 soft=False · Clinical prose and billing narrative written in Hindi instead of required Bodo (Devanagari); all other elements (persona fit, entity tags, plausibility) acceptable.
- `2f97625028784d7ab66673d76e697478` · `phc_register` · `mni` · score=0.2 soft=False · All clinical prose in English; expected Manipuri/Meitei script. All entity types allowed, persona/domain fit, no other violations.
- `b5204bb0fe954a2cb47f1c994a300872` · `er_triage_notes` · `sat` · score=0.2 soft=False · All clinical prose in English; expected Santali Ol Chiki narrative absent.
- `b5204bb0fe954a2cb47f1c994a300872` · `opd_slip` · `sat` · score=0.28 soft=False · Prose is English/Latin with sparse transliterated Santali words instead of Ol Chiki; OPD slip is multi-paragraph chart-length; 19yo male labeled homemaker mismatches persona.
- `e9ec69ab351340d49920d8203b96c015` · `asha_worker_note` · `sd` · score=0.2 soft=False · Prose entirely in English Latin script instead of required Sindhi Arabic; all tags allowed and persona/domain otherwise plausible.
- `e9ec69ab351340d49920d8203b96c015` · `phc_register` · `sd` · score=0.55 soft=False · Sindhi Arabic-script prose contains repeated Devanagari intrusions (ॿ, मशवरो) and Latin fragments inside narrative, violating expected script purity despite valid tags.
- `e9ec69ab351340d49920d8203b96c015` · `automated_sms` · `sd` · score=0.45 soft=False · Gurmukhi intrusion ('ਮਸ਼ورੀ') in otherwise Sindhi Arabic prose; not mostly wrong but violates script purity.
- `6feb104df37242faae24a67c95682734` · `asha_worker_note` · `ur` · score=0.55 soft=False · Patient name Latin + South-Indian cultural mismatch for Bihar/Urdu persona; other prose/tags/domain fit ok.
