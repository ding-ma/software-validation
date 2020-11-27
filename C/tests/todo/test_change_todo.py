import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS
from .test_todo_add import create_to_do

url_todo = "http://localhost:4567/todos"

todo_data = {
    "title": "changed_last_title",
    "doneStatus": False,
    "description": "changed_last_decript"
}


def change_todo(last_todo):
    r = requests.put(url_todo + "/" + last_todo['id'], data=json.dumps(todo_data), headers=send_json_recv_json_headers)
    assert r.status_code == 200


def assert_changed_todo(last_todo):
    todo = requests.get(url_todo + "/" + last_todo['id'], headers=recv_json_headers)
    assert todo.status_code == 200 and todo_data['title'] in todo.text and todo_data['description'] in todo.text


def test_change_todo():
    t1_file = open(os.path.join("test_data", "change_todo_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "change_todo_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()

        proc = start_server()
        for j in range(i + 1):  # add x amount of todos
            last = create_to_do(str(i))

        t2_start = time()
        change_todo(last)
        t2_end = time()

        assert_changed_todo(last)
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])

    t1_file.close()
