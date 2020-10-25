import json

import requests
import xmltodict

from .project_test_data import *
from ..headers import *


def xml_to_dict(xml):
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d['project'] = d['projects']['project']
    return d


#####
# None of the tests with xml that takes in a body works.
# They return error code 40X
#####
def test_get_projects(app):
    resp = requests.get(url_project, headers=recv_xml_headers)
    d = xml_to_dict(resp.text)
    assert resp.status_code == 200 and "projects" in d


def test_post_project_id_not_exist(app):
    r = requests.post(url_project + "/100", headers=recv_xml_headers, json=project_create_xml_invalid_id)
    assert r.status_code == 404


def test_post_project_no_body_field_xml(app):
    r = requests.post(url_project + "/1", headers=recv_xml_headers)
    assert r.status_code == 200


def test_put_project(app):
    r = requests.put(url_project + "/1", headers=recv_xml_headers, json=project_create_xml)
    assert r.status_code == 400


def test_post_project_task(app):
    r = requests.post(url_project + "/1/tasks", headers=recv_xml_headers, json=project_create_xml)
    assert r.status_code == 400


def test_post_project_categories(app):
    r = requests.post(url_project + "/1/categories", headers=recv_json_headers, json=project_create_xml)
    assert r.status_code == 400
