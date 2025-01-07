import os
import filecmp
import subprocess

def print_expected_and_actual(baseline_file, results_file):
    print(f"Expected results can be found in {baseline_file}")
    with open(baseline_file, 'r') as bf:
        print(bf.read())
    print(f"Actual results can be found in {results_file}")
    with open(results_file, 'r') as rf:
        print(rf.read())


def test_output_files(baseline_fold, results_fold, date):
    """Tests if the generated files match the baseline."""
    baseline_files = os.path.join(baseline_fold, "files_list.txt")
    results_files = os.path.join(results_fold, f"files_{date}.txt")

    # Running bash command to find the file excluding files containing "qc_report", sorting files and generates
    # files_{date}.txt
    command = f"cd {results_fold}/results_{date}; find . -type f \\( -name '.DS_Store' -o -name 'files_*.txt' \\) -prune -o -print | grep -v qc_report | grep -v detection_summary_ " \
              f"| sort --version-sort >  {results_files}"
    subprocess.run(command, shell=True, check=True)

    # Comparing the baseline files_list.txt to generated files_{date}.txt
    if filecmp.cmp(baseline_files, results_files):
        print("Output files are present as expected.")
        return "passed"
    else:
        print("Some output files are missing and/or additional files were generated.")
        print("Baseline files:")
        with open(baseline_files, 'r') as bf:
            print(bf.read())
        print("Generated files:")
        with open(results_files, 'r') as rf:
            print(rf.read())
        return "failed"


def test_error(log_fold, date, scenario):
    """Tests if the error file is empty."""
    log_file = os.path.join(log_fold, f"{scenario}_{date}.err")

    # Get the size of the file
    file_size = os.path.getsize(log_file)

    # Check if the file is empty
    if file_size == 0:
        print(f"No error was generated. File {log_file} is empty.")
        return "passed"
    else:
        print(f"Some errors were generated. Check the {log_file} file.")
        return "failed"
        

def test_qcreport(baseline_fold, results_fold, date, file_type):
    """ Compares a baseline QC report with a generated QC report to determine if they match."""
    baseline_file = os.path.join(baseline_fold, f"run_qc_report.{file_type}")
    results_file = os.path.join(results_fold, f"results_{date}", "qc_report", f"run_qc_report_{date}_copy_for_testing.{file_type}")

    # Compare two files and print the result.
    if filecmp.cmp(baseline_file, results_file, shallow=False):
        print("The generated QC report matches the expected.")
        return "passed"
    else:
        print("The generated QC report does not match what was expected.")
        print("Baseline QC report:")
        with open(baseline_file, 'r') as bf:
            print(bf.read())
        print("Generated QC report:")
        with open(results_file, 'r') as rf:
            print(rf.read())
        return "failed"


def test_homl_search_blastn(baseline_fold, results_fold, sample, date, mode, blast_results_fold, file_name, message, print_if_failed):
    """ Compares the baseline read classification file with the generated read classification file to determine if
    they match. """
    baseline_file = os.path.join(baseline_fold, file_name)
    results_file = os.path.join(results_fold, f"results_{date}", sample, mode, blast_results_fold, file_name)

    # Compare two files and print the result.
    if filecmp.cmp(baseline_file, results_file, shallow=False):
        print(message + " is as expected.")
        return "passed"
    else:
        print(message + " is NOT as expected.")
        if print_if_failed:
            print_expected_and_actual(baseline_file, results_file)
        else:
            print(f"Compare {results_file} with {baseline_file} for more details")
        return "failed"


def test_read_class_kaiju(baseline_fold, results_fold, sample, date):
    """ Checks the Kaiju summary viral filtered file for specific field values. """
    out_file = os.path.join(results_fold, f"results_{date}", sample, "read_classification", "kaiju",
                            f"{sample}_kaiju_summary_viral_filtered.tsv")
    baseline_file = os.path.join(baseline_fold, f"{sample}_kaiju_summary_viral_filtered_top_hit.tsv")
                            
    with open(baseline_file) as file_h:
        exp_per_reads, exp_num_reads, exp_taxon_id, exp_taxon_name = file_h.read().strip().split('\t')
        exp_per_reads = float(exp_per_reads)
        exp_num_reads = float(exp_num_reads)
    
    result = "passed"

    with open(out_file, 'r') as file:
        line = file.readline()
        line = file.readline()
        fields = line.strip().split('\t')
        if len(fields) == 5:
            if float(fields[1]) != exp_per_reads:
                result = "failed"
                print(f"Incorrect percent of reads; expected: {exp_per_reads}, actual: {fields[1]}")
            if float(fields[2]) != exp_num_reads:
                result = "failed"
                print(f"Incorrect number of reads; expected: {exp_num_reads}, actual: {fields[2]}")
            if fields[3] != exp_taxon_id:
                result = "failed"
                print(f"Incorrect taxon id; expected: {exp_taxon_id}, actual: {fields[3]}")
            if fields[4] != exp_taxon_name:
                result = "failed"
                print(f"Incorrect taxon name; expected: {exp_taxon_name}, actual: {fields[4]}")
        else:
            result = "failed"
            print("Incorrect number of fields")
        
    if result == "passed":
        print("The top hit in the filtered kaiju results is as expected.")
        
    return result


def test_kraken(baseline_fold, results_fold, sample, date):
    """ Compares the baseline bracken report viral filtered file with the generated file to determine if they match."""
    baseline_file = os.path.join(baseline_fold, f"{sample}_bracken_report_viral_filtered.txt")
    results_file = os.path.join(results_fold, f"results_{date}", sample, "read_classification", "kraken",
                                f"{sample}_bracken_report_viral_filtered.txt")

    # Compare two files and print the result.
    if filecmp.cmp(baseline_file, results_file, shallow=False):
        print("Kraken2 and Bracken viral results filtered are as expected.")
        return "passed"
    else:
        print(f"Kraken2 and Bracken viral results filtered are NOT as expected.")
        print_expected_and_actual(baseline_file, results_file)
        return "failed"


def test_read_class_html_report(baseline_fold, results_fold, sample, date, message):
    """ Compares the baseline read classification report with the generated read classification report to determine if
    they match. """
    baseline_file = os.path.join(baseline_fold, f"{sample}_read_classification_report.html")
    results_file = os.path.join(results_fold, f"results_{date}", sample, "read_classification", "summary", f"{sample}_read_classification_report.html")

    # Compare two files and print the result.
    if filecmp.cmp(baseline_file, results_file, shallow=False):
        print(message + " is as expected.")
        return "passed"
    else:
        print(message + " is NOT as expected.")
        print(f"Compare {results_file} with {baseline_file} for more details")
        return "failed"


def test_blast_ref_vs_canu_assmbl(baseline_fold, results_fold, sample, date):
    """Checks the BLASTN reference vs assembly file for specific field values."""
    out_file = os.path.join(results_fold, f"results_{date}", sample, "assembly", "blast_to_ref",
                                f"{sample}_blastn_reference_vs_canu_assembly.txt")
    baseline_file = os.path.join(baseline_fold, f"{sample}_blastn_reference_vs_canu_assembly_top_hit.txt")
    with open(baseline_file) as file_h:
        exp_ref, exp_length, exp_identity, exp_evalue = file_h.read().strip().split('\t')
        exp_length = float(exp_length)
        exp_identity = float(exp_identity)
        exp_evalue = float(exp_evalue)

    result = "passed"

    with open(out_file, 'r') as file:
        line = file.readline()
        line = file.readline()
        fields = line.strip().split('\t')
        if len(fields) >= 13:
            if fields[1] != exp_ref:
                result = "failed"
                print(f"Incorrect reference; expected: {exp_ref}, actual: {fields[1]}")
            if float(fields[2]) < exp_length:
                result = "failed"
                print(f"Incorrect length; should be higher than {exp_length}; is {fields[2]}")
            if float(fields[3]) < exp_identity:
                result = "failed"
                print(f"Incorrect length; should be higher than {exp_identity}; is {fields[3]}")
            if float(fields[12]) != exp_evalue:
                result = "failed"
                print(f"Incorrect e-value; expected: {exp_evalue}, actual: {fields[12]}")
        else:
            result = "failed"
            print("Line does not have enough fields")
            
    if result == "passed":
        print("The top hit in the blastn reference vs canu assembly result is as expected.")

    return result


def test_mapping_coverage(baseline_fold, results_fold, sample, date):
    """ Compares the baseline coverage file with the generated file to determine if they match."""
    baseline_file = os.path.join(baseline_fold, f"{sample}_coverage.txt")
    results_file = os.path.join(results_fold, f"results_{date}", sample, "mapping", f"{sample}_coverage.txt")

    # Compare two files and print the result.
    if filecmp.cmp(baseline_file, results_file, shallow=False):
        print("The coverage of mapping the reads to the reference genome is as expected.")
        return "passed"
    else:
        print(f"The coverage of mapping the reads to the reference genome is NOT as expected.")
        print_expected_and_actual(baseline_file, results_file)
        return "failed"
