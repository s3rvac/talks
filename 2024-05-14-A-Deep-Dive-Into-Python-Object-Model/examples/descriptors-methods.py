# Descriptors: The mechanism behind methods, properties, and static/class
# methods.

# Here is a contrived example of manually creating a method.

import types

class Method:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner=None):
        if instance is None:
            return self.func
        return types.MethodType(self.func, instance)

def foo(self):
    return 42

class A:
    foo = Method(foo)

a = A()
print(a.foo()) # 42
print(A.foo(a)) # 42
print(A.foo) # <function foo at 0x7e201f7da2a0>
print(a.foo) # <bound method foo of <__main__.A object at 0x7b4638993140>>

# (In reality, functions are descriptors by themselves, so it suffices to just
# create a function in a class and it will automatically be able to bind `self`
# and create `types.MethodType`.)
