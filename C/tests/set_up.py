import subprocess

ITERATIONS = [1, 5, 10, 25, 50, 100, 300, 500, 800, 1000, 3000, 5000, 10000]
BASE_PORT = 2000
NUMBER_TESTS = 9
PAUSE = 0.01
PORTS = [[c + row * len(ITERATIONS) + BASE_PORT for c in range(len(ITERATIONS))] for row in range(NUMBER_TESTS)]


def start_server(port):
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
    subprocess.Popen(['curl', 'http://localhost:{}/shutdown'.format(port)], stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT)
    process.kill()
