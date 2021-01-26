import os
import shutil

def run_create_data_rscript(data, n_vars, samples_per_cond, n_diffexp, output_file, upregulated=1, poisson=0, singleHigh=0, singleLow=0):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/syntheticDataFunc.R " + data + ' ' + str(n_vars) + ' ' + str(samples_per_cond) + ' ' + str(n_diffexp) + ' ' + output_file)
    return

def run_rscript_test(string):
    os.system("/opt/conda/envs/r-bio/bin/Rscript src/test.R " + string)
    return
