class A:
    def __init__(self, x):
        self.x = x
        self._x = x
        self.__x = x

a = A(1)

print(a.x) # 1
a.x = 2
print(a.x) # 2

print(a._x) # 1
a._x = 2
print(a._x) # 2

# print(a.__x) # AttributeError: 'A' object has no attribute '__x'
print(a._A__x) # 1
a._A__x = 2
print(a._A__x) # 2
