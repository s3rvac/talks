#
# An example of using a semaphore in Python.
#

import concurrent.futures
import threading
import time


semaphore = threading.Semaphore(value=4)


def task(i):
    # ...
    #
    # As part of the task, do something for which we want to limit the number
    # of concurrent accesses to 4, e.g. perform an API request to a service
    # that imposes a maximal number of concurrent requests.
    with semaphore:
        # Just print something here to have some output.
        print(threading.current_thread().name, i)

        # Just to see the effect in the output from the script.
        time.sleep(1)


with concurrent.futures.ThreadPoolExecutor(10) as pool:
    pool.map(task, range(100))
