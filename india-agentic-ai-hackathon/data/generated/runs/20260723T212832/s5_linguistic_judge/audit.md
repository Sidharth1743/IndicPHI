# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `2`
- rows_judged: **138**
- soft_fail_count: **0**
- failure_count: **15**
- judge_repaired_count: **32**
- pass_rate: **0.891**
- label_distribution: `{'fail': 0.10869565217391304, 'pass': 0.8913043478260869}`
- positional_length_bias: `{'pearson_r': 0.0809412936969853, 'n': 138.0}`

## Failures (audited — not silent)

- `18473c8835b140ff8c0b5ed0d35a5271` · `insurance_claim` · `doi` · score=0.35 soft=False · Hindi prose instead of Dogri; Bari Brahmana village mismatches Kathua district.
- `8116ee5699344b79a2c9c8d1e053dde5` · `insurance_claim` · `doi` · score=0.55 soft=False · Narrative prose mixes English dates/numbers outside tags with Dogri Devanagari; not fully compliant with expected script/language for clinical content.
- `df61060159844e75aeafcafe43b1bc0d` · `discharge_summary` · `mni` · score=0.2 soft=False · Clinical prose entirely in English; expected Manipuri/Meitei script for narrative.
- `df61060159844e75aeafcafe43b1bc0d` · `referral_letter` · `mni` · score=0.3 soft=False · Clinical prose in Bengali script + English mix instead of required Meitei; all entity TYPEs allowed and persona/domain fit otherwise.
- `0b19143502244d21a03f71ef838ab4ff` · `asha_worker_note` · `sat` · score=0.35 soft=False · Narrative prose entirely in Roman script with mixed Hindi/Santali transliteration; no Ol Chiki script used despite explicit Santali requirement.
- `0b19143502244d21a03f71ef838ab4ff` · `automated_sms` · `sat` · score=0.2 soft=False · SMS prose entirely in English; expected Santali Ol Chiki narrative.
- `0b19143502244d21a03f71ef838ab4ff` · `hospital_billing` · `sat` · score=0.55 soft=False · Meta notes about untagged receipt/state fields and placeholder text indicate drift; receipt number invented outside allow-list despite soft billing rule.
- `e899bd99966c4ac6b77d784bae3482f0` · `asha_worker_note` · `sat` · score=0.35 soft=False · Prose uses Roman script + English code-mixing instead of required Santali Ol Chiki; all other elements (entities, persona, domain) acceptable.
- `e899bd99966c4ac6b77d784bae3482f0` · `insurance_claim` · `sat` · score=0.2 soft=False · Clinical prose is English; expected Santali Ol Chiki. All tags/IDs/types/persona fit otherwise.
- `825c4438c02440dc90d3ddec7ffec8ee` · `automated_sms` · `sd` · score=0.55 soft=False · Prose mixes Devanagari into expected Sindhi Arabic script; other entities/persona fit.
- `825c4438c02440dc90d3ddec7ffec8ee` · `discharge_summary` · `sd` · score=0.2 soft=False · Clinical prose entirely in English instead of required Sindhi Arabic script; all tags allowed and persona/domain fit otherwise.
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `insurance_claim` · `sd` · score=0.25 soft=False · Clinical narrative entirely in Devanagari/Hindi-Urdu mix instead of required Sindhi Arabic script; language not Sindhi prose despite tags and IDs being allow-listed.
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `hospital_billing` · `sd` · score=0.3 soft=False · Prose entirely in Devanagari; expected Sindhi Arabic script. All TYPE tags allowed and IDs Latin; persona/domain fit ok.
- `fe3a6e05b50a4eb1b679f5fba0c5440b` · `discharge_summary` · `sd` · score=0.65 soft=False · Devanagari 'डॉक्टर' intrudes into otherwise Arabic-script Sindhi prose; all tags allowed, persona/clinical fit and length OK.
- `829db9fbfeda404d89ff9b8a405b5e4d` · `opd_slip` · `ta` · score=0.55 soft=False · Occupation 'News Paper Boy' conflicts with female/40yo persona; all other prose, tags, script and clinical content align.
