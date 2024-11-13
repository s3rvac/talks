#
# An example of creating threads manually.
#

import threading


def foo(i):
    print(i)


threads = [threading.Thread(target=foo, args=(i,)) for i in range(5)]

# Start running all threads.
for t in threads:
    t.start()

# Wait until all threads are done.
for t in threads:
    t.join()
