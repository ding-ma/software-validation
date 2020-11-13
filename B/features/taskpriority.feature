# As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.
@fixture.app
Feature: Prioritize Tasks
    As a student, 
    I categorize tasks as HIGH, MEDIUM or LOW priority, 
    so I can better manage my time.

    # Normal Flow

    Scenario: Prioritize a task to MEDIUM
    Given a task <task_id> and a category <category_id>
    When a user categorizes the task as <category_name> priority
    Then the task should be properly linked with category <category_id>

    Examples: Priority Levels
        | task_id   | task_name   | category_id | category_name |
        |   2        |             |             |               |
        |           |             |             |               |
        |           |             |             |               |
        |           |             |             |               |
        |           |             |             |               |