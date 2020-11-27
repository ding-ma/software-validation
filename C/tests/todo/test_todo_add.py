import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS

url_todo = "http://localhost:4567/todos"

todo_data = {
    "title": "",
    "doneStatus": False,
    "description": ""
}


def create_to_do(run_id):
    todo_data['title'] = "my_test-" + run_id
    todo_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_todo, data=json.dumps(todo_data), headers=send_json_recv_json_headers)
    res = r.json()
    todos = requests.get(url_todo).json()["todos"]
    assert r.status_code == 201 and res in todos
    return res


def assert_todos(run_id):
    r = requests.get(url_todo, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_todo():
    t1_file = open(os.path.join("test_data", "add_todo_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "add_todo_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()

        proc = start_server()
        for j in range(i):  # add x amount of todos
            if i == ITERATIONS[-1]:
                t2_start = time()
                create_to_do(str(i))
                t2_end = time()
                assert_todos(str(i))
                t2_writer.writerow([j, t2_start, t2_end, t2_end - t2_start])
            else:
                create_to_do(str(i))
                assert_todos(str(i))
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        sleep(5)  # make sure not to run into jar issues

    t1_file.close()
