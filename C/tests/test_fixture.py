import pytest
from .conftest import start_server, shutdown_server


# we will do this to have a better average
@pytest.mark.monitor_test
def test_start_stop_fixture_time():
    for _ in range(10):
        p = start_server()
        shutdown_server(p)


@pytest.mark.monitor_test
def test_fixture_time():
    pass
