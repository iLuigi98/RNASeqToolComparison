#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript, run_rscript_test
from analysis import run_diff_exp_rscript

def main(targets):
    #Create synthetic data with parameters represents different number of samples per condition, truly differentially expressed genes, etc.
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)
        
        # #Create synthetic data #1 with 5 samples per conditon & 200 differentially expressed genes
        # synthetic_data1 = run_create_data_rscript(data_cfg.get('data1'), data_cfg.get('n_vars1'),
        #                                           data_cfg.get('samples_per_cond1'), 
        #                               data_cfg.get('n_diffexp1'), data_cfg.get('output_file1'))
        # #Create synthetic data #2 with 5 samples per conditon & 500 differentially expressed genes
        # synthetic_data2 = run_create_data_rscript(data_cfg.get('data2'), data_cfg.get('n_vars1'),
        #                                           data_cfg.get('samples_per_cond1'), 
        #                               data_cfg.get('n_diffexp2'), data_cfg.get('output_file2'))


        # new stuff --------------------------------------------------------------------------------


        #Create synthetic data baseline4000_0
        synthetic_data4 = run_create_data_rscript(data_cfg.get('data4'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp4'), data_cfg.get('output_file4'),
                                      upregulated=data_cfg.get('upregulated_ratio5'))


        #Create synthetic data baseline2000_2000
        synthetic_data5 = run_create_data_rscript(data_cfg.get('data5'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp4'), data_cfg.get('output_file5'),
                                      upregulated=data_cfg.get('upregulated_ratio5'))


        #Create synthetic data poisson0_0
        synthetic_data6 = run_create_data_rscript(data_cfg.get('data6'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp6'), data_cfg.get('output_file6'),
                                      poisson=data_cfg.get('poisson_ratio'))

        #Create synthetic data poisson625_625
        synthetic_data7 = run_create_data_rscript(data_cfg.get('data7'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp7'), data_cfg.get('output_file7'),
                                      upregulated=data_cfg.get('upregulated_ratio7'),
                                      poisson=data_cfg.get('poisson_ratio'))

        #Create synthetic data single0_0
        synthetic_data8 = run_create_data_rscript(data_cfg.get('data8'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp8'), data_cfg.get('output_file8'),
                                      singleHigh=data_cfg.get('single_count'),
                                      singleLow=data_cfg.get('single_count'))

        #Create synthetic data single625_625
        synthetic_data9 = run_create_data_rscript(data_cfg.get('data9'), data_cfg.get('n_vars'),
                                                  data_cfg.get('samples_per_cond'), 
                                      data_cfg.get('n_diffexp9'), data_cfg.get('output_file9'),
                                      upregulated=data_cfg.get('upregulated_ratio9'),
                                      singleHigh=data_cfg.get('single_count'),
                                      singleLow=data_cfg.get('single_count'))
    
    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)
        
        #Run DESeq2 on synthetic_data1 from above
        deseq2_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        
        #Run edgeR on synthetic_data1 from above
        edgeR_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData1'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        
        #Run DESeq2 on synthetic_data2 from above
        deseq2_data2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'),
                                            analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                            analysis_cfg.get('out_dir'))
        
        #Run edgeR on synthetic_data2 from above
        edgeR_data1 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData2'), 
                                           analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                           analysis_cfg.get('out_dir'))
        
    
    
    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)
        testing = run_rscript_test(**t_data_cfg)
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
