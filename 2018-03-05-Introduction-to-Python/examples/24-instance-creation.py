# For a full version of that also covers metaclasses, see 24-instance-creation-meta.py

class A:
    def __new__(cls, x):
        print('A.__new__()')
        return object.__new__(cls)

    def __init__(self, x):
        print('A.__init__()')
        self.x = x

# The following instantiation prints:
#
#     A.__new__()
#     A.__init__()
#
a = A(1)

print(a.x) # 1
