import pytest 
import subprocess
import threading 
import asyncio

@pytest.fixture(scope="function")
async def app():
    proc = asyncio.create_subprocess_shell(
        "java -jar runTodoManagerRestAPI-1.5.5.jar",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    yield proc
    proc.terminate()
    proc.wait()
    # proc.kill()

# # @pytest.fixture(scope="function")
# # def app():
# #     process = subprocess.run(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], capture_output=True)
# #     yield