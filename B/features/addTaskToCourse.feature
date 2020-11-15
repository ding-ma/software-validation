Feature: Add a task to a course to do list

    As a student, I add a task to a course to do list, so I can remember it.

    # Normal flow
    Scenario: Add a new task to course to do list
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user adds the following task to the course todo list
        | task_title            | task_description   | tasksof | task_doneStatus |
        | ECSE 429 Assignment B | Project B Gherkins | 2       | False             |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | ECSE 429 Assignment B | Project B Gherkins | False           | 2       |
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Alternative Flow
    Scenario: Add a completed task to course to do list
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user adds the following task to the course todo list
        | task_title            | task_description   | tasksof | task_doneStatus |
        | ECSE 429 Assignment B | Project B Gherkins | 2       | True            |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | ECSE 429 Assignment B | Project B Gherkins | True            | 2       |
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |

    # Error Flow
    Scenario: Add a task to a project that does not exist
    Given the following projects
        | project_id   | project_title  | project_completed | project_active | project_description        |
        | 1            | Office Work    | False             | False          |                            |
        | 2            | ECSE 429       | False             | True           | Software validation course |
    And the following tasks in this ECSE 429 course to do list
        | task_id     | task_title  | task_description | task_doneStatus | tasksof |
        | \d*         | write essay | essay #4         | False           | 2       |
        | \d*         | read paper  | paper #3         | True            | 2       |
        | \d*         | project 1   | class #4         | False           | 2       |
    When a user adds the following task to a course todo list that does not exist
        | task_title            | task_description   | tasksof | task_doneStatus |
        | ECSE 429 Assignment B | Project B Gherkins | 3       | True            |
    Then the tasks in the course to do list should contain
        | task_id   | task_title            | task_description   | task_doneStatus | tasksof | 
        | \d*       | write essay           | essay #4           | False           | 2       |
        | \d*       | read paper            | paper #3           | True            | 2       |
        | \d*       | project 1             | class #4           | False           | 2       |