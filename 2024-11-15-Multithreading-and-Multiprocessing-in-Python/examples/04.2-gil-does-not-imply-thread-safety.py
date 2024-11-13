#
# An illustration that the Global Interpreter Lock (GIL) does not imply thread
# safety.
#
# To make the issue more likely to occur, we decrease the thread-switch
# interval (from 0.005 to 0.001) + I recommend to run this script with PyPy
# instead of CPython (it has GIL as well).
#

import threading
import sys


# Decrease the thread-switch interval to make the issue more likely to occur.
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
