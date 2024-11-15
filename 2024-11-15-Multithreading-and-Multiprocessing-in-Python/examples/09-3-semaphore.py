import concurrent.futures
import threading
import time


semaphore = threading.Semaphore(value=4)


def task(i):
    # ...
    with semaphore:
        print(threading.current_thread().name, i)

        # Just to see the effect in the output from the script.
        time.sleep(1)


with concurrent.futures.ThreadPoolExecutor(10) as pool:
    pool.map(task, range(100))
