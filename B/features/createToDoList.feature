Feature: Create a to do list for a new class.

    As a student, I create a to do list for a new class I am taking, so I can manage course work.

    # Normal flow
    Scenario: Create a to do list for a new class
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    When a user creates the following course to do list
        | project_title         | project_description    | project_active  | project_completed | 
        | COMP 360              | Todo list for COMP 360 | True            | False             | 
    Then the projects should contain
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
        | 3            | COMP 360       | False             | True           | Todo list for COMP 360     |


    # Alternative Flow
    Scenario: Create an inactive and completed to do list for a new class
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    When a user creates the following course to do list
        | project_title         | project_description    | project_active  | project_completed | 
        | COMP 360              | Todo list for COMP 360 | False           | True              | 
    Then the projects should contain
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
        | 3            | COMP 360       | True              | False          | Todo list for COMP 360     |

    # Error Flow
    Scenario: Create a to do list for a new class without a title 
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    When a user creates the following course to do list with an id
        | project_id   | project_title         | project_description    | project_active  | project_completed | 
        | 1            |                       | Todo list for COMP 360 | False           | True              | 
    Then the projects should contain
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
