# As a student, I mark a task as done on my course to do list, so I can track my accomplishments.
Feature: Change task done status
    As a student, 
    I mark a task as done on my course to do list, 
    so I can track my accomplishments.

    # Normal Flow
    Scenario Outline: Mark a task as done
        Given the a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user marks the task <task_title> as done
        Then the task should have a a doneStatus of <final_task_doneStatus>
        Examples:
            | task_title  | task_description | task_doneStatus | final_task_doneStatus | 
            | write essay | essay #4         | False           | True                  |
            | read paper  | paper #3         | True            | True                  |
            | project 1   | class #4         | False           | True                  |
    # Alternative Flow
    Scenario Outline: Mark a task as not done
        Given the a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user marks the task <task_title> as not done
        Then the task should have a a doneStatus of <final_task_doneStatus>
        Examples:
            | task_title  | task_description | task_doneStatus | final_task_doneStatus | 
            | write essay | essay #4         | True            | False                 |
            | read paper  | paper #3         | True            | False                 |
            | project 1   | class #4         | False           | False                 |

    # Error Flow
    Scenario Outline: Mark a non-exitent task as done
        Given the a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user marks the wrong task <wrong_task_id> as done
        Then there should be a not found error
        Examples:
            | task_title  | task_description | task_doneStatus | final_task_doneStatus | wrong_task_id    |
            | write essay | essay #4         | False           | True                  | -1               |
            | read paper  | paper #3         | True            | True                  | 0                |
            | project 1   | class #4         | False           | True                  | -999             |
