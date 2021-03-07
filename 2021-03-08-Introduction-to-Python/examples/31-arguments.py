def foo(x=[]):
    x.append(4)
    return x

print(foo([1, 2, 3])) # [1, 2, 3, 4]
print(foo())          # [4]
print(foo())          # [4, 4]

# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments
