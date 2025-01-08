# Regression tests for the [ONTViSc pipeline](https://github.com/eresearchqut/ontvisc)
## TO DO WHAT THE TESTS ARE AND WHY WE NEED THEM

# Prerequisites
You will need:
- Java
- [Nextflow](https://www.nextflow.io/docs/latest/index.html)
- Singularity
- Python with [pytest](https://docs.pytest.org/en/stable/getting-started.html)

# Clone the repository
git clone https://github.com/mantczakaus/ontvisc_regression_tests.git
cd ontvisc_regression_tests

# Test the `test` config first

## Modify
Modify the following files according to the specified instructions.

### conf/nextflow.config
Change `PATH_TO_FOLDER` to, for example, the folder to which you cloned the tests. This should be done for the `cacheDir` directive for `singularity` and `conda`. If you want to use Seqera Platform to monitor the runs, set the `accessToken`, `workspaceId` and change `enabled` to `true`. You can use [Seqera Platform](https://seqera.services.biocommons.org.au) from Australian BioCommons if you are an Australian researcher. Otherwise, you can still use the general version of [Seqera Platform](https://docs.seqera.io/platform/24.2). <br>
By default the tests are set up to be submitted to the PBS scheduler `executor = 'pbspro'` but you can change the config to incorporate the scheduler available on your environment, e.g. `executor = 'slurm'`.


### scripts/run_reg_test_and_verify_with_pytest.sh
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
`cd PATH_TO_FOLDER` (path to the folder to which you cloned the tests) 
```
cd ontvisc_regression_tests/scripts
bash run_reg_test_and_verify_with_pytest.sh
```

## 
Investigate output
1) Check if the ONTViSc pipeline run successfully. In the folder `ontvisc_regression_tests/execution/reg_test`, check the files `.nextflow.log`, `reg_test_<date_of_the_execution>.out` and `reg_test_<date_of_the_execution>.err`.
2) If the pipeline is completed, go to `ontvisc_regression_tests/execution/reg_test/results` and look for a file `results_verification_<date_of_the_execution>.txt`. This is a report showing if generated output match the expected output (folder `baselines`)

# Execute remaining test scenarios

## Modify
Modify the following files according to the specified instructions.

### scripts/run_regression_scenarios_and_verify_with_pytest.sh
Change in the same way as 'run_reg_test_and_verify_with_pytest.sh'

# Authors
- Magdalena Antczak (QCIF/QUT)
- Marie-Emilie Gauthier (QUT)
- Sonam Wangmo (JCU)

## TO DO CITE