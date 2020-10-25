import requests

from ..headers import *

url = "http://localhost:4567/projects"

project_create = {
    "title": "sometitle",
    "completed": True,
    "active": False,  # todo this is a bug from docs
    "description": "some description"
}
project_create_bool_as_string = {
    "title": "sometitle",
    "completed": "True",
    "active": "False",
    "description": "some description"
}
# pytest tests\projects\test_projects_edge_case.py

def test_get_project_id_not_exist(app):
    r = requests.get(url + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_project_id_not_exist(app):
    r = requests.head(url + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_project_id_not_exist(app):
    r = requests.post(url + "/100", headers=recv_json_headers, json=project_create)
    assert r.status_code == 404


def test_post_project_bool_string(app):
    r = requests.post(url + "/1", headers=recv_json_headers, json=project_create_bool_as_string)
    print(r.text)
    assert r.status_code == 400 and "Failed Validation: completed should be BOOLEAN" in r.text

def test_post_project_no_body_field_json(app):
    r = requests.post(url + "/1", headers=recv_json_headers)
    print(r.text)
    assert r.status_code == 200 and "Office Work" in r.text

def test_put_project_id_not_exist(app):
    r = requests.put(url + "/100", headers=recv_json_headers, json=project_create)
    assert r.status_code == 404


def test_put_project_no_body_field_json(app):
    r = requests.put(url + "/1", headers=recv_json_headers)
    print(r.text)
    assert r.status_code == 200 and r.json()['title'] == ""


def test_put_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create
    project_create_tmp['title'] = None
    r = requests.put(url + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == "some description"


def test_delete_project_exist_id(app):
    r = requests.delete(url + "/1")
    assert r.status_code == 200


def test_delete_project__no_exist_id(app):
    r = requests.delete(url + "/100")
    assert r.status_code == 404


# TODO expected behavior
def test_get_project_task_wrong_id(app):
    r = requests.get(url + "/100/tasks", headers=recv_json_headers)
    print(r.text)
    assert r.status_code == 200 and "scan paperwork" in r.text


def test_delete_project_task_wrong_ids(app):
    r = requests.delete(url + "/100/tasks/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_get_project_categories_wrong_id(app):
    r = requests.get(url + "/100/categories", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['categories'] == []


def test_post_project_categories(app):
    r = requests.post(url + "/100/categories", headers=recv_json_headers, json={"id": "100"})
    assert r.status_code == 404


def test_post_project_categories_id_as_int(app):
    r = requests.post(url + "/100/categories", headers=recv_json_headers, json={"id": 100})
    assert r.status_code == 404


def test_delete_project_categories_wrong_ids(app):
    r = requests.delete(url + "/100/categories/100")
    assert r.status_code == 404
