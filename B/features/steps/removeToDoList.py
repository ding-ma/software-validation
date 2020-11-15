import requests
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