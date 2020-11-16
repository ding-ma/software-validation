Feature: Remove a task to a course to do list

  As a student, I remove an unnecessary task from my course to do list, so I can forget about it.

    # regular flow
  Scenario Outline: Remove a completed task to the course to do list
    Given a user creates a project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    And a user adds a task with title <task_title>, description <task_description> and done status <task_doneStatus> to the project
    When a user removes that task from the course to do list
    Then the task should no longer be contained in the todo list
    Examples:
      | project_title | project_completed | project_active | project_description        | task_title  | task_description | task_doneStatus |
      | ECSE 429      | True              | True           | Software validation course | write paper | miam             | True            |
      | COMP 429      | True              | True           | pire cours                 | some title  | desct?           | True            |

    # alternate flow
  Scenario Outline: Remove an uncompleted task to the course to do list
    Given a user creates a project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    And a user adds a task with title <task_title>, description <task_description> and done status <task_doneStatus> to the project
    When a user removes that task from the course to do list
    Then the task should no longer be contained in the todo list
    Examples:
      | project_title | project_completed | project_active | project_description        | task_title  | task_description | task_doneStatus |
      | ECSE 429      | False             | True          | Software validation course | write paper | miam             | False            |
      | COMP 429      | False             | True           | pire cours                 | some title  | desct?           | False           |

    # error flow
  Scenario Outline: Remove an non existing task to the course todo list
    Given a user creates a project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    And a user adds a task with title <task_title>, description <task_description> and done status <task_doneStatus> to the project
    When a user removes a nonexisting task from the course to do list
    Then we should receive an error message
    Examples:
      | project_title | project_completed | project_active | project_description        | task_title  | task_description | task_doneStatus |
      | ECSE 429      | True              | False          | Software validation course | write paper | miam             | True            |
      | COMP 429      | False             | True           | pire cours                 | some title  | desct?           | False           |
