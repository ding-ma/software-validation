import requests

from .category_test_data import *
from ..headers import *


def test_get_category_id_not_exist(app):
    r = requests.get(url_category + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_category_id_not_exist(app):
    r = requests.head(url_category + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_category_id_not_exist(app):
    r = requests.post(url_category + "/100", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 404


def test_post_category_no_body_field_json(app):
    r = requests.post(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and "Office" in r.text


def test_put_category_id_not_exist(app):
    r = requests.put(url_category + "/100", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 404


def test_put_category_no_body_field_json(app):
    r = requests.put(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 400

    
def test_put_category_no_body_field_json_null_entry(app):
    category_create_tmp = category_create_json
    category_create_tmp['title'] = "rand"
    r = requests.put(url_category + "/1", headers=recv_json_headers, json=category_create_tmp)
    assert r.status_code == 200 and r.json()['title'] == "rand" and r.json()['description'] == "some description"


def test_delete_category_exist_id(app):
    r = requests.delete(url_category + "/1")
    assert r.status_code == 200


def test_delete_category__no_exist_id(app):
    r = requests.delete(url_category + "/100")
    assert r.status_code == 404


def test_delete_category_task_wrong_ids(app):
    r = requests.delete(url_category + "/100/tasks/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_get_category_projects_wrong_id(app):
    r = requests.get(url_category + "/100/categories", headers=recv_json_headers)
    assert r.status_code == 404


def test_post_category_projects(app):
    r = requests.post(url_category + "/100/categories", headers=recv_json_headers, json={"id": "100"})
    assert r.status_code == 404


def test_post_category_projects_id_as_int(app):
    r = requests.post(url_category + "/100/categories", headers=recv_json_headers, json={"id": 100})
    assert r.status_code == 404


def test_delete_category_projects_wrong_ids(app):
    r = requests.delete(url_category + "/100/categories/100")
    assert r.status_code == 404
