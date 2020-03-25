# Methods vs functions.

class X:
    def __init__(self, x):
        self.x = x

    def add(self, other):
        return self.x + other.x

a = X(1)
b = X(2)
print(a.add(b)) # 3
print(X.add(a, b)) # 3
print(X.add) # <function X.add at 0x7f83bb046040>
print(a.add) # <bound method X.add of <__main__.X object at 0x7fa9414ee910>>
