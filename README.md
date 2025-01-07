# ontvisc_regression_tests
Regression tests for the ONTViSC pipeline

# Modify
## ontvisc_regression_tests/conf/nextflow.config
Change `PATH_TO_FOLDER` for the `cacheDir` directive for `singularity` and `conda`.
If you want to use Seqera Platform to monitor the runs, set the `accessToken`, `workspaceId` and change `enabled` to `true`. You can use [Seqera Platform](https://seqera.services.biocommons.org.au) from Australian BioCommons if you are an Australian researcher. Otherwise, you can still use the general deployment of [Seqera Platform](https://docs.seqera.io/platform/24.2) 

