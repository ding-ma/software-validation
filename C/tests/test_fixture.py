import pytest
import subprocess


# we will do this to have a better average
@pytest.mark.monitor_test
def test_start_fixture_time():
    for _ in range(10):
        process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True)
        status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True)
        while status_code:  # Verify the system is up before starting the test
            status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True)

        subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True)
        process.kill()
