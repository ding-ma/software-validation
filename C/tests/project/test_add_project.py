import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import *

url_projects = "http://localhost:%d/projects"
PORT_IDX = 3
project_data = {
    "title": "",
    "completed": False,
    "active": False,
    "description": ""
}


def create_project(run_id, port):
    project_data['title'] = "my_test-" + run_id
    project_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_projects % port, data=json.dumps(project_data), headers=send_json_recv_json_headers)
    res = r.json()
    projects = requests.get(url_projects % port).json()["projects"]
    assert r.status_code == 201 and res in projects
    return res


def assert_projects(run_id, port):
    r = requests.get(url_projects % port, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_project():
    t1_file = open(os.path.join("test_data", "add_project_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "add_project_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = time()

        proc = start_server(p)
        for j in range(i):  # add x amount of projects
            if i - 1 == j:
                t2_start = time()
                create_project(str(i), p)
                t2_end = time()
                assert_projects(str(i), p)
                t2_writer.writerow([j + 1, t2_start, t2_end, t2_end - t2_start])
            else:
                create_project(str(i), p)
                assert_projects(str(i), p)
            sleep(PAUSE)
        shutdown_server(proc, p)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])

    t1_file.close()
    t2_file.close()

