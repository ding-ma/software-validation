import requests
import subprocess
import xmltodict
from features.steps.helper import *


@when(u'a user changes the description of the following tasks')
def step_impl(context):
    for row in context.table:
        task_update = {
            "title": row["task_title"],
            "description": row["task_description"]
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 200


@then(u'the task descriptions should be changed')
def step_impl(context):
    for row in context.table:
        r = requests.get(url_todo_id % int(row["task_id"]), headers=recv_json_headers)
        todo = r.json()["todos"][0]
        assert r.status_code == 200 and str(row["task_description"]) == str(todo["description"])


@when(u'a user removes the description of the following tasks')
def step_impl(context):
    for row in context.table:
        task_update = {
            "title": row["task_title"],
            "description": ""
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 200


@when(u'a user changes the description of a non-existent task')
def step_impl(context):
    for row in context.table:
        task_update = {
           "description": row["task_description"]
        }
        r = requests.put(url_todo_id % int(row["task_id"]),data=json.dumps(task_update), headers=send_json_recv_json_headers)
        assert r.status_code == 404
