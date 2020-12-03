import subprocess

import requests
from time import sleep

ITERATIONS = [1, 5, 10, 25, 50, 100, 150, 300, 500, 700, 1000, 2000, 3000, 5000, 8000, 10000] 
BASE_PORT = 2000
NUMBER_TESTS = 9
PAUSE = 0.01
PORTS = [[c + row * len(ITERATIONS) + BASE_PORT for c in range(len(ITERATIONS))] for row in range(NUMBER_TESTS)]


def start_server(port):
    # print("running on port", port)
    # global status_code
    process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar", "-port={}".format(port)], 
                               stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    process = subprocess.Popen(['curl', 'http://localhost:{}/docs'.format(port)], 
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return_code = process.communicate()
    while process.returncode:  # Verify the system is up before starting the test
        process = subprocess.Popen(['curl', 'http://localhost:{}/docs'.format(port)], 
                                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return_code = process.communicate()                     
    
    return process


def shutdown_server(process, port):
    subprocess.Popen(['curl', 'http://localhost:{}/shutdown'.format(port)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        requests.get("http://localhost:{}/docs".format(port))
    except requests.exceptions.ConnectionError:
        # kill PID so we dont get zombie process
        process.kill()
        return
    # If the server is not down, shut it again.
    return shutdown_server(process, port)
