import requests
import subprocess
import xmltodict
from features.steps.helper import *

@given(u'the following tasks')
def step_impl(context):
    for row in context.table:
        create_todo = requests.post(url_todo,data=json.dumps({"title": str(row['task_title']), "description": str(row["task_description"]), "doneStatus": bool(row["task_doneStatus"]) } ), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        todos = requests.get(url_todo).json()["todos"]
        # print(todos)
        assert create_todo.status_code == 201 and todo_res in todos


@when(u'a user marks the following task as done')
def step_impl(context):
    for row in context.table:
        task_update = {
            "title": row["task_title"],
            "doneStatus": True
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 200


@then(u'the task done status should be changed')
def step_impl(context):
    for row in context.table:
        r = requests.get(url_todo_id % int(row["task_id"]), headers=recv_json_headers)
        todo = r.json()["todos"][0]
        assert r.status_code == 200 and str(row["task_doneStatus"]).casefold() == str(todo["doneStatus"]).casefold()


@when(u'a user marks the following tasks as not done')
def step_impl(context):
    for row in context.table:
        task_update = {
            "title": row["task_title"],
            "doneStatus": False
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 200


@when(u'a user marks a non-existent task as done')
def step_impl(context):
    for row in context.table:
        task_update = {
           "doneStatus": True
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 404


@then(u'nothing should happen')
def step_impl(context):
    pass