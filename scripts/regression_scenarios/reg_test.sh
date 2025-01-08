#!/bin/bash -l

# Change `PATH_TO_FOLDER` to the folder to which you cloned the tests 
reg_dir=PATH_TO_FOLDER/ontvisc_regression_tests

# Load the necessary modules. The following commands need to be adjusted according to what is available in your environment. 
# You may need to specify versions, some of the programs may be available without the need to load them, etc.
module load java
module load nextflow
module load singularity
module load python

# do not change the following
today=$(date +'%Y%m%d')
revision=${revision}
resume=${resume}

scenario=reg_test
cd ${reg_dir}/execution/${scenario}

NXF_OPTS='-Xms1g -Xmx4g'

# execute the test
nextflow run eresearchqut/ontvisc \
	-config ${reg_dir}/conf/nextflow.config \
	-r ${revision} \
	-name ${scenario}_${today}_$RANDOM \
	${resume} \
	-profile singularity,test \
	--outdir results/results_${today}

# verify the results
cd ${reg_dir}/scripts/verify_results_with_pytest
bash verify_results_with_pytest.sh ${scenario} $today ${reg_dir} \
> ${reg_dir}/execution/${scenario}/results/results_verification_$today.txt \

