import requests
import subprocess
import xmltodict
from behave import use_fixture
from features.steps.helper import *



@given('the following tasks and categories')
def step_impl(context):
    for row in context.table:
        requests.post(url_todo, headers=recv_json_headers)
        create_todo = requests.post(url_todo,data=json.dumps({"title": str(row['task_title']), "description": str(row["task_description"]), "doneStatus": bool(row["task_doneStatus"]) } ), headers=send_json_recv_json_headers)
        create_category = requests.post(url_category,data=json.dumps({"title": row['category_title'], "description": row["category_description"]}), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        category_res = create_category.json()
        todos = requests.get(url_todo).json()["todos"]
        categories = requests.get(url_category).json()["categories"]
        assert create_todo.status_code == 201 and todo_res in todos and create_category.status_code == 201 and category_res in categories


@when('a user links a category to the given tasks')
def step_impl(context):
    for row in context.table:
        category = {
            "id": row["category_id"]
        }
        r = requests.post("http://localhost:4567/todos/%d/categories" % int(row["task_id"]), data=json.dumps(category), headers=send_json_recv_json_headers)
    
        assert r.status_code == 201

@then('the task should be properly linked with the category')
def step_impl(context):
    for row in context.table:
        category = {
            "id": row["category_id"]
        }
        # verify that we created a categories relationship with "id" == 1
        modified_todo = requests.get("http://localhost:4567/todos/%d" % int(row["task_id"]) , headers=recv_json_headers)
        modified_todo_json = modified_todo.json()["todos"][0]
        # print(modified_todo)
        
        assert modified_todo.status_code == 200 and "categories" in modified_todo_json and category in modified_todo_json["categories"]

@then(u'the category should not be linked to any task')
def step_impl(context):
    for row in context.table:
        categories = requests.get("http://localhost:4567/categories/%d" % int(row["category_id"]) , headers=recv_json_headers)
        categories_json = categories.json()["categories"][0]
        
        assert categories.status_code == 200 and "todos" not in categories_json


@when(u'a user links a task to the given category')
def step_impl(context):
    for row in context.table:
        task = {
            "id": row["task_id"]
        }
        r = requests.post("http://localhost:4567/categories/%d/todos" % int(row["category_id"]), data=json.dumps(task), headers=send_json_recv_json_headers)
    
        assert r.status_code == 201

@then(u'the category should be properly linked to the task')
def step_impl(context):
    for row in context.table:
        task = {
            "id": row["task_id"]
        }
        # verify that we created a categories relationship with "id" == 1
        modified_category = requests.get("http://localhost:4567/categories/%d" % int(row["category_id"]) , headers=recv_json_headers)
        modified_category_json = modified_category.json()["categories"][0]
        
        assert modified_category.status_code == 200 and "todos" in modified_category_json and task in modified_category_json["todos"]




@when(u'a user links an invalid category to the given tasks')
def step_impl(context):
    for row in context.table:
        category = {
            "id": row["category_id"]
        }
        r = requests.post("http://localhost:4567/todos/%d/categories" % int(row["task_id"]), data=json.dumps(category), headers=send_json_recv_json_headers)

        # print(r.status_code)
        assert r.status_code == 404


@then(u'the task should not be linked to any category')
def step_impl(context):
    for row in context.table:
        # verify that we created a categories relationship with "id" == 1
        modified_todo = requests.get("http://localhost:4567/todos/%d" % int(row["task_id"]) , headers=recv_json_headers)
        modified_todo_json = modified_todo.json()["todos"][0]

        
        assert modified_todo.status_code == 200 and "categories" not in modified_todo_json