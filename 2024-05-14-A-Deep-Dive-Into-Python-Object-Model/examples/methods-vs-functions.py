# Methods vs functions.

class A:
    def foo(self):
        return 42

a = A()
print(a.foo()) # 42
print(A.foo(a)) # 42
print(A.foo) # <function A.foo at 0x7e87b2245300>
print(a.foo) # <bound method A.foo of <__main__.A object at 0x7fa77c3305c0>>
