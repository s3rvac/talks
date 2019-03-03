class A:
    a = 1

    def __init__(self, b):
        self.b = b

x = A(1)
y = A(1)
print(x.a, x.b, y.a, y.b) # 1 1 1 1
x.b = 2
print(x.a, x.b, y.a, y.b) # 1 2 1 1
A.a = 3
print(x.a, x.b, y.a, y.b) # 3 2 3 1
