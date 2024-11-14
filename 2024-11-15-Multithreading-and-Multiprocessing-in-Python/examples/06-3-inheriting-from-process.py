#
# An example of iheriting from multiprocessing.Process.
#

import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, id):
        super().__init__()
        self.id = id

    # This method is called when the process is started.
    def run(self):
        for i in range(10):
            print(f"process {self.id} - {i}")


processes = [MyProcess(id) for id in range(5)]

for p in processes:
    p.start()

for p in processes:
    p.join()
