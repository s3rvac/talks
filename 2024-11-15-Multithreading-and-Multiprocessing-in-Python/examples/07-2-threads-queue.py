#
# An example of using queue.Queue for thread-safe communication between
# threads.
#

import threading
import queue
import time


def worker(q):
    while True:
        task = q.get()

        # Simulate the processing of the task.
        time.sleep(0.1)
        print(f"Processed task {task}")

        q.task_done()


def main():
    q = queue.Queue()

    # Start the worker thread in the background.
    threading.Thread(target=worker, args=(q,), daemon=True).start()

    # Send twenty task requests to the worker.
    for item in range(20):
        q.put(item)

    # Wait until all the tasks are done.
    q.join()


if __name__ == "__main__":
    main()
