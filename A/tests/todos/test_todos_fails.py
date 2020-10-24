from ..headers import *
import requests
import json

url = "http://localhost:4567/todos"

def test_post_todos_empty_data():
    r = requests.post(url)
    # must return an error message saying that the "title" field is required in a post request
    assert r.status_code == 400 and "title : field is mandatory" in r.json()["errorMessages"]
# # todo validate for any side effect
# # todo confirms operation of each api 


######################################
###   wrong ones (change this name)    ###
######################################

# forget to put an id: /todos/categories test no ide before category and no id after category
# forget to put an id: /todos/tasksof test no ide before tasksof and no id after tasksof
# /todo
# /categories
# ... 
# "we should be able to create todo without a ID using the field values in the body of the messag" try one iwth ID
# if we are missing some id ? 

