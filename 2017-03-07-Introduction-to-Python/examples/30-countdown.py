def countdown(n):
    print('starting to count from', n)
    while n > 0:
        yield n
        n -= 1
    print('done')

c = countdown(5)
print(c)       # <generator object countdown at 0x7fc2fb7744c0>
x = next(c)    # starting to count from 5
print(x)       # 5
print(next(c)) # 4
print(next(c)) # 3
print(next(c)) # 2
print(next(c)) # 1
next(c)        # done, StopIteration
