# The underlying storage is a dict.

class X:
    def __init__(self, a):
        self.a = a

    def foo(self):
        return 42

print(X.__dict__) # {'__module__': '__main__', '__init__': <...>, 'foo': <...>, '__dict__': <...>, '__weakref__': <...>, '__doc__': None}
print(type(X.__dict__))  # <class 'mappingproxy'> (because it also looks at base classes)

x = X(1)
print(x.__dict__) # {'a': 1}
