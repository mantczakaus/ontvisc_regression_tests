execute_scenario(){
	scenario=$1
	revision=$2
	resume=$3
	today=$(date +'%Y%m%d')
	execution_dir=PATH_TO_FOLDER/ontvisc_regression_tests/execution # Change PATH_TO_FOLDER
	mkdir -p ${execution_dir}
	logs_dir=${execution_dir}/$scenario/logs
	mkdir -p ${logs_dir}
	# Comment/uncomment based on the scheduler
	qsub -k oed -v revision=$revision,resume=$resume -o ${logs_dir}/$scenario\_${today}.out -e ${logs_dir}/$scenario\_${today}.err regression_scenarios/$scenario.sh
	# sbatch -o ${logs_dir}/$scenario\_${today}.out -e ${logs_dir}/$scenario\_${today}.err regression_scenarios/$scenario.sh $revision $resume 
}

revision=main
# revision=v1.3
resume=' '
# resume=-resume
execute_scenario reg_01 $revision $resume
execute_scenario reg_02 $revision $resume
execute_scenario reg_03 $revision $resume
execute_scenario reg_04 $revision $resume
execute_scenario reg_05 $revision $resume