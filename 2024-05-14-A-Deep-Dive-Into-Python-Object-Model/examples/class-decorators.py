# An example of a class decorator.

import functools
import inspect

def debug_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('DEBUG:', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper

def debug_methods(cls):
    for key, value in vars(cls).items():
        if inspect.isfunction(value):
            setattr(cls, key, debug_func(value))
    return cls

@debug_methods
class A:
    def foo(self):
        return 1

    def bar(self):
        return 2

a = A()
a.foo() # DEBUG: foo (<__main__.A object at 0x7f7dff7dcd30>,) {}
a.bar() # DEBUG: bar (<__main__.A object at 0x7f7dff7dcd30>,) {}
