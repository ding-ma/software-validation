import csv
import json
import os
from time import time_ns, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import *
from .test_add_project import create_project

url_projects = "http://localhost:%d/projects"
PORT_IDX = 5
project_data = {
    "title": "",
    "completed": False,
    "active": False,
    "description": ""
}


def delete_project(last_project, port):
    deleted_project = requests.delete(url_projects % port + "/" + last_project['id'], headers=recv_json_headers)
    assert deleted_project.status_code == 200


def assert_deleted_project(deleted_project, port):
    projects = requests.get(url_projects % port, headers=recv_json_headers)
    assert projects.status_code == 200 and deleted_project not in projects.json()["projects"]


def test_delete_project():
    t1_file = open(os.path.join("test_data", "delete_project_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_project_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = time_ns()
        proc = start_server(p)
        for j in range(1, i + 1):
            last = create_project(str(j), p)
            sleep(PAUSE)
        # only delete the last one
        t2_start = time_ns()
        delete_project(last, p)
        t2_end = time_ns()

        assert_deleted_project(last, p)
        shutdown_server(proc, p)

        t1_end = time_ns()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])

    t1_file.close()
    t2_file.close()
