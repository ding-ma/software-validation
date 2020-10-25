##########################
###     ENDPOINTS      ###
##########################

url_todo = "http://localhost:4567/todos"
url_todo_id = "http://localhost:4567/todos/%d"
url_tod_id_tasksof = "http://localhost:4567/todos/%d/tasksof"
url_tod_id_tasksof_delete = "http://localhost:4567/todos/%d/tasksof/%d"
url_todo_id_categories = "http://localhost:4567/todos/%d/categories"
url_todo_id_categories_delete = "http://localhost:4567/todos/%d/categories/%d"

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