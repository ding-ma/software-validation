# As a student, I want to change a task description, to better represent the work to do.
Feature: Change task description
    As a student, 
    I want to change a task description, 
    to better represent the work to do.

    # Normal Flow
    Scenario: Change task description
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 3         | write essay | essay #4         | False           |
        | 4         | read paper  | paper #3         | True            |
        | 5         | project 1   | class #4         | False           |
    When a user changes the description of the following tasks
        | task_id   | task_title  | task_description |
        | 3         | write essay | new essay #4     |
        | 4         | read paper  | old paper #3     |
        | 5         | project 1   | cool class #4    |
    Then the task descriptions should be changed
        | task_id   | task_description |
        | 3         | new essay #4     |
        | 4         | old paper #3     |
        | 5         | cool class #4    |

    # Alternative Flow
    Scenario: Remove task description
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 3         | write essay | essay #4         | True            |
        | 4         | read paper  | paper #3         | True            |
        | 5         | project 1   | class #4         | False           |
    When a user removes the description of the following tasks
        | task_id   | task_title  |
        | 3         | write essay |
        | 4         | read paper  |
        | 5         | project 1   |
    Then the task descriptions should be changed
        | task_id   | task_title  | task_description |
        | 3         | write essay |                  |
        | 4         | read paper  |                  |
        | 5         | project 1   |                  |

    # Error Flow
    Scenario: Change description of a non-existent task
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 3         | write essay | essay #4         | False           |
        | 4         | read paper  | paper #3         | True            |
        | 5         | project 1   | class #4         | False           |
    When a user changes the description of a non-existent task
        | task_id   | task_title  | task_description |
        | 10        | DNE         | new_description  |
        | 11        | NA          | nice description |
    Then nothing should happen
