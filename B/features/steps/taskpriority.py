import requests
import subprocess
import xmltodict
from behave import *

from features.steps.helper import *

@given(u'the category with title {category_title} and description {category_description}')
def step_impl(context, category_title, category_description):
        create_category = requests.post(url_category,data=json.dumps({"title": str(category_title), "description": str(category_description)}), headers=send_json_recv_json_headers)
        category_res = create_category.json()
        categories = requests.get(url_category).json()["categories"]
        context.category_id = category_res["id"]
        assert create_category.status_code == 201 and category_res in categories

@when(u'a user links a task to a category')
def step_impl(context):
        task = {
            "id": context.task_id
        }
        r = requests.post("http://localhost:4567/categories/%d/todos" % int(context.category_id), data=json.dumps(task), headers=send_json_recv_json_headers)
    
        assert r.status_code == 201

@when(u'a user links the category to the given task')
def step_impl(context):
    category = {
        "id": context.category_id
    }
    r = requests.post("http://localhost:4567/todos/%d/categories" % int(context.task_id), data=json.dumps(category), headers=send_json_recv_json_headers)

    assert r.status_code == 201


@then(u'the task should be linked to the category')
def step_impl(context):
    task = {
        "id": context.task_id
    }
    modified_category = requests.get("http://localhost:4567/categories/%d" % int(context.category_id) , headers=recv_json_headers)
    modified_category_json = modified_category.json()["categories"][0]
    
    assert modified_category.status_code == 200 and "todos" in modified_category_json and task in modified_category_json["todos"]

@then(u'the category should be linked to the task')
def step_impl(context):
    category = {
        "id": context.category_id
    }
    modified_todo = requests.get("http://localhost:4567/todos/%d" % int(context.task_id) , headers=recv_json_headers)
    modified_todo_json = modified_todo.json()["todos"][0]
    
    assert modified_todo.status_code == 200 and "categories" in modified_todo_json and category in modified_todo_json["categories"]



@then(u'the category should not be linked to the task')
def step_impl(context):
    modified_todo = requests.get("http://localhost:4567/todos/%d" % int(context.task_id) , headers=recv_json_headers)
    modified_todo_json = modified_todo.json()["todos"][0]

    assert modified_todo.status_code == 200 and "categories" not in modified_todo_json

@then(u'the task should not be linked to the category')
def step_impl(context):
    categories = requests.get("http://localhost:4567/categories/%d" % int(context.category_id) , headers=recv_json_headers)
    categories_json = categories.json()["categories"][0]
    
    assert categories.status_code == 200 and "todos" not in categories_json

@when(u'a user links an invalid category with {wrong_category_id} to the given task')
def step_impl(context, wrong_category_id):
    category = {
        "id": wrong_category_id
    }
    r = requests.post("http://localhost:4567/todos/%d/categories" % int(context.task_id), data=json.dumps(category), headers=send_json_recv_json_headers)
    context.r = r
    assert r.status_code == 404