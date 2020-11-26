import csv
import json
import os
from time import time

import requests

from ..headers import send_json_recv_json_headers, recv_json_headers
from ..set_up import start_server, shutdown_server, ITERATIONS_T2


url_todo = "http://localhost:4567/todos"

todo_data = {
    "title": "",
    "doneStatus": False,
    "description": ""
}


def delete_todo(run_id):
    pass


def assert_deleted_todo(run_id):
    pass


def test_delete_todo():
    pass
