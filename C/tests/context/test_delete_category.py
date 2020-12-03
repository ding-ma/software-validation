import csv
import os

import requests
from time import sleep, perf_counter

from .test_add_category import create_category
from ..headers import recv_json_headers
from ..set_up import *

url_categories = "http://localhost:%d/categories"
PORT_IDX = 2
category_data = {
    "title": "test",
    "description": ""
}


def delete_category(last_category, port):
    deleted_category = requests.delete(url_categories % port + "/" + last_category['id'], headers=recv_json_headers)
    assert deleted_category.status_code == 200


def assert_deleted_category(deleted_category, port):
    categories = requests.get(url_categories % port, headers=recv_json_headers)
    assert categories.status_code == 200 and deleted_category not in categories.json()["categories"]


def test_delete_category():
    t1_file = open(os.path.join("test_data", "delete_category_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "delete_category_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = perf_counter()
        proc = start_server(p)
        for j in range(1, i + 1):
            last = create_category(str(j), p)
            sleep(PAUSE)
        # only delete the last one
        t2_start = perf_counter()
        delete_category(last, p)
        t2_end = perf_counter()

        assert_deleted_category(last, p)
        shutdown_server(proc, p)

        t1_end = perf_counter()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])
        # sleep(30)

    t1_file.close()
    t2_file.close()
