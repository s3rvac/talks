#
# An example of using a threading event in Python.
#

import threading
import time

task2_should_start_event = threading.Event()


def task1():
    # ... simulate some work by sleeping
    print("Task 1: processing")
    time.sleep(1)
    print("Task 1: done")

    # Signal the other thread that it can start processing the second task.
    task2_should_start_event.set()


def task2():
    # Wait until we can start processing the task.
    task2_should_start_event.wait()

    # ... simulate some work by sleeping
    print("Task 2: processing")
    time.sleep(1)
    print("Task 2: done")


threads = [threading.Thread(target=task1), threading.Thread(target=task2)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
