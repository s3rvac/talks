#
# Exception Groups and except*
#
# - https://peps.python.org/pep-0654/
# - https://docs.python.org/3/library/exceptions.html#lib-exception-groups
# - https://docs.python.org/3/reference/compound_stmts.html#except-star
# - https://docs.python.org/3/tutorial/errors.html#tut-exception-groups
#

def f():
    excs = [OSError("error 1"), SystemError("error 2")]
    raise ExceptionGroup("multiple failures", excs)

# f()  # Uncomment to see the output.

# Handle all exceptions in the group:
try:
    f()
except Exception as e:
    print(f"caught {type(e)}: {e}")  # caught <class 'ExceptionGroup'>: (2 sub-exceptions)

# Handle only one of the exceptions in the group (notice that asterisk after `except`):
try:
    f()
except* OSError as e:
    print(f"caught {type(e)}: {e}")  # caught <class 'ExceptionGroup'>: (1 sub-exception)
except* SystemError as e:
    print(f"caught {type(e)}: {e}")  # caught <class 'ExceptionGroup'>: (1 sub-exception)
