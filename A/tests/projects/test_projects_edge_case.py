import requests

from .project_test_data import *
from ..headers import *


def test_get_project_id_not_exist(app):
    r = requests.get(url_project + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_project_id_not_exist(app):
    r = requests.head(url_project + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_project_id_not_exist(app):
    r = requests.post(url_project + "/100", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 404


def test_post_project_bool_string(app):
    r = requests.post(url_project + "/1", headers=recv_json_headers, json=project_create_bool_as_string)
    assert r.status_code == 400 and "Failed Validation: completed should be BOOLEAN" in r.text


def test_post_project_no_body_field_json(app):
    r = requests.post(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and "Office Work" in r.text


def test_put_project_id_not_exist(app):
    r = requests.put(url_project + "/100", headers=recv_json_headers, json=project_create_json)
    assert r.status_code == 404


def test_put_project_no_body_field_json(app):
    r = requests.put(url_project + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['title'] == ""


def test_put_project_no_body_field_json_null_entry(app):
    project_create_tmp = project_create_json
    project_create_tmp['title'] = None
    r = requests.put(url_project + "/1", headers=recv_json_headers, json=project_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "" and r.json()['description'] == "some description"


def test_delete_project_exist_id(app):
    r = requests.delete(url_project + "/1")
    assert r.status_code == 200


def test_delete_project__no_exist_id(app):
    r = requests.delete(url_project + "/100")
    assert r.status_code == 404


def test_delete_project_task_wrong_ids(app):
    r = requests.delete(url_project + "/100/tasks/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_get_project_categories_wrong_id(app):
    r = requests.get(url_project + "/100/categories", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['categories'] == []


def test_post_project_categories(app):
    r = requests.post(url_project + "/100/categories", headers=recv_json_headers, json={"id": "100"})
    assert r.status_code == 404


def test_post_project_categories_id_as_int(app):
    r = requests.post(url_project + "/100/categories", headers=recv_json_headers, json={"id": 100})
    assert r.status_code == 404


def test_delete_project_categories_wrong_ids(app):
    r = requests.delete(url_project + "/100/categories/100")
    assert r.status_code == 404
