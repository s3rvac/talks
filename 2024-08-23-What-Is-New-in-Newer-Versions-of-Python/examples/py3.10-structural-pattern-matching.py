#
# Python 3.10: Structural Pattern Matching
#
# - https://peps.python.org/pep-0634/ - Structural Pattern Matching: Specification
# - https://peps.python.org/pep-0635/ - Structural Pattern Matching: Motivation and Rationale
# - https://peps.python.org/pep-0636/ - Structural Pattern Matching: Tutorial
# - https://docs.python.org/3/reference/compound_stmts.html#the-match-statement
#

import dataclasses
import enum
import random

# ---- A basic example with an enum ----


class Colors(enum.Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


color = random.choice(list(Colors))
match color:  # subject
    case Colors.RED:
        print("So, you like the color red!")
    case Colors.GREEN:
        print("Green is a nice color!")
    case Colors.BLUE:
        print("Blue? Yuck!")
    case _:  # wildcard
        print("I don't know that color!")


# ---- A more elaborate example with a point ----


@dataclasses.dataclass
class Point:
    x: int
    y: int


# https://peps.python.org/pep-0636/#matching-multiple-values
# https://peps.python.org/pep-0636/#or-patterns
# https://peps.python.org/pep-0636/#capturing-matched-sub-patterns
# https://peps.python.org/pep-0636/#adding-conditions-to-patterns
# https://peps.python.org/pep-0636/#going-to-the-cloud-mappings
# https://peps.python.org/pep-0636/#matching-builtin-classes
# Matching objects
    # - https://peps.python.org/pep-0635/#patterns-and-functional-style
