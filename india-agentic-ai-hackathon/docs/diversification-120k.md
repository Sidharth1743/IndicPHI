# How 120k stays diverse

Equal languages alone is not enough. Diversity is forced by stacking quotas:
**language → doc type × domain → personas → entity profiles**.

## Headline numbers

| Metric | Value |
|--------|------:|
| Total documents | 120,000 |
| Languages | 23 (equal slices) |
| Docs per language | ~5,217 |
| Taxonomy cells per language | 98 (14 doc types × 7 domains) |
| Docs per cell | ~53 |
| Docs per persona | 3 |
| Personas / language | ~1,739 |
| Personas total | ~40,000 |

Cinema-seat analogy: every document is a pre-assigned seat (language row, form
type, clinical domain). Then a different persona sits in each seat with
doc-type-specific PHI tags. The LLM does not choose the crowded seats.

## Layer 1 — Equal languages

English is slice #23 — same size as Hindi or Tamil (~5,217 docs each).

Languages: as, bn, brx, doi, en, gu, hi, kn, ks, kok, mai, ml, mni, mr, ne, or,
pa, sa, sat, sd, ta, te, ur.

## Layer 2 — 14 × 7 taxonomy grid (per language)

Inside one language (~5,217 docs), spread across all document types and domains
so nothing collapses into endless OPD + General Medicine.

Example cells (~53 docs each):

| Cell | Language | Doc type | Domain |
|------|----------|----------|--------|
| A | hi | Prescription | Maternal Health |
| B | hi | Lab Report | Oncology |
| C | ta | ASHA Note | TB & NCD |
| D | en | Insurance Claim | Surgical |

23 × 98 × ~53 ≈ 120,000

## Layer 3 — Same cell, different people

Domains are only 7. Variety inside a cell comes from
`nvidia/Nemotron-Personas-India` (age, sex, district, occupation).

Example: Hindi · Prescription · Maternal Health

1. Meena Devi, 77F — Kanpur Nagar · Urban · Homemaker  
2. Sunita, 24F — Rural Bihar · ANC visit  
3. Fatima, 31F — Mumbai Suburban · Working  

## Layer 4 — Entities without collapse

Entity types are fixed in config. Diversity means which types appear on which
forms (`entity_profiles.yaml`, `require_all_profile_entities`), and unique
surrogate values (ISED) with stable identity within a doc (DICS).

| Doc type | Usually include | Rotate / rare / placement |
|----------|-----------------|---------------------------|
| Prescription | NAME, AGE, GENDER, DOCTOR, HOSPITAL, MRN | AADHAAR, ABHA (sparse) |
| Insurance | NAME, INSURANCE_POLICY_NUMBER, HOSPITAL, ADDRESS, PAN | BANK, IFSC, AADHAAR (Verhoeff-valid) |
| Telemedicine | NAME, PHONE, DOCTOR, AGE, GENDER | IP, URL, IMEI, MAC once in session header |
| Lab Report | NAME, MRN, HOSPITAL, AGE | PHONE sometimes |
| SMS Alert | NAME, PHONE | Almost no IDs |

Same persona across forms keeps identity (DICS); entity *types* change with the form.

## Pipeline path (one document)

S1 Persona → S2 Cell (lang×doc×domain) → S2b Persona summary (Sarvam-30B) →
S3 Prompt + entity profile + format/placement examples →
S4 English-pivot generation (**NeMo Data Designer** + Sarvam-105B) →
  ↻ repair missing tags / stuffing →
S4b Tag-preserving translation → ↻ repair wrong script →
S5 Linguistic judge (Grok) → S6 Deterministic auditor →
S7–S8 **NeMo Curator** dedup + semantic + balance → S9 GLiNER → S10 split

Sarvam invents wording. Config invents the seating chart. Python enforces
structure. Generator **repair** recovers known soft fails before drop.

## Diversity profile (69-doc probe)

`configs/synthetic-data/pipeline.diversity.yaml`: all 23 languages × 1 persona ×
3 docs. Use to measure language/script yield and repair effectiveness before
scaling to 120k.

Observed (`20260720T192801`): **20/23** languages in curated set after equalize;
repairs recovered several tag/script cases. Remaining gaps concentrated on
low-resource scripts (`brx`, `sat`, `sd`) and S5 quality flags — addressed by
stronger prompts + flag-targeted repair (3–5×).

## Why this does not collapse at 120k

7 domains repeat on purpose — but each is crossed with 14 forms × 23 languages ×
~40k personas × rotating entity profiles. Category repetition is fine; same note
/ same surrogates is what we block.
