class A:
    def foo(self):
        print('A.foo()')

x = A()
y = A()
x.foo() # A.foo()
y.foo() # A.foo()

def foo2(self):
    print('A.foo2()')
A.foo2 = foo2
x.foo2() # A.foo2()
y.foo2() # A.foo2()
