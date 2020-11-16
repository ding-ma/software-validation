import requests
import subprocess
import xmltodict
from behave import *

from features.steps.helper import *

@given(u'the a task with title {task_title}, description {task_description} and done status {task_doneStatus}')
def step_impl(context, task_title, task_description, task_doneStatus):
    create_todo = requests.post(url_todo,data=json.dumps({"title": str(task_title), "description": str(task_description), "doneStatus": bool(task_doneStatus) } ), headers=send_json_recv_json_headers)
    todo_res = create_todo.json()
    todos = requests.get(url_todo).json()["todos"]
    context.task_id = todo_res["id"]
    context.task_title = todo_res["title"]
    context.task = todo_res
    assert create_todo.status_code == 201 and todo_res in todos


@when(u'a user marks the task {task_title} as done')
def step_impl(context,task_title):
    task_update = {
        "title": str(task_title),
        "doneStatus": True
    }
    r = requests.put(url_todo_id % int(context.task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    assert r.status_code == 200

@when(u'a user marks the task {task_title} as not done')
def step_impl(context,task_title):
    task_update = {
        "title": str(task_title),
        "doneStatus": False
    }
    r = requests.put(url_todo_id % int(context.task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    assert r.status_code == 200

@then(u'the task should have a a doneStatus of {task_doneStatus}')
def step_impl(context, task_doneStatus):
    r = requests.get(url_todo_id % int(context.task_id), headers=recv_json_headers)
    todo = r.json()["todos"][0]
    assert r.status_code == 200 and str(task_doneStatus).casefold() == str(todo["doneStatus"]).casefold()

@when(u'a user marks the wrong task {wrong_task_id} as done')
def step_impl(context, wrong_task_id):
    task_update = {
        "title": "",
        "doneStatus": True
    }
    r = requests.put(url_todo_id % int(wrong_task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    context.r = r
    assert r.status_code == 404

@then(u'there should be a not found error')
def step_impl(context):
    assert context.r.status_code == 404