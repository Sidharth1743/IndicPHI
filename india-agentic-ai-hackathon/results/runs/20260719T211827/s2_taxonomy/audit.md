# Stage 2 — Taxonomy Assignment Audit

- timestamp_utc: `2026-07-19T15:48:28.024227+00:00`
- input: `/home/sidharth/Desktop/nvidia-hack/data/generated/runs/20260719T211827/s1_persona_sampling/personas.jsonl`
- personas_in: **20**
- documents_out: **20**
- grid: `14 doc types × 7 domains = 98 cells`
- seed: `303`

## Global doc_type counts

- `asha_worker_note`: 2
- `automated_sms`: 1
- `discharge_summary`: 2
- `er_triage_notes`: 2
- `insurance_claim`: 2
- `lab_report`: 1
- `phc_register`: 2
- `prescription`: 2
- `radiology_report`: 2
- `surgical_note`: 1
- `telemedicine_transcript`: 3

## Global domain counts

- `general_medicine`: 3
- `maternal_health`: 1
- `oncology_chronic`: 3
- `psychiatry_behavioral`: 4
- `surgical`: 5
- `tb_ncd`: 4

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
