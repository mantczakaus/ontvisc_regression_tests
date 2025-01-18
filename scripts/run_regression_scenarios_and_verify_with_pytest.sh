execute_scenario(){
	### do not change the following
	scenario="$1"
	revision="$2"
	resume="$3"
	reg_dir="$4"
	modules_command="$5"
	execution_dir="${reg_dir}/execution"
	mkdir -p "${execution_dir}"
	logs_dir="${execution_dir}/${scenario}/logs"
	mkdir -p "${logs_dir}"
	today=$(date +'%Y%m%d')

	### select the command to run based on the scheduler you have available
	qsub -k oed \
	-v revision="$revision",resume="$resume",regdir="$reg_dir",modules="$modules_command" \
	-o "${logs_dir}/${scenario}_${today}.out" \
	-e "${logs_dir}/${scenario}_${today}.err" \
	-l walltime=24:00:00 \
	-l select=1:ncpus=2:mem=4gb \
	-N "$scenario" \
	regression_scenarios/"$scenario".sh
	# sbatch \
	# -o "${logs_dir}/${scenario}_${today}.out" \
	# -e "${logs_dir}/${scenario}_${today}.err" \
	# --nodes=1 \
	# --cpus-per-task=2 \
	# --mem=4G \
	# --time=24:00:00 \
	# regression_scenarios/"$scenario".sh \
	# "$revision" \
	# "$resume"
}

### choose revision to test
revision=main
# revision=v1.3

### choose resume option
resume=' '
# resume=-resume

### Change PATH_TO_FOLDER to the path of the folder where you cloned the ontvisc_regression_tests repository
reg_dir="PATH_TO_FOLDER/ontvisc_regression_tests"

# Load the necessary modules. The following commands need to be adjusted according to what is available in your environment. 
# You may need to specify versions, some of the programs may be available without the need to load them, etc.
modules_command="""module load java
module load singularity
module unload python
module load python/3.10.12-gcccore-12.2.0"""

### Comment/uncomment the scenarios you want to run
execute_scenario "reg_03" "$revision" "$resume" "$reg_dir" "$modules_command"
