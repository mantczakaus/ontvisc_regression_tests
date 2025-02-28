# Regression tests for the [ONTViSc pipeline](https://github.com/eresearchqut/ontvisc)
TO DO WHAT THE TESTS ARE AND WHY WE NEED THEM
## Test scenarios


## Verification of results
### test_output_files(baseline_fold, results_fold, date)
- Purpose: Tests if the generated files match the baseline.
- Passed: When the generated files list matches the baseline files list.
- Failed: When there are missing or additional files compared to the baseline.

### test_error(log_fold, date, scenario)
- Purpose: Tests if the error file is empty.
- Passed: When the error file is empty.
- Failed: When the error file contains any errors.

### test_qcreport(baseline_fold, results_fold, date, file_type)
- Purpose: Compares a baseline QC report with a generated QC report to determine if they match.
- Passed: When the generated QC report matches the baseline QC report.
- Failed: When the generated QC report does not match the baseline QC report.

### test_homl_search_blastn(baseline_fold, results_fold, sample, date, mode, blast_results_fold, file_name, message, print_if_failed)
- Purpose: Compares the baseline read classification file with the generated read classification file to determine if they match.
- Passed: When the generated read classification file matches the baseline file.
- Failed: When the generated read classification file does not match the baseline file.

### test_read_class_kaiju(baseline_fold, results_fold, sample, date)
- Purpose: Checks the Kaiju summary viral filtered file for specific field values.
- Passed: When the specific field values in the generated file match the expected values.
- Failed: When the specific field values in the generated file do not match the expected values.
- Fields compared:
  - Percent of reads
  - Number of reads
  - Taxon ID
  - Taxon name

### test_kraken(baseline_fold, results_fold, sample, date)
- Purpose: Compares the baseline bracken report viral filtered file with the generated file to determine if they match.
- Passed: When the generated bracken report matches the baseline report.
- Failed: When the generated bracken report does not match the baseline report.

### test_read_class_html_report(baseline_fold, results_fold, sample, date, message)
- Purpose: Compares the baseline read classification report with the generated read classification report to determine if they match.
- Passed: When the generated read classification report matches the baseline report.
- Failed: When the generated read classification report does not match the baseline report.

### test_blast_ref_vs_canu_assmbl(baseline_fold, results_fold, sample, date)
- Purpose: Checks the BLASTN reference vs assembly file for specific field values.
- Passed: When the specific field values in the generated file match the expected values.
- Failed: When the specific field values in the generated file do not match the expected values.
- Fields compared:
  - Reference
  - Length
  - Identity
  - E-value

### test_mapping_coverage(baseline_fold, results_fold, sample, date)
- Purpose: Compares the baseline coverage file with the generated file to determine if they match.
- Passed: When the generated coverage file matches the baseline file.
- Failed: When the generated coverage file does not match the baseline file.


# Prerequisites
You will need:
- Java
- [Nextflow](https://www.nextflow.io/docs/latest/index.html)
- Singularity
- Python with [pytest](https://docs.pytest.org/en/stable/getting-started.html)

# Clone the repository
'''
git clone https://github.com/mantczakaus/ontvisc_regression_tests.git
cd ontvisc_regression_tests
'''
TO DO note on PATH_TO_FOLDER

# Test the `test` config first
Run this test case on its own first. It will allow you to make sure that everything is set up correctly and to download the ONTViSc pipeline into your Nextflow `assets` folder without any conflicts.

## Modify
Modify the following files according to the specified instructions.

### conf/nextflow.config
Change `PATH_TO_FOLDER` to, for example, the folder to which you cloned the tests. This should be done for the `cacheDir` directive for `singularity` and `conda`. If you want to use Seqera Platform to monitor the runs, set the `accessToken`, `workspaceId` and change `enabled` to `true`. You can use [Seqera Platform](https://seqera.services.biocommons.org.au) from Australian BioCommons if you are an Australian researcher. Otherwise, you can still use the general version of [Seqera Platform](https://docs.seqera.io/platform/24.2). <br>
By default the tests are set up to be submitted to the PBS scheduler `executor = 'pbspro'` but you can change the config to incorporate the scheduler available on your environment, e.g. `executor = 'slurm'`.


### scripts/run_reg_test_and_verify_with_pytest.sh
TO DO change to incorporate changes to other scenarios (e.g. external modules)
Set `revision` (`main` by default) and `resume` (only two options can be used `-resume` or `' '`).
Change `PATH_TO_FOLDER` to the folder to which you cloned the tests (variable `execution_dir`).
By default the tests are set up to be submitted to the PBS scheduler but the analogical command for Slurm is also provided.

### scripts/regression_scenarios/reg_test.sh
Change `PATH_TO_FOLDER` to the folder to which you cloned the tests (variable `reg_dir`).
Load the necessary modules. By default this is set to the following:
```
module load java
module load nextflow
module load singularity
module load python
```
This needs to be adjusted according to what is available in your environment. You may need to specify versions, some of the programs may be available without the need to load them, etc.

## Run
```
cd PATH_TO_FOLDER #path to the folder to which you cloned the tests
cd ontvisc_regression_tests/scripts
bash run_reg_test_and_verify_with_pytest.sh
```

## Investigate output
Check if the ONTViSc pipeline run successfully. In the folder `ontvisc_regression_tests/execution/reg_test`, check the files `.nextflow.log`, `reg_test_<date_of_the_execution>.out` and `reg_test_<date_of_the_execution>.err`. <br><br>
If the pipeline is completed, go to `ontvisc_regression_tests/execution/reg_test/results` and look for a file `results_verification_<date_of_the_execution>.txt`. This is a report showing if generated output match the expected output (folder `baselines`). Below an example of the output <br>
![Example output reg_test failed](images/output_reg_test_failed.png) <br>

`============================= test session starts ==============================` indicates the start of the pytest session, including the platform, Python version, pytest version, and other relevant information. <br><br>
`collecting ... collected 11 items / 8 deselected / 3 selected` hows the number of test items collected and how many were selected or deselected for this run. <br><br>
The next section shows the results of specific tests. If they failed, it provides details about the specific failure and/or a message indicating where to check for errors. <br><br>
`=================================== FAILURES ===================================` provides detailed information about the failures and shows the assertion errors. <br><br>
`=========================== short test summary info ============================` provides a short summary of the test results, lists the failed tests and their respective assertion errors. <br><br>
`================== 2 failed, 1 passed, 8 deselected in 0.36s ===================` provides a final summary of the test results, including the number of failed, passed, and deselected tests, as well as the total time taken for the tests.

## TO DO Note on CANU results

# Test other scenarios
Provided you run the `test` config scenario first, you can run the rest of scenarios in parallel.

## Download data
TO DO

## Download databases 
TO DO AFTER DESCRIBING SCENARIOS AT THE BEGINNING
See more about which databases you will need in the [ONTViSc guide](https://github.com/eresearchqut/ontvisc?tab=readme-ov-file#installing-the-required-indexes-and-references).

## Modify
Modify the following files according to the specified instructions.

### scripts/run_regression_scenarios_and_verify_with_pytest.sh

### scripts/regression_scenarios/reg_&lt;SCENARIO&gt;.sh
Specify directories of the databases, you will need. Depending on scenario, these could be:
- `PATH_TO_BLAST_DB_FOLDER` (directory where you store the nt database)


### samplesheets/&lt;SCENARIO&gt;.csv
Change `PATH_TO_FOLDER` to the folder to which you cloned the tests.

### 

# Authors
- Magdalena Antczak (QCIF/QUT)
- Marie-Emilie Gauthier (QUT)
- Sonam Wangmo (JCU)

TO DO NOTE ABOUT PYTEST


## TO DO CITE