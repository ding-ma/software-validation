import requests

from .project_test_data import *
from ..headers import *


# /projects

def test_get_projects(app):
    resp = requests.get(url_project, headers=recv_json_headers)
    assert resp.status_code == 200 and "projects" in resp.json()


def test_head_projects(app):
    resp = requests.head(url_project, headers=recv_json_headers)
    assert resp.status_code == 200 and not resp.content


def test_post_project(app):
    resp = requests.post(url_project, headers=recv_json_headers, json=project_create_json)
    projects = requests.get(url_project, headers=recv_json_headers)
    assert resp.status_code == 201 and len(projects.json()['projects']) == 2


# /projects/:id

def test_get_project_id(app):
    r = requests.get(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['projects']) == 1


def test_get_project_id_not_exist(app):
    r = requests.get(url_project + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_project_id(app):
    r = requests.head(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_head_project_id_not_exist(app):
    r = requests.head(url_project + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_project_id(app):
    project_create_json['title'] = 'new title'
    r = requests.post(url_project + "/1", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 200 and r.json()['title'] == project_create_json['title']


def test_post_project_id_not_exist(app):
    r = requests.post(url_project + "/100", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 404


def test_post_project_no_body_field_json(app):
    r = requests.post(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and "Office Work" in r.text


def test_post_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create_json
    project_create_tmp['title'] = None
    r = requests.post(url_project + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and "Office Work" in r.text and "some description" in r.text


def test_put_project_id(app):
    project_create_json['title'] = 'new title'
    r = requests.put(url_project + "/1", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 200 and r.json()['title'] == project_create_json['title']


def test_put_project_id_not_exist(app):
    r = requests.put(url_project + "/100", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 404


def test_put_project_no_body_field_json(app):
    r = requests.put(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == ""


def test_put_project_no_body_field_null_entry(app):
    project_create_tmp = project_create_json
    project_create_tmp['title'] = None
    r = requests.put(url_project + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == "some description"


def test_delete_project_id(app):
    r = requests.delete(url_project + "/1")
    assert r.status_code == 200


def test_delete_project_no_exist_id(app):
    r = requests.delete(url_project + "/100")
    assert r.status_code == 404


# /projects/:id/tasks
def test_get_project_task(app):
    r = requests.get(url_project + "/1/tasks", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['todos']) == 2


def test_head_project_task(app):
    r = requests.head(url_project + "/1/tasks", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_post_project_task(app):
    r = requests.post(url_project + "/1/tasks", headers=recv_json_headers, json={"id": "1"})
    assert r.status_code == 201


def test_delete_project_task(app):
    r = requests.delete(url_project + "/1/tasks/1", headers=recv_json_headers)
    assert r.status_code == 200


def test_get_project_categories(app):
    r = requests.get(url_project + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['categories'] == []


def test_head_project_categories(app):
    r = requests.head(url_project + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_post_project_categories(app):
    r = requests.post(url_project + "/1/categories", headers=recv_json_headers, json={"id": "1"})
    testIfPosted = requests.get(url_project + "/1/categories", headers=recv_json_headers)
    assert r.status_code == 201 and len(testIfPosted.json()['categories']) == 1


def test_delete_project_categories(app):
    r = requests.delete(url_project + "/1/categories/1")
    assert r.status_code == 404 and "Could not find any instances with projec" in r.text
