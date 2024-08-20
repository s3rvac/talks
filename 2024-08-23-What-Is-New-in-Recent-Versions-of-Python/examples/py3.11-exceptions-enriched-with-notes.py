#
# Exceptions can be enriched with notes
#
# - https://peps.python.org/pep-0678/
# - https://docs.python.org/3/tutorial/errors.html#tut-exception-notes
#

try:
    raise ValueError("some error message")
except Exception as e:
    e.add_note("Some useful information")
    raise
