import sys

class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class B:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(1, 2)
assert '__dict__' in dir(a)

# 'b' will have a lower memory footprint and provide faster attribute access
# than 'a' due to the use of __slots__:
b = B(1, 2)
assert '__dict__' not in dir(b)
