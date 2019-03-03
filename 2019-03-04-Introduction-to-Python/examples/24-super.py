class A:
    def foo(self):
        print('A.foo()')

class B(A):
    def foo(self):
        print('B.foo()')
        super().foo()

class C(A):
    def foo(self):
        print('C.foo()')
        super().foo()

class D(B, C):
    def foo(self):
        print('D.foo()')
        super().foo()

x = D()
print(D.__mro__) # (D, B, C, A, object)
x.foo()          # Prints:
                 # D.foo()
                 # B.foo()
                 # C.foo()
                 # A.foo()
