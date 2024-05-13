# An example of using custom class parameters.

class Base:
    @classmethod
    def __init_subclass__(cls, x):
        super().__init_subclass__()
        cls.x = x

class A(Base, x=10):
    pass

print(A.x)
