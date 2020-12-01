from threading import Thread, currentThread
from time import sleep, time
import psutil
import csv
import os

from tests.todo.test_delete_todo import test_delete_todo
from tests.todo.test_add_todo import test_add_todo
from tests.todo.test_change_todo import test_change_todo

from tests.project.test_delete_project import test_delete_project
from tests.project.test_add_project import test_add_project
from tests.project.test_change_project import test_change_project

from tests.context.test_delete_category import test_delete_category
from tests.context.test_add_category import test_add_category
from tests.context.test_change_category import test_change_category


# def get_jar_pid():
#     for p in psutil.process_iter(attrs=None, ad_value=None):
#         if p.name == "java.exe":
#             return p.pid
#     return None


def logger():
    log = open(os.path.join("test_data", "system_logs.csv"), "w", newline='')
    log_writer = csv.writer(log)
    log_writer.writerow(["time", "cpu_usage(%)", "used_memory", "free_memory"])

    while getattr(currentThread(), "run", True):
        # children = psutil.Process().children(recursive=True)
        # for process in children:
        #     print(process)
        # process = psutil.Process(get_jar_pid())
        now = time()
        cpu_usage = psutil.cpu_percent()
        log_writer.writerow([now, cpu_usage,  psutil.virtual_memory().used, psutil.virtual_memory().free])
        sleep(0.02)
    log.close()


def main():
    logger_thread = Thread(target=logger)
    logger_thread.start()

    print("Starting Test ---- Test Add Category")
    # test_add_category()
    create_category = Thread(target=test_add_category)
    create_category.start()
    create_category.join()

    print("Starting Test ---- Test Change Category")
    # test_change_category()
    change_category = Thread(target=test_change_category)
    change_category.start()
    change_category.join()

    print("Starting Test ---- Test Delete Category")
    # test_delete_category()
    delete_category = Thread(target=test_delete_category)
    delete_category.start()
    delete_category.join()

    print("Starting Test ---- Test Add Project")
    # test_add_project()
    create_project = Thread(target=test_add_project)
    create_project.start()
    create_project.join()
    #
    # print("Starting Test ---- Test Change Project")
    # # test_change_project()
    # change_project = Thread(target=test_change_project)
    # change_project.start()
    # change_project.join()
    #
    # print("Starting Test ---- Test Delete Project")
    # # test_delete_project()
    # delete_project = Thread(target=test_delete_project)
    # delete_project.start()
    # delete_project.join()
    #
    # print("Starting Test ---- Test Add Todo")
    # # test_add_todo()
    # create_todo = Thread(target=test_add_todo)
    # create_todo.start()
    # create_todo.join()
    #
    # print("Starting Test ---- Test Change Todo")
    # # test_change_todo()
    # change_todo = Thread(target=test_change_todo)
    # change_todo.start()
    # change_todo.join()
    #
    # print("Starting Test ---- Test Delete Todo")
    # # test_delete_todo()
    # delete_todo = Thread(target=test_delete_todo)
    # delete_todo.start()
    # delete_todo.join()

    logger_thread.run = False
    logger_thread.join()




if __name__ == "__main__":
    main()
