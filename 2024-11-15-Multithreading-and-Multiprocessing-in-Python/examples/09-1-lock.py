import concurrent.futures
import threading


lock = threading.Lock()
n = 0


def foo(_):
    global n
    for _ in range(100_000):
        with lock:
            n += 1


with concurrent.futures.ThreadPoolExecutor(4) as pool:
    pool.map(foo, range(10))

assert n == 1_000_000, n
