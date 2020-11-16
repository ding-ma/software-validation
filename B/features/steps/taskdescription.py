import requests
import subprocess
from features.steps.helper import *

@when(u'a user changes the description to {new_task_description}')
def step_impl(context, new_task_description):
    task_update = {
        "title": context.task_title,
        "description": new_task_description
    }
    context.new_task_description = new_task_description
    r = requests.put(url_todo_id % int(context.task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    assert r.status_code == 200

@when(u'a user removes the task description')
def step_impl(context):
    task_update = {
        "title": context.task_title,
        "description": ""
    }
    context.new_task_description = ""
    r = requests.put(url_todo_id % int(context.task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    assert r.status_code == 200

@then(u'the task description should be changed')
def step_impl(context):
    r = requests.get(url_todo_id % int(context.task_id), headers=recv_json_headers)
    todo = r.json()["todos"][0]
    assert r.status_code == 200 and str(context.new_task_description) == str(todo["description"])

@then(u'the task description should be empty')
def step_impl(context):
    r = requests.get(url_todo_id % int(context.task_id), headers=recv_json_headers)
    todo = r.json()["todos"][0]
    assert r.status_code == 200 and str(context.new_task_description) == str(todo["description"])

@when(u'a user selects the {wrong_task_id} to change the description to {new_task_description}')
def step_impl(context, wrong_task_id, new_task_description):
    task_update = {
        "description": new_task_description
    }
    r = requests.put(url_todo_id % int(wrong_task_id),data=json.dumps(task_update), headers=send_json_recv_json_headers)
    context.r = r
    assert r.status_code == 404