# As a student,I want to adjust the priority of a task,to help better manage my time.

Feature: Adjust Task Priority 

    As a student,
    I want to adjust the priority of a task,
    to help better manage my time.

    # Normal Flow
    Scenario Outline: Change priority to low
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus> linked to category with title <category_title> and description <category_description>
        And the category with title <new_category_title> and description <new_category_description>
        When a user unlinks a task from old category
        And a user links a task to a category
        Then the task should be linked to the category
        And the category should not be linked to the task
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | new_category_title | new_category_description |
            | write essay | essay #4         | False           | MEDIUM        | medium priority      | LOW                | low priority             |
            | read paper  | paper #3         | True            | MEDIUM        | medium priority      | LOW                | low priority             |
            | project 1   | class #4         | False           | HIGH          | high priority        | LOW                | low priority             |
    
    # Alternative Flow
    Scenario Outline: Change priority to medium
        Given a task with title <task_title>, description <task_description> and done status <task_doneStatus> linked to category with title <category_title> and description <category_description>
        And the category with title <new_category_title> and description <new_category_description>
        When a user unlinks a task from old category
        And a user links a task to a category
        Then the task should be linked to the category
        And the category should not be linked to the task
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | new_category_title | new_category_description |
            | write essay | essay #4         | False           | LOW           | low priority         | MEDIUM             | medium priority          |
            | read paper  | paper #3         | True            | LOW           | low priority         | MEDIUM             | medium priority          |
            | project 1   | class #4         | False           | HIGH          | high priority        | MEDIUM             | medium priority          |

    # Error Flow
    Scenario Outline: Change priority with no initial priority
        Given the a task with title <task_title>, description <task_description> and done status <task_doneStatus>
        And the category with title <category_title> and description <category_description>
        Then the category should not be able to be unlinked
        Examples:
            | task_title  | task_description | task_doneStatus | category_title| category_description | new_category_title | new_category_description |
            | write essay | essay #4         | False           | LOW           | low priority         | MEDIUM             | medium priority          |
            | read paper  | paper #3         | True            | LOW           | low priority         | MEDIUM             | medium priority          |
            | project 1   | class #4         | False           | HIGH          | high priority        | MEDIUM             | medium priority          |