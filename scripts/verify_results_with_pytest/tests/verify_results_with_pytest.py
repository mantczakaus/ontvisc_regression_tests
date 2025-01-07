import pytest
import src.tests as regression_tests


@pytest.mark.reg_test
@pytest.mark.reg_01
@pytest.mark.reg_02
@pytest.mark.reg_03
@pytest.mark.reg_04
@pytest.mark.reg_05
def test_output_files(cmdline_args, scenario):
    date, baseline_fold, results_fold, _, = cmdline_args

    # Call the test_files function with the provided command line arguments
    result_test_files = regression_tests.test_output_files(baseline_fold, results_fold, date)

    # Check the result
    assert result_test_files == "passed", "Some output files are missing and/or additional files were generated."


@pytest.mark.reg_test
@pytest.mark.reg_01
@pytest.mark.reg_02
@pytest.mark.reg_03
@pytest.mark.reg_04
@pytest.mark.reg_05
def test_error(cmdline_args, scenario):
    date, baseline_fold, results_fold, log_fold = cmdline_args

    # Call the test_error function with the provided command line arguments
    result_test_error = regression_tests.test_error(log_fold, date, scenario)

    # Check the result
    assert result_test_error == "passed", f"Some errors were generated during the pipeline run."


@pytest.mark.reg_01
@pytest.mark.reg_02
def test_qcreport_txt(cmdline_args):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_qcreport function with the provided command line arguments
    result_test_qcreport = regression_tests.test_qcreport(baseline_fold, results_fold, date, "txt")

    # Check the result
    assert result_test_qcreport == "passed", "The generated QC report does not match what was expected."
    

@pytest.mark.reg_01
@pytest.mark.reg_02
def test_qcreport_html(cmdline_args):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_qcreport function with the provided command line arguments
    result_test_qcreport = regression_tests.test_qcreport(baseline_fold, results_fold, date, "html")

    # Check the result
    assert result_test_qcreport == "passed", "The generated QC report does not match what was expected."


@pytest.mark.reg_01
@pytest.mark.reg_02
@pytest.mark.reg_03
def test_blastn_viral_spp_abundance(cmdline_args, sample, mode):
    date, baseline_fold, results_fold, _ = cmdline_args
    
    if mode == "read_classification":
        blast_results_fold = "homology_search"
    else:
        blast_results_fold = "blastn"
    message = f"Viral species abundance from {mode} results" 

    # Call the test_homl_search_blastn function with the provided environment variables
    result_test_homl_search_blastn = regression_tests.test_homl_search_blastn(baseline_fold, results_fold, 
        sample, date, mode, blast_results_fold, f"{sample}_{mode}_viral_spp_abundance.txt", message, True)

    # Check the result
    assert result_test_homl_search_blastn == "passed", message + " is NOT as expected."
    
@pytest.mark.reg_01
@pytest.mark.reg_02
@pytest.mark.reg_03
def test_blastn_html_report(cmdline_args, sample, mode):
    date, baseline_fold, results_fold, _ = cmdline_args
  
    if mode == "read_classification":
        blast_results_fold = "homology_search"
    else:
        blast_results_fold = "blastn"
    message = f"Blastn html report from {mode} results" 
  
    # Call the test_homl_search_blastn function with the provided environment variables
    result_test_homl_search_blastn = regression_tests.test_homl_search_blastn(baseline_fold, results_fold, 
        sample, date, mode, blast_results_fold, f"{sample}_blast_report.html", message, False)

    # Check the result
    assert result_test_homl_search_blastn == "passed", message + " is NOT as expected."


@pytest.mark.reg_01
def test_read_class_kaiju(cmdline_args, sample):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_kaiju_awk function with the provided environment variables
    results_test_kaiju_awk = regression_tests.test_read_class_kaiju(baseline_fold, results_fold, sample, date)

    # Check the result
    assert results_test_kaiju_awk == "passed", f"The top hit in the filtered kaiju results is NOT as expected."
 

@pytest.mark.reg_01
def test_kraken(cmdline_args, sample):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_kraken function with the provided environment variables
    result_test_kraken = regression_tests.test_kraken(baseline_fold, results_fold, sample, date)

    # Check the result
    assert result_test_kraken == "passed", "Kraken2 and Bracken viral results filtered are NOT as expected."
    

@pytest.mark.reg_01
def test_read_class_html_report(cmdline_args, sample):
    date, baseline_fold, results_fold, _ = cmdline_args
  
    message = "Read classification summary html report"
  
    # Call the test_homl_search_blastn function with the provided environment variables
    result_test_read_class_html_report = regression_tests.test_read_class_html_report(baseline_fold, results_fold, sample, date, message)

    # Check the result
    assert result_test_read_class_html_report == "passed", message + " is NOT as expected."


@pytest.mark.reg_test
@pytest.mark.reg_04
def test_blast_ref_vs_canu_assmbl(cmdline_args, sample):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_ref_vs_canu_awk function with the provided environment variables
    results_test_blast_ref_vs_canu_assmbl = regression_tests.test_blast_ref_vs_canu_assmbl(baseline_fold, results_fold, sample, date)

    # Check the result
    assert results_test_blast_ref_vs_canu_assmbl == "passed", "The top hit in the blastn reference vs canu assembly result is NOT as expected."


@pytest.mark.reg_05
def test_mapping_coverage(cmdline_args, sample):
    date, baseline_fold, results_fold, _ = cmdline_args

    # Call the test_mapping_coverage function with the provided environment variables
    result_test_mapping_coverage = regression_tests.test_mapping_coverage(baseline_fold, results_fold, sample, date)

    # Check the result
    assert result_test_mapping_coverage == "passed", "Coverage test failed"
