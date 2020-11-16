import requests
from behave import *

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
                new_todos = requests.get(url_todo).json()["todos"]
                
                assert r.status_code == 200 and deleted_todo not in new_todos

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


@given(
    "the project with title {project_title}, description {project_completed}, complete status {project_active}, and active status {project_description}")
def step_impl(context, project_title, project_completed, project_active, project_description):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_completed: str
    :type project_active: str
    :type project_description: str
    """
    raise NotImplementedError(
        u'STEP: Given the project with title <project_title>, description <project_completed>, complete status <project_active>, and active status <project_description>')