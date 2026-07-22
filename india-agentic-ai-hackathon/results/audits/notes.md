# Diversity run comparison notes

Compared full diversity runs (23 languages × 1 persona × 3 docs = 69 docs).

| Run | Seed | Config extras |
| --- | --- | --- |
| `20260720T213322` | 707 | baseline (pre multi-constraint / EN-pivot repair) |
| `20260721T095916` | 1301 | `repair_multi_constraint: true`, `repair_via_english_pivot: true` |

Aborted attempt `20260721T094842` (seed 1301) failed at S3 on a YAML parse error in `annotation_rules.yaml` — fixed before the successful seed-1301 run.

## Headline metrics

| Metric | Old `213322` (seed 707) | New `095916` (seed 1301) |
| --- | --- | --- |
| Issues total | 36 | **24** |
| S4 entity coverage | 0.91 (6 soft-fails) | **1.00** (0 soft-fails) |
| S4b script fails | 8–9 | 9 (similar) |
| S5 pass rate | 72.5% (19 fails) | **84.1%** (11 fails) |
| Judge repairs that stuck | 9 | **12** |
| EN-pivot repair calls | off | **78** |
| S6 passed | 48 | **54** |
| Curated (after balance) | 20 langs | **22** langs |

## What got better

- **No localized TYPE crash** — old had Bengali `রোগীর_নাম` / `এম.আর.এন`; new has none of that in S4b.
- **S4 coverage fixed** — no missing-required soft-fails (old: bn/doi/en/kn/sat/te).
- **Must-work languages** — old S5 fails in must-work: **as, hi, pa, te** (4); new: only **pa** (1).
- **Repair oscillation** — crude invent↔script A/B flip largely gone; leftovers stick on the same flag (`dialect_script_impurity` on rare/hard scripts), not whack-a-mole.

## What still fails (same shape)

Almost all remaining S5 fails are **script/language**, not tags/domain:

- **Rare:** `brx`, `mni`, `sat`
- **Hard scripts:** `ks` (Arabic), `doi` (Dogri≠Hindi)
- **One must-work leak:** `pa` er_triage still English-heavy / code-mixed

S4b soft-fails cluster the same way: `ks` / `mni` / `sat` / `brx` — model capacity on rare scripts, not tag protection.

## S6 leftovers (seed 1301 only)

- `bn` referral — DICS below threshold
- `kok` insurance — PAN format + script purity
- `mr` lab_report — invented `DATE`
- `sa` lab_report — Latin body (script purity)

Small volume; not systemic like the old localized-TYPE / missing-entity failures.

## Bottom line

Tag + coverage path is fixed. Remaining pain is rare/hard scripts (`ks`/`mni`/`sat`/`brx`/`doi`) plus one Punjabi code-mix. Next validation: **new seed + larger N** to confirm the win is not seed-specific.

## Config experiment (2026-07-21 evening)

- `reasoning_effort: medium` ON for persona_summary / generation / translation / judge / data_designer
- `repair_via_english_pivot: false` (user), keep `repair_multi_constraint: true`
- persona_summary `max_tokens` 256→2048; judge 2048→4096 (reasoning shares budget)
- Data Designer now reads `reasoning_effort` from config (was hardcoded null)

### Sarvam language guidance (docs)

- Chat (`sarvam-105b`): reasoning via `low|medium|high`; `null` disables.
- Dedicated `/translate` (`sarvam-translate:v1`) supports **all 22** Eighth-Schedule langs incl. `ks-IN`, `mni-IN`, `sat-IN`, `brx-IN`.
- Mayura (`mayura:v1`) = 11 core only; has `output_script=fully-native` (translate:v1 does **not**).
- Formal mode + entity handling recommended for docs; char caps 1000/2000 → need chunking for clinical notes.
- Our S4b currently uses **chat completion**, not `/translate` — main lever for ks/mni script quality.
