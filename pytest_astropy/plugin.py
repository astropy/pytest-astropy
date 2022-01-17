# Add a --runslow option to run slow tests
# From https://docs.pytest.org/en/latest/example/simple.html#control-skipping-of-tests-according-to-command-line-option

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run-slow",
        action="store_true",
        default=False,
        help="run slow tests",
    )
    parser.addoption(
        "--run-hugemem",
        action="store_true",
        default=False,
        help="run memory intensive tests",
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")
    config.addinivalue_line("markers",
                            "hugemem: mark test as using a lot of memory")


def pytest_collection_modifyitems(config, items):
    run_slow = config.getoption("--run-slow")
    run_hugemem = config.getoption("--run-hugemem")

    skip_slow = pytest.mark.skip(reason="need --run-slow option to run")
    skip_hugemem = pytest.mark.skip(reason="need --run-hugemem option to run")

    for item in items:
        if "slow" in item.keywords and not run_slow:
            item.add_marker(skip_slow)
        if "hugemem" in item.keywords and not run_hugemem:
            item.add_marker(skip_hugemem)
