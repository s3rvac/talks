# What happens when you instantiate a class (a fuller version with a
# metaclass).

class Meta(type):
    def __new__(cls, name, bases, attrs):
        print('Meta.__new__()')
        return super().__new__(cls, name, bases, attrs)

    def __init__(self, name, bases, attrs):
        print('Meta.__init__()')
        return super().__init__(name, bases, attrs)

    def __call__(self, *args, **kwargs):
        print('Meta.__call__()')
        return super().__call__(*args, **kwargs)

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
