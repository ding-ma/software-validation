# Project A

To activate the virtual environment for this project.

Note: This project requires Python 3.8.

* `pip install pipenv`
* `pipenv install` 
* `pipenv shell`

To run the tests, we use: `python run.py`

* Note: this will start the REST API before each test and end it after each test. Please make sure nothing is running on port 4567 before running the above command. 


* `docker build --tag todomanager:1.5.5 .`
* `docker run -p 4567:4567 todomanager:1.5.5`