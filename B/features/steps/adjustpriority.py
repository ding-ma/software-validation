import requests
import subprocess
import xmltodict
from behave import *

from features.steps.helper import *
@given(u'a task with title {task_title}, description {task_description} and done status {task_doneStatus} linked to category with title {category_title} and description {category_description}')
def step_impl(context, task_title, task_description, task_doneStatus, category_title, category_description):
        # Create task
        doneStatus = True
        if task_doneStatus == "False":
            doneStatus = False
        create_todo = requests.post(url_todo,data=json.dumps({"title": str(task_title), "description": str("seeee"), "doneStatus": doneStatus } ), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        todos = requests.get(url_todo).json()["todos"]
        context.task_id = todo_res["id"]
        context.task_title = todo_res["title"]
        context.task = todo_res
        assert create_todo.status_code == 201 and todo_res in todos
        
        # Create old category
        create_category = requests.post(url_category,data=json.dumps({"title": str(category_title), "description": str(category_description)}), headers=send_json_recv_json_headers)
        category_res = create_category.json()
        categories = requests.get(url_category).json()["categories"]
        context.old_category_id = category_res["id"]
        assert create_category.status_code == 201 and category_res in categories

        # Link them
        task = {
            "id": context.task_id
        }
        r = requests.post("http://localhost:4567/categories/%d/todos" % int(context.old_category_id), data=json.dumps(task), headers=send_json_recv_json_headers)
        assert r.status_code == 201

@when(u'a user unlinks a task from old category')
def step_impl(context):
    task = {
            "id": context.task_id
    }
    r = requests.delete("http://localhost:4567/categories/%d/todos/%d" % (int(context.old_category_id), int(context.task_id)), data=json.dumps(task), headers=send_json_recv_json_headers)
    assert r.status_code == 200

@then(u'the category should not be able to be unlinked')
def step_impl(context):
    r = requests.delete("http://localhost:4567/categories/%d/todos/%d" % (int(context.category_id), int(context.task_id)), headers=send_json_recv_json_headers)
    assert r.status_code == 404