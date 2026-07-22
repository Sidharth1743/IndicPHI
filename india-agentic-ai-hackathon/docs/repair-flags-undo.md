# Repair flags (undo guide)

S5 quality repair improvements are **config-gated**. Defaults in code are `false`
(old behavior). Diversity profile turns them **on**.

## Flags (`generation` block)

| Key | On means | Undo |
| --- | --- | --- |
| `repair_multi_constraint` | Accumulate judge flags across rounds; inject STABILITY GUARDS so fixing invent/domain does not English-wipe script (and vice versa) | set `false` |
| `repair_via_english_pivot` | For non-English docs: repair `generated_text_en`, then re-translate with tag protection, then re-judge | set `false` |

## Language SLA (`linguistic_judge` block)

| Key | Meaning | Undo |
| --- | --- | --- |
| `must_work_languages` | Log `MUST-WORK language fail(s)` when hi/ta/te/bn/… fail after repair | omit or `[]` |
| `rare_script_languages` | Log `rare-script fail(s)` for brx/mni/sat (expected capacity loss) | omit or `[]` |

These SLA lists do **not** auto-pass documents; they only change stderr / audit labeling.

## Quick undo (diversity runs)

In `configs/synthetic-data/pipeline.diversity.yaml`:

```yaml
generation:
  repair_multi_constraint: false
  repair_via_english_pivot: false
```

Or omit both keys (code defaults to `false`).
