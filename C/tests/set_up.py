import subprocess
import requests

ITERATIONS = [i * 25 for i in range(1, 41)]


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
    except Exception:
        # If the server is not down, shut it again.
        shutdown_server(process)
