# Project A


This test suite requires:
* Python 3.8
* cURL
* Java JRE

To activate the virtual environment for this project.
1. `pip install pipenv`
1. `pipenv install` 
1. `pipenv shell`

To run the tests, we use: `python run.py` for all tests.
Otherwise, you can use `pytest tests/dir/file/you/want` to run a single file or a subdirectory.

Run TodoManagerRestAPI server with: `java -jar runTodoManagerRestAPI-1.5.5.jar`

The application can also be ran with docker:
1. `docker build --tag todomanager:1.5.5 .`
1. `docker run -p 4567:4567 todomanager:1.5.5`