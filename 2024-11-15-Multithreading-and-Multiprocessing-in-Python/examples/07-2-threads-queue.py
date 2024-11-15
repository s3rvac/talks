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


if __name__ == "__main__":
    q = queue.Queue()

    threading.Thread(target=worker, args=(q,), daemon=True).start()

    for item in range(20):
        q.put(item)

    q.join()
