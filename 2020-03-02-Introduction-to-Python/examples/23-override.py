class A:
    def foo(self):
        print('A')

class B(A):
    def foo(self):
        print('B')

x = B()
x.foo() # B
