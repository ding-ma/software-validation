import subprocess
import time

import pytest


# pytest tests\projects\test_projects_xml.py -s
@pytest.fixture(scope="function")
def app():
    subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True)
    time.sleep(0.5)
    yield
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True)

