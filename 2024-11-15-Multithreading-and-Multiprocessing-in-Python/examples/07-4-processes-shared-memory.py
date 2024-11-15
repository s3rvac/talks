import multiprocessing


def init_worker(results):
    global shared_results
    shared_results = results


def worker(i):
    shared_results[i] = i * 2


if __name__ == "__main__":
    N = 5

    results = multiprocessing.Array("i", N)

    with multiprocessing.Pool(N, initializer=init_worker, initargs=(results,)) as pool:
        pool.map(worker, range(N))
        print(list(results))
