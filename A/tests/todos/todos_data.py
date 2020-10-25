import json

##########################
###     ENDPOINTS      ###
##########################

url = "http://localhost:4567/todos"
url_id = "http://localhost:4567/todos/%d"
url_id_tasksof = "http://localhost:4567/todos/%d/tasksof"
url_id_tasksof_delete = "http://localhost:4567/todos/%d/tasksof/%d"
url_id_categories = "http://localhost:4567/todos/%d/categories"
url_id_categories_delete = "http://localhost:4567/todos/%d/categories/%d"

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
  "description": "For /todos/:id/tasksof"
}

todo_data3 = {
  "title": "New todo for category",
  "doneStatus": False,
  "description": "For /todos/:id/categories"
}

todo_put_data = {
  "title": "Put change",
  "doneStatus": True,
  "description": "YOLO"
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
  <description>For /todos/:id/tasksof xml</description>
  <title>newtodo xml</title>
</todo>"""
todo_xml3 = """<todo>
  <doneStatus>false</doneStatus>
  <description>for /todos/:id/categories xml</description>
  <title>New todo for category xml</title>
</todo>"""
todo_xml_put = """<todo>
  <doneStatus>false</doneStatus>
  <description>YOLO</description>
  <title>Put change xml</title>
</todo>"""