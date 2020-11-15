Feature: Create a to do list for a new class.

    As a student, I create a to do list for a new class I am taking, so I can manage course work.

    # Normal flow
    Scenario: Create a to do list for a new class
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    When a user creates the following course to do list
        | course_title            | course_description   | tasksof         | course_doneStatus |
        | read paper            | paper #3           | 2               | True            |
    Then the tasks in the course to do list should contain
        | course_id   | course_title            | course_description   | course_doneStatus | tasksof | 
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Alternative Flow
    Scenario: Remove an uncompleted task to the course to do list
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | course_id     | course_title  | course_description | course_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user removes the following task from the course to do list
        | course_title            | course_description   | tasksof     | course_doneStatus |
        | write essay           | essay #4           | 2           | False           |
    Then the tasks in the course to do list should contain
        | course_id   | course_title            | course_description   | course_doneStatus | tasksof | 
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Error Flow
    Scenario: Remove an unexisting task to the course todo list 
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | course_id     | course_title  | course_description | course_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user removes a task that does not exist to a course todo list
        | course_title            | course_description   | tasksof | course_doneStatus |
        | ECSE 429 Assignment B | Project B Gherkins | 2       | True            |
    Then the tasks in the course to do list should contain
        | course_id   | course_title            | course_description   | course_doneStatus | tasksof | 
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |