import multiprocessing


def foo(i):
    print(i)


if __name__ == "__main__":
    processes = [multiprocessing.Process(target=foo, args=(i,)) for i in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.terminate()

    for p in processes:
        p.join()
