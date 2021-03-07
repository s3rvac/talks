# A full version of 24-instance-creation.py that also covers metaclasses.

class Meta(type):
    def __new__(meta, name, bases, dict):
        print('Meta.__new__()')
        return super().__new__(meta, name, bases, dict)

    def __init__(self, name, bases, dict):
        print('Meta.__init__()')
        return super().__init__(name, bases, dict)

    def __call__(self, n):
        print('Meta.__call__()')
        return super().__call__(n)

# The following creation of A prints:
#
#   Meta.__new__()
#   Meta.__init__()
#
class A(metaclass=Meta):
    def __new__(cls, n):
        print('A.__new__()')
        return super().__new__(cls)

    def __init__(self, n):
        print('A.__init__()')
        self.n = n

print()

# The following instantiation prints:
#
#     Meta.__call__()
#     A.__new__()
#     A.__init__()
#
a = A(1)
