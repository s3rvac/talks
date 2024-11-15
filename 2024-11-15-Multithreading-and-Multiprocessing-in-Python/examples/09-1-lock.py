import concurrent.futures
import threading


lock = threading.Lock()
n = 0


def foo(_):
    global n
    new_n = 0
    for _ in range(100_000):
        new_n += 1

    with lock:
        n += new_n


with concurrent.futures.ThreadPoolExecutor(4) as pool:
    pool.map(foo, range(10))

assert n == 1_000_000, n
