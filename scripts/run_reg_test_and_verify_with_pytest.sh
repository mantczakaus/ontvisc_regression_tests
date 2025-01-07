revision=main
# revision=v1.3
resume=' '
# resume=-resume
execution_dir=PATH_TO_FOLDER/ontvisc_regression_tests/execution

scenario=reg_test
today=$(date +'%Y%m%d')
mkdir -p ${execution_dir}
logs_dir=${execution_dir}/$scenario/logs
mkdir -p ${logs_dir}

qsub -k oed \
-v revision=$revision,resume=$resume \
-o ${logs_dir}/$scenario\_${today}.out \
-e ${logs_dir}/$scenario\_${today}.err \
-l walltime=24:00:00 \
-l select=1:ncpus=2:mem=4gb \
-N $scenario \
regression_scenarios/$scenario.sh

#sbatch -o ${logs_dir}/$scenario\_${today}.out -e ${logs_dir}/$scenario\_${today}.err regression_scenarios/$scenario.sh $revision $resume 
