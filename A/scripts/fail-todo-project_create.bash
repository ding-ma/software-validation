#!/bin/bash

java -jar ../runTodoManagerRestAPI-1.5.5.jar > /dev/null 2>&1 &

url=http://localhost:4567
 
printf "Creating new todo\n"

curl --location --request POST "${url}/todos" \
--header 'Content-Type: text/plain' \
--data-raw '{
        "title": "testing session 1",
        "doneStatus": false,
        "description": "testing session 1"
}'

printf "\nCreated Succesfully!\n"

printf "Creating new project\n"

curl --location --request POST "${url}/projects" \
--header 'Content-Type: text/plain' \
--data-raw '{
	"title": "Project A",
    completed: false,
    active: true,
    description: "Project for ECSE429"
}'

printf "\nCreated Succesfully!\n"

printf "Creating new todo-project relationship\n"

curl --location --request POST "${url}/todos/3/taskof" \
--header 'Content-Type: text/plain' \
--data-raw '{
  id: "2"
}'

printf "\nCreated Unsuccesfully!\n"

printf "GET project #2\n"

curl --location --request GET "${url}/projects/2" \


printf "\nGET todo #3\n"

curl --location --request GET "${url}/todos/3" \


printf "\nClosing application\n"

curl -s --location --request GET "${url}/shutdown"