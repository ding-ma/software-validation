Feature: Remove a task to a course to do list

    As a student, I remove an unnecessary task from my course to do list, so I can forget about it.

    # Normal flow
    Scenario: Remove a completed task to the course to do list
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user removes the following task from the course to do list
        | task_title            | task_description   | tasksof         | task_doneStatus |
        | read paper            | paper #3           | 2               | True            |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Alternative Flow
    Scenario: Remove an uncompleted task to the course to do list
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user removes the following task from the course to do list
        | task_title            | task_description   | tasksof     | task_doneStatus |
        | write essay           | essay #4           | 2           | False           |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Error Flow
    Scenario: Remove an unexisting task to the course todo list 
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user removes a task that does not exist to a course todo list
        | task_title            | task_description   | tasksof | task_doneStatus |
        | ECSE 429 Assignment B | Project B Gherkins | 2       | True            |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |