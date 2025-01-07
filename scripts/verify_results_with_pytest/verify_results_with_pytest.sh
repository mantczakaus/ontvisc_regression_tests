export PYTEST_ADDOPTS="--color=yes"

scenario=$1
date=$2

pytest -v -s -m ${scenario} tests/verify_results_with_pytest.py \
--date=${date} \
--baseline_fold=PATH_TO_FOLDER/baselines/${scenario} \
--results_fold=PATH_TO_FOLDER/execution/${scenario}/results \
--log_fold=PATH_TO_FOLDER/execution/${scenario}/logs


# Note:
# What is -v?
# - The -v option stands for "verbose" and it increases the verbosity of the test output.
# - When you run pytest -v, it provides a more detailed output for each test case,
#   including the test names and their statuses (pass/fail/skipped/etc.).
# - This can be particularly useful for getting a clearer understanding of which tests are running and their results.

# What is -s?
# - The -s option tells pytest to disable output capturing.
# - By default, pytest captures all output (stdout and stderr) generated during the test run and
#   only shows it if a test fails.
# - When you use the -s option, all output is immediately printed to the terminal. This can be useful for debugging,
#   as you can see print statements and other output in real-time.
# - This is especially helpful when you are debugging issues and need to see what is happening inside your tests
#   without waiting for them to finish.

# What is -m?
# The -m option in pytest is used to select and run tests based on their markers.
# Markers are custom labels or tags that you can assign to your test functions or classes using
# @pytest.mark.marker_name decorator.

# In our case we have used scenario names as the marker Eg: reg_test, reg_01, etc...