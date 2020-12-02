import csv
import os
from time import time_ns, sleep

import requests

from .test_add_todo import create_to_do
from ..headers import recv_json_headers
from ..set_up import *

url_todo = "http://localhost:%d/todos"
PORT_IDX = 8
todo_data = {
    "title": "",
    "doneStatus": False,
    "description": ""
}


def delete_todo(last_todo, port):
    deleted_todo = requests.delete(url_todo % port + "/" + last_todo['id'], headers=recv_json_headers)
    assert deleted_todo.status_code == 200


def assert_deleted_todo(deleted_todo, port):
    todos = requests.get(url_todo % port, headers=recv_json_headers)
    assert todos.status_code == 200 and deleted_todo not in todos.json()["todos"]


def test_delete_todo():
    t1_file = open(os.path.join("test_data", "delete_todo_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_todo_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = time_ns()
        proc = start_server(p)
        for j in range(1, i + 1):
            last = create_to_do(str(j), p)
            sleep(PAUSE)
        # only delete the last one
        t2_start = time_ns()
        delete_todo(last, p)
        t2_end = time_ns()

        assert_deleted_todo(last, p)
        shutdown_server(proc, p)

        t1_end =time_ns()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])
        # sleep(30)

    t1_file.close()
    t2_file.close()
