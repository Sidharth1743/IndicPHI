# Stage 2 — Taxonomy Assignment Audit

- timestamp_utc: `2026-07-19T11:52:23.753720+00:00`
- input: `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T172223/s1_persona_sampling/personas.jsonl`
- personas_in: **10**
- documents_out: **10**
- grid: `14 doc types × 7 domains = 98 cells`
- seed: `42`

## Global doc_type counts

- `automated_sms`: 5
- `discharge_summary`: 1
- `hospital_billing`: 1
- `prescription`: 2
- `referral_letter`: 1

## Global domain counts

- `general_medicine`: 1
- `maternal_health`: 1
- `oncology_chronic`: 1
- `psychiatry_behavioral`: 2
- `tb_ncd`: 5

## Per-language fill

| language | docs | cells_touched / total | min_cell | max_cell |
|----------|------|-----------------------|----------|----------|
| bn | 1 | 1 / 98 | 0 | 1 |
| en | 1 | 1 / 98 | 0 | 1 |
| gu | 1 | 1 / 98 | 0 | 1 |
| hi | 1 | 1 / 98 | 0 | 1 |
| kn | 1 | 1 / 98 | 0 | 1 |
| ml | 1 | 1 / 98 | 0 | 1 |
| mr | 1 | 1 / 98 | 0 | 1 |
| pa | 1 | 1 / 98 | 0 | 1 |
| ta | 1 | 1 / 98 | 0 | 1 |
| te | 1 | 1 / 98 | 0 | 1 |

## Persona slot uniqueness

How many distinct taxonomy cells each persona received across its slots:

- 1 unique cell(s): 10 persona(s)
