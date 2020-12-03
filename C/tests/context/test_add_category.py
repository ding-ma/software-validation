import csv
import json
import os

import requests
from time import perf_counter, sleep

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import *

PORT_IDX = 0
url_categories = "http://localhost:%d/categories"

category_data = {
    "title": "test",
    "description": ""
}


def create_category(run_id, port):
    category_data['title'] = "my_test-" + run_id
    category_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_categories % port, data=json.dumps(category_data), headers=send_json_recv_json_headers)
    assert r.status_code == 201
    return r.json()


def assert_categories(run_id, port):
    r = requests.get(url_categories % port, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_category():
    t1_file = open(os.path.join("test_data", "add_category_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "add_category_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = perf_counter()

        proc = start_server(p)
        for j in range(i):  # add x amount of categories
            if j == i - 1:
                t2_start = perf_counter()
                create_category(str(i), p)
                t2_end = perf_counter()
                assert_categories(str(i), p)
                t2_writer.writerow([j + 1, t2_start, t2_end, t2_end - t2_start])
            else:
                create_category(str(i), p)
                assert_categories(str(i), p)
            sleep(PAUSE)
        shutdown_server(proc, p)

        t1_end = perf_counter()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        # sleep(30)

    t1_file.close()
    t2_file.close()
