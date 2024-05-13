# An example of a descriptor: a custom implementation of `property`
#
# Note: The code below is for illustration purposes only. The full
# implementation (including set or delete) is here:
# https://docs.python.org/3/howto/descriptor.html#properties

class property:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.func(instance)

class A:
    @property
    def name(self):
        return "John"

a = A()
print(a.name) # "John"
