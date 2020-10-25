import json

import requests

from ..headers import *

url = "http://localhost:4567/todos"

# post data
todo_data = json.dumps({
    "title": "bore et dolore magna",
    "doneStatus": False,
    "description": "it amet, consectetur"
})

todo_data2 = json.dumps({
  "title": "New todo",
  "doneStatus": False,
  "description": "For /todos/:id/tasksof"
})

todo_data3 = json.dumps({
  "title": "New todo for category",
  "doneStatus": False,
  "description": "For /todos/:id/categories"
})

todo_put_data = json.dumps({
  "title": "Put change",
  "doneStatus": True,
  "description": "YOLO"
})



#######################
###     /todos      ###
#######################

def test_get_todos():
    r = requests.get(url, headers=recv_json_headers)
    assert r.status_code == 200 and "todos" in r.json()

def test_head_todos():
    r = requests.head(url)
    r_todos = requests.get(url, headers=recv_json_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_json_json():
    r = requests.post(url,data=todo_data, headers=send_json_recv_json_headers)
    res = r.json()
    todos = requests.get(url).json()["todos"]
    assert r.status_code == 201 and res in todos
    # NOTE: potential vulnerability, False in Python and "false" in Java, boolean conversion is vulnerable

def test_post_todos_json_xml():
    r = requests.post(url,data=todo_data, headers=send_json_recv_xml_headers)
    res = r.text
    todos = requests.get(url,headers=recv_xml_headers).text
    assert r.status_code == 201 and res in todos

#######################
###   /todos/:id    ###
#######################

url_id = "http://localhost:4567/todos/%d"

def test_get_todos_id():
    r = requests.get(url_id % 1, headers=recv_json_headers)
    todo = r.json()
    # make sure only one id object is returned
    assert r.status_code == 200 and "todos" in todo and len(todo["todos"]) == 1

def test_head_todos_id():
    r = requests.head(url_id % 1, headers=recv_json_headers)
    r_todos = requests.get(url_id % 1, headers=recv_json_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_id():
    """ Amend a specific instances of todo using a id with a body containing the fields to amend  """
    r = requests.post(url_id % 1, data=todo_data, headers=send_json_recv_json_headers)
    res = r.json()
    todo = requests.get(url_id % 1, headers=recv_json_headers).json()["todos"][0]
    assert r.status_code == 200 and res == todo

def test_put_todos_id():
    r = requests.put(url_id % 2,data=todo_put_data, headers=send_json_recv_json_headers)
    res = r.json()
    todo = requests.get(url_id % 2, headers=recv_json_headers).json()["todos"][0]
    assert r.status_code == 200 and res == todo
    # NOTE: potential vulnerability, False in Python and "false" in Java, boolean conversion is vulnerable

def test_delete_todos_id():
    deleted_todo = requests.get(url_id % 2, headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_id % 2, headers=send_json_recv_json_headers)
    todos = requests.get(url, headers=recv_json_headers).json()["todos"]
    assert r.status_code == 200 and deleted_todo not in todos

###############################
###   /todos/:id/tasksof    ###
###############################

url_id_tasksof = "http://localhost:4567/todos/%d/tasksof"

def test_get_todos_id_tasksof():
    """ Return all the project items related to todo, with given id, by the relationship named tasksof """
    r = requests.get(url_id_tasksof % 1, headers=recv_json_headers)
    assert r.status_code == 200 and "projects" in r.json()

def test_head_todos_id_tasksof():
    r = requests.head(url_id_tasksof % 1, headers=recv_json_headers)
    r_todos = requests.get(url_id_tasksof % 1, headers=recv_json_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_id_tasksof():
    """ Create an instance of a relationship named tasksof between todo instance :id and the project instance represented by the id in the body of the message  """

    # first create a new todo
    r = requests.post(url,data=todo_data2, headers=send_json_recv_json_headers)
    todo = r.json()
    todo_id = int(todo["id"])

    # create project
    project = {
        "id": "1"
    }

    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_id_tasksof % todo_id, data=json.dumps(project), headers=send_json_recv_json_headers)

    # verify that we created a tasksof relationship with "id" == 1
    modified_todo = requests.get(url_id % todo_id , headers=recv_json_headers).json()["todos"][0]

    assert r.status_code == 201 and "tasksof" in modified_todo and project in modified_todo["tasksof"]

###################################
###   /todos/:id/tasksof/:id    ###
###################################

url_id_tasksof_delete = "http://localhost:4567/todos/%d/tasksof/%d"

def test_delete_todos_id_tasksof():
    """ Delete the instance of the relationship named tasksof between todo and project using the :id  """
    original_todo = requests.get(url_id % 2 , headers=recv_json_headers).json()["todos"][0]

    r = requests.delete(url_id_tasksof_delete % (int(original_todo["id"]), 1), headers=send_json_recv_json_headers)

    # verify that we created a tasksof relationship has been deleted
    modified_todo = requests.get(url_id % int(original_todo["id"]) , headers=recv_json_headers).json()["todos"][0]

    assert r.status_code == 200 and "tasksof" not in modified_todo and "tasksof" in original_todo

##################################
###   /todos/:id/categories    ###
##################################

url_id_categories = "http://localhost:4567/todos/%d/categories"

def test_get_todos_id_categories():
    """ Return all the category items related to todo, with given id, by the relationship named categories """
    r = requests.get(url_id_categories % 1, headers=recv_json_headers)
    assert r.status_code == 200 and "categories" in r.json() # validate that attribute categories is in response

def test_head_todos_id_categories():
    r = requests.head(url_id_categories % 1, headers=recv_json_headers)
    r_todos = requests.get(url_id_categories % 1, headers=recv_json_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_id_categories():
    """ Create an instance of a relationship named categories between todo instance :id and the category instance represented by the id in the body of the message  """

    # first create a new todo
    r = requests.post(url,data=todo_data3, headers=send_json_recv_json_headers)
    todo = r.json()
    todo_id = int(todo["id"])

    # create project
    category = {
        "id": "1"
    }

    # create a relationship between todo instance we just created and the project instance represented by the id in the body of the message
    r = requests.post(url_id_categories % todo_id, data=json.dumps(category), headers=send_json_recv_json_headers)

    # verify that we created a categories relationship with "id" == 1
    modified_todo = requests.get(url_id % todo_id , headers=recv_json_headers).json()["todos"][0]

    assert r.status_code == 201 and "categories" in modified_todo and category in modified_todo["categories"]


######################################
###   /todos/:id/categories/:id    ###
######################################

url_id_categories_delete = "http://localhost:4567/todos/%d/categories/%d"

def test_delete_todos_id_categories():
    """ Delete the instance of the relationship named categories between todo and category using the :id  """
    original_todo = requests.get(url_id % 1 , headers=recv_json_headers).json()["todos"][0]

    r = requests.delete(url_id_categories_delete % (int(original_todo["id"]), 1), headers=send_json_recv_json_headers)

    # verify that we created a categories relationship has been deleted
    modified_todo = requests.get(url_id % int(original_todo["id"]) , headers=recv_json_headers).json()["todos"][0]

    assert r.status_code == 200 and "categories" not in modified_todo and "categories" in original_todo

