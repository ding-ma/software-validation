import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server,  ITERATIONS
from .test_add_project import create_project

url_projects = "http://localhost:4567/projects"

project_data = {
    "title": "",
    "completed": False,
    "active": False,
    "description": ""
}

def delete_project_with_assert(run_id):
    deleted_project = requests.get(url_projects + "/" + run_id, headers=recv_json_headers).json()["projects"][0]
    r = requests.delete(url_projects + "/" + run_id, headers=send_json_recv_json_headers)
    projects = requests.get(url_projects, headers=recv_json_headers).json()["projects"]
    assert r.status_code == 200 and deleted_project not in projects


def delete_project(last_project):
    deleted_project = requests.delete(url_projects + "/" + last_project['id'], headers=recv_json_headers)
    assert deleted_project.status_code == 200


def assert_deleted_project(deleted_project):
    projects = requests.get(url_projects, headers=recv_json_headers)
    assert projects.status_code == 200 and deleted_project not in projects.json()["projects"]


def test_delete_project():
    t1_file = open(os.path.join("test_data", "delete_project_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_project_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()
        proc = start_server()
        for j in range(1, i+1):
            last = create_project(str(j))
        # only delete the last one
        t2_start = time()
        delete_project(last)
        t2_end = time()

        assert_deleted_project(last)
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end-t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end-t2_start])
        sleep(20)

    t1_file.close()
