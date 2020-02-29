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
    def bar(self):
        print('D.bar()')

x = D()
print(D.__mro__) # (D, B, C, A, object)
x.bar()          # D.bar()
x.foo()          # B.foo()
