# Project A

To activate the virtual environment for this project.

Note: This project requires Python 3.8.

* `pip install pipenv`
* `pipenv install` 
* `pipenv shell`

Run TodoManagerRestAPI server with: `java -jar runTodoManagerRestAPI-1.5.5.jar`

To run the tests, we use: `python run.py`


* `docker build --tag todomanager:1.5.5 .`
* `docker run -p 4567:4567 todomanager:1.5.5`