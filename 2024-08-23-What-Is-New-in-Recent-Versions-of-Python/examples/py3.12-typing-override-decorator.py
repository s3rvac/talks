#
# typing.override() decorator
#
# - https://peps.python.org/pep-0698/
# - https://typing.readthedocs.io/en/latest/spec/class-compat.html#override
#

import typing


class A:
    def method(self) -> str: ...


class B(A):
    # Type check error: "Method method overrides class A in an incompatible manner".
    @typing.override
    def method(self, x: int) -> str: ...


# Note: There is also a `typing.final` decorator from PEP 591.
# https://typing.readthedocs.io/en/latest/spec/qualifiers.html#at-final
@typing.final
class Final: ...


# Type check error: "Base class Final is marked final and cannot be subclassed".
class Derived(Final): ...
