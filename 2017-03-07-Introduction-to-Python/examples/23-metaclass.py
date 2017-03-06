class A:
    def foo(self):
        print('A.foo()')

a = A()
print(type(a))    # <class '__main__.A'>
print(type(A))    # <class 'type'>
print(type(type)) # <class 'type'> (huh?)

# How to create a class without the 'class' keyword:

def A_foo(self):
    print('A.foo()')

A = type('A', (object,), {'foo': A_foo})
a = A()
a.foo() # A.foo()
