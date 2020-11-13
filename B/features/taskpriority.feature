# As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.
Feature: Prioritize Tasks
    As a student, I categorize tasks as HIGH, MEDIUM or LOW priority, so I can better manage my time.

    # Normal Flow
    Scenario: Prioritize a task to MEDIUM
    Given a task
    When a user categorizes the task as MEDIUM priority
    Then the task should be properly categorized