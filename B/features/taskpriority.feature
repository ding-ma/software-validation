# As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.
Feature: Prioritize Tasks
    As a student, 
    I categorize tasks as HIGH, MEDIUM or LOW priority, 
    so I can better manage my time.

    # Normal Flow

    Scenario: Prioritize a task to category
    Given a task and a category id
        | task_id   | task_title  | task_description | task_doneStatus | category_id | category_title| category_description |
        | 3         | write essay | essay #4         | False           | 2           | LOW           | low priority         |
        | 4         | read paper  | paper #3         | True            | 3           | MEDIUM        | medium priority      |
        | 5         | project 1   | class #4         | False           | 4           | HIGH          | high priority        |
    When a user categorizes the task as to the given category
        | task_id   | task_title  | task_description | task_doneStatus | category_id | category_title| category_description |
        | 3         | write essay | essay #4         | False           | 2           | LOW           | low priority         |
        | 4         | read paper  | paper #3         | True            | 3           | MEDIUM        | medium priority      |
        | 5         | project 1   | class #4         | False           | 4           | HIGH          | high priority        |
    Then the task should be properly linked with the category