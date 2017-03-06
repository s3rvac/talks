# Everything is an object, even integers:
a = 256
print(a.bit_length())

# ...and documentation strings:
def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial.__doc__)
