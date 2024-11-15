import threading


def foo(i):
    print(i)


threads = [threading.Thread(target=foo, args=(i,)) for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()
