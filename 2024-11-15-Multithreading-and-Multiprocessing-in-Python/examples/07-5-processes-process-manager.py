import multiprocessing


def worker(results, i):
    results[f"x_{i}"] = i * 2


if __name__ == "__main__":
    manager = multiprocessing.Manager()
    results = manager.dict()

    with multiprocessing.Pool(5) as pool:
        pool.starmap(worker, [(results, i) for i in range(10)])

    print(dict(results))
