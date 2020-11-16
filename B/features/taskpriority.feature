# As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.
Feature: Prioritize Tasks
    As a student, 
    I categorize tasks as HIGH, MEDIUM or LOW priority, 
    so I can better manage my time.

    # Normal Flow
    Scenario Outline: Link a task to a category
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        And the category with title <category_title> and description <category_description>
        When a user links a task to a category
        Then the task should be linked to the category
        And the category should not be linked to the task
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description |
            | write essay | essay #4         | False           | LOW           | low priority         |
            | read paper  | paper #3         | True            | MEDIUM        | medium priority      |
            | project 1   | class #4         | False           | HIGH          | high priority        |  

    # Alternative Flow
    Scenario Outline: Link a category to a task
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        And the category with title <category_title> and description <category_description>
        When a user links the category to the given task
        Then the category should be linked to the task
        And the task should not be linked to the category
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description |
            | write essay | essay #4         | False           | LOW           | low priority         |
            | read paper  | paper #3         | True            | MEDIUM        | medium priority      |
            | project 1   | class #4         | False           | HIGH          | high priority        |  

    # Error Flow
    Scenario Outline: Prioritize a task to category
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        And the category with title <category_title> and description <category_description>
        When a user links an invalid category with <wrong_category_id> to the given task
        Then the task should not be linked to the category
        And the category should not be linked to the task
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | wrong_category_id |
            | write essay | essay #4         | False           | LOW           | low priority         | -1                |
            | read paper  | paper #3         | True            | MEDIUM        | medium priority      | 0                |
            | project 1   | class #4         | False           | HIGH          | high priority        | -999             |
