import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server,  ITERATIONS
from .test_add_category import create_category

url_categories = "http://localhost:4567/categories"

category_data = {
    "title": "test",
    "description": ""
}

def delete_category_with_assert(run_id):
    deleted_category = requests.get(url_categories + "/" + run_id, headers=recv_json_headers).json()["categories"][0]
    r = requests.delete(url_categories + "/" + run_id, headers=send_json_recv_json_headers)
    categories = requests.get(url_categories, headers=recv_json_headers).json()["categories"]
    assert r.status_code == 200 and deleted_category not in categories


def delete_category(last_category):
    deleted_category = requests.delete(url_categories + "/" + last_category['id'], headers=recv_json_headers)
    assert deleted_category.status_code == 200


def assert_deleted_category(deleted_category):
    categories = requests.get(url_categories, headers=recv_json_headers)
    assert categories.status_code == 200 and deleted_category not in categories.json()["categories"]


def test_delete_category():
    t1_file = open(os.path.join("test_data", "delete_category_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_category_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()
        proc = start_server()
        for j in range(1, i+1):
            last = create_category(str(j))
        # only delete the last one
        t2_start = time()
        delete_category(last)
        t2_end = time()

        assert_deleted_category(last)
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end-t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end-t2_start])
        sleep(20)

    t1_file.close()
