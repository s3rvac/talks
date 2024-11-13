#
# An example of using a thread pool via the multiprocessing module.
#

import multiprocessing.pool


def foo(i):
    # Do some work...
    return i, i * 2


# Create a pool of 5 threads and run foo in it.
with multiprocessing.pool.ThreadPool(5) as pool:
    results = pool.map(foo, range(10))
    for i, result in results:
        print(f"foo({i}) = {result}")
