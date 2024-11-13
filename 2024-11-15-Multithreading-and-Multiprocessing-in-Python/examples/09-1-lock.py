#
# An example of using a lock in Python to protect shared resources.
#

import concurrent.futures
import threading


lock = threading.Lock()
n = 0


def foo(i):
    # First, compute the new value in a local variable so that we do not have
    # hold the lock for too long.
    global n
    new_n = 0
    for _ in range(100_000):
        new_n += 1

    # Use the lock for atomic increment of the shared variable.
    with lock:
        n += new_n


with concurrent.futures.ThreadPoolExecutor(4) as pool:
    pool.map(foo, range(10))

assert n == 1_000_000, n
