import json

import requests
import xmltodict


##########################
###      HEADERS       ###
##########################

# headers used to receive response in xml format
recv_xml_headers = {
    "Accept": "application/xml"
}

recv_json_headers = {
    "Accept": "application/json"
}

send_xml_headers = {
    "Content-Type":  "application/xml"
}

send_json_headers = {
    "Content-Type":  "application/json"
}

send_json_recv_xml_headers = {
    "Content-Type":  "application/json",
    "Accept": "application/xml"
}

send_xml_recv_json_headers = {
    "Content-Type":  "application/xml",
    "Accept": "application/json"
}

send_xml_recv_xml_headers = {
    "Content-Type":  "application/xml",
    "Accept": "application/xml"
}

send_json_recv_json_headers = {
    "Content-Type":  "application/json",
    "Accept": "application/json"
}

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

##########################
###     ENDPOINTS      ###
##########################

url_todo = "http://localhost:4567/todos"
url_todo_id = "http://localhost:4567/todos/%d"
url_todo_id_tasksof = "http://localhost:4567/todos/%d/tasksof"
url_todo_id_tasksof_delete = "http://localhost:4567/todos/%d/tasksof/%d"
url_todo_id_categories = "http://localhost:4567/todos/%d/categories"
url_todo_id_categories_delete = "http://localhost:4567/todos/%d/categories/%d"
url_category = "http://localhost:4567/categories"
url_project = "http://localhost:4567/projects"


##########################
###     JSON DATA      ###
##########################

# post data
todo_data = {
  "title": "bore et dolore magna",
  "doneStatus": False,
  "description": "it amet, consectetur"
}

todo_data2 = {
  "title": "New todo",
  "doneStatus": False,
  "description": "For testing"
}

todo_data3 = {
  "title": "New todo for category",
  "doneStatus": False,
  "description": "For test"
}

todo_put_data = {
  "title": "Put change",
  "doneStatus": True,
  "description": "YOLO"
}

todo_connect_category = {
  "id" : "2"
}

#######################
###     XML DATA    ###
#######################

todo_xml = """<todo>
  <doneStatus>true</doneStatus>
  <description>it amet, asdasdconsectetur</description>
  <title>bore et dolore magna</title>
</todo>"""
todo_xml2 = """<todo>
  <doneStatus>true</doneStatus>
  <description>For /todos/:id/sdfgsd xml</description>
  <title>newtodo xml</title>
</todo>"""
todo_xml3 = """<todo>
  <doneStatus>false</doneStatus>
  <description>for /todos/:id/sdfg xml</description>
  <title>New todo for category xml</title>
</todo>"""
todo_xml_put = """<todo>
  <doneStatus>false</doneStatus>
  <description>YOLO</description>
  <title>Put change xml</title>
</todo>"""