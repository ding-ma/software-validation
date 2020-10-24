from ..headers import *
import requests
import xmltodict
import json

url = "http://localhost:4567/todos"

todo_xml = """<todo>
  <doneStatus>false</doneStatus>
  <description>it amet, consectetur</description>
  <title>bore et dolore magna</title>
</todo>"""

def xml_to_dict(xml):    
    """ Help function to turn xml into a dict """
    d = json.loads(json.dumps(xmltodict.parse(xml)))
    d["todos"] = d["todos"]["todo"]
    return d

#######################
###     /todos      ###
#######################

def test_get_todos_xml():
    r = requests.get(url, headers=recv_xml_headers)
    d = xml_to_dict(r.text)
    assert r.status_code == 200 and "todos" in d

def test_get_todos_head_xml():
    r = requests.head(url, headers=recv_xml_headers)
    r_todos = requests.get(url, headers=recv_xml_headers)
    r_todos.headers.pop("date")
    r.headers.pop("date")
    # make sure HEAD does not return a message-body in the response and HTTP headers should be identical to GET 
    assert r.status_code == 200 and r.headers == r_todos.headers and not r.content

def test_post_todos_xml_json():
    """ Create existing title twice. """
    r = requests.post(url,data=todo_xml, headers=send_xml_headers)
    res = r.json()
    todos_list = requests.get(url).json()["todos"]
    assert r.status_code == 201 and res in todos_list
    # NOTE: difference between documented input (sample data) and actual accepted input errorMessage: "Invalid Creation: Failed Validation: Not allowed to create with id"

def test_post_todos_xml_xml():
    """ Create existing title twice. """
    r = requests.post(url,data=todo_xml, headers=send_xml_recv_xml_headers)
    res = r.text
    todos = requests.get(url,headers=recv_xml_headers).text
    assert r.status_code == 201 and res in todos

#######################
###   /todos/:id    ###
#######################

###############################
###   /todos/:id/tasksof    ###
###############################

###################################
###   /todos/:id/tasksof/:id    ###
###################################

##################################
###   /todos/:id/categories    ###
##################################

######################################
###   /todos/:id/categories/:id    ###
######################################


