import requests
from features.steps.helper import *

@given(u'the following projects')
def step_impl(context):
    new_project = {
        "title": "ECSE 429",
        "active": True,
        "description": "Software validation course" 
    }
    create_project = requests.post(url_project ,data=json.dumps(new_project), headers=send_json_recv_json_headers)
    r_json = create_project.json()
    projects = requests.get(url_project).json()["projects"]
    assert create_project.status_code == 201 and r_json in projects

@given(u'the following tasks in this ECSE 429 course to do list')
def step_impl(context):
    for row in context.table:
        
        # create the todo
        create_todo = requests.post(url_todo,data=json.dumps({"title": str(row['task_title']), "description": str(row["task_description"]), "doneStatus": True if row["task_doneStatus"] == "True" else False}), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        todos = requests.get(url_todo).json()["todos"]

        # create the link with ECSE 429 course project
        project = {"id": "2"}
        todo_project_relationship = requests.post(url_todo_id_tasksof % int(todo_res["id"]) ,data=json.dumps(project), headers=send_json_recv_json_headers)
        todo = requests.get(url_todo_id % int(todo_res["id"])).json()["todos"][0]
        
        # print("{} vs {} on line 31".format(todo_res["doneStatus"], bool(row["task_doneStatus"])))
        # print("{} on line 32".format(todos))
        assert create_todo.status_code == 201 and todo_res in todos and todo["tasksof"][0]["id"] == project["id"]

@when(u'a user adds the following task to the course todo list')
def step_impl(context):
     for row in context.table:
        # create the todo
        create_todo = requests.post(url_todo,data=json.dumps({"doneStatus": True if row["task_doneStatus"] == "True" else False,"title": str(row['task_title']), "description": str(row["task_description"])}), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        todos = requests.get(url_todo).json()["todos"]

        # create the link with ECSE 429 course project
        project = {"id": str(row["tasksof"])}
        todo_project_relationship = requests.post(url_todo_id_tasksof % int(todo_res["id"]) ,data=json.dumps(project), headers=send_json_recv_json_headers)
        todo = requests.get(url_todo_id % int(todo_res["id"])).json()["todos"][0]

        assert create_todo.status_code == 201 and todo_res in todos and todo["tasksof"][0]["id"] == project["id"]

@when(u'a user adds the following task to a course todo list that does not exist')
def step_impl(context):
    for row in context.table:
        # create the todo
        create_todo = requests.post(url_todo,data=json.dumps({"doneStatus": True if row["task_doneStatus"] == "True" else False,"title": str(row['task_title']), "description": str(row["task_description"])}), headers=send_json_recv_json_headers)
        todo_res = create_todo.json()
        todos = requests.get(url_todo).json()["todos"]

        # create the link with ECSE 429 course project
        project = {"id": str(row["tasksof"])}
        todo_project_relationship = requests.post(url_todo_id_tasksof % int(todo_res["id"]) ,data=json.dumps(project), headers=send_json_recv_json_headers)

        # assert failed to create relationship with non existing project.
        assert create_todo.status_code == 201 and todo_res in todos and "errorMessages" in todo_project_relationship.json()

@then(u'the tasks in the course to do list should contain')
def step_impl(context):
    todos = requests.get(url_todo).json()["todos"]
    for row in context.table:
        # create the todo
        todo = {"title": str(row['task_title']), "description": str(row["task_description"]), "doneStatus": "true" if str(row["task_doneStatus"])== "True" else "false"}
        result = [ _["title"] == todo["title"] and _["description"] == todo["description"] and _["doneStatus"] == todo["doneStatus"] for _ in todos]
        assert any(result)
