# Project C

## Dynamic Analysis 
This test suite requires:
* Python 3.8
* cURL
* Java JRE

To activate the virtual environment for this project.
1. `pip install pipenv`
1. `pipenv install` 
1. `pipenv shell`

Modify `test_thread = Thread(target=test_add_todo_t1)`, in `run.py` as needed in order to run all the tests. The data points from the system needs to be matched to the test data point with the time stamp.

!! Don't forget the save your files in another directory as the tests will overwrite them !!

## Static Analysis

Sonarqube is ran within a docker container, which is orchestrated by docker-compose
Since sonarqube is the only service in the docekr-compose, you can simply run 

```
docker-compose up
```

You will then need to login to sonarqube, located (here)[http://localhost:9000] with System Administrator credentials (login=admin, password=admin).

Token: 82da8d3e710d9239772b1e0f385d555233286c04

Once you are inside the `thingifier-1.5.5` folder, run the following script in order to generate project information.

```
mvn clean sonar:sonar \
  -Dsonar.projectKey=todo-manager \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=82da8d3e710d9239772b1e0f385d555233286c04 \
  -Dsonar.java.binaries=target
```

To shutdown sonarqube, simply enter `ctrl + c` within the running terminal, or type

```
docker-compose down
```
