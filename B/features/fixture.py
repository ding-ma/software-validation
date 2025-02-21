import subprocess
import requests
from behave import fixture
import sys

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


@fixture(name="fixture.app")
def app(context):
    #  we simply don't start the jar if we dont wan't the runTodoManagerRestAPI to run.
    if "--disable-server" in sys.argv:
        yield
    else:
        try:
            process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True)

            while status_code:  # Verify the system is up before starting the test
                status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            yield process
        finally:
            subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            process.kill()

