# Idea — Indic-PHI Synthetic Data Pipeline

Real Indian clinical text cannot be freely shared (DPDP). HackGrid synthesizes
multilingual clinical documents with **inline PHI/PII surrogate tags**, audits
them (LLM + Python), **repairs known failures**, curates with NeMo Curator, and
exports GLiNER-ready spans.

**Generator:** Sarvam-105B — native support for **all 22 official Indian
languages + English** (native script, romanized, code-mixed). We still use an
**English-pivot** for S4 tag discipline, then translate in S4b.

### Flowchart (S1–S10)

```text
=======================================================================
                         [STAGE 0] FOUNDATION
  NeMo Data Designer + NeMo Curator + Sarvam / Azure keys
=======================================================================
                                  |
                                  v
+---------------------------------------------------------------------+
| [S1] PERSONA SAMPLING — Nemotron-Personas-India (23 languages)      |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S2] TAXONOMY — 14 doc types × 7 clinical domains                   |
| [S2b] Persona clinical summary (Sarvam-30B)                         |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S3] PROMPT CONSTRUCTION — profiles + format examples +             |
|      placement hints + domain / script anti-failure guidance        |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S4] NeMo Data Designer + Sarvam-105B (EN + [[TYPE|value]] tags)    | <--+
|      ↻ generator repair: missing tags / stuffing                     |    |
+---------------------------------------------------------------------+    |
                                  |                                        |
                                  v                                        |
+---------------------------------------------------------------------+    |
| [S4b] Tag-preserving translation → target Indic script              | ---+
|      Rare: dedicated ↔ few-shot chat ladder (prefer-chat: doi/ks/sd)  |
|      Arabic script-lock if Devanagari leaks; sd ≥2 chat / 240s       |
|      ↻ non-rare: generator repair on wrong language / script        |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S5] LINGUISTIC JUDGE — Grok-4.3 (Azure Foundry)                    | <--+
| Flags: dialect_script_impurity, instruction_drift,                  |    |
|        surrogate_plausibility_collapse, domain_persona_mismatch,    |    |
|        invented_entity_type, length_violation, …                    |    |
| Persona fail → tag-only patch → rejudge → LLM (max 2)               | ---+
| Other flags → language-locked LLM repair (no neighbor soft-pass)    |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S6] DETERMINISTIC AUDITOR — Verhoeff / phone / PHI / DICS          |
| ↻ design: fix checksums / tags then re-audit                        |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S7–S8] NeMo Curator fuzzy dedup + semantic near-dup + balance      |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [S9] GLiNER FORMAT + intrinsic metrics + failures.md                |
| [S10] Persona-held-out train / eval split                           |
+---------------------------------------------------------------------+
```

### Why two-lane audit + repair

- **S5 (LLM):** language/script, domain fit, persona plausibility — needs judgment.
- **S6 (Python):** Aadhaar Verhoeff, phone format, PHI residue — zero hallucination.
- **Repair loop:** known cheap failures go back with clear instructions instead of
  wasting the document. Persona: **post-judge** tag patch then at most one LLM
  (diversity stays high at first generation). Rare langs: dedicated translate
  first; repairs stay language-locked (no Hindi/English stand-in).
  Code-switching / code-mix is **not** implemented yet.
  Prevention first: S3 prompts/examples teach good vs bad.

### NVIDIA stack (required)

| Component | Stage | Role |
|-----------|-------|------|
| Nemotron-Personas-India | S1 | Demographic seed |
| NeMo Data Designer | S4 | Batch generation over seed prompts |
| NeMo Curator | S7 | Fuzzy near-dup (no `cpu_minhash` bypass) |
| Sarvam-105B / 30B | S4 / S4b / S2b | Generation, translation, summaries |
