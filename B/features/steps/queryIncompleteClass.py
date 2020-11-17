import requests
import subprocess
import xmltodict
from behave import *

from features.steps.helper import *

@given(u'a task with description {task_description}, task {task_title}, and done status {task_doneStatus} linked to project with title {project_title}, done status {project_completed}, active status {project_active} and description {project_description}')
def step_impl(context, task_title, task_description, task_doneStatus, project_title, project_completed, project_active, project_description):
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
        
        # Create old project
        create_project = requests.post(url_project,data=json.dumps({"title": str(project_title), "description": str(project_description)}), headers=send_json_recv_json_headers)
        project_res = create_project.json()
        projects = requests.get(url_project).json()["projects"]
        context.old_project_id = project_res["id"]

        # Link them
        task = {
            "id": context.task_id
        }
        r = requests.post("http://localhost:4567/projects/%d/tasks" % int(context.old_project_id), data=json.dumps(task), headers=send_json_recv_json_headers)
        assert create_todo.status_code == 201 and todo_res in todos and create_project.status_code == 201 and project_res in projects and r.status_code == 201

@given(u'a complete task with title {task_title}, description {task_description} linked to project')
def step_impl(context, task_title, task_description):
    # Create task 
    create_todo = requests.post(url_todo,data=json.dumps({"title": str(task_title), "description": str(task_description), "doneStatus": True } ), headers=send_json_recv_json_headers)
    todo_res = create_todo.json()
    todos = requests.get(url_todo).json()["todos"]
    context.complete_task_id = todo_res["id"]
    context.complete_task_title = todo_res["title"]
    context.complete_task = todo_res
    assert create_todo.status_code == 201 and todo_res in todos

    # Link to project
    task = {
        "id": context.complete_task_id
    }
    r = requests.post("http://localhost:4567/projects/%d/tasks" % int(context.old_project_id), data=json.dumps(task), headers=send_json_recv_json_headers)
    assert r.status_code == 201

@then(u'only incomplete task for class should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/projects/%d/tasks?doneStatus=false" % int(context.old_project_id), headers=send_json_recv_json_headers)
    assert(r.json()["todos"][0]["doneStatus"] == "false")

@then(u'no tasks for class should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/projects/%d/tasks?doneStatus=false" % int(context.old_project_id), headers=send_json_recv_json_headers)
    assert(len(r.json()["todos"]) == 0)

@then(u'tasks for class should be returned')
def step_impl(context):
    r = requests.get("http://localhost:4567/projects/%d/tasks" % int(context.old_project_id), headers=send_json_recv_json_headers)
    assert(len(r.json()["todos"]) != 0)



