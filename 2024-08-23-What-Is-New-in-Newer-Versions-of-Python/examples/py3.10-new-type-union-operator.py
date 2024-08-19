#
# Python 3.10: New Type Union Operator
#
# - https://peps.python.org/pep-0604/ - New Type Union Operator
# - https://docs.python.org/3/library/stdtypes.html#types-union
#

# Equivalent of `x: typing.Union[int, str]`.
def foo(x: int | str):
    ...

# Equivalent of `x: typing.Optional[int]`.
def bar(x: int | None):
    ...

# Can be used for isinstance() and issubclass():
isinstance(5, int | str)
issubclass(bool, int | float)

# There is no magic; it calls `type.__or__()` and returns `typing.Union`.
print(int | str)  # "int | str"
print(type(int | str))  # <class 'types.UnionType'>
