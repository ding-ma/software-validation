import requests

from .category_test_data import *
from ..headers import *


# /categories

def test_get_categories(app):
    resp = requests.get(url_category, headers=recv_json_headers)
    assert resp.status_code == 200 and "categories" in resp.json()


def test_head_categories(app):
    resp = requests.head(url_category, headers=recv_json_headers)
    assert resp.status_code == 200 and not resp.content


def test_post_category(app):
    resp = requests.post(url_category, headers=recv_json_headers, json=category_create_json)
    categories = requests.get(url_category, headers=recv_json_headers)
    assert resp.status_code == 201 and len(categories.json()['categories']) == 3


# /categories/:id

def test_get_category_id(app):
    r = requests.get(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['categories']) == 1


def test_get_category_id_not_exist(app):
    r = requests.get(url_category + "/100", headers=recv_json_headers)
    assert r.status_code == 404


def test_head_category_id(app):
    r = requests.head(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_head_category_id_not_exist(app):
    r = requests.head(url_category + "/100", headers=recv_json_headers)
    assert r.status_code == 404 and not r.content


def test_post_category_id(app):
    category_create_json['title'] = 'new title'
    r = requests.post(url_category + "/1", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 200 and r.json()['title'] == category_create_json['title']


def test_post_category_id_not_exist(app):
    r = requests.post(url_category + "/100", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 404


def test_post_category_no_body_field_json(app):
    r = requests.post(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 200 and "Office" in r.text


def test_post_category_no_body_field_json_null_entry(app):
    category_create_tmp = category_create_json
    category_create_tmp['title'] = None
    r = requests.post(url_category + "/1", headers=recv_json_headers, json=category_create_tmp)
    assert r.status_code == 200 and "Office" in r.text and "some description" in r.text


def test_put_category_id(app):
    category_create_json['title'] = 'new title'
    r = requests.put(url_category + "/1", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 200 and r.json()['title'] == category_create_json['title']


def test_put_category_id_not_exist(app):
    r = requests.put(url_category + "/100", headers=recv_json_headers, json=category_create_json)
    assert r.status_code == 404


def test_put_category_no_body_field_json(app):
    r = requests.put(url_category + "/1", headers=recv_json_headers)
    assert r.status_code == 400 and "title : field is mandatory" in r.text

def test_delete_category_id(app):
    r = requests.delete(url_category + "/1")
    assert r.status_code == 200


def test_category_category_no_exist_id(app):
    r = requests.delete(url_category + "/100")
    assert r.status_code == 404


# /categories/:id/todos
def test_get_category_task(app):
    r = requests.get(url_category + "/1/todos", headers=recv_json_headers)
    assert r.status_code == 200 and len(r.json()['todos']) == 0


def test_head_category_task(app):
    r = requests.head(url_category + "/1/todos", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_post_category_task(app):
    r = requests.post(url_category + "/1/todos", headers=recv_json_headers, json={"id": "1"})
    assert r.status_code == 201


def test_delete_category_task(app):
    r = requests.post(url_category + "/1/todos", headers=recv_json_headers, json={"id": "1"})
    r = requests.delete(url_category + "/1/todos/1", headers=recv_json_headers)
    assert r.status_code == 200


def test_get_category_projects(app):
    r = requests.get(url_category + "/1/projects", headers=recv_json_headers)
    assert r.status_code == 200 and r.json()['projects'] == []


def test_head_category_projects(app):
    r = requests.head(url_category + "/1/projects", headers=recv_json_headers)
    assert r.status_code == 200 and not r.content


def test_post_category_projects(app):
    r = requests.post(url_category + "/1/projects", headers=recv_json_headers, json={"id": "1"})
    testIfPosted = requests.get(url_category + "/1/projects", headers=recv_json_headers)
    assert r.status_code == 201 and len(testIfPosted.json()['projects']) == 1


def test_delete_category_projects(app):
    r = requests.delete(url_category + "/1/projects/1")
    assert r.status_code == 404 and "Could not find any instances with categories" in r.text
