import subprocess
import requests

ITERATIONS = [1, 2, 5, 10, 20, 50, 75, 100, 150, 200, 300, 500, 700, 1000, 2000, 3000, 5000, 7500, 10000]


def start_server():
    process = subprocess.Popen(["java", "-jar", "runTodoManagerRestAPI-1.5.5.jar"], shell=True,
                               stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True, stdout=subprocess.DEVNULL,
                                  stderr=subprocess.STDOUT)
    while status_code:  # Verify the system is up before starting the test
        status_code = subprocess.call(['curl', 'http://localhost:4567'], shell=True, stdout=subprocess.DEVNULL,
                                      stderr=subprocess.STDOUT)
    return process


def shutdown_server(process):
    subprocess.call(['curl', 'http://localhost:4567/shutdown'], shell=True, stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    try:
        requests.get("http://localhost:4567/docs")
    except requests.exceptions.ConnectionError:
        # kill PID so we dont get zombie process
        process.kill()
        return
    # If the server is not down, shut it again.
    return shutdown_server(process)
