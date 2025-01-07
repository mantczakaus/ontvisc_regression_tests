#!/bin/bash -l

reg_dir=PATH_TO_FOLDER

module load java
module load nextflow
module load singularity

today=$(date +'%Y%m%d')
revision=${revision}
resume=${resume}

scenario=reg_test
cd ${reg_dir}/execution/${scenario}

NXF_OPTS='-Xms1g -Xmx4g'

nextflow run eresearchqut/ontvisc \
	-config ${reg_dir}/conf/nextflow.config \
	-r ${revision} \
	-name ${scenario}_${today}_$RANDOM \
	${resume} \
	-profile singularity,test \
	--outdir results/results_${today}

cd ${reg_dir}/scripts/verify_results_with_pytest
bash verify_results_with_pytest.sh ${scenario} $today \
> ${reg_dir}/execution/${scenario}/results/results_verification_$today.txt
