#!/bin/bash -l

# do not change the following
today=$(date +'%Y%m%d')
revision="${revision}"
resume="${resume}"
reg_dir="${regdir}"
modules_command="${modules}"

scenario=reg_test
cd "${reg_dir}/execution/${scenario}"

$modules_command

NXF_OPTS='-Xms1g -Xmx4g'

# execute the test
nextflow run eresearchqut/ontvisc \
	-config "${reg_dir}/conf/nextflow.config" \
	-r "${revision}" \
	-name "${scenario}_${today}_$RANDOM" \
	"${resume}" \
	-profile singularity,test \
	--outdir results/results_${today}

# verify the results
cd "${reg_dir}/scripts/verify_results_with_pytest"
bash verify_results_with_pytest.sh "${scenario}" "$today" "${reg_dir}" \
> "${reg_dir}/execution/${scenario}/results/results_verification_$today.txt"
