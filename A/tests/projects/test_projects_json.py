import requests

from ..headers import *

url = "http://localhost:4567/projects"

project_create = {
    "title": "sometitle",
    "completed": True,
    "active": False,  # todo this is a bug from docs
    "description": "some description"
}


# /projects

def test_get_projects(app):
    resp = requests.get(url, headers=recv_json_headers)
    assert resp.status_code == 200 and "projects" in resp.json()


def test_head_projects(app):
    resp = requests.head(url, headers=recv_json_headers)
    assert resp.status_code == 200 and not resp.content


def test_post_project(app):
    resp = requests.post(url, headers=recv_json_headers, json=project_create)
    projects = requests.get(url, headers=recv_json_headers)
    assert resp.status_code == 201 and len(projects.json()['projects']) == 2


# /projects/:id

def test_get_project_id(app):
    r = requests.get(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['projects']) == 1


def test_get_project_id_not_exist(app):
    r = requests.get(url + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_project_id(app):
    r = requests.head(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_head_project_id_not_exist(app):
    r = requests.head(url + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_project_id(app):
    project_create['title'] = 'new title'
    r = requests.post(url + "/1", headers=recv_json_headers, json=project_create)
    assert r.status_code == 200 and r.json()['title'] == project_create['title']


def test_post_project_id_not_exist(app):
    r = requests.post(url + "/100", headers=recv_json_headers, json=project_create)
    assert r.status_code == 404


def test_post_project_no_body_field_json(app):
    r = requests.post(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and "Office Work" in r.text


def test_post_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create
    project_create_tmp['title'] = None
    r = requests.post(url + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and "Office Work" in r.text and "some description" in r.text


def test_put_project_id(app):
    project_create['title'] = 'new title'
    r = requests.put(url + "/1", headers=recv_json_headers, json=project_create)
    assert r.status_code == 200 and r.json()['title'] == project_create['title']


def test_put_project_id_not_exist(app):
    r = requests.put(url + "/100", headers=recv_json_headers, json=project_create)
    assert r.status_code == 404


def test_put_project_no_body_field_json(app):
    r = requests.put(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == ""


def test_put_project_no_body_field_null_entry(app):
    project_create_tmp = project_create
    project_create_tmp['title'] = None
    r = requests.put(url + "/1", headers=recv_json_headers, json=project_create_tmp)
    print(r.text)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == "some description"


def test_delete_project_id(app):
    r = requests.delete(url + "/1")
    assert r.status_code == 200


def test_delete_project_no_exist_id(app):
    r = requests.delete(url + "/100")
    assert r.status_code == 404


# /projects/:id/tasks
def test_get_project_task(app):
    r = requests.get(url + "/1/tasks", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['todos']) == 2


# TODO this is unexpected
def test_get_project_task_wrong_id(app):
    r = requests.get(url + "/100/tasks", headers=recv_json_headers)
    print(r.text)
    assert r.status_code == 200 and "scan paperwork" in r.text


def test_head_project_task(app):
    r = requests.head(url + "/1/tasks", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


# todo this shouldnt be passing, give nothing with 200
def test_head_project_task_wrong_id(app):
    r = requests.head(url + "/100/tasks", headers=recv_json_headers)
    assert r.status_code == 200


def test_post_project_task(app):
    r = requests.post(url + "/1/tasks", headers=recv_json_headers, json={"id": "1"})
    assert r.status_code == 201


def test_delete_project_task(app):
    r = requests.delete(url + "/1/tasks/1", headers=recv_json_headers)
    assert r.status_code == 200


def test_get_project_categories(app):
    r = requests.get(url + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['categories'] == []


def test_head_project_categories(app):
    r = requests.head(url + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_post_project_categories(app):
    r = requests.post(url + "/1/categories", headers=recv_json_headers, json={"id": "1"})
    testIfPosted = requests.get(url + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 201 and len(testIfPosted.json()['categories']) == 1


def test_delete_project_categories(app):
    r = requests.delete(url + "/1/categories/1")
    assert r.status_code == 404 and "Could not find any instances with projec" in r.text
