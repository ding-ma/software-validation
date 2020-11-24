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

To run the tests, we use: `python run.py`

* Note: this will start the REST API before each test and end it after each test. Please make sure nothing is running on port 4567 before running the above command. 


### About pytest-monitor
* See [Official Docs](https://pytest-monitor.readthedocs.io/en/latest/?badge=latest)
* Here is an [example](https://github.com/CFMTech/pytest-monitor)

Note that the tests will generate a .pymon file which is a small lightweight database. You will need to run SQL query in order to get the tests data.  

