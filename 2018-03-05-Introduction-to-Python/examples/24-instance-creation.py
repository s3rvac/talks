class A:
    def __new__(cls, x):
        print('A.__new__()')
        return object.__new__(cls)

    def __init__(self, x):
        print('A.__init__()')
        self.x = x

a = A(1) # Prints A.__new__() and A.__init__().

print(a.x) # 1
