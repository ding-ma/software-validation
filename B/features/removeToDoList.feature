Feature: Remove a to do list for a class.

  As a student,
  I remove a to do list for a class which I am no longer taking,
  to declutter my schedule.

  # normal flow
  Scenario Outline: Remove a completed to do list for a class I am no longer taking
    Given an existing project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    When a user removes that project
    Then the projects should not be contained
    Examples:
      | project_title | project_completed | project_active | project_description |
      | ECSE 429      | False             | True           | Sofaaaon course     |
      | COMP 360      | False             | True           | Todss60             |

    # alternate flow
  Scenario Outline: Remove an uncompleted and active to do list for a class
    Given  an existing project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    When a user removes that project
    Then the projects should not be contained
    Examples:
      | project_title | project_completed | project_active | project_description |
      | ECSE 429      | True              | True           | Sofaaaon course     |
      | COMP 360      | False             | True           | Todss60             |

  # error flow
  Scenario Outline: Remove a nonexistent to do list for a class
    Given  an non existing project with title <project_title>, description <project_description>, complete status <project_completed> and active status <project_active>
    When a user removes a non existing project
    Then the projects should not be contained
    Examples:
      | project_title | project_completed | project_active | project_description |
      | ECSE 429      | True              | True           | Sofaaaon course     |
      | COMP 360      | False             | True           | Todss60             |
