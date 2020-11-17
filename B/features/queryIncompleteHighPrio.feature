# As a student,I query all incomplete HIGH priority tasks from all my classes,to identity my short-termgoals.

Feature: Query incomplete high priority tasks

    As a student,
    I query all incomplete HIGH priority tasks from all my classes,
    to identity my short-termgoals.

    # Normal Flow
    Scenario Outline: 1 incomplete HIGH priority task
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus> linked to category with title <category_title> and description <category_description>
        And a complete task with title <task_title>, description <task_description>
        Then only incomplete task for category should be returned
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | 
            | write essay | essay #4         | False           | HIGH          | high priority        | 
            | read paper  | paper #3         | False           | HIGH          | high priority        | 
            | project 1   | class #4         | False           | HIGH          | high priority        | 
    
    # Alternative Flow
    Scenario Outline: 0 incomplete HIGH priority tasks
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus> linked to category with title <category_title> and description <category_description>
        And a complete task with title <task_title>, description <task_description>
        Then no tasks for category should be returned
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description |
            | write essay | essay #4         | True           | HIGH          | high priority         |
            | read paper  | paper #3         | True           | HIGH          | high priority         | 
            | project 1   | class #4         | True           | HIGH          | high priority         | 

    # Error Flow
    Scenario Outline: No doneStatus filter used for HIGH priority tasks
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus> linked to category with title <category_title> and description <category_description>
        And a complete task with title <task_title>, description <task_description>
        Then tasks for category should be returned
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | task_notDoneStatus |
            | write essay | essay #4         | False           | HIGH          | high priority         | TRUE               |
            | read paper  | paper #3         | False           | HIGH          | high priority         | TRUE               |
            | project 1   | class #4         | False           | HIGH          | high priority         | TRUE               |