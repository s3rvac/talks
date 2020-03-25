# Hooking into attribute access.

class X:
    a = 5

    def __init__(self, b):
        self.b = b

    def __getattr__(self, name):
        print('__getattr__', name)
        return name

    def __getattribute__(self, name):
        print('__getattribute__', name)
        return super().__getattribute__(name)

x = X(1)

# Prints:
# __getattribute__ a
# 5
print(x.a)

# Prints:
# __getattribute__ b
# 1
print(x.b)

# Prints:
# __getattribute__ c
# __getattr__ c
# c
print(x.c)
