import subprocess
import requests

ITERATIONS = [1, 2, 5, 10, 25, 50, 75, 100, 150, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 7500, 10000]
BASE_PORT = 3000
NUMBER_TESTS = 9
PORTS = [[c + row * len(ITERATIONS) + BASE_PORT for c in range(len(ITERATIONS))] for row in range(NUMBER_TESTS)]


def start_server(port):
    print("running on port", port)
    process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar", "-port={}".format(port)], shell=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    status_code = subprocess.check_call(['curl', 'http://localhost:{}/docs'.format(port)], shell=True,
                                        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    while status_code:  # Verify the system is up before starting the test
        status_code = subprocess.check_call(['curl', 'http://localhost:{}/docs'.format(port)], shell=True,
                                            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return process


def shutdown_server(process, port):
    subprocess.call(['curl', 'http://localhost:{}/shutdown'.format(port)], shell=True, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    try:
        requests.get("http://localhost:{}/docs".format(port))
    except requests.exceptions.ConnectionError:
        # kill PID so we dont get zombie process
        process.kill()
        return
    # If the server is not down, shut it again.
    return shutdown_server(process)
