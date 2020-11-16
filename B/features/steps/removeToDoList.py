import requests
from behave import *

from features.steps.helper import *


@when(u'a user removes the following course to do list')
def step_impl(context):
    projects = requests.get(url_project).json()["projects"]
    for row in context.table:
        for project in projects:
            if row["project_id"] == project["id"] and row["project_title"] == project["title"] and row[
                "project_description"] == project["description"] and process_bool(row["project_active"]) == project[
                "active"] and process_bool(row["project_completed"]) == project["completed"]:
                # delete this project
                deleted_project = \
                    requests.get(url_project_id % int(project["id"]), headers=recv_json_headers).json()["projects"][0]
                r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
                new_projects = requests.get(url_project).json()["projects"]

                assert r.status_code == 200 and deleted_project not in new_projects and len(new_projects) == len(
                    projects) - 1


@when(u'a user removes the following course to do list which is nonexistent')
def step_impl(context):
    projects = requests.get(url_project).json()["projects"]
    for row in context.table:
        project = {"id": row["project_id"],
                   "title": row["project_title"],
                   "description": row["project_description"],
                   "active": process_bool(row["project_active"]),
                   "completed": process_bool(row["project_completed"])
                   }

        # delete this project
        r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
        new_projects = requests.get(url_project).json()[
            "projects"]  # validate that there was no side effects and it didn't change the existing projects.

        assert project not in projects and r.status_code == 404 and len(new_projects) == len(projects)


@given(
    "an existing project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    create_project = requests.post(url_project, data=json.dumps(
        {
            "completed": to_bool(project_completed),
            "active": to_bool(project_active),
            "title": project_title,
            "description": project_description
        }), headers=send_json_recv_json_headers)
    project_res = create_project.json()
    projects = requests.get(url_project).json()["projects"]
    context.project = project_res
    assert create_project.status_code == 201 and project_res in projects


@when(
    "a user removes that project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    projects = requests.get(url_project).json()["projects"]
    project = {"id": context.project["id"],
               "title": context.project["title"],
               "description": context.project["description"],
               "active": process_bool(context.project["active"]),
               "completed": process_bool(context.project["completed"])
               }

    deleted_project = requests.get(url_project_id % int(project["id"]), headers=recv_json_headers).json()["projects"][0]
    r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
    new_projects = requests.get(url_project).json()["projects"]
    context.projects = new_projects
    assert r.status_code == 200 and deleted_project not in new_projects and len(new_projects) == len(projects) - 1


@then("the projects should not be contained")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.project not in context.projects


@given(
    "an non existing project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """

    context.project = {
        "id": 200,
        "completed": bool(project_completed),
        "active": bool(project_active),
        "title": project_title,
        "description": project_description
    }
    projects = requests.get(url_project)
    assert context.project not in projects.json() and projects.status_code == 200


@when("a user removes a non existing project")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    projects = requests.get(url_project).json()["projects"]
    project = context.project

    # delete this project
    r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
    new_projects = requests.get(url_project).json()[
        "projects"]  # validate that there was no side effects and it didn't change the existing projects.
    context.projects = new_projects
    assert project not in projects and r.status_code == 404 and len(new_projects) == len(projects)


@step(
    "the a non existing task with title {task_title}, description {task_description} and done status {task_doneStatus}")
def step_impl(context, task_title, task_description, task_doneStatus):
    """
    :type context: behave.runner.Context
    :type task_title: str
    :type task_description: str
    :type task_doneStatus: str
    """
    context.task = {
        "id": 200,
        "title": task_title,
        "description": task_description,
        "active": bool(task_doneStatus)
    }
    todos = requests.get(url_todo)

    assert context.tas not in todos.json() and todos.status_code == 200
