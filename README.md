# RNASeqToolComparison

## Overview

This project is a replication and exploration of the paper:  
**"Post-mortem molecular profiling of three psychiatric disorders"**  
by *Ramaker et al., Genome Medicine (2017)*

Our goals were:
- Replicate core transcriptomic findings comparing **schizophrenia (SZ)**, **bipolar disorder (BPD)**, **major depressive disorder (MDD)**, and controls
- Evaluate RNA-Seq tools such as **STAR** and **Kallisto** to determine trade-offs in speed, accuracy, and computational cost


## Motivation

Analyzing psychiatric disease at the molecular level requires large-scale RNA-Seq data and thoughtful tool selection. Different tools yield different alignments, affecting gene expression quantification, differential expression results, and ultimately the biological conclusions.

In this project, we examined:
- How choice of tools (STAR vs Kallisto) impacts output
- Scenarios where speed, cost-efficiency, or accuracy should be prioritized
- How improper tool choices can mislead research outcomes


---

## Methods & Data

- **Transcriptomic Data**: Modeled after the post-mortem RNA-Seq data used in the original study
- **Brain Regions**:
  - Anterior Cingulate Cortex (AnCg)
  - Dorsolateral Prefrontal Cortex (DLPFC)
  - Nucleus Accumbens (nAcc)

- **Tools Used**:
  - `STAR` – high accuracy aligner, slower and resource-intensive
  - `Kallisto` – fast, pseudoalignment-based, lower sensitivity
  - `DESeq2` – for differential gene expression
  - `R` and `Python` – for data processing, visualization

---

## Key Findings (Replication Summary)

- Most significant gene expression changes occurred in **SZ** patients, especially in the **AnCg**
- **EGR1** was significantly downregulated in SZ across cohorts, suggesting regulatory disruption
- Gene sets showed:
  - **Depletion of neuron-specific transcripts**
  - **Enrichment of astrocyte-specific transcripts** in SZ and BPD
- GABA-related metabolites aligned with reduced expression of GAD1/GAD2 enzymes

## Technologies & Skills

- RNA-Seq Analysis & Alignment  
- STAR vs Kallisto benchmarking  
- Differential Expression with DESeq2  
- PCA & Cluster Analysis  
- Python (pandas, seaborn), R  
- Git & GitHub version control

## Paper Reference

**Ramaker et al. (2017)**  
[Post-mortem molecular profiling of three psychiatric disorders](https://doi.org/10.1186/s13073-017-0458-5)  
*Genome Medicine, 9, 72 (2017)*

## Author

**Luigi Cheng**  
M.S. Data Science (UCSD, in progress)  
GitHub: [@iLuigi98](https://github.com/iLuigi98)  
Portfolio: [luigidata.com](https://luigidata.com)
