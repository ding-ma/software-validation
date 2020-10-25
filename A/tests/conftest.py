import subprocess
import time

import pytest


# pytest tests\projects\test_projects_xml.py -s
@pytest.fixture(scope="function")
def app():
    process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True)
    status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True)
    while status_code:
        status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True)
    yield
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True)
    process.kill()

