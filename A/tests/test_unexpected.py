from .headers import *
from .todos.todos_data import *
import requests
import xmltodict
import json

""" This file evaluates any unexpected side effects with all endpoints (testing endpoints with unexpected data) """

#######################
###     /todos      ###
#######################

def test_post_empty():
    """ Send a post request to /todos """
    r = requests.post(url,data={}, headers=send_json_recv_json_headers)
    assert r.status_code == 400 and "error" in r.text

#######################
###   /todos/:id    ###
#######################

def test_get_todos_id():
    test_id = 0 # inexisting id, since they start at 1
    r = requests.get(url_id % test_id, headers=recv_json_headers)
    assert r.status_code == 404 and "error" in r.text

def test_post_todos_id():
    """ Amend a specific instances of todo using a id with a body containing the fields to amend  """
    # test case without required field in body  
    r = requests.post(url_id % 1, headers=send_json_recv_json_headers) 
    res = r.json()
    todo = requests.get(url_id % 1, headers=recv_json_headers).json()["todos"][0]
    # NOTE: when sending empty data to POST /todos/:id, we don't get an error mesage and the request successful
    assert r.status_code == 200 and res == todo

def test_double_delete_todos_id(jar):
    deleted_todo = requests.get(url_id % 2, headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_id % 2, headers=send_json_recv_json_headers)

    # try deleting it once more
    r2 = requests.delete(url_id % 2, headers=send_json_recv_json_headers)

    todos = requests.get(url, headers=recv_json_headers).json()["todos"]
    assert r.status_code == 200 and r2.status_code == 404 and "error" in r2.text and deleted_todo not in todos

###############################
###   /todos/:id/tasksof    ###
###############################


def test_post_todos_id_tasksof():
    """ Create an instance of a relationship named tasksof between todo instance :id and the project instance represented by the id in the body of the message """
    
    # first create a new todo
    r = requests.post(url,data=todo_xml2, headers=send_xml_recv_xml_headers)
    todo = json.loads(json.dumps(xmltodict.parse(r.text)))["todo"]
    todo_id = int(todo["id"])

    # create project
    project = """<project><id>1</id></project>"""
    
    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_id_tasksof % todo_id, data=project, headers=send_xml_recv_xml_headers)
    # NOTE: this gives us project id not found BUG not working, can't create relationships using XML, also it is not documented how the XML should be

    # verify that we created a tasksof relationship with "id" == 1
    modified_todo = requests.get(url_id % todo_id , headers=recv_xml_headers).json()["todos"][0]
    
    assert r.status_code == 201 and "tasksof" in modified_todo and project in modified_todo

###################################
###   /todos/:id/tasksof/:id    ###
###################################

# forget to put an id: /todos/tasksof test no ide before tasksof and no id after tasksof

##################################
###   /todos/:id/categories    ###
##################################

def test_post_todos_id_categories():
    """ Create an instance of a relationship named categories between todo instance :id and the category instance represented by the id in the body of the message  """
    
    # first create a new todo
    r = requests.post(url,data=todo_xml3, headers=send_xml_recv_xml_headers)
    todo = json.loads(json.dumps(xmltodict.parse(r.text)))["todo"]
    todo_id = int(todo["id"])

    # create project
    category ="""<category>
    <id></id>
    </category>
    """
    
    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_id_categories % todo_id, data=category, headers=send_xml_recv_xml_headers)

    # verify that we created a categories relationship with "id" == 1
    modified_todo = requests.get(url_id % todo_id , headers=recv_xml_headers).text
    
    assert r.status_code == 201 and "categories" in modified_todo and category in modified_todo


######################################
###   /todos/:id/categories/:id    ###
######################################

# forget to put an id: /todos/categories test no ide before category and no id after category
