#!/bin/bash

java -jar ../runTodoManagerRestAPI-1.5.5.jar > /dev/null 2>&1 &

url=http://localhost:4567
 
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

printf "Closing application\n"

curl -s --location --request GET "${url}/shutdown"