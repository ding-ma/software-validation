import json

import requests
import xmltodict

from .category_test_data import *
from ..headers import *

#####
# None of the tests with xml that takes in ID in body work.
# The ID is read as int not string
# Returns error code 40X
#####

def xml_to_dict(xml):
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    print("neeeeeed")
    print(d)
    d['category'] = d['categories']['category']
    return d

def test_get_categories(app):
    resp = requests.get(url_category, headers=recv_xml_headers)
    d = xml_to_dict(resp.text)
    assert resp.status_code == 200 and "categories" in d

def test_post_category(app):
    r = requests.post(url_category, headers=recv_xml_headers, json=category_create_xml)
    assert r.status_code == 400

def test_post_categories_id_not_exist(app):
    r = requests.post(url_category + "/100", headers=recv_xml_headers, json=category_create_xml)
    assert r.status_code == 404


def test_post_category_no_body_field_xml(app):
    r = requests.post(url_category + "/1", headers=recv_xml_headers)
    assert r.status_code == 200


def test_put_category(app):
    r = requests.put(url_category + "/1", headers=recv_xml_headers, json=category_create_xml)
    assert r.status_code == 400


def test_post_category_todo(app):
    r = requests.post(url_category + "/1/todos", headers=recv_xml_headers, json=category_create_xml)
    assert r.status_code == 400


def test_post_category_projects(app):
    r = requests.post(url_category + "/1/projects", headers=recv_json_headers, json=category_create_xml)
    assert r.status_code == 400
