import pytest

from ..headers import *
import requests
import json
from .todos_data import *
from ..test_fixture import start_server,shutdown_server


def create_to_do(run_id):
    todo_data['title'] = "my_test-"+run_id
    todo_data['description'] = "my_decrip-"+run_id
    r = requests.post(url_todo,data=json.dumps(todo_data), headers=send_json_recv_json_headers)
    res = r.json()
    todos = requests.get(url_todo).json()["todos"]
    assert r.status_code == 201 and res in todos


def assert_todos(run_id):
    r = requests.get(url_todo, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-"+run_id in r.text and "my_decrip-"+run_id in r.text


@pytest.mark.monitor_test
def test_add_10_todo_t1():
    p = start_server()
    for i in range(10):
        create_to_do(str(i))
        assert_todos(str(i))
    shutdown_server(p)


@pytest.mark.monitor_test
def test_add_10_todo_t2(app):
    for i in range(10):
        create_to_do(str(i))


@pytest.mark.monitor_test
def test_add_100_todo_t1():
    p = start_server()
    for i in range(100):
        create_to_do(str(i))
        assert_todos(str(i))
    shutdown_server(p)


@pytest.mark.monitor_test
def test_add_100_todo_t2(app):
    for i in range(100):
        create_to_do(str(i))


@pytest.mark.monitor_test
def test_add_1000_todo_t1():
    p = start_server()
    for i in range(1000):
        create_to_do(str(i))
        assert_todos(str(i))
    shutdown_server(p)


@pytest.mark.monitor_test
def test_add_1000_todo_t2(app):
    for i in range(1000):
        create_to_do(str(i))

