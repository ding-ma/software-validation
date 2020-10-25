
# from ..headers import *
# import requests
# import json


# url = "http://localhost:4567/todos"


# def test_post_todos_empty_data():
#     r = requests.post(url)
#     # must return an error message saying that the "title" field is required in a post request
#     assert r.status_code == 400 and "title : field is mandatory" in r.json()["errorMessages"]
# # # todo validate for any side effect



######################################
###   wrong ones (change this name)    ###
######################################

# forget to put an id: /todos/categories test no ide before category and no id after category
# forget to put an id: /todos/tasksof test no ide before tasksof and no id after tasksof
# /todo
# /categories
# ...
# "we should be able to create todo without a ID using the field values in the body of the messag" try one iwth ID
missing some id ? 
# delete something that is already deleted
#######################
###     /todos      ###
#######################

#######################
###   /todos/:id    ###
#######################

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



