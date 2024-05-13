# Creating a class manually via type().

class A:
    def foo(self):
        print('A.foo()')

a = A()
a.foo() # A.foo()

# How to create A without the 'class' keyword:

A = type('A', (object,), {'foo': lambda self: print('A.foo()')})

a = A()
a.foo() # A.foo()

# A bare minimum to create a class:
X = type('', (), {})
print(X) # <class '__main__.'>
