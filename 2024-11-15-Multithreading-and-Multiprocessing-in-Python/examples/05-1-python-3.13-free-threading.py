import threading

N = 12


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


threads = [
    threading.Thread(target=fib, args=(32,))
    for _ in range(N)
]
for t in threads:
    t.start()
for t in threads:
    t.join()
