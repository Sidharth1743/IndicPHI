This is an excellent architectural pivot. By dropping the second LLM (Qwen3-30B) and moving all annotation and formatting validation to **deterministic Python logic**, you are eliminating a massive source of latency, cutting inference costs, and completely removing the risk of "judge hallucination" for strictly structural rules.

An LLM is needed to judge dialect and script purity, but you do not need an LLM to check if an array index is correct or if an Aadhaar checksum passes.

Here is the refined flowchart and stage breakdown, integrating your exact domains, document types, metrics, and this new streamlined audit loop.

### **Indic-PHI Synthetic Data Pipeline (Streamlined Architecture)**

```text
=======================================================================
                         [STAGE 0] FOUNDATION
  Setup NIM endpoints, language tools, and NeMo environments.
=======================================================================
                                  |
            +-------------------------------------------+
            |            NEMO DATA DESIGNER             |
            +-------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 1] PERSONA SAMPLING                                          |
| Sample Nemotron PersonaHub India across 23 languages (3 docs/each)  |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 2] DOCUMENT TAXONOMY (14 Types × 7 Domains)                  |
| Domains: Gen. Med, Maternal, TB/NCD, Surgical, Paediatric,          |
|          Oncology/Chronic, Psychiatry/Behavioral                    |
| Docs: OPD, Prescr., ASHA, SMS, Billing, Discharge, Referral,        |
|       Radiology, ER, Telemed, Surgical, Lab, PHC, Insurance         |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 3] PROMPT CONSTRUCTION                                       |
| Combine Persona + Doc Type + Domain + Inline Annotation Rules       |
+---------------------------------------------------------------------+
                                  |
            +-------------------------------------------+
            |  NIM INFERENCE, AUDIT & ERROR MONITORING  |
            +-------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 4] GENERATOR: Sarvam-30B                                     | <----+
| Generate clinical text with INLINE surrogate PHI annotations        |      |
+---------------------------------------------------------------------+      |
                                  |                                          |
                                  v                                          |
+---------------------------------------------------------------------+      |
| [STAGE 5] LINGUISTIC AUDITOR (LLM Judge): Sarvam-105B               | --[FAIL]
| Judge Metrics: Calibration, Consistency, Positional Bias, Label Dist|      |
| Error Monitor: Instruction Drift, Cross-Language Entity Shift,      |      |
|                Surrogate Plausibility Collapse                      |      |
+---------------------------------------------------------------------+      |
                                  |                                          |
                                  v                                          |
+---------------------------------------------------------------------+      |
| [STAGE 6] ANNOTATION & FORMAT AUDITOR: Deterministic Python Logic   | --[FAIL]
| Validation: Aadhaar checksum, pincode ranges, PHI residue scan      |      |
| Error Monitor: Entity Type Collapse, Tokenization/Truncation Failure|      |
| Metrics Checked Here: DICS (Doc Internal Consistency Score)         |      |
+---------------------------------------------------------------------+
                                  |
            +-------------------------------------------+
            |               NEMO CURATOR                |
            +-------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 7] DEDUPLICATION                                             |
| MinHash + LSH (Jaccard > 0.8) near-duplicate removal                |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 8] DISTRIBUTION BALANCING                                    |
| Target 120k total docs, stratified across 23 languages              |
+---------------------------------------------------------------------+
                                  |
            +-------------------------------------------+
            |      ASSEMBLY & INTRINSIC EVALUATION      |
            +-------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 9] GLiNER FORMAT & INTRINSIC DATA METRICS                    |
| Format: Convert to span-based token-indexed JSON                    |
| Metrics: ECR, ISED, Annotation Span P/R/F1 against Gold             |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 10] TRAIN / TEST SPLIT                                       |
| 50-50 split stratified by language (modifiable later)               |
+---------------------------------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 11] DATASET RELEASE                                          |
| Hugging Face structure + Dataset Card + DPDP Audit Trail            |
+---------------------------------------------------------------------+
                                  |
            +-------------------------------------------+
            |     EXTRINSIC / FINE-TUNING EVALUATION    |
            +-------------------------------------------+
                                  |
                                  v
+---------------------------------------------------------------------+
| [STAGE 12] GLiNER MODEL FINE-TUNING & METRICS                       |
| 4.1 Downstream NER F1: Train model & Evaluate on Gold               |
| 4.2 Entity Type Breakdown: Report F1 on each entity type            |
| 4.3 Learning Curve: Train on 10%, 20%, 30%... Plot F1 vs Size       |
+---------------------------------------------------------------------+

```

---

### **Key Updates to the Workflow**

#### **1. The Streamlined Audit Loop (Stages 5 & 6)**

- **Stage 5 (Linguistic Auditor):** Because Sarvam-105B is now the _only_ LLM acting as a judge, the **Judge Model Meta-Evaluation metrics** (Calibration, Judge Consistency, Positional Bias, Label Distribution Alignment) are applied exclusively here. This LLM monitors for semantic failures: _Instruction Drift_, _Cross-Language Entity Shift_, and _Surrogate Plausibility Collapse_.
- **Stage 6 (Annotation & Format Auditor):** All structural validation is merged into a single **Deterministic Python Logic Engine**. This script uses regex, exact string matching, and mathematical validation to check:
- **Format Rules:** Aadhaar checksums, valid pincode ranges, and checking for real PHI residue.
- **Annotation Errors:** It catches _Tokenization/Truncation Failures_ (e.g., span indices that don't align with string boundaries) and _Entity Type Collapse_ (using basic statistical checks on the taxonomy outputs).
- **DICS (Document Internal Consistency Score):** Because DICS simply requires matching strings (e.g., ensuring "Murugan" is used for Patient Name every time in the same document), Python does this natively and perfectly with zero hallucination.

#### **2. Intrinsic & Extrinsic Evaluation Anchors**

- **Stage 9 (Intrinsic Metrics):** Once the data is generated and formatted for GLiNER, you compute the dataset's structural health: **ECR** (Entity Coverage Rate), **ISED** (Inter Sample Entity Diversity), and your **Annotation Span Precision/Recall/F1 against Gold**.
- **Stage 12 (Extrinsic Fine-Tuning):** The final evaluation framework remains intact. You will train your GLiNER model and measure **Downstream NER F1** on gold data, break down performance by **Entity Type**, and plot the **Learning Curve Analysis** (10%, 20%, 30%...) to measure efficiency.
