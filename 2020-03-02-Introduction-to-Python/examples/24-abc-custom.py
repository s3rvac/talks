import abc

# Our custom abstract base class:
class Fooable(abc.ABC):
    # Alternatively, you can specify abc.ABCMeta as a metaclass
    # (see https://docs.python.org/3/library/abc.html#abc.ABC).

    @abc.abstractmethod
    def foo(self):
        """Returns the foo value (whatever that is)."""

class A(Fooable):
    def foo(self):
        return 1

class B(Fooable):
    def foo(self):
        return 2

class C(Fooable):
    # Does not provide foo().
    pass

a = A()
b = B()
# This fails as C does not provide foo():
# TypeError: Can't instantiate abstract class C with abstract methods foo
c = C()
