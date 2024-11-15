import threading
import time

task2_should_start_event = threading.Event()


def task1():
    print("Task 1: processing")
    time.sleep(1)
    print("Task 1: done")

    task2_should_start_event.set()


def task2():
    task2_should_start_event.wait()

    print("Task 2: processing")
    time.sleep(1)
    print("Task 2: done")


threads = [threading.Thread(target=task1), threading.Thread(target=task2)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
