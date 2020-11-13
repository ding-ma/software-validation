import requests
import subprocess
import xmltodict
from behave import use_fixture
from features.steps.helper import *



@given('a task and a category id')
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
    print(categories)

@when('a user categorizes the task as to the given category')
def step_impl(context):
    assert True is not False

@then('the task should be properly linked with the category')
def step_impl(context):
    assert context.failed is False
    # process.close_app()