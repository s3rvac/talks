import concurrent.futures
import functools

@functools.cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)

with concurrent.futures.ThreadPoolExecutor(20) as pool:
    pool.map(fib, [35] * 20)
