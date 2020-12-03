import csv
import json
import os

import requests
from time import sleep, perf_counter

from .test_add_todo import create_to_do
from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import *

url_todo = "http://localhost:%d/todos"
PORT_IDX = 7
todo_data = {
    "title": "changed_last_title",
    "doneStatus": False,
    "description": "changed_last_decript"
}


def change_todo(last_todo, port):
    r = requests.put(url_todo % port + "/" + last_todo['id'], data=json.dumps(todo_data),
                     headers=send_json_recv_json_headers)
    assert r.status_code == 200


def assert_changed_todo(last_todo, port):
    todo = requests.get(url_todo % port + "/" + last_todo['id'], headers=recv_json_headers)
    assert todo.status_code == 200 and todo_data['title'] in todo.text and todo_data['description'] in todo.text


def test_change_todo():
    t1_file = open(os.path.join("test_data", "change_todo_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "change_todo_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = perf_counter()

        proc = start_server(p)
        for j in range(i + 1):  # add x amount of todos
            last = create_to_do(str(i), p)
            sleep(PAUSE)

        t2_start = perf_counter()
        change_todo(last, p)
        t2_end = perf_counter()

        assert_changed_todo(last, p)
        shutdown_server(proc, p)

        t1_end = perf_counter()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])
        # sleep(30)

    t1_file.close()
    t2_file.close()
