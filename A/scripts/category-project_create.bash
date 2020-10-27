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

printf "Creating new category\n"

curl --location --request POST "${url}/categories" \
--header 'Content-Type: text/plain' \
--data-raw '{
	title: "Homework"
}'

printf "\nCreated Succesfully!\n"

printf "Creating new category-project relationship\n"

curl --location --request POST "${url}/categories/3/projects" \
--header 'Content-Type: text/plain' \
--data-raw '{
  id: "2"
}'

printf "\nCreated Succesfully!\n"

printf "GET category #3\n"

curl --location --request GET "${url}/categories/3" \


printf "\nGET project #2\n"

curl --location --request GET "${url}/projects/2" \

printf "\nClosing application\n"

curl -s --location --request GET "${url}/shutdown"