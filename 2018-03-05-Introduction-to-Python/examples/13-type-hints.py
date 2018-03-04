# The presence of type hints has no effect on runtime whatsoever. It is used by
# source analyzers (e.g. http://mypy-lang.org/).
def hello(name: str) -> str:
    return f'Hello {name}'

hello('Joe') # Hello Joe
hello(5)     # Hello 5

# The type hints can be accessed via __annotations__:
print(hello.__annotations__) # {'name': <class 'str'>, 'return': <class 'str'>}

i: int = 'hey!' # OK
i = [1, 2, 3]   # OK
