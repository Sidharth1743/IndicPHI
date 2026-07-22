# Stage 5 — Linguistic Judge Audit

- provider/model: `azure_foundry` / `grok-4.3`
- requests_per_minute: `500.0`
- timeout_s: `600.0`
- network_retries: `4`
- rows_judged: **20**
- soft_fail_count: **0**
- failure_count: **5**
- pass_rate: **0.750**
- label_distribution: `{'fail': 0.25, 'pass': 0.75}`
- positional_length_bias: `{'pearson_r': 0.17236968490111626, 'n': 20.0}`

## Failures (audited — not silent)

- `b2958cfe1a8946b88be2780178fdfa1a` · `opd_slip` · `hi` · score=0.55 soft=False · Domain Oncology/Complex Chronic Care not followed; content is TB workup instead. Hindi prose and allowed entity tags otherwise correct.
- `315f86955b8745379f872ad0cf6fc38b` · `discharge_summary` · `ml` · score=0.55 soft=False · District Ernakulam mismatches persona Pathanamthitta; ABHA saritha.thomas inconsistent with Annamma/Mary Thomas names.
- `588a02fac9ad4b8d82b655e6d190a312` · `discharge_summary` · `ml` · score=0.6 soft=False · District set to Wayanad (not Thiruvananthapuram); ABHA address name 'gopalakrishnan' mismatches patient Ramesh Kumar
- `28085860cdbd4188a9769b9902f6890d` · `opd_slip` · `mr` · score=0.55 soft=False · Oncology domain specified but content is pulmonary TB diagnosis and RNTCP treatment; minor fit issues despite correct Marathi prose and valid entity tags.
- `2d4ff3d6af4a4c5dbf5bd49b6c47ed2a` · `asha_worker_note` · `pa` · score=0.72 soft=False · Village Kapurthala surrogate clashes with Faridkot district; all other language, entity types, persona and domain fit are correct.
