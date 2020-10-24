import requests
import json
import xmltodict
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

baseUrl = "http://localhost:4567/projects"
xmlHeaders = headers = {'Content-Type': 'application/xml'}
jsonProjectCreate = {
    "title": "re magna aliqua. Uta",
    "completed": True,
    "active": False,  # todo this is a bug from docs
    "description": "um dolor sit amet, c"
}

xmlProjectData = json2xml.Json2xml(readfromstring(json.dumps(jsonProjectCreate)), wrapper="project").to_xml()


# /projects

def test_get_base_projects():
    resp = requests.get(baseUrl)
    assert resp.status_code == 200 and len(resp.json()['projects']) == 1


def test_head_projects():
    resp = requests.head(baseUrl)
    assert resp.status_code == 200


def test_post_project_json():
    resp = requests.post(baseUrl, json=jsonProjectCreate)
    assert resp.status_code == 201 and jsonProjectCreate['title'] in resp.json()


def test_post_project_xml():
    resp = requests.post(baseUrl, data=xmlProjectData, headers=xmlHeaders)
    assert resp.status_code == 201


def test_get_added_projects():
    resp = requests.get(baseUrl)
    assert resp.status_code == 200


def test_head_project():
    r = requests.head(baseUrl)
    assert r.status_code == 200


# /projects/:id

def test_get_project_id():
    r = requests.get(baseUrl + "/1")


def test_get_project_id_not_exist():
    r = requests.get(baseUrl + "/100")


def test_head_project_id():
    r = requests.head(baseUrl + "/1")


def test_head_project_id_not_exist():
    r = requests.head(baseUrl + "/100")


def test_post_project_id():
    pass


def test_post_project_id_not_exist():
    pass


def test_post_project_no_body_field_json():
    pass


def test_post_project_no_body_field_json_null_entry():
    pass


def test_post_project_no_body_field_json_extra_entry():
    pass


def test_post_project_no_body_field_xml():
    pass


def test_post_project_no_body_field_xml_null_entry():
    pass


def test_post_project_no_body_field_xml_extra_entry():
    pass


def test_put_project_id():
    pass


def test_put_project_id_not_exist():
    pass


def test_put_project_no_body_field_json():
    pass


def test_put_project_no_body_field_json_null_entry():
    pass


def test_put_project_no_body_field_json_extra_entry():
    pass


def test_put_project_no_body_field_xml():
    pass


def test_put_project_no_body_field_xml_null_entry():
    pass


def test_put_project_no_body_field_xml_extra_entry():
    pass


def test_delete_project_id():
    pass


def test_delete_project_no_exist_id():
    pass


def test_delete_project_negative_id():
    pass


def test_delete_project_null_id():
    pass


def test_delete_project_json_body():
    pass


def test_delete_project_xml_body():
    pass


# /projects/:id/tasks
def get_project_task():
    pass


def get_project_wrong_id_with_good_task_id_json():
    pass


def get_project_good_id_with_wrong_task_id_json():
    pass


def get_project_wrong_id_wrong_task_id_json():
    pass


def get_project_good_id_task_id_as_int_json():
    pass


def head_project_good_id_good_task_json():
    pass


def head_project_wrong_id_good_task_json():
    pass


def head_project_good_wrong_id_json():
    pass


def head_project_good_no_body_json():
    pass


def head_project_good_id_good_task_xml():
    pass


def head_project_wrong_id_good_task_xml():
    pass


def head_project_good_wrong_id_xml():
    pass


def head_project_good_no_body_xml():
    pass


def post_project_good_id_good_json():
    pass


def post_project_good_id_bad_json():
    pass


def post_project_good_id_bad_int_json():
    pass


def post_project_bad_id_bad_json():
    pass


def post_project_bad_id_bad_int_json():
    pass


def post_project_bad_id_good_json():
    pass

def post_project_good_id_good_xml():
    pass


def post_project_good_id_bad_xml():
    pass


def post_project_good_id_bad_int_xml():
    pass


def post_project_bad_id_bad_xml():
    pass


def post_project_bad_id_bad_int_xml():
    pass


def post_project_bad_id_good_xml():
    pass
# /projects/:id/tasks/:id

def delete_project_good_id_good():
    pass

def delete_project_good_id_bad():
    pass

