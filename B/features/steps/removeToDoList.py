import requests
from behave import *

from features.steps.helper import *

@when(u'a user removes the following course to do list')
def step_impl(context):
    projects = requests.get(url_project).json()["projects"]
    for row in context.table:
        for project in projects:
            if row["project_id"] == project["id"] and row["project_title"] == project["title"] and row["project_description"] == project["description"] and process_bool(row["project_active"]) == project["active"] and process_bool(row["project_completed"]) == project["completed"]:
              
                # delete this project
                deleted_project = requests.get(url_project_id % int(project["id"]), headers=recv_json_headers).json()["projects"][0]
                r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
                new_projects = requests.get(url_project).json()["projects"]

                assert r.status_code == 200 and deleted_project not in new_projects and len(new_projects) == len(projects) - 1


@when(u'a user removes the following course to do list which is nonexistent')
def step_impl(context):
    projects = requests.get(url_project).json()["projects"]
    print(projects)
    for row in context.table:
        project = {"id":row["project_id"],
         "title": row["project_title"],
         "description": row["project_description"],
         "active": process_bool(row["project_active"]),
         "completed": process_bool(row["project_completed"]) 
        }
              
        # delete this project
        r = requests.delete(url_project_id % int(project["id"]), headers=send_json_recv_json_headers)
        new_projects = requests.get(url_project).json()["projects"] # validate that there was no side effects and it didn't change the existing projects.
        
        assert project not in projects and r.status_code == 404 and len(new_projects) == len(projects)


@given(
    "the a project with title {project_title}, description {project_description},project status {project_status} and done status {project_completed}")
def step_impl(context, project_title, project_description, project_status, project_completed):
    """
    :type context: behave.runner.Context
    :type project_title: str
    :type project_description: str
    :type project_status: str
    :type project_completed: str
    """
    raise NotImplementedError(
        u'STEP: Given the a project with title <project_title>, description <project_description>,project status <project_status> and done status <project_completed>')


@when('a user removes "ECSE 429" from the projects')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When a user removes "ECSE 429" from the projects')


@then("the projects should contain {isContained}")
def step_impl(context, isContained):
    """
    :type context: behave.runner.Context
    :type isContained: str
    """
    raise NotImplementedError(u'STEP: Then the projects should contain <isContained>')