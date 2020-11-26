import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server,  ITERATIONS
from .test_todo_add import create_to_do

url_todo = "http://localhost:4567/todos"

todo_data = {
    "title": "",
    "doneStatus": False,
    "description": ""
}


def delete_todo_with_assert(run_id):
    deleted_todo = requests.get(url_todo + "/" + run_id, headers=recv_json_headers).json()["todos"][0]
    r = requests.delete(url_todo + "/" + run_id, headers=send_json_recv_json_headers)
    todos = requests.get(url_todo, headers=recv_json_headers).json()["todos"]
    assert r.status_code == 200 and deleted_todo not in todos


def delete_todo(last_todo):
    deleted_todo = requests.delete(url_todo + "/" + last_todo['id'], headers=recv_json_headers)
    assert deleted_todo.status_code == 200


def assert_deleted_todo(deleted_todo):
    todos = requests.get(url_todo, headers=recv_json_headers)
    assert todos.status_code == 200 and deleted_todo not in todos.json()["todos"]


def test_delete_todo():
    t1_file = open(os.path.join("test_data", "delete_todo_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_todo_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()
        proc = start_server()
        for j in range(1, i+1):
            last = create_to_do(str(j))
        # only delete the last one
        t2_start = time()
        delete_todo(last)
        t2_end = time()

        assert_deleted_todo(last)
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end-t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end-t2_start])
        sleep(5)

    t1_file.close()
