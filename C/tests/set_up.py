import subprocess

ITERATIONS_T1 = [i*50 for i in range(1, 21)]
ITERATIONS_T2 = [i for i in range(1, 5000)]


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
    process.kill()
