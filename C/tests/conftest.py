import subprocess
import requests
import pytest


@pytest.fixture(scope="session", autouse=True)
def set_up_and_tear_down():
    # Set up make sure the app is not running at first
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    try:
        requests.get("http://localhost:4567/docs")
    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        raise e
    yield
    # Clean up if the app is running, kill it
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    try:
        requests.get("http://localhost:4567/docs")
    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        raise e


def start_server():
    process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    while status_code:  # Verify the system is up before starting the test
        status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return process


def shutdown_server(process):
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    process.kill()


# pytest tests\projects\test_projects_xml.py -s
@pytest.fixture(scope="function")
def app():
    p = start_server()
    yield
    shutdown_server(p)
