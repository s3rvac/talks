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

# A basic example with an enum.


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


# A more elaborate example with a point.


@dataclasses.dataclass
class Point:
    x: int
    y: int


p = Point(10, 5)
match p:
    case Point(0, 0):
        print("Origin")
    case Point(x, y) if x == y:  # Capture pattern + a guard condition.
        print(f"Y=X at {x}")
    case Point(0, x) | Point(x, 0):  # Multiple patterns.
        print(f"Point on an axis at {x}")


# Matching a built-in type.


d = {"name": "Petr", "age": 30, "city": "Brno"}
match d:
    case {"name": "Petr", "age": age}:
        print(f"The chosen one, Petr, is {age} years old.")
    case {"name": name, "age": age} if age > 40:
        print(f"Whoa, {name} is very old!")
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old.")
