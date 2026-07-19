# Stage 2 — Taxonomy Assignment Audit

- timestamp_utc: `2026-07-19T13:45:25.654316+00:00`
- input: `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T191524/s1_persona_sampling/personas.jsonl`
- personas_in: **20**
- documents_out: **20**
- grid: `14 doc types × 7 domains = 98 cells`
- seed: `202`

## Global doc_type counts

- `asha_worker_note`: 1
- `automated_sms`: 1
- `discharge_summary`: 2
- `insurance_claim`: 1
- `lab_report`: 2
- `opd_slip`: 4
- `phc_register`: 1
- `prescription`: 2
- `radiology_report`: 2
- `surgical_note`: 4

## Global domain counts

- `maternal_health`: 1
- `oncology_chronic`: 7
- `psychiatry_behavioral`: 6
- `surgical`: 3
- `tb_ncd`: 3

## Per-language fill

| language | docs | cells_touched / total | min_cell | max_cell |
|----------|------|-----------------------|----------|----------|
| bn | 2 | 2 / 98 | 0 | 1 |
| en | 2 | 2 / 98 | 0 | 1 |
| gu | 2 | 2 / 98 | 0 | 1 |
| hi | 2 | 2 / 98 | 0 | 1 |
| kn | 2 | 2 / 98 | 0 | 1 |
| ml | 2 | 2 / 98 | 0 | 1 |
| mr | 2 | 2 / 98 | 0 | 1 |
| pa | 2 | 2 / 98 | 0 | 1 |
| ta | 2 | 2 / 98 | 0 | 1 |
| te | 2 | 2 / 98 | 0 | 1 |

## Persona slot uniqueness

How many distinct taxonomy cells each persona received across its slots:

- 1 unique cell(s): 20 persona(s)
