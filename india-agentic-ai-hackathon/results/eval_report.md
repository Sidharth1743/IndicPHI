# Eval report — SDG synthetic-data smokes

Packaged under `results/runs/` (full artifacts) and `results/logs/` (console).

## Runs included

| Run ID | Role | Curated (approx) | Notes |
|--------|------|------------------|-------|
| `20260719T185353` | tiny smoke seed 101 | 8–9 | 10 docs |
| `20260719T191524` | medium seed 202 | 9 | 20 docs; S5 resume after DNS/timeout |
| `20260719T211827` | medium seed 303 (`latest`) | 9 | S4 entity coverage 1.0 |

## Latest (`20260719T211827`) funnel

- S4 entity complete: **1.0** (0 gen soft-fails)
- S5 pass rate: **0.85** (3 judge fails: ml script, pa gender morphology ×2)
- S6 pass: **15/17** (Aadhaar Verhoeff; invented STATE type)
- Curated / GLiNER: **9**

Full per-failure audit: `results/runs/20260719T211827/failures.md`
Also: `results/audits/failures_20260719T211827.md`

## Logs

See `results/logs/smoke_*.log` and `smoke_medium_*.log`.
