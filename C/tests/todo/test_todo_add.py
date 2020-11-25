from ..headers import *
import requests
import json

url_todo = "http://localhost:4567/todos"

todo_data = {
    "title": "",
    "doneStatus": False,
    "description": ""
}


def create_to_do(run_id):
    todo_data['title'] = "my_test-" + run_id
    todo_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_todo, data=json.dumps(todo_data), headers=send_json_recv_json_headers)
    res = r.json()
    todos = requests.get(url_todo).json()["todos"]
    assert r.status_code == 201 and res in todos


def assert_todos(run_id):
    r = requests.get(url_todo, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text
