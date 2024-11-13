#
# An example of using a threading condition variable in Python.
#
# Based on the example on
# https://docs.python.org/3/library/threading.html#condition-objects.
#
# This would be better done via e.g. queue.Queue, so treat the following
# example as just an illustration.
#

import threading
import random
import time

items = []
cv = threading.Condition()


def produce_item():
    item = random.randint(1, 100)
    items.append(item)
    print(f"Produced item {item}")


def is_an_item_available():
    return bool(items)


def consume_item():
    item = items.pop()
    print(f"Consumed item {item}")


def producer():
    while True:
        with cv:
            produce_item()
            cv.notify()
        time.sleep(random.random())


def consumer():
    while True:
        with cv:
            cv.wait_for(is_an_item_available)
            consume_item()


producer_thread = threading.Thread(target=producer)
producer_thread.start()

consumer_thread = threading.Thread(target=consumer, daemon=True)
consumer_thread.start()

producer_thread.join()
