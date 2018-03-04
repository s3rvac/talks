# Hooking into attribute lookup.

class HasAllAttrs:
    def __init__(self, n):
        self.n = n

    def __getattr__(self, name):
        return name

x = HasAllAttrs(1234)
print(x.n)   # 1234
print(x.foo) # foo
print(x.bar) # bar

# We can also hook into the lookup of all attributes by overriding
# __getattribute__() instead of __getattr__().
# Be careful with this though!
class HasAllAttrs2:
    def __init__(self, n):
        self.n = n

    def __getattribute__(self, name):
        return name

x = HasAllAttrs2(1234)
print(x.n)   # n
print(x.foo) # foo
print(x.bar) # bar
