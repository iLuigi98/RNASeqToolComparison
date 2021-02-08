#! /usr/bin/env python
import sys
import os
import json
sys.path.insert(0, 'src')
from etl import run_create_data_rscript, run_rscript_test
from analysis import run_diff_exp_rscript, run_comparison_rscript
import logging

logging.basicConfig(filename="log.txt", filemode='a',
 format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
 datefmt='%H:%M:%S',
 level=logging.DEBUG)

def main(targets):
    #Create synthetic data with parameters represents different number of samples per condition, truly differentially expressed genes, etc.
    if 'build' in targets:
        with open('config/build-params.json') as fh:
            data_cfg = json.load(fh)

        #All the synthetic data below is created with 12,500 genes and with 5 samples per condition

        #Create baseline synthetic data #1 with 0 differentially expressed genes
        baseline0_0 = run_create_data_rscript(data_cfg.get('data1'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file1'), data_cfg.get('seqdepth'))

        #Create baseline synthetic data #2 with 1250 differentially expressed genes with 1250 upregulated in condition 1 & 0 downin condition 2
        baseline1250_0 = run_create_data_rscript(data_cfg.get('data2'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file2'), data_cfg.get('seqdepth'))

        #Create baseline synthetic data #3 with 1250 differentially expressed genes with 625 upregulated in condition 1 & 625 downregulated in condition 2
        baseline625_625 = run_create_data_rscript(data_cfg.get('data3'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file3'), data_cfg.get('seqdepth'))

        #Create baseline synthetic data #4 with 1250 differentially expressed genes with 4000 upregulated in condition 1 & 0 in condition 2
        baseline4000_0 = run_create_data_rscript(data_cfg.get('data4'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file4'), data_cfg.get('seqdepth'))

        #Create baseline synthetic data #5 with 4000 differentially expressed genes with 2000 upregulated in condition 1 & 2000 in condition 2
        baseline2000_2000 = run_create_data_rscript(data_cfg.get('data5'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp4000'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file5'), data_cfg.get('seqdepth'))

        #Create synthetic data #6 whose counts were drawn from poisson distribution with 0 genes differentially expressed
        poisson0_0 = run_create_data_rscript(data_cfg.get('data6'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file6'), data_cfg.get('seqdepth'))

        #Create synthetic data #7 whose counts were drawn from poisson distribution with 625 upregulated in condition 1 & 625 in condition 2
        poisson625_625 = run_create_data_rscript(data_cfg.get('data7'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('poisson_dispersion'), data_cfg.get('type1'), data_cfg.get('outlier0'), data_cfg.get('output_file7'), data_cfg.get('seqdepth'))

        #Create synthetic data #8 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
        single0_0 = run_create_data_rscript(data_cfg.get('data8'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_file8'), data_cfg.get('seqdepth'))

        #Create synthetic data #9 where fraction of genes for which we selected a single sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
        single625_625 = run_create_data_rscript(data_cfg.get('data9'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type2'), data_cfg.get('single_count'), data_cfg.get('output_file9'), data_cfg.get('seqdepth'))

    #Create synthetic data #10 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 0 differentially expressed genes
        random0_0 = run_create_data_rscript(data_cfg.get('data10'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp0'), data_cfg.get('upregulated_ratio1'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_file10'), data_cfg.get('seqdepth'))

        #Create synthetic data #11 where fraction of genes for which we selected a random sample and multiplied the corresponding count with a factor between 5 and 10 with 625 genes expressed in cond 1 & 625 in cond 2
        random625_625 = run_create_data_rscript(data_cfg.get('data11'), data_cfg.get('n_vars'), data_cfg.get('samples_per_cond'), data_cfg.get('repl_id'), data_cfg.get('n_diffexp1250'), data_cfg.get('upregulated_ratio_half'), data_cfg.get('regular_dispersion'), data_cfg.get('type3'), data_cfg.get('random_outlier'), data_cfg.get('output_file11'), data_cfg.get('seqdepth'))



    #Run differential gene expression analysis tools on the synthetic data
    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        for i in range(1, 12):
            synthetic_num = str(i)

            #Run DESeq2 on the 11 synthetic datasets above
            logging.info("Performing DESeq2 on synthetic data #" + synthetic_num)
            deseq2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                          analysis_cfg.get('DESeq2_dir'))
            logging.info("Finished performing DESeq2 on synthetic data #" + synthetic_num)

            #Run edgeR.exact on the 11 synthetic datasets above
            logging.info("Performing edgeR on synthetic data #" + synthetic_num)
            edgeR = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                          analysis_cfg.get('edgeR_dir'))
            logging.info("Finished performing edgeR on synthetic data #" + synthetic_num)

            #Run voom.limma on the 11 synthetic datasets above
            logging.info("Performing voom.limma on synthetic data #" + synthetic_num)
            voom_limma = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'),
                                          analysis_cfg.get('voom_limma_dir'))
            logging.info("Finished performing voom.limma on synthetic data #" + synthetic_num)

            #Run NOISeq on the 11 synthetic datasets above
            logging.info("Performing NOISeq on synthetic data #" + synthetic_num)
            NOISeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'),
                                          analysis_cfg.get('NOISeq_dir'))
            logging.info("Finished performing NOISeq on synthetic data #" + synthetic_num)

            #Run ttest on the 11 synthetic datasets above
            logging.info("Performing ttest on synthetic data #" + synthetic_num)
            ttest = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                          analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'),
                                          analysis_cfg.get('ttest_dir'))
            logging.info("Finished performing ttest on synthetic data #" + synthetic_num)


            #Run PoissonSeq on the 11 synthetic datasets above
            logging.info("Performing PoissonSeq on synthetic data #" + synthetic_num)
            POIS = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                           analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'),
                                           analysis_cfg.get('PoissonSeq_dir'))
            logging.info("Finished performing PoissonSeq on synthetic data #" + synthetic_num)

             #Run ABSSeq on the 11 synthetic datasets above
            logging.info("Performing ABSSeq on synthetic data #" + synthetic_num)
            ABSSeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), analysis_cfg.get('synData' + synthetic_num),
                                            analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'),
                                            analysis_cfg.get('ABSSeq_dir'))
            logging.info("Finished performing ABSSeq on synthetic data #" + synthetic_num)


    if 'compare' in targets:
        with open('config/comparison-params.json') as fh:
            compare_data_cfg = json.load(fh)
        
        comparison = run_comparison_rscript(compare_data_cfg.get('ABSSeq_dir'), compare_data_cfg.get('DESeq_dir'), compare_data_cfg.get('edgeR_dir'), compare_data_cfg.get('NOISeq_dir'), compare_data_cfg.get('ttest_dir'), compare_data_cfg.get('PoissonSeq_dir'), compare_data_cfg.get('voom_dir'), compare_data_cfg.get('out_dir'))



    if 'test' in targets:
        with open('config/test-params.json') as fh:
            t_data_cfg = json.load(fh)

        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        # Creating a test synthetic data for tools to be performed on
        test_data = run_create_data_rscript(t_data_cfg.get('test_data'), t_data_cfg.get('n_vars'), t_data_cfg.get('samples_per_cond'), t_data_cfg.get('repl_id'), t_data_cfg.get('n_diffexp0'), t_data_cfg.get('upregulated_ratio1'), t_data_cfg.get('regular_dispersion'), t_data_cfg.get('type1'), t_data_cfg.get('outlier0'), t_data_cfg.get('output_test'), t_data_cfg.get('seqdepth'))
        
        #Run DESeq2 on the test data
        logging.info("Performing DESeq2 on synthetic data test_data")
        deseq2 = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp1'), analysis_cfg.get('Rmdfunc1'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing DESeq2 on synthetic data test_data")

        #Run edgeR.exact on the test data
        logging.info("Performing edgeR on synthetic data test_data")
        edgeR = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp2'), analysis_cfg.get('Rmdfunc2'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing edgeR on synthetic data test_data")

        #Run voom.limma on the test data
        logging.info("Performing voom.limma on synthetic data test_data")
        voom_limma = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp3'), analysis_cfg.get('Rmdfunc3'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing voom.limma on synthetic data test_data")

        #Run NOISeq on the test data
        logging.info("Performing NOISeq on synthetic data test_data")
        NOISeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp4'), analysis_cfg.get('Rmdfunc4'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing NOISeq on synthetic data test_data")

        #Run ttest on the test data
        logging.info("Performing ttest on synthetic data test_data")
        ttest = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp5'), analysis_cfg.get('Rmdfunc5'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing ttest on synthetic data test_data")


        #Run PoissonSeq on the test data
        logging.info("Performing PoissonSeq on synthetic data test_data")
        POIS = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp6'), analysis_cfg.get('Rmdfunc6'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing PoissonSeq on synthetic data test_data")

        #Run ABSSeq on the test data
        logging.info("Performing ABSSeq on synthetic data test_data")
        ABSSeq = run_diff_exp_rscript(analysis_cfg.get('in_dir'), t_data_cfg.get('analysis_test'),
                                        analysis_cfg.get('diffExp7'), analysis_cfg.get('Rmdfunc7'),
                                        t_data_cfg.get('test_dir'))
        logging.info("Finished performing ABSSeq on synthetic data test_data")
        
    return

if __name__ == '__main__':
    targets = sys.argv[1]
    main(targets)
