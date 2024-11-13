#
# An example of using multiprocessing.Manager to share data between processes.
#

import multiprocessing


def worker(results, i):
    results[f"x_{i}"] = i * 2


if __name__ == '__main__':
    # Create a dictionary that can be shared between processes to store the
    # results of the workers.
    manager = multiprocessing.Manager()
    results = manager.dict()

    with multiprocessing.Pool(5) as pool:
        # Run the workers with the shared dictionary.
        pool.starmap(worker, [(results, i) for i in range(10)])

    print(dict(results))
