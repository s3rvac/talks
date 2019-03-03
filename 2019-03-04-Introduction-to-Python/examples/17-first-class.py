def foo(n):
    return n + 1

print(foo(1)) # 2

# Assigning functions to variables:
bar = foo
print(bar(1)) # 2

# Passing functions as an argument:
def execute(func, arg):
    return func(arg)
print(execute(foo, 1)) # 2

# Creating functions during runtime:
def adder(n):
    def f(k):
        return k + n
    return f
g = adder(1)
print(g(5)) # 6
