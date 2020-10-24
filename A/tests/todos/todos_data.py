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
###     XML DATA    ###
#######################

todo_xml = """<todo>
  <doneStatus>false</doneStatus>
  <description>it amet, consectetur</description>
  <title>bore et dolore magna</title>
</todo>"""
