import requests
from behave import *

from features.steps.helper import *

@when("a user removes that task from the course to do list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    # delete this todo
    deleted_todo = requests.get(url_todo_id % int(context.task['id']), headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_todo_id % int(context.task['id']), headers=send_json_recv_json_headers)
    new_todos = requests.get(url_todo).json()["todos"]
    context.deleted_task = deleted_todo
    assert r.status_code == 200 and deleted_todo not in new_todos

@then("the task should no longer be contained in the todo list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.project = requests.get(url_project_id % int(context.project["id"]), headers=send_json_recv_json_headers).json()["projects"][0]
    assert context.project.get("tasks") == None


@when("a user removes a nonexisting task from the course to do list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    not_existing_task = {
        "id":"12345",
        "title": "random",
         "description": "not existing",
         "doneStatus": False}
    
    # create the link with course to do list 
    r = requests.delete(url_todo_id % int(not_existing_task['id']), headers=send_json_recv_json_headers)
    context.error_request = r.json()
    assert r.status_code == 404
