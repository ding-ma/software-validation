from threading import Thread, currentThread
from time import sleep, time
import psutil
import csv
import os
from tests.todo.test_todo_add import test_add_todo_t2, test_add_todo_t1


def logger():
    t = currentThread()
    log = open(os.path.join("test_data", "system_logs.csv"), "w", newline='')
    log_writter = csv.writer(log)
    log_writter.writerow(["time", "cpu_usage(%)", "free_memory(mb)", "used_memory(mb)"])

    while getattr(t, "run", True):
        now = time()
        cpu_usage = psutil.cpu_percent()
        free_mem = psutil.virtual_memory().free
        used_mem = psutil.virtual_memory().used
        log_writter.writerow([now, cpu_usage, free_mem, used_mem])
        sleep(0.01)
    log.close()


def main():
    logger_thread = Thread(target=logger)
    logger_thread.start()
    test_thread = Thread(target=test_add_todo_t2)
    test_thread.start()
    test_thread.join()
    logger_thread.run = False
    logger_thread.join()


if __name__ == "__main__":
    main()
