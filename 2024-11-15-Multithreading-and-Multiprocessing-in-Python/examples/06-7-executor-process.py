#
# An example of using a process pool executor.
#

import concurrent.futures


def foo(i):
    # Do some work...
    return i, i * 2


# Create a pool of 5 processes and run foo in it.
with concurrent.futures.ProcessPoolExecutor(5) as pool:
    results = pool.map(foo, range(10))
    for i, result in results:
        print(f"foo({i}) = {result}")

# Apart from map(), there is also submit() (but that's it). The main difference
# between the concurrent.futures and multiprocessing modules is that the former
# works through futures.
