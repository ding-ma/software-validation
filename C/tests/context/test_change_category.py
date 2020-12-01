import csv
import json
import os
from time import time, sleep

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS, PORTS
from .test_add_category import create_category

url_categories = "http://localhost:%d/categories"
PORT_IDX = 1

category_data = {
    "title": "test",
    "description": ""
}


def change_category(last_category, port):
    r = requests.put(url_categories % port + "/" + last_category['id'], data=json.dumps(category_data),
                     headers=send_json_recv_json_headers)
    assert r.status_code == 200


def assert_changed_category(last_category, port):
    category = requests.get(url_categories % port + "/" + last_category['id'], headers=recv_json_headers)
    assert category.status_code == 200 and category_data['title'] in category.text and category_data[
        'description'] in category.text


def test_change_category():
    t1_file = open(os.path.join("test_data", "change_category_time_stamps_t1.csv"), "w", newline='')
    t1_writer = csv.writer(t1_file)
    t1_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    t2_file = open(os.path.join("test_data", "change_category_time_stamps_t2.csv"), "w", newline='')
    t2_writer = csv.writer(t2_file)
    t2_writer.writerow(["Iteration", "Time_start", "Time_end", "Time_difference"])

    for i, p in zip(ITERATIONS, PORTS[PORT_IDX]):
        print(i)
        t1_start = time()

        proc = start_server(p)
        for j in range(i + 1):  # add x amount of categories
            last = create_category(str(i), p)

        t2_start = time()
        change_category(last, p)
        t2_end = time()

        assert_changed_category(last, p)
        shutdown_server(proc, p)

        t1_end = time()
        t1_writer.writerow([i, t1_start, t1_end, t1_end - t1_start])
        t2_writer.writerow([i, t2_start, t2_end, t2_end - t2_start])

    t1_file.close()
    t2_file.close()
