#
# Type parameter syntax
#
# - https://peps.python.org/pep-0695/
# - https://typing.readthedocs.io/en/latest/spec/generics.html#variance-inference
# - https://typing.readthedocs.io/en/latest/spec/aliases.html#type-aliases
# - https://docs.python.org/3/reference/compound_stmts.html#type-params
# - https://docs.python.org/3/reference/simple_stmts.html#type
# - https://docs.python.org/3/reference/executionmodel.html#annotation-scopes
#

# A generic class (`str` is the upper-bound type).
class A[T: str]:
    def method(self) -> T: ...


# A generic function.
def foo[T](a: T, b: T) -> T: ...


# A non-generic type alias.
type IntOrStr = int | str

# A generic type alias.
type ListOrSet[T] = list[T] | set[T]
