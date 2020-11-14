# As a student, I mark a task as done on my course to do list, so I can track my accomplishments.
Feature: Change task done status
    As a student, 
    I mark a task as done on my course to do list, 
    so I can track my accomplishments.

    # Normal Flow
    Scenario: Mark a task as done
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 4         | write essay | essay #4         | False           |
        | 6         | read paper  | paper #3         | True            |
        | 8         | project 1   | class #4         | False           |
    When a user marks the following task as done
        | task_id   | task_title  |
        | 4         | write essay |
        | 6         | read paper  |
        | 8         | project 1   |
    Then the task done status should be changed
        | task_id   | task_doneStatus | 
        | 4         | True            |
        | 6         | True            |
        | 8         | True            |

    # Alternative Flow
    Scenario: Mark a task as not done
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 4         | write essay | essay #4         | True            |
        | 6         | read paper  | paper #3         | True            |
        | 8         | project 1   | class #4         | False           |
    When a user marks the following tasks as not done
        | task_id   | task_title  |
        | 4         | write essay |
        | 6         | read paper  |
        | 8         | project 1   |
    Then the task done status should be changed
        | task_id   | task_doneStatus | 
        | 4         | False           |
        | 6         | False           |
        | 8         | False           |

    # Error Flow
    Scenario: Mark a non-exitent task as done
    Given the following tasks
        | task_id   | task_title  | task_description | task_doneStatus | 
        | 4         | write essay | essay #4         | False           |
        | 6         | read paper  | paper #3         | True            |
        | 8         | project 1   | class #4         | False           |
    When a user marks a non-existent task as done
        | task_id    | task_doneStatus | 
        | 10         | True            |
        | 11         | True            |
    Then nothing should happen
