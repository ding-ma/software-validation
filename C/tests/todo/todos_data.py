##########################
###     ENDPOINTS      ###
##########################

url_todo = "http://localhost:4567/todos"
url_todo_id = "http://localhost:4567/todos/%d"
url_todo_id_tasksof = "http://localhost:4567/todos/%d/tasksof"
url_todo_id_tasksof_delete = "http://localhost:4567/todos/%d/tasksof/%d"
url_todo_id_categories = "http://localhost:4567/todos/%d/categories"
url_todo_id_categories_delete = "http://localhost:4567/todos/%d/categories/%d"

##########################
###     JSON DATA      ###
##########################

# post data
todo_data = {
  "title": "",
  "doneStatus": False,
  "description": ""
}
