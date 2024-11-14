#
# An example of iheriting from threading.Thread.
#

import threading


class MyThread(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    # This method is called when the thread is started.
    def run(self):
        for i in range(10):
            print(f"thread {self.id} - {i}")


threads = [MyThread(id) for id in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
