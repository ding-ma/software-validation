import pytest


@pytest.fixture(scope="function")
def app():
    pass
    # proc = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True)
    # print("active", proc)
    # yield proc
    # proc.kill()
