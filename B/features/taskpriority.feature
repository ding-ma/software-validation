# As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.
Feature: Prioritize Tasks
    As a student, 
    I categorize tasks as HIGH, MEDIUM or LOW priority, 
    so I can better manage my time.

    # Normal Flow
    Scenario: Link a task to a category
    Given the following tasks and categories
        | task_id   | task_title  | task_description | task_doneStatus | category_id | category_title| category_description |
        | 3         | write essay | essay #4         | False           | 3           | LOW           | low priority         |
        | 4         | read paper  | paper #3         | True            | 4           | MEDIUM        | medium priority      |
        | 5         | project 1   | class #4         | False           | 5           | HIGH          | high priority        |
    When a user links a category to the given tasks
        | task_id   | category_id |
        | 3         | 3           |
        | 4         | 4           |
        | 5         | 5           |
    Then the task should be properly linked with the category
        | task_id   | category_id |
        | 3         | 3           |
        | 4         | 4           |
        | 5         | 5           |
    And the category should not be linked to any task
        | category_id |
        | 3           |
        | 4           |
        | 5           |

    # Alternative Flow
    Scenario: Link a category to a task
    Given the following tasks and categories
        | task_id   | task_title  | task_description | task_doneStatus | category_id | category_title| category_description |
        | 3         | write essay | essay #4         | False           | 3           | LOW           | low priority         |
        | 4         | read paper  | paper #3         | True            | 4           | MEDIUM        | medium priority      |
        | 5         | project 1   | class #4         | False           | 5           | HIGH          | high priority        |
    When a user links a task to the given category
        | category_id | task_id   |
        | 3           | 3         |
        | 4           | 4         |
        | 5           | 5         |
    Then the category should be properly linked to the task
        | category_id | task_id   |
        | 3           | 3         |
        | 4           | 4         |
        | 5           | 5         |
    And the task should not be linked to any category
        | task_id   |
        | 3         |
        | 4         |
        | 5         |

    # Error Flow
    Scenario: Prioritize a task to category
    Given the following tasks and categories
        | task_id   | task_title  | task_description | task_doneStatus | category_id | category_title| category_description |
        | 3         | write essay | essay #4         | False           | 3           | LOW           | low priority         |
        | 4         | read paper  | paper #3         | True            | 4           | MEDIUM        | medium priority      |
        | 5         | project 1   | class #4         | False           | 5           | HIGH          | high priority        |
    When a user links an invalid category to the given tasks
        | task_id   | category_id |
        | 3         | 6           |
        | 4         | 7           |
        | 5         | 8           |
    Then the task should not be linked to any category
        | task_id   |
        | 3         |
        | 4         |
        | 5         |