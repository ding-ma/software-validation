import json

import requests
import xmltodict

from ..headers import *

url = "http://localhost:4567/projects"

project_create = """<project>
  <active>true</active>
  <description>t enim ad minim veni</description>
  <id>1</id>
  <completed>true</completed>
  <title>incididunt ut labora</title>
</project>
"""

project_create_invalid_id = """<project>
  <active>true</active>
  <description>t enim ad minim veni</description>
  <id>100</id>
  <completed>true</completed>
  <title>incididunt ut labora</title>
</project>
"""

project_create_null_id = """<project>
  <active>true</active>
  <description>t enim ad minim veni</description>
  <id>null</id>
  <completed>true</completed>
  <title>incididunt ut labora</title>
</project>
"""


def xml_to_dict(xml):
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d['project'] = d['projects']['project']
    return d


#####
# None of the tests with xml that takes in a body works.
# They return error code 40X
#####
def test_get_projects(app):
    resp = requests.get(url, headers=recv_xml_headers)
    d = xml_to_dict(resp.text)
    assert resp.status_code == 200 and "projects" in d


# THIS IS A TEST THAT DOES NOT WORK BUT IT SHOULD
def test_post_project(app):
    resp = requests.post(url, headers=recv_xml_headers, json=project_create)
    print(resp.text, resp.status_code)
    assert resp.status_code == 400 and "java.lang.IllegalStateException" in resp.text


def test_post_project_id(app):
    r = requests.post(url + "/1", headers=recv_xml_headers, json=project_create)
    assert r.status_code == 400 and "java.lang.IllegalStateException" in r.text


def test_post_project_id_not_exist(app):
    r = requests.post(url + "/100", headers=recv_xml_headers, json=project_create_invalid_id)
    assert r.status_code == 404


def test_post_project_no_body_field_xml(app):
    r = requests.post(url + "/1", headers=recv_xml_headers)
    assert r.status_code == 200


def test_put_project(app):
    r = requests.put(url + "/1", headers=recv_xml_headers, json=project_create)
    assert r.status_code == 400


def test_post_project_task(app):
    r = requests.post(url + "/1/tasks", headers=recv_xml_headers, json=project_create)
    assert r.status_code == 400


def test_post_project_categories(app):
    r = requests.post(url + "/1/categories", headers=recv_json_headers, json=project_create)
    assert r.status_code == 400
