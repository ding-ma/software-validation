import requests
from behave import *

from features.steps.helper import *

@when(u'a user adds a task with title {task_title}, description {task_description} and done status {task_doneStatus} to the project')
def step_impl(context,task_title, task_description, task_doneStatus):
    """
    :type context: behave.runner.Context
    :type task_title: str
    :type task_description: str
    :type task_doneStatus: str
    """
    project = {"id":context.project["id"]} 

    # create the todo
    create_todo = requests.post(url_todo, data=json.dumps(
        {"title": task_title,
         "description": task_description,
         "doneStatus": to_bool(task_doneStatus)
        }), headers=send_json_recv_json_headers)
    todo_res = create_todo.json()
    todos = requests.get(url_todo).json()["todos"]

    # create the link with ECSE 429 course project
    todo_project_relationship = requests.post(url_todo_id_tasksof % int(todo_res["id"]), data=json.dumps(project),
                                                  headers=send_json_recv_json_headers)
    todo = requests.get(url_todo_id % int(todo_res["id"])).json()["todos"][0]
    context.task = todo

    assert create_todo.status_code == 201 and todo_project_relationship.status_code == 201 and todo_res in todos 


@then(u'this task should be contained in the course to do list')
def step_impl(context):
    context.project = requests.get(url_project_id % int(context.project["id"]), headers=send_json_recv_json_headers).json()["projects"][0]
    compare = [True if task["id"] == context.task["id"] else False for task in context.project["tasks"]]
    assert any(compare) 
    
@then(u'the project should be associated to the task')
def step_impl(context):
    assert context.task["tasksof"][0]["id"] == context.project["id"]