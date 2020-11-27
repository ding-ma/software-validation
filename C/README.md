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

To shutdown sonarqube, simply enter `ctrl + c` within the running terminal, or type

```
docker-compose down
```
