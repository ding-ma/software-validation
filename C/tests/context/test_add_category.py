import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS

url_categories = "http://localhost:4567/categories"

category_data = {
    "title": "test",
    "description": ""
}

def create_category(run_id):
    category_data['title'] = "my_test-" + run_id
    category_data['description'] = "my_decrip-" + run_id
    r = requests.post(url_categories, data=json.dumps(category_data), headers=send_json_recv_json_headers)
    res = r.json()
    categories = requests.get(url_categories).json()["categories"]
    assert r.status_code == 201 and res in categories
    return res


def assert_categories(run_id):
    r = requests.get(url_categories, headers=recv_json_headers)
    assert r.status_code == 200 and "my_test-" + run_id in r.text and "my_decrip-" + run_id in r.text


def test_add_category():
    t1_file = open(os.path.join("test_data", "add_category_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "add_category_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i in ITERATIONS:
        print(i)
        t1_start = time()

        proc = start_server()
        for j in range(i):  # add x amount of categories
            if i == ITERATIONS[-1]:
                t2_start = time()
                create_category(str(i))
                t2_end = time()
                assert_categories(str(i))
                t2_writer.writerow([j, t2_start, t2_end, t2_end - t2_start])
            else:
                create_category(str(i))
                assert_categories(str(i))
        shutdown_server(proc)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])

    t1_file.close()
