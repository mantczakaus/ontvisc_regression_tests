# Regression tests for the ONTViSC pipeline

# Modify
## conf/nextflow.config
Change `PATH_TO_FOLDER` to, for example, the folder to which you cloned the tests. This should be done for the `cacheDir` directive for `singularity` and `conda`. If you want to use Seqera Platform to monitor the runs, set the `accessToken`, `workspaceId` and change `enabled` to `true`. You can use [Seqera Platform](https://seqera.services.biocommons.org.au) from Australian BioCommons if you are an Australian researcher. Otherwise, you can still use the general version of [Seqera Platform](https://docs.seqera.io/platform/24.2). 

## scripts/run_reg_test_and_verify_with_pytest.sh
Set `revision` (`main` by default) and `resume` (only two options can be used `-resume` or `' '`).
Change `PATH_TO_FOLDER` to the folder to which you cloned the tests (variable `execution_dir`).
By default the tests are set up to be submitted to the PBS scheduler with the following options:
'''
-k oed <this makes sure that the output and error file are immediately generated in the specified location>
-v <variables>
-o <path to standard output file>
-e <path to standard error file>
'''
Analogical command for Slurm should be
'''
sbatch -o ${logs_dir}/$scenario\_${today}.out -e ${logs_dir}/$scenario\_${today}.err regression_scenarios/$scenario.sh $revision $resume 
'''

## scripts/run_regression_scenarios_and_verify_with_pytest.sh
Change in the same way as 'run_reg_test_and_verify_with_pytest.sh'