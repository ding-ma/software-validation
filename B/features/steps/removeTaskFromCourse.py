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
    context.new_todos = new_todos
    for todo in new_todos:
        assert r.status_code == 200 and not (
                todo['title'] == deleted_todo['title'] and
                todo['completed'] == deleted_todo['completed'] and
                todo['active'] == deleted_todo['active'] and
                todo['description'] == deleted_todo['description']
        )


@then("the task should not be contained")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    r = requests.get(url_project)
    tasks = r.json()
    not_exist_task = context.task
    for task in tasks['projects']:
        assert r.status_code == 200 and not (
                task['title'] == not_exist_task['title'] and
                task['completed'] == not_exist_task['completed'] and
                task['active'] == not_exist_task['active'] and
                task['description'] == not_exist_task['description']
        )


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
