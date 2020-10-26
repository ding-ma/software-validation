#!/bin/bash
java -jar ../runTodoManagerRestAPI-1.5.5.jar

url=http://localhost:4567/docs
# just some url
 
# curl ${url} -I

curl -o /dev/null -s -w "%{http_code}\n" ${url}
# cat headers