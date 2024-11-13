#
# An example of using a process pool via the multiprocessing module.
#

import multiprocessing


def foo(i):
    # Do some work...
    return i, i * 2


# Create a pool of 5 processes and run foo in it.
with multiprocessing.Pool(5) as pool:
    results = pool.map(foo, range(10))
    for i, result in results:
        print(f"foo({i}) = {result}")

# Available pool methods:
# - apply()
# - apply_async()
# - map()
# - map_async()
# - imap()
# - imap_unordered()
# - starmap()
# - starmap_async()
#
# See https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing.pool
