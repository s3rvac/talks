import concurrent.futures

N = 12


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


with concurrent.futures.ThreadPoolExecutor(N) as executor:
    executor.map(fib, [32] * N)
