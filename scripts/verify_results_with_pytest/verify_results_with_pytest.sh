export PYTEST_ADDOPTS="--color=yes"

module load python

scenario=$1
date=$2

pytest -v -s -m ${scenario} tests/verify_results_with_pytest.py \
--date=${date} \
--baseline_fold=PATH_TO_FOLDER/baselines/${scenario} \
--results_fold=PATH_TO_FOLDER/execution/${scenario}/results \
--log_fold=PATH_TO_FOLDER/execution/${scenario}/logs