# In Python, almost everything is an object. A few examples:

# Integers are objects, so you can, for example, call bit_length() to get the
# number of bits needed to store the number.
x = 256
print(x.bit_length()) # 9

# Even the ellipsis is an object. It can be used as a placeholder for missing
# code or in multidimensional slicings when using numpy.
x = ...
print(x) # Ellipsis

# Also function descriptions:
def factorial(n):
	"""Returns the factorial of n."""
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)

print(factorial.__doc__) # "Returns the factorial of n."

# You can also inspect and mess with bytecode:
def add(a, b):
    return a + b

import dis
dis.dis(add.__code__)
# Prints:
#
#  15           0 LOAD_FAST                0 (a)
#               2 LOAD_FAST                1 (b)
#               4 BINARY_ADD
#               6 RETURN_VALUE
