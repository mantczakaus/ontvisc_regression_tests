execute_scenario(){
	scenario=$1
	revision=$2
	resume=$3
	today=$(date +'%Y%m%d')
	execution_dir=PATH_TO_FOLDER/execution
	mkdir -p ${execution_dir}
	logs_dir=${execution_dir}/$scenario/logs
	mkdir -p ${logs_dir}
	qsub -koed -v revision=$revision,resume=$resume -o ${logs_dir}/$scenario\_${today}.out -e ${logs_dir}/$scenario\_${today}.err regression_scenarios/$scenario.pbs
}

# execute_scenario reg_test v1.3 -resume
execute_scenario reg_test main ' '