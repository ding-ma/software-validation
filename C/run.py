from threading import Thread, currentThread
from time import sleep, time
import psutil
import csv
import os

from tests.todo.test_delete_todo import test_delete_todo
from tests.todo.test_add_todo import test_add_todo
from tests.todo.test_change_todo import test_change_todo


def logger():
    log = open(os.path.join("test_data", "system_logs.csv"), "w", newline='')
    log_writer = csv.writer(log)
    log_writer.writerow(["time", "cpu_usage(%)", "used_memory(bytes)"])
    process = psutil.Process()

    while getattr(currentThread(), "run", True):
        now = time()
        cpu_usage = psutil.cpu_percent()
        log_writer.writerow([now, cpu_usage,  process.memory_info().rss])
        sleep(0.01)
    log.close()


def main():
    logger_thread = Thread(target=logger)
    logger_thread.start()

    print("Starting Test ---- Test Add Todo")
    create_todo = Thread(target=test_add_todo)
    create_todo.start()
    create_todo.join()

    print("Starting Test ---- Test Change Todo")
    change_todo = Thread(target=test_change_todo)
    change_todo.start()
    change_todo.join()

    print("Starting Test ---- Test Delete Todo")
    delete_todo = Thread(target=test_delete_todo)
    delete_todo.start()
    delete_todo.join()

    # todo: add any other tasks here....

    logger_thread.run = False
    logger_thread.join()


if __name__ == "__main__":
    main()
