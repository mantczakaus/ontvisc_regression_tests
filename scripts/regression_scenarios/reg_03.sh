#!/bin/bash -l

# Change `PATH_TO_BLAST_DB_FOLDER` to the folder where you store the blast database
blast_db_dir=PATH_TO_BLAST_DB_FOLDER

# do not change the following
today=$(date +'%Y%m%d')
revision="${revision}"
resume="${resume}"
reg_dir="${regdir}"
modules_command="${modules}"

scenario=reg_03
cd "${reg_dir}/execution/${scenario}"

$modules_command

NXF_OPTS='-Xms1g -Xmx4g'

# execute the test
nextflow run eresearchqut/ontvisc \
	-config "${reg_dir}/conf/nextflow.config" \
	-r "${revision}" \
	-name "${scenario}_${today}_$RANDOM" \
	"${resume}" \
	-profile singularity \
	--outdir results/results_${today} \
	--samplesheet "${reg_dir}/samplesheets/REG03.csv" \
	--analysis_mode denovo_assembly \
	--flye \
	--flye_mode nano-raw \
	--flye_options '--genome-size 0.01m --meta' \
	--blast_threads 8 \
	--blastn_db "${blast_db_dir}/nt"

# verify the results
cd "${reg_dir}/scripts/verify_results_with_pytest"
bash verify_results_with_pytest.sh "${scenario}" "$today" \
> "${reg_dir}/execution/${scenario}/results/results_verification_$today.txt"
