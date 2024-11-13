#
# An example of using a re-entrant/recursive lock in Python.
#
# Based on https://stackoverflow.com/a/16568426/2580955.
#

import threading


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.lock = threading.RLock()

    def changeA(self):
        with self.lock:
            self.a = self.a + 1

    def changeB(self):
        with self.lock:
            self.b = self.b + 1

    def changeAandB(self):
        with self.lock:
            self.changeA()  # A regular threading.Lock would block here.
            self.changeB()


x = MyClass(1, 2)
x.changeAandB()
