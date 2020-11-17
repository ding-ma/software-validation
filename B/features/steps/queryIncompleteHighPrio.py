import requests
import subprocess
import xmltodict
from behave import *

from features.steps.helper import *

@given(u'a complete task with title {task_title}, description {task_description}')
def step_impl(context, task_title, task_description):
    # Create task 
    create_todo = requests.post(url_todo,data=json.dumps({"title": str(task_title), "description": str(task_description), "doneStatus": True } ), headers=send_json_recv_json_headers)
    todo_res = create_todo.json()
    todos = requests.get(url_todo).json()["todos"]
    context.complete_task_id = todo_res["id"]
    context.complete_task_title = todo_res["title"]
    context.complete_task = todo_res

    # Link to category
    task = {
        "id": context.complete_task_id
    }
    r = requests.post("http://localhost:4567/categories/%d/todos" % int(context.old_category_id), data=json.dumps(task), headers=send_json_recv_json_headers)
    assert create_todo.status_code == 201 and todo_res in todos and r.status_code == 201


@then(u'only incomplete task for category should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/categories/%d/todos?doneStatus=false" % int(context.old_category_id), headers=send_json_recv_json_headers)
    assert(r.json()["todos"][0]["doneStatus"] == "false")

@then(u'no tasks for category should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/categories/%d/todos?doneStatus=false" % int(context.old_category_id), headers=send_json_recv_json_headers)
    assert(len(r.json()["todos"]) == 0)

@then(u'tasks for category should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/categories/%d/todos" % int(context.old_category_id), headers=send_json_recv_json_headers)
    assert(len(r.json()["todos"]) != 0)



