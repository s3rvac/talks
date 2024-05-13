# An example showing that that one can use keyword arguments in a class.

class Meta(type):
    def __new__(meta, name, bases, dct, **kwargs):
        print(kwargs)

class A(metaclass=Meta, a=1, b=2): # Prints {'a': 1, 'b': 2}
    pass
