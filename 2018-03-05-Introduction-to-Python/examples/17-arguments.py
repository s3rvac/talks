def add(a=0, b=0):
    return a + b

# Default arguments:
print(add(1, 2)) # 3
print(add(1))    # 1
print(add())     # 0

# Keyword arguments:
print(add(1, b=1)) # 2
print(add(b=1))    # 1

# Variable-length arguments:
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(sum(1, 2, 3, 4)) # 10

# Variable-length arguments, including keyword arguments:
def foo(*args, **kwargs):
    print(args, kwargs)

foo(1, 2, a=5, b=6) # (1, 2) {'a': 5, 'b': 6}
