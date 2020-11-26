import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS_T2, ITERATIONS_T1

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


def assert_todos(run_id):
    r = requests.get(url_todo, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_todo_t1():
    time_stamps = open(os.path.join("test_data", "add_todo_time_stamps_t1.csv"), "w", newline='')
    time_writer = csv.writer(time_stamps)
    time_writer.writerow([ "Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS_T1:
        print(i)
        t1_start = time()

        proc = start_server()
        for j in range(i):  # add x amount of todos
            create_to_do(str(i))
            assert_todos(str(i))
        shutdown_server(proc)

        t1_end = time()
        time_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        sleep(5)  # make sure not to run into jar issues

    time_stamps.close()


def test_add_todo_t2():
    time_stamps = open(os.path.join("test_data", "add_todo_time_stamps_t2.csv"), "w", newline='')
    time_writer = csv.writer(time_stamps)
    time_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    proc = start_server()
    for i in ITERATIONS_T2:
        print(i)
        t2_start = time()
        create_to_do(str(i))
        t2_end = time()
        time_writer.writerow([ i, t2_start, t2_end, t2_end - t2_start])

    shutdown_server(proc)
    time_stamps.close()
