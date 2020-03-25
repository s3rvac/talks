# Descriptors: The mechanism behind methods, properties, and static/class
# methods.

# Here is an example of manually creating the add() method from
# methods-vs-functions.py:

import types

class Method:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return types.MethodType(self.func, instance)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __repr__(self):
        return repr(self.func)

def X_add(self, other):
    return self.x + other.x

class X:
    def __init__(self, x):
        self.x = x

    add = Method(X_add)

a = X(1)
b = X(2)
print(a.add(b)) # 3
print(X.add(a, b)) # 3
print(X.add) # <function X_add at 0x7f379c37aee0>
print(a.add) # <bound method X_add of <__main__.X object at 0x7f379c3e7fa0>>

# (In reality, functions are descriptors by themselves, so it suffices to just
# create a function in a class and it will automatically be able to bind `self`
# and create `types.MethodType`.)
