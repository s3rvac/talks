# A more complex example of a descriptor: cached property.
#
# Note: The code below is for illustration purposes only. The full
# implementation (including thread safety) is here:
# https://github.com/python/cpython/blob/v3.12.3/Lib/functools.py#L958-L1006

_NOT_FOUND = object()

class cached_property:
    def __init__(self, func):
        self.func = func
        self.func_name = func.__name__

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        cached_value = instance.__dict__.get(self.func_name, _NOT_FOUND)
        if cached_value is _NOT_FOUND:
            cached_value = self.func(instance)
            instance.__dict__[self.func_name] = cached_value
        return cached_value

class A:
    @cached_property
    def value(self):
        print("Calculating the value...")
        return 42

a = A()
print(a.value) # Prints "Calculating the value..." followed by 42.
print(a.value) # Prints just 42.
