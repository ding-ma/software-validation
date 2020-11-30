import json

import requests
import xmltodict

from .headers import *
from .projects.project_test_data import *
from .categories.category_test_data import *
from .todos.todos_data import *

""" This file evaluates any unexpected side effects with all endpoints by testing each endpoint with unexpected data. """


# NOTE: if we delete last task in a category it deletes itself (BUG)
# NOTE: if we delete last task in a project it deletes itself (BUG)

#######################
###     /todos      ###
#######################

def test_post_empty(app):
    """ Send a post request to /todos """
    r = requests.post(url_todo, data={}, headers=send_json_recv_json_headers)
    assert r.status_code == 400 and "error" in r.text


#######################
###   /todos/:id    ###
#######################

def test_get_todos_id(app):
    test_id = 0  # inexisting id, since they start at 1
    r = requests.get(url_todo_id % test_id, headers=recv_json_headers)
    assert r.status_code == 404 and "error" in r.text


def test_post_todos_id(app):
    """ Amend a specific instances of todo using a id with a body containing the fields to amend  """
    # test case without required field in body
    r = requests.post(url_todo_id % 1, headers=send_json_recv_json_headers)
    res = r.json()
    todo = requests.get(url_todo_id % 1, headers=recv_json_headers).json()["todos"][0]
    # NOTE: when sending empty data to POST /todos/:id, we don't get an error mesage and the request successful
    assert r.status_code == 200 and res == todo


def test_double_delete_todos_id(app):
    deleted_todo = requests.get(url_todo_id % 2, headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_todo_id % 2, headers=send_json_recv_json_headers)

    # try deleting it once more
    r2 = requests.delete(url_todo_id % 2, headers=send_json_recv_json_headers)

    todos = requests.get(url_todo, headers=recv_json_headers).json()["todos"]
    assert r.status_code == 200 and r2.status_code == 404 and "error" in r2.text and deleted_todo not in todos


###############################
###   /todos/:id/tasksof    ###
###############################

def test_post_todos_id_tasksof(app):
    """ Create an instance of a relationship named tasksof between todo instance :id and the project instance represented by the id in the body of the message """

    # first create a new todo
    create = requests.post(url_todo, data=todo_xml2, headers=send_xml_recv_xml_headers)
    todo = json.loads(json.dumps(xmltodict.parse(create.text)))["todo"]
    todo_id = int(todo["id"])

    # create project
    project = """<project><id>1</id></project>"""
    # NOTE: since we can't take ids in XML, this gives a BUG
    # This returns {"errorMessages": ["Could not find thing matching value for id"]}

    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_todo_id_tasksof % todo_id, data=project, headers=send_xml_recv_xml_headers)
    # NOTE: this gives us project id not found BUG not working, can't create relationships using XML, also it is not documented how the XML should be

    # verify that we created a tasksof relationship with "id" == 1
    modified_todo = requests.get(url_todo_id % todo_id, headers=recv_xml_headers).text
    # assert r.status_code == 201 and "tasksof" in modified_todo and project in modified_todo

    # failed to create relationship
    assert r.status_code == 404 and "tasksof" not in modified_todo and project not in modified_todo and "error" in r.text


###################################
###   /todos/:id/tasksof/:id    ###
###################################

def test_get_todos_tasksof(app):
    # NOTE: This is an undocumented behaviour where /todos/tasksof is redirecting us to /projects (BUG, shouldn't accept this path without :ids)
    r = requests.get("http://localhost:4567/todos/tasksof", headers=recv_json_headers)
    projects = r.json()
    # make sure only one id object is returned
    assert r.status_code == 200


##################################
###   /todos/:id/categories    ###
##################################

def test_post_todos_id_categories(app):
    """ Create an instance of a relationship named categories between todo instance :id and the category instance represented by the id in the body of the message  """

    # first create a new todo
    create = requests.post(url_todo, data=todo_xml3, headers=send_xml_recv_xml_headers)
    todo = json.loads(json.dumps(xmltodict.parse(create.text)))["todo"]
    todo_id = int(todo["id"])

    # create project
    category = """<category><id>1</id></category>"""

    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_todo_id_categories % todo_id, data=category, headers=send_xml_recv_xml_headers)

    # verify that we created a categories relationship with "id" == 1
    modified_todo = requests.get(url_todo_id % todo_id, headers=recv_xml_headers).text

    # assert r.status_code == 201 and "categories" in modified_todo and category in modified_todo
    assert r.status_code == 404 and "categories" not in modified_todo and category not in modified_todo and "error" in r.text


######################################
###   /todos/:id/categories/:id    ###
######################################


def test_get_todos_categories(app):
    # NOTE: This is an undocumented behaviour where /todos/categories is redirecting us to /categories (BUG, shouldn't accept this path without :ids)
    r = requests.get("http://localhost:4567/todos/categories", headers=recv_json_headers)
    categories = r.json()
    # make sure only one id object is returned
    assert r.status_code == 200


######################################
###   /projects                    ###
######################################


# NOTE: this test should return error as id does not exist
def test_get_project_task_wrong_id(app):
    r = requests.get(url_project + "/100/tasks", headers=recv_json_headers)
    assert r.status_code == 200


# NOTE: this test should return error as id does not exist
def test_head_project_task_wrong_id(app):
    r = requests.head(url_project + "/100/tasks", headers=recv_json_headers)
    assert r.status_code == 200


# NOTE: The tests fails with xml body
def test_post_project_id(app):
    r = requests.post(url_project + "/1", headers=recv_xml_headers, json=project_create_xml)
    assert r.status_code == 400 and "java.lang.IllegalStateException" in r.text


def test_post_project(app):
    resp = requests.post(url_project, headers=recv_xml_headers, json=project_create_xml)
    print(resp.text, resp.status_code)
    assert resp.status_code == 400 and "java.lang.IllegalStateException" in resp.text


# NOTE: Create connection from task to category, but only shows up in 1 direction
def test_connect_categories_tasks(app):
    r = requests.post(url_todo + "/2/categories", headers=recv_json_headers, json=category_connect_todo)
    r2 = requests.get(url_todo + "/2/categories", headers=recv_json_headers)
    r3 = requests.get(url_category + "/1/todos", headers=recv_json_headers)
    assert r2.status_code == 200 and len(r2.json()['categories']) == 1 and r3.status_code == 200 and len(r3.json()['todos']) == 0
    
# NOTE: Create connection from category to task, but only shows up in 1 direction
def test_connect_tasks_categories(app):
    r = requests.post(url_category + "/1/todos", headers=recv_json_headers, json=todo_connect_category)
    r2 = requests.get(url_todo + "/2/categories", headers=recv_json_headers)
    r3 = requests.get(url_category + "/1/todos", headers=recv_json_headers)
    assert r2.status_code == 200 and len(r2.json()['categories']) == 0 and r3.status_code == 200 and len(r3.json()['todos']) == 1
    