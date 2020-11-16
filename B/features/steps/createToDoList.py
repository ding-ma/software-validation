import requests
from behave import *

from features.steps.helper import *

@given("a user creates a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
@when("a user creates a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    project =  {
            "completed": to_bool(project_completed),
            "active": to_bool(project_active),
            "title": project_title,
            "description": project_description
        }
    create_project = requests.post(url_project, data=json.dumps(project), headers=send_json_recv_json_headers)
    project_res = create_project.json()
    projects = requests.get(url_project).json()["projects"]
    context.projects = projects
    context.project = project_res
    assert create_project.status_code == 201 and project_res in projects


@then(
    "the projects should contain a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    r = requests.get(url_project)
    projects = r.json()["projects"]
    compare = [True if project_title == project["title"] and project_description == project["description"] and to_bool(project_active) == json_to_bool(project["active"]) and to_bool(project_completed) == json_to_bool(project["completed"]) else False for project in projects]
    assert r.status_code == 200 and any(compare)


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
    r = requests.get(url_project)
    projects = r.json()["projects"]
    for project in projects:
        assert r.status_code == 200 and not (project_title == project["title"] and project_description == project["description"] and to_bool(project_active) == json_to_bool(project["active"]) and to_bool(project_completed) == json_to_bool(project["completed"]))


@given(
    "there is not a project with title {project_title}, description {project_description}, complete status {project_completed} and active status {project_active}")
def step_impl(context, project_title, project_description, project_completed, project_active):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_completed: str
    :type project_active: str
    """
    r = requests.get(url_project)
    projects = r.json()["projects"]
    context.projects = projects
    for project in projects:
        assert r.status_code == 200 and not (project_title == project["title"] and project_description == project["description"] and to_bool(project_active) == json_to_bool(project["active"]) and to_bool(project_completed) == json_to_bool(project["completed"]))


@when("a user creates a project with id {id}")
def step_impl(context, id):
    """
    :type context: behave.runner.Context
    :type id: str
    """
    create_project = requests.post(url_project, data=json.dumps(
        {
            "id": id,

        }), headers=send_json_recv_json_headers)
    project_res = create_project.json()
    assert create_project.status_code == 400 and 'errorMessages' in project_res
