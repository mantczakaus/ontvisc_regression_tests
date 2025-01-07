import os
import pytest


def pytest_addoption(parser):
    parser.addoption("--date", action="store", help="Date to be used for the test")
    parser.addoption("--baseline_fold", action="store", help="Directory of the baseline folder")
    parser.addoption("--results_fold", action="store", help="Directory of the result folder")
    parser.addoption("--log_fold", action="store", help="Directory of the log folder")


@pytest.fixture
def cmdline_args(request):
    date = request.config.getoption("--date")
    baseline_fold = request.config.getoption("--baseline_fold")
    results_fold = request.config.getoption("--results_fold")
    log_fold = request.config.getoption("--log_fold")

    # To check if all the arguments are provided while running the test or not. If not error message will be displayed.
    if not date:
        pytest.fail(
            "Date commandline argument not provided --date=DATE (Eg: --date=20240123)")
    if not baseline_fold:
        pytest.fail("Baseline directory not provided --baseline_fold=BASELINE_FOLD ")

    if not results_fold:
        pytest.fail("Result directory not provided --results_fold=RESULT_FOLD")

    if not log_fold:
        pytest.fail("Log directory not provided --log_fold=LOG_FOLD")

    return date, baseline_fold, results_fold, log_fold


# Dictionary to map markers to sample names
scenario_to_sample = {
    'reg_test': 'test',
    'reg_01': 'MT011',
    'reg_02': 'ET300',
    'reg_03': 'MT010',
    'reg_04': 'MT483',
    'reg_05': 'MT483',
}


def pytest_configure(config):
    # Store the marker used in the test run
    os.environ['ACTIVE_MARKER'] = config.getoption("-m")


@pytest.fixture
def scenario(request):
    active_marker = os.getenv('ACTIVE_MARKER')
    if active_marker in scenario_to_sample:
        return active_marker
    pytest.fail("No valid marker found for the scenario")


@pytest.fixture
def sample(scenario):
    return scenario_to_sample.get(scenario, None)
    

# Dictionary to map markers to analysis mode
scenario_to_mode = {
    'reg_test': 'assembly',
    'reg_01': 'read_classification',
    'reg_02': 'clustering',
    'reg_03': 'assembly',
    'reg_04': 'assembly',
    'reg_05': 'map2ref',
}


@pytest.fixture
def mode(scenario):
    return scenario_to_mode.get(scenario, None)
    