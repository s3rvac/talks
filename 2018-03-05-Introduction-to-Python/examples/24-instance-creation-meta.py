# A full version of 24-instance-creation.py that also covers metaclasses.

class Meta(type):
    def __new__(meta, name, bases, dict):
        print('Meta.__new__()')
        return type.__new__(meta, name, bases, dict)

    def __init__(cls, name, bases, dict):
        print('Meta.__init__()')
        return type.__init__(cls, name, bases, dict)

    def __call__(cls, n):
        print('Meta.__call__()')
        return type.__call__(cls, n)

# The following creation of A prints:
#
#   Meta.__new__()
#   Meta.__init__()
#
class A(metaclass=Meta):
    def __new__(cls, x):
        print('A.__new__()')
        return object.__new__(cls)

    def __init__(self, x):
        print('A.__init__()')
        self.x = x

print()

# The following instantiation prints:
#
#     Meta.__call__()
#     A.__new__()
#     A.__init__()
#
a = A(1)
