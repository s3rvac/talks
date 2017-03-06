def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Python functions are first-class objects. For example, you can assign them to
# variables:

f = factorial
print(f(5)) # 120

# Pass them to other functions:
def execute(f, x):
    return f(x)

x = execute(factorial, 5)
print(x) # 120

# Create them during runtime and return them:
def create(i):
    def add(n):
        return n + i
    return add

adder = create(1)
print(adder(5)) # 6
