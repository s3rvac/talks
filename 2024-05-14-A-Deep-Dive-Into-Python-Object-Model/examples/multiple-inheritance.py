# Multiple inheritance and MRO.

class A:
    def foo(self):
        print('A.foo()')

class B(A):
    def foo(self):
        print('B.foo()')

class C(A):
    def foo(self):
        print('C.foo()')

class D(B, C):
    def foobar(self):
        print('D.foobar()')

d = D()
print(D.__mro__) # (D, B, C, A, object)
d.foobar() # D.foobar()
d.foo() # B.foo()
