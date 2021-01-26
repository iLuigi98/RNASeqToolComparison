#command arguments from config/analysis-params.json which specifies what tool is being used & file directories
myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')

indir <- myArgs[1]
data <- myArgs[2]
tool <- myArgs[3]
rmdFunc <- myArgs[4]
outdir <- myArgs[5]

if (tool == 'DESeq2') {
    #Run DESeq2 on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), fit.type = "parametric", test = "Wald", beta.prior = TRUE, independent.filtering = TRUE, cooks.cutoff = TRUE, impute.outliers = TRUE)
    }

if (tool == 'edgeR.exact') {
    #Run edgeR on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "TMM", disp.type = "tagwise", trend.method = "movingave")
    }



if (tool == 'baySeq') {
    #Run baySeq on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "edgeR", equaldisp  = TRUE, sample.size = 5000, estimation = "edgeR", pET = "iteratively")
    }

if (tool == 'NBPSeq') {
    #Run edgeR on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "TMM", disp.method = "NBP")
    }

if (tool == 'NOISeq.prenorm') {
    #Run DESeq2 on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "TMM")
    }

if (tool == 'TCC') {
    #Run edgeR on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "tmm", test.method = "deseq", iteration = 3, normFDR = 0.1, floorPDEG = 0.05)
    }

if (tool == 'voom.limma') {
    #Run edgeR on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "TMM")
    }


# #Compare the two tools
# file.table <- data.frame(input.files = file.path('out', c("data1_DESeq2.rds", "data1_edgeR.exact.rds")), stringsAsFactors = FALSE)
# params <- list(incl.nbr.samples = 5, incl.replicates = 1, incl.dataset = "dataExample", incl.de.methods = NULL,
#                    fdr.threshold = 0.05, tpr.threshold = 0.05, typeI.threshold = 0.05, ma.threshold = 0.05, fdc.maxvar = 1500, 
#                    overlap.threshold = 0.05, fracsign.threshold = 0.05, mcc.threshold = 0.05, nbrtpfp.threshold = 0.05,
#                    comparisons = c("auc", "fdr", "tpr", "ma", "correlation"))
# runComparison(file.table = file.table, parameters = params, output.directory = 'out')
#Run DESeq2 on synthetic data #1
#runDiffExp(data.file = '~/Downloads/', result.extent = "DESeq2", Rmdfunction = "DESeq2.createRmd", output.directory = )