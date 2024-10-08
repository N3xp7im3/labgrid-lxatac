import traceback

import pytest


@pytest.fixture(scope="function")
def barebox(strategy):
    try:
        strategy.transition("barebox")
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into barebox failed: {e}", returncode=3)

    return strategy.barebox


@pytest.fixture(scope="function")
def shell(strategy):
    try:
        strategy.transition("shell")
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into shell failed: {e}", returncode=3)

    return strategy.shell


@pytest.fixture(scope="function")
def online(strategy):
    try:
        strategy.transition("network")
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into online state failed: {e}", returncode=3)


@pytest.fixture(scope="function")
def system0_shell(strategy):
    try:
        strategy.transition("system0")
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into system0 shell failed: {e}", returncode=3)

    return strategy.shell


@pytest.fixture(scope="function")
def system1_shell(strategy):
    try:
        strategy.transition("system1")
    except Exception as e:
        traceback.print_exc()
        pytest.exit(f"Transition into system1 shell failed: {e}", returncode=3)

    return strategy.shell


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: These tests run especially slow.")
