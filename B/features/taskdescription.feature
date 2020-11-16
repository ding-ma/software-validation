# As a student, I want to change a task description, to better represent the work to do.
Feature: Change task description
    As a student, 
    I want to change a task description, 
    to better represent the work to do.

    # Normal Flow
    Scenario Outline: Change task description
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user changes the description to <new_task_description>
        Then the task description should be changed
        Examples:
            | task_title  | task_description | task_doneStatus | new_task_description |
            | write essay | essay #4         | False           | new essay #4         |
            | read paper  | paper #3         | True            | old paper #3         |
            | project 1   | class #4         | False           | cool class #4        |

    # Alternative Flow
    Scenario Outline: Remove task description
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user removes the task description
        Then the task description should be empty
        Examples:
            | task_title  | task_description | task_doneStatus |
            | write essay | essay #4         | False           |
            | read paper  | paper #3         | True            |
            | project 1   | class #4         | False           |

    # Error Flow
    Scenario Outline: Change description of a non-existent task
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        When a user selects the <wrong_task_id> to change the description to <new_task_description>
        Then there should be a not found error
        Examples:
            | task_title  | task_description | task_doneStatus | new_task_description | wrong_task_id |
            | write essay | essay #4         | False           | wrong                | -1            |
            | read paper  | paper #3         | True            | ok                   | 0             |
            | project 1   | class #4         | False           | test                 | -99           |

