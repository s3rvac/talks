#
# Experimental support for running without GIL
#
# (Requires a CPython build with the `--disable-gil` option. Try running the
# code with GIL enabled and disabled to see the difference in performance.)
#
# - https://docs.python.org/3.13/whatsnew/3.13.html#free-threaded-cpython
# - https://peps.python.org/pep-0703/
#
# Here is an example timing on my machine:
# - With GIL:    5.7 seconds
# - Without GIL: 1.9 seconds
#

import concurrent.futures

N = 12


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


with concurrent.futures.ThreadPoolExecutor(N) as executor:
    executor.map(fib, [32] * N)
