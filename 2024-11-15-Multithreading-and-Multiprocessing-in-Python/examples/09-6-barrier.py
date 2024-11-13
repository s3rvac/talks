#
# An example of using a threading barrier in Python.
#

import datetime
import random
import threading
import time

barrier = threading.Barrier(5)


def foo(i):
    time.sleep(random.randint(1, 10))
    print(f"{datetime.datetime.now()}: thread {i} woke up")
    barrier.wait()
    print(f"{datetime.datetime.now()}: thread {i} passed the barrier")


threads = [threading.Thread(target=foo, args=(i,)) for i in range(1, 6)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
