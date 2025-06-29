# RNASeqToolComparison

# Differential Gene Expression Tools Research

**Authors**: Joseph Bui, Brandon Tsui, Luigi Cheng  
**Original Repo**: [github.com/JosephBui21/RNASeqToolComparison](https://github.com/JosephBui21/RNASeqToolComparison)

## Abstract
RNA-Seq is a next-generation sequencing (NGS) method used to capture a snapshot of RNA presence and quantity in a sample. Differential gene expression (DGE) analysis reveals expression changes between groups (e.g., healthy vs disease). This project investigates the performance of several DGE tools:

- **ABSSeq**
- **voom.limma**
- **PoissonSeq**
- **DESeq2**
- **NOISeq**
- **ttest**
- **edgeR**

We evaluated these tools on synthetic RNA-seq datasets using metrics such as:
- Area Under the Curve (AUC)
- False Discovery Rate (FDR)
- Type I Error Rate
- Sensitivity

## Background
RNA-Seq has replaced older microarray techniques for transcriptomics, providing better accuracy and dynamic range. With many software options now available, researchers face challenges selecting appropriate tools for DGE. This study benchmarks commonly used methods to guide tool selection based on dataset characteristics and accuracy priorities.

We focused exclusively on **differential expression tools**, since earlier steps like quality control are better assessed via runtime and computational performance.


## Dataset
We used **synthetic post-alignment RNA-seq datasets** generated using `compcodeR` to simulate different experimental conditions:

- Varying number of DE genes (up/down-regulated)
- Inclusion of single/random outliers
- Use of Poisson vs Negative Binomial distribution
- Sample sizes: 2, 5, and 10 per condition

Advantages:
- Ground truth is known → allows calculation of true accuracy
- Reflects a variety of realistic RNA-seq scenarios

##  Methods
### Data Simulation
Used `generateSyntheticData()` from `compcodeR` with:
- 12,500 genes
- Configurable dispersion, upregulation, and outlier parameters

### Differential Expression Execution
- Tools supported by `compcodeR`: used `runDiffExp()`
- ABSSeq and PoissonSeq were run separately on extracted count matrices
- Adjusted p-value cutoff: 0.05

### Tool Summaries
- **ABSSeq**: Absolute count differences using negative binomial models
- **voom.limma**: Linear model after voom transformation and t-tests
- **PoissonSeq**: Poisson log-linear model + permutation FDR estimation
- **DESeq2**: NB modeling + GLM + Wald test
- **NOISeq**: Non-parametric, fold-change driven
- **ttest**: EdgeR with t-tests on normalized counts
- **edgeR.exact**: NB-based exact test for replicated RNA-seq


## Results
### Area Under the ROC Curve (AUC)
- All tools improved with increasing sample size
- **DESeq2**, **edgeR.exact**, **voom.limma**, **ttest**, **PoissonSeq** performed comparably

### Accuracy
- Accuracy scaled with sample size
- Most tools performed well except **ABSSeq**

### False Discovery Rate (FDR)
- **DESeq2**, **edgeR**, **voom.limma**, and **ttest** had lower, stable FDR
- **ABSSeq** had high and variable FDR
- **PoissonSeq** underperformed but improved with sample size

---

## Conclusion
- No tool dominated across all metrics
- **DESeq2** and **edgeR** are strong general-purpose choices
- **edgeR** may be preferred for speed-sensitive projects
- **voom.limma** and **ttest** perform better with Poisson-like distributions
- **ABSSeq** underperformed except when few DE genes are expected (low FDR)

Future work could involve:
- Testing against real-life messy RNA-seq datasets
- Incorporating additional tools with novel statistical assumptions
- Assessing end-to-end pipelines beyond DGE only

## References
- ABSSeq
- voom.limma
- PoissonSeq
- DESeq2
- NOISeq
- edgeR
- compcodeR
- RNA-Seq methodology overview


For more detailed methodology and full visualizations, please refer to our complete **research report** available in the repository.

> Maintained by Luigi Cheng  
> Portfolio: [https://iluigi98.github.io](https://iluigi98.github.io)
"""
