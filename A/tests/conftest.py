import asyncio

import pytest


@pytest.fixture(scope="function")
async def app():
    proc = asyncio.create_subprocess_shell(
        "java -jar runTodoManagerRestAPI-1.5.5.jar",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    yield proc
    await proc.kill()
