import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS, PORTS
from .test_add_project import create_project

url_projects = "http://localhost:%d/projects"
PORT_IDX = 4
project_data = {
    "title": "",
    "completed": False,
    "active": False,
    "description": ""
}

def change_project(last_project, port):
    r = requests.put(url_projects %port + "/" + last_project['id'], data=json.dumps(project_data), headers=send_json_recv_json_headers)
    assert r.status_code == 200


def assert_changed_project(last_project, port):
    project = requests.get(url_projects %port + "/" + last_project['id'], headers=recv_json_headers)
    assert project.status_code == 200 and project_data['title'] in project.text and project_data['description'] in project.text


def test_change_project():
    t1_file = open(os.path.join("test_data", "change_project_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "change_project_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i,p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = time()

        proc = start_server(p)
        for j in range(i + 1):  # add x amount of projects
            last = create_project(str(i),p)

        t2_start = time()
        change_project(last,p)
        t2_end = time()

        assert_changed_project(last,p)
        shutdown_server(proc,p)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])
        # sleep(30)

    t1_file.close()
    t2_file.close()
