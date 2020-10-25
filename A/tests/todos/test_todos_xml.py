import requests
import xmltodict

from .todos_data import *
from ..headers import *


def xml_to_dict_todos(xml):
    """ Help function to turn xml into a dict """
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d["todos"] = d["todos"]["todo"]
    return d


def xml_to_dict_projects(xml):
    """ Help function to turn xml into a dict """
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d["projects"] = d["projects"]["project"]
    return d

def xml_to_dict_categories(xml):    
    """ Help function to turn xml into a dict """
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d["categories"] = d["categories"]["category"]
    return d

#######################
###     /todos      ###
#######################

def test_get_todos():
    r = requests.get(url_todo, headers=recv_xml_headers)
    d = xml_to_dict_todos(r.text)
    assert r.status_code == 200 and "todos" in d


def test_get_todos_head():
    r = requests.head(url_todo, headers=recv_xml_headers)
    r_todos = requests.get(url_todo, headers=recv_xml_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_xml_json():
    """ Create existing title twice. """
    r = requests.post(url_todo, data=todo_xml, headers=send_xml_headers)
    res = r.json()
    todos_list = requests.get(url_todo).json()["todos"]
    assert r.status_code == 201 and res in todos_list
    # NOTE: difference between documented input (sample data) and actual accepted input errorMessage: "Invalid Creation: Failed Validation: Not allowed to create with id"

def test_post_todos_xml_xml():
    """ Create existing title twice. """
    r = requests.post(url_todo, data=todo_xml, headers=send_xml_recv_xml_headers)
    res = r.text
    todos = requests.get(url_todo, headers=recv_xml_headers).text
    assert r.status_code == 201 and res in todos

#######################
###   /todos/:id    ###
#######################

def test_get_todos_id():
    test_id = 1
    r = requests.get(url_todo_id % test_id, headers=recv_xml_headers)
    todo = xml_to_dict_todos(r.text)
    # make sure only one id object with 1 is returned
    assert r.status_code == 200 and "todos" in todo and int(todo["todos"]["id"]) == test_id


def test_head_todos_id():
    r = requests.head(url_todo_id % 1, headers=recv_xml_headers)
    r_todos = requests.get(url_todo_id % 1, headers=recv_xml_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_id():
    """ Amend a specific instances of todo using a id with a body containing the fields to amend  """
    r = requests.post(url_todo_id % 1, data=todo_xml, headers=send_xml_recv_xml_headers)
    res = r.text
    todo = requests.get(url_todo_id % 1, headers=recv_xml_headers).text
    assert r.status_code == 200 and res in todo

def test_put_todos_id():
    r = requests.put(url_todo_id % 1, data=todo_xml_put, headers=send_xml_recv_xml_headers)
    res = r.text
    todo = requests.get(url_todo_id % 1, headers=recv_xml_headers).text
    assert r.status_code == 200 and res in todo


def test_delete_todos_id():
    deleted_todo = requests.get(url_todo_id % 1, headers=recv_xml_headers).text
    r = requests.delete(url_todo_id % 1, headers=send_xml_recv_xml_headers)
    todos = requests.get(url_todo, headers=recv_xml_headers).text
    assert r.status_code == 200 and deleted_todo not in todos


###############################
###   /todos/:id/tasksof    ###
###############################

def test_get_todos_id_tasksof():
    """ Return all the project items related to todo, with given id, by the relationship named tasksof """
    r = requests.get(url_tod_id_tasksof % 1, headers=recv_xml_headers)
    d = xml_to_dict_projects(r.text)
    assert r.status_code == 200 and "projects" in d


def test_head_todos_id_tasksof():
    r = requests.head(url_tod_id_tasksof % 1, headers=recv_xml_headers)
    r_todos = requests.get(url_tod_id_tasksof % 1, headers=recv_xml_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

###################################
###   /todos/:id/tasksof/:id    ###
###################################

def test_delete_todos_id_tasksof():
    """ Delete the instance of the relationship named tasksof between todo and project using the :id  """
    original_todo = requests.get(url_todo_id % 2, headers=recv_xml_headers).text

    r = requests.delete(url_tod_id_tasksof_delete % (2, 1), headers=send_xml_recv_xml_headers)

    # verify that we created a tasksof relationship has been deleted
    modified_todo = requests.get(url_todo_id % 2, headers=recv_xml_headers).text

    assert r.status_code == 200 and "tasksof" not in modified_todo and "tasksof" in original_todo

##################################
###   /todos/:id/categories    ###
##################################

def test_get_todos_id_categories():
    """ Return all the category items related to todo, with given id, by the relationship named categories """
    r = requests.get(url_todo_id_categories % 1, headers=recv_xml_headers)
    d = xml_to_dict_categories(r.text)
    assert r.status_code == 200 and "categories" in d


def test_head_todos_id_categories():
    r = requests.head(url_todo_id_categories % 1, headers=recv_xml_headers)
    r_todos = requests.get(url_todo_id_categories % 1, headers=recv_xml_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content


######################################
###   /todos/:id/categories/:id    ###
######################################


def test_delete_todos_id_categories():
    """ Delete the instance of the relationship named categories between todo and category using the :id  """
    original_todo = requests.get(url_todo_id % 1, headers=recv_xml_headers).text

    r = requests.delete(url_todo_id_categories_delete % (1, 1), headers=send_xml_recv_xml_headers)

    # verify that we created a categories relationship has been deleted
    modified_todo = requests.get(url_todo_id % 1, headers=recv_xml_headers).text

    assert r.status_code == 200 and "categories" not in modified_todo and "categories" in original_todo

