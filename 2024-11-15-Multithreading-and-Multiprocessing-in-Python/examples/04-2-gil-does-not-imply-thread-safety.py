import threading
import sys


sys.setswitchinterval(0.001)

n = 0


def foo():
    global n
    for _ in range(1_000_000):
        n += 1


threads = [threading.Thread(target=foo) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

assert n == 10_000_000, n
