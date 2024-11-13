#
# An example of communicating between threads using shared memory.
#

import threading
import time

requests = 0


def monitor_progress():
    last_requests = requests
    while True:
        print(f"{requests - last_requests} req/s")
        last_requests = requests
        time.sleep(1)


# Start the monitoring thread in the background.
threading.Thread(target=monitor_progress, daemon=True).start()

while True:
    # Simulate requests by incrementing the counter.
    requests += 1
    time.sleep(0.001)
