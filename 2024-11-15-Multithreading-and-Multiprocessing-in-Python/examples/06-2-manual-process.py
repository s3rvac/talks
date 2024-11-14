#
# An example of creating processes manually.
#

import multiprocessing


def foo(i):
    print(i)


if __name__ == '__main__':
    processes = [multiprocessing.Process(target=foo, args=(i,)) for i in range(5)]

    # Start running all processes.
    for p in processes:
        p.start()

    # You can terminate processes via terminate() / kill().
    for p in processes:
        p.terminate()

    # Wait until all processes are done.
    for p in processes:
        p.join()
