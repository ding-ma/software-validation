import requests
from behave import *

from features.steps.helper import *


@when(u'a user removes the following task from the course to do list')
def step_impl(context):
    todos = requests.get(url_todo).json()["todos"]
    for row in context.table:

        for todo in todos:
            if row["task_title"] == todo["title"] and row["task_description"] == todo["description"] and row[
                "task_doneStatus"] == todo["doneStatus"]:
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
            if row["task_title"] == todo["title"] and row["task_description"] == todo["description"] and row[
                "task_doneStatus"] == todo["doneStatus"]:
                # delete this todo
                deleted_todo = requests.get(url_todo_id % int(todo["id"]), headers=recv_json_headers).json()["todos"][0]
                r = requests.delete(url_todo_id % int(todo["id"]), headers=send_json_recv_json_headers)
                assert r.status_code == 404 and "errorMessages" in r.json()


@when("a user removes that task from the course to do list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """

    # delete this todo
    deleted_todo = requests.get(url_todo_id % int(context.task['id']), headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_todo_id % int(context.task['id']), headers=send_json_recv_json_headers)
    new_todos = requests.get(url_todo).json()["todos"]
    context.new_todos = new_todos
    assert r.status_code == 200 and deleted_todo not in new_todos


@then("the task should not be contained")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.task not in context.projects


@when("a user removes that non existing task from the course to do list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    todos = requests.get(url_todo).json()["todos"]
    todo = context.task
    # delete this todo
    deleted_todo = requests.get(url_todo_id % int(todo["id"]), headers=recv_json_headers)
    r = requests.delete(url_todo_id % int(todo["id"]), headers=send_json_recv_json_headers)
    context.new_todo = deleted_todo
    assert r.status_code == 404 and "errorMessages" in r.json() and deleted_todo.status_code == 404
