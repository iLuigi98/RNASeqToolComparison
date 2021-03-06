#command arguments from config/analysis-params.json which specifies what tool is being used & in/out file directories
myArgs <- commandArgs(trailingOnly = TRUE)
library('compcodeR')
#library('baySeq')
library('ABSSeq')
library("PoissonSeq")

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

if (tool == 'voom.limma' | tool == 'ttest' | tool == 'NOISeq') {
    #Run voom limma, ttest, or NOISeq on synthetic data
    runDiffExp(data.file = file.path(indir, data), result.extent = tool, Rmdfunction = rmdFunc, output.directory = file.path(outdir), norm.method = "TMM")
    }

if (tool == 'PoissonSeq') {
    #reformat compcode data to work for PoissonSeq
    path <- paste("~/RNASeqToolComparison",indir,data, sep="/")
    temp_data <- readRDS(path)
    n <- temp_data@count.matrix
    y <- c(1,1,1,1,1,2,2,2,2,2)
    type <-'twoclass'
    pair <- FALSE
    transformed_data <- list(n=n, y=y, type=type, pair=pair)
    pois_res <- PS.Main(transformed_data)
    ordered_pois_res <- pois_res[order(pois_res['gname'], decreasing=FALSE),]
    labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(n))), ncol=2)
    colnames(labels) <- c("actual", "gene_number")
    results <- merge(x=labels, y=pois_res, by.x="gene_number", by.y="gname", all.x=TRUE)
    result_df <- as.data.frame(results)
    result_df$prediction <- ifelse(result_df$pval < 0.05, 1, 0)
    result_df$prediction[is.na(result_df$prediction)] <- 0
    result_df$dif <- abs(result_df$actual - result_df$prediction)

    filename <- paste(substr(data, 0, nchar(data)-4),"_", tool, ".rds",sep="")
    out <- paste("~/RNASeqToolComparison/out/PoissonSeq", filename,  sep="/")
    saveRDS(result_df, out)
}

if (tool == 'ABSSeq') {
    #reformat compcode data to work for PoissonSeq
    path <- paste("~/RNASeqToolComparison",indir,data, sep="/")
    temp_data <- readRDS(path)
    groups <- c(1,1,1,1,1,2,2,2,2,2)
    absdata <- ABSDataSet(temp_data@count.matrix, groups)

    obj <- ABSSeq(absdata, useaFold=TRUE)
    abs_res <- results(obj,c("Amean","Bmean","foldChange","pvalue","adj.pvalue"))

    labels <- matrix(c(temp_data@variable.annotations$differential.expression, c(1:NROW(temp_data@count.matrix))), ncol=2)
    colnames(labels) <- c("actual", "gene_number")
    abs_res <- cbind(gene = rownames(abs_res), abs_res)
    rownames(abs_res) <- 1:nrow(abs_res)
    abs_res <- cbind(gene_number = rownames(abs_res), abs_res)
    rownames(abs_res) <- 1:nrow(abs_res)
    results <- merge(x=labels, y=abs_res, by="gene_number",all.x=TRUE)
    result_df <- as.data.frame(results)
    result_df$prediction <- ifelse(result_df$adj.pval < 0.05, 1, 0)
    result_df$prediction[is.na(result_df$prediction)] <- 0
    result_df$dif <- abs(result_df$actual - result_df$prediction)
    result_df <- result_df[c("gene","Amean","Bmean","foldChange","pvalue","adj.pvalue","actual","prediction","dif")]

    filename <- paste(substr(data, 0, nchar(data)-4),"_", tool, ".rds",sep="")
    out <- paste("~/RNASeqToolComparison/out/ABSSeq", filename,  sep="/")
    saveRDS(result_df, out)
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
