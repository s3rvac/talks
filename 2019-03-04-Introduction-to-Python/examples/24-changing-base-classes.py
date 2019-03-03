# Changing base classes during runtime (just for illustration, I do not
# recommend doing this in practice):

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
