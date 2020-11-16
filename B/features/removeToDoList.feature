Feature: Remove a to do list for a class.

  As a student,
  I remove a to do list for a class which I am no longer taking,
  to declutter my schedule.

  Scenario Outline: Remove a completed to do list for a class I am no longer taking
    Given the a project with title <project_title>, description <project_description>,project status <project_status> and done status <project_completed>
    When a user removes "ECSE 429" from the projects
    Then the projects should contain <isContained>
    Examples:
      | project_title | project_completed | project_active | project_description | isContained |
      | Office Work   | False             | False          |                     | True        |
      | ECSE 429      | True              | True           | some desct          | False       |
    # Normal flow
#  Scenario: Remove a completed to do list for a class I am no longer taking
#    Given the following projects
#      | project_id | project_title | project_completed | project_active | project_description        |
#      | 1          | Office Work   | False             | False          |                            |
#      | 2          | ECSE 429      | True              | True           | Software validation course |
#    When a user removes the following course to do list
#      | project_id | project_description        | project_title | project_active | project_completed |
#      | 2          | Software validation course | ECSE 429      | True           | True              |
#    Then the projects should contain
#      | project_id | project_title | project_completed | project_active | project_description |
#      | 1          | Office Work   | False             | False          |                     |
#
#    # Alternative Flow
#  Scenario: Remove an uncompleted and active to do list for a class
#    Given the following projects
#      | project_id | project_title | project_completed | project_active | project_description        |
#      | 1          | Office Work   | False             | False          |                            |
#      | 2          | ECSE 429      | False             | True           | Software validation course |
#    When a user removes the following course to do list
#      | project_id | project_description        | project_title | project_active | project_completed |
#      | 2          | Software validation course | ECSE 429      | True           | False             |
#    Then the projects should contain
#      | project_id | project_title | project_completed | project_active | project_description |
#      | 1          | Office Work   | False             | False          |                     |
#
#    # Error Flow
#  Scenario: Remove a nonexistent to do list for a class
#    Given the following projects
#      | project_id | project_title | project_completed | project_active | project_description        |
#      | 1          | Office Work   | False             | False          |                            |
#      | 2          | ECSE 429      | False             | True           | Software validation course |
#    When a user removes the following course to do list which is nonexistent
#      | project_id | project_description | project_title | project_active | project_completed |
#      | 3          | nonexistent course  | nonexistent   | True           | False             |
#    Then the projects should contain
#      | project_id | project_title | project_completed | project_active | project_description        |
#      | 1          | Office Work   | False             | False          |                            |
#      | 2          | ECSE 429      | False             | True           | Software validation course |
#
