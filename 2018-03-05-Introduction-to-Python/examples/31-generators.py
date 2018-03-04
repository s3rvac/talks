def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print(next(fib)) # 0
print(next(fib)) # 1
print(next(fib)) # 1
print(next(fib)) # 2
print(next(fib)) # 3
print(next(fib)) # 5
print(next(fib)) # 8
