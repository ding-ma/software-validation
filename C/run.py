from threading import Thread, currentThread
from time import sleep, time
import psutil
import subprocess
from tests.todo.test_todo_add import create_to_do, assert_todos
import csv
import os


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


def logger():
    t = currentThread()
    log = open(os.path.join("test_data", "add_todo.csv"), "w", newline='')
    log_writter = csv.writer(log)
    log_writter.writerow(["time", "cpu_usage", "free_memory", "used_memory"])

    while getattr(t, "run", True):
        now = time()
        cpu_usage = psutil.cpu_percent()
        free_mem = psutil.virtual_memory().free
        used_mem = psutil.virtual_memory().used
        log_writter.writerow([now, cpu_usage, free_mem, used_mem])
        sleep(0.01)
    log.close()


def start_test():
    time_stamps = open(os.path.join("test_data", "add_todo_time_stamp.csv"), "w", newline='')
    time_writer = csv.writer(time_stamps)
    time_writer.writerow(["Type", "Time_difference", "Iteration", "Time_Stamp"])

    t1_start = time()
    time_writer.writerow(["T1", t1_start, "NA", "NA"])
    proc = start_server()
    for i in range(3000):
        print(i)
        t2_start = time()
        create_to_do(str(i))  # todo create function generator
        t2_end = time()
        time_writer.writerow(["T2", t2_end - t2_start, i, t2_end])
        assert_todos(str(i))

    shutdown_server(proc)
    t1_end = time()
    time_writer.writerow(["T1", t1_end, "NA", "NA"])


def main():
    logger_thread = Thread(target=logger)
    logger_thread.start()
    test_thread = Thread(target=start_test)
    test_thread.start()
    test_thread.join()
    logger_thread.run = False
    logger_thread.join()


if __name__ == "__main__":
    main()
