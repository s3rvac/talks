# Object in Python do not have a fixed layout.

class X:
    def __init__(self, a):
        self.a = a

x = X(1)
print(x.a) # 1

# For example, we can add new attributes to objects:
x.b = 5
print(x.b) # 5

# Or even new methods into a class:
X.foo = lambda self: 10
print(x.foo()) # 10

# Or even changing base classes during runtime (this is just for illustration,
# I do not recommend doing this in practice):

class A:
    def foo(self):
        return 1

class B(A):
    pass

class C:
    def foo(self):
        return 2

b = B()
print(b.foo(), B.__bases__) # 1 (<class '__main__.A'>,)
B.__bases__ = (C,)
print(b.foo(), B.__bases__) # 2 (<class '__main__.C'>,)
