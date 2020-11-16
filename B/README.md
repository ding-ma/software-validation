# Part B of the project 


## Setup and execution

To setup the environment
```
pipenv shell
pipenv install
```

To run the tests 

```
behave 
```

If you want to see stdout or stderr while running the test run one of the following commands
```
behave --no-capture
behave --no-capture-stderr
```

If you wish to run the test in a random order, you need to run the random_execute file

```
python random_execute.py
```
If you wish to run the test without starting the server
```
python random_execute.py --disable-server
```
## Folder Directory

All the `.feature` files will be stored in the `/features` folder. 
The corresponding steps python test will be in the `/features/steps` folder.


## Documentation

Documentation of the [behave package](https://behave.readthedocs.io/en/latest/tutorial.html).

