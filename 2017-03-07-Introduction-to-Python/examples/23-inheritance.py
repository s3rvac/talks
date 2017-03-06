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
    def foo(self):
        print('D.foo()')

x = D()
print(D.__mro__) # (D, B, C, A, object)
x.foo()          # D.foo()
