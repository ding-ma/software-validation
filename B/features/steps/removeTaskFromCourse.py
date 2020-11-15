import requests
from features.steps.helper import *

@when(u'a user removes the following task from the course to do list')
def step_impl(context):
    todos = requests.get(url_todo).json()["todos"]
    for row in context.table:

        for todo in todos:
            if row["task_title"] == todo["title"] and row["task_description"] == todo["description"] and row["task_doneStatus"] == todo["doneStatus"]:
              
                # delete this todo
                deleted_todo = requests.get(url_todo_id % int(todo["id"]), headers=recv_json_headers).json()["todos"][0]
                r = requests.delete(url_todo_id % int(todo["id"]), headers=send_json_recv_json_headers)
                assert r.status_code == 200 and deleted_todo not in todos

@when(u'a user removes a task that does not exist to a course todo list')
def step_impl(context):
    todos = requests.get(url_todo).json()["todos"]
    for row in context.table:
        for todo in todos:
            if row["task_title"] == todo["title"] and row["task_description"] == todo["description"] and row["task_doneStatus"] == todo["doneStatus"]:
              
                # delete this todo
                deleted_todo = requests.get(url_todo_id % int(todo["id"]), headers=recv_json_headers).json()["todos"][0]
                r = requests.delete(url_todo_id % int(todo["id"]), headers=send_json_recv_json_headers)
                assert r.status_code == 404 and "errorMessages" in r.json()
