# Construction and finalization.

class A:
    # __new__() is a special-cased static method so you do not have to declare
    # it as such.
    def __new__(cls, a):
        print('A.__new__()')
        return super().__new__(cls)

    def __init__(self, a):
        print('A.__init__()')
        self.a = a

    def __del__(self):
        print('A.__del__()')

# The following piece of code prints:
#
#     A.__new__()
#     A.__init__()
#
a = A(1)

# The following piece of code MAY print:
#
#     A.__del__()
#
# It depends on the interpreter. For example, in CPython, which uses reference
# counting, it will print the string. However, in PyPy, which uses a
# full-fledged garbage collector, it will not print that.
del a
