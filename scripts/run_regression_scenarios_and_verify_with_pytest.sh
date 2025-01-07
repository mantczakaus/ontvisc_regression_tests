execute_scenario(){
	### Change PATH_TO_FOLDER to the path of the folder where you cloned the ontvisc_regression_tests repository
	execution_dir=PATH_TO_FOLDER/ontvisc_regression_tests/execution 

	### do not change the following
	scenario=$1
	revision=$2
	resume=$3
	today=$(date +'%Y%m%d')
	mkdir -p ${execution_dir}
	logs_dir=${execution_dir}/$scenario/logs
	mkdir -p ${logs_dir}

	### select the command to run based on the scheduler you have available
	qsub -k oed \
	-v revision=$revision,resume=$resume \
	-o ${logs_dir}/$scenario\_${today}.out \
	-e ${logs_dir}/$scenario\_${today}.err \
	-l walltime=24:00:00 \
	-l select=1:ncpus=2:mem=4gb \
	-N $scenario \
	regression_scenarios/$scenario.sh
	# sbatch \
	# -o ${logs_dir}/$scenario\_${today}.out \
	# -e ${logs_dir}/$scenario\_${today}.err \
	# --nodes=1 \
	# --cpus-per-task=2 \
	# --mem=4G \
	# --time=24:00:00 \
	# regression_scenarios/$scenario.sh \
	# $revision \
	# $resume 
}

### choose revision to test
revision=main
# revision=v1.3

### choose resume option
resume=' '
# resume=-resume

### Comment/uncomment the scenarios you want to run
execute_scenario reg_01 $revision $resume
execute_scenario reg_02 $revision $resume
execute_scenario reg_03 $revision $resume
execute_scenario reg_04 $revision $resume
execute_scenario reg_05 $revision $resume