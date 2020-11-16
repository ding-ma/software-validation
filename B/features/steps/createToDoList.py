import requests
from behave import *

from features.steps.helper import *


@when(u'a user creates the following course to do list')
def step_impl(context):
    for row in context.table:
        # create the todo
        create_project = requests.post(url_project, data=json.dumps(
            {
                "completed": True if row["project_completed"] == "True" else False,
                "active": True if row["project_active"] == "True" else False,
                "title": row['project_title'],
                "description": row["project_description"]
            }), headers=send_json_recv_json_headers)
        project_res = create_project.json()
        projects = requests.get(url_project).json()["projects"]
        assert create_project.status_code == 201 and project_res in projects


@then(u'the projects should contain')
def step_impl(context):
    projects = requests.get(url_project).json()["projects"]
    for row in context.table:
        # create the project
        project = {
            "id": row['project_id'],
            "title": row['project_title'],
            "completed": "true" if row["project_completed"] == "True" else "false",
            "active": "true" if row["project_active"] == "True" else "false",
            "description": row["project_description"]}
        result = [_["id"] == project["id"] and _["title"] == project["title"] and _["description"] == project[
            "description"] and _["completed"] == project["completed"] and _["active"] == project["active"] for _ in
                  projects]
        assert any(result)


@when(u'a user creates the following course to do list with an id')
def step_impl(context):
    for row in context.table:
        # create the todo
        create_project = requests.post(url_project, data=json.dumps(
            {
                "id": row["project_id"],
                "completed": True if row["project_completed"] == "True" else False,
                "active": True if row["project_active"] == "True" else False,
                "title": row['project_title'],
                "description": row["project_description"]
            }), headers=send_json_recv_json_headers)
        project_res = create_project.json()
        projects = requests.get(url_project).json()["projects"]
        assert create_project.status_code == 400 and 'errorMessages' in project_res


@given(
    u'the a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}')
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """

    projects = requests.get(url_project)
    assert projects.status_code == 200 and project_title not in projects
    context.projects = projects


@when(
    "a user creates a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
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
            "completed": bool(project_completed),
            "active": bool(project_active),
            "title": project_title,
            "description": project_description
        }), headers=send_json_recv_json_headers)
    project_res = create_project.json()
    projects = requests.get(url_project).json()["projects"]
    context.project_res = project_res
    assert create_project.status_code == 201 and project_res in projects


@then(
    "the projects should a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    projects = requests.get(url_project)
    assert projects.status_code == 200 and context.project_res in projects.json()['projects']


@then(
    "the projects should not contain a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    projects = requests.get(url_project)
    assert projects.status_code == 200 and context.project_res not in projects.json()['projects']


@when(
    "a user creates a project without a title, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    create_project = requests.post(url_project, data=json.dumps(
        {
            "id": 1,
            "completed": bool(project_active),
            "active": bool(project_completed),
            "description": project_description
        }), headers=send_json_recv_json_headers)
    project_res = create_project.json()
    projects = requests.get(url_project).json()["projects"]
    context.project_res = project_res
    assert create_project.status_code == 400 and 'errorMessages' in project_res
