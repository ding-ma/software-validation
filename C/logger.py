import os
import csv
import psutil
from time import sleep, time


def logger():
    log = open(os.path.join("test_data", "system_logs.csv"), "w", newline='')
    log_writer = csv.writer(log)
    log_writer.writerow(["time", "cpu_usage(%)", "used_memory", "free_memory"])

    while True:
        # process = psutil.Process(get_jar_pid())
        now = time()
        cpu_usage = psutil.cpu_percent()
        log_writer.writerow([now, cpu_usage,  psutil.virtual_memory().used, psutil.virtual_memory().free])
        sleep(0.015)
    log.close()


logger()
