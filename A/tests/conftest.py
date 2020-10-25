import pytest 
import os, signal
import subprocess
import requests
import time

@pytest.fixture(scope="function")
def jar():
    proc = subprocess.Popen(["java","-jar","runTodoManagerRestAPI-1.5.5.jar"], shell=True)
    time.sleep(5)
    yield proc
    # kill this process
    proc.kill()


# # @pytest.fixture(scope="function")
# # def app():
# #     process = subprocess.run(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], capture_output=True)
# #     yield