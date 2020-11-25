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
* `test_fiture_time.py` gives us a baseline of how much time it needs to start and shutdown the fixture. Those will need to be added to the time of T1

Note that the tests will generate a `.pymon` file which is a small lightweight database. You will need to run SQL query in order to get the tests data.  

### Here are some important metrics from pytest-monitor
* _TOTAL_TIME (FLOAT)_: Total time spent running the item (in seconds).
* _USER_TIME (FLOAT)_: Time spent in User mode (in seconds).
* _KERNEL_TIME (FLOAT)_: Time spent in Kernel mode (in seconds).
* _CPU_USAGE (FLOAT)_: System-wide CPU usage as a percentage (100 % is equivalent to one core).
* _MEM_USAGE (FLOAT)_: Maximum resident memory used during the test execution (in megabytes).
