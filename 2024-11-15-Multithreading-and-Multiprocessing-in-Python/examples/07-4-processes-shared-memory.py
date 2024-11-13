#
# An example of using shared memory to share data between processes.
#

import multiprocessing


def init_worker(results):
    global shared_results
    shared_results = results


def worker(i):
    shared_results[i] = i * 2


if __name__ == "__main__":
    N = 5

    # Create a shared memory object.
    results = multiprocessing.Array("i", N)

    # We need to pass the results variable to the workers via an initializer;
    # passing it as an argument to the worker fails with the following error:
    #
    #   RuntimeError: SynchronizedArray objects should only be shared between
    #   processes through inheritance
    #
    with multiprocessing.Pool(N, initializer=init_worker, initargs=(results,)) as pool:
        # Run the workers with the shared array.
        pool.map(worker, range(N))

        # Print the results.
        print(list(results))
