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
    assert r.status_code == 404 and r.json()['errorMessages']


def test_post_project_no_body_field_json(app):
    r = requests.post(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['title'] == project_create['title']


def test_post_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create
    project_create_tmp['title'] = None
    r = requests.post(url + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "new title"


def test_put_project_id_not_exist(app):
    r = requests.put(url + "/100", headers=recv_json_headers, json=project_create)
    assert r.status_code == 404


def test_put_project_no_body_field_json(app):
    r = requests.put(url + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['title'] == project_create['title']


def test_put_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create
    project_create_tmp['title'] = None
    r = requests.put(url + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "new title"


def test_delete_project_no_exist_id(app):
    r = requests.delete(url + "/1")
    assert r.status_code == 404


def test_get_project_task_wrong_id(app):
    r = requests.get(url + "/100/tasks", headers=recv_json_headers)
    assert r.status_code == 404


# todo this shouldnt be passing
def test_head_project_task_wrong_id(app):
    r = requests.head(url + "/100/tasks", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_delete_project_task_wrong_ids(app):
    r = requests.delete(url + "/100/tasks/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_get_project_categories_wrong_id(app):
    r = requests.get(url + "/100/categories", headers=recv_json_headers)
    assert r.status_code == 404


def test_post_project_categories(app):
    r = requests.post(url + "/100/categories", headers=recv_json_headers, json={"id": "100"})
    assert r.status_code == 404


def test_post_project_categories_id_as_int(app):
    r = requests.post(url + "/100/categories", headers=recv_json_headers, json={"id": 100})
    assert r.status_code == 404


def test_delete_project_categories_wrong_ids(app):
    r = requests.delete(url + "/100/categories/100")
    assert r.status_code == 404
