import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS

url_projects = "http://localhost:4567/projects"

project_data = {
    "title": "",
    "completed": False,
    "active": False,
    "description": ""
}

def create_project(run_id):
    project_data['title'] = "my_test-" + run_id
    project_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_projects, data=json.dumps(project_data), headers=send_json_recv_json_headers)
    res = r.json()
    projects = requests.get(url_projects).json()["projects"]
    assert r.status_code == 201 and res in projects
    return res


def assert_projects(run_id):
    r = requests.get(url_projects, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_project():
    t1_file = open(os.path.join("test_data", "add_project_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "add_project_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()

        proc = start_server()
        for j in range(i):  # add x amount of projects
            if i == ITERATIONS[-1]:
                t2_start = time()
                create_project(str(i))
                t2_end = time()
                assert_projects(str(i))
                t2_writer.writerow([j, t2_start, t2_end, t2_end - t2_start])
            else:
                create_project(str(i))
                assert_projects(str(i))
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])

    t1_file.close()
