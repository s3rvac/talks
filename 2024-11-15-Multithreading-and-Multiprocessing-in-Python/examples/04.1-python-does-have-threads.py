#
# A very simple example of using threads in Python.
#
# Illustrating that Python does have threads. If you want an additional proof,
# do some CPU-heavy work in the foo function and watch the task manager - you
# will see five thread running.
#

import threading


def foo():
    for i in range(10):
        print(f"thread {threading.get_native_id()} - {i}")


threads = [threading.Thread(target=foo) for _ in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
