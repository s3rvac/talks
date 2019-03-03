# Cooperative multiple inheritance, mixins, super().

class WithX:
    def __init__(self):
        super().__init__()
        self.x = 1

class WithY:
    def __init__(self):
        super().__init__()
        self.y = 2

class A(WithX, WithY):
    def __init__(self, n):
        super().__init__()
        self.n = n

a = A(3)
print(A.__mro__) # (A, WithX, WithY, object)
print(a.x) # 1
print(a.y) # 2
print(a.n) # 3
