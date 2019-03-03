# The presence of type hints has no effect on runtime whatsoever. It is used by
# source analyzers (e.g. http://mypy-lang.org/).
#
# Requires Python >= 3.5.
def hello(name: str) -> str:
    return 'Hello {}'.format(name)

hello('Joe') # Hello Joe
hello(5)     # Hello 5

# The type hints can be accessed via __annotations__:
print(hello.__annotations__) # {'name': <class 'str'>, 'return': <class 'str'>}

# Requires Python >= 3.6:
i: int = 'hey!' # OK
i = [1, 2, 3]   # OK
