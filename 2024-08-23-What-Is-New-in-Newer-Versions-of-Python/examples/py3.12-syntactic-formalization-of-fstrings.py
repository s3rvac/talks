#
# Syntactic formalization of f-strings
#
# - https://docs.python.org/3/whatsnew/3.12.html#whatsnew312-pep701
# - https://peps.python.org/pep-0701/
#

# 1) Your can now reuse the same quote character in an f-string.
friends = ["Alice", "Bob", "Charlie"]
print(f"My friends: {", ".join(friends)}")

# 2) You can arbitrarily nest f-strings (previously, you needed to use a
# different quote for each f-string occurrence).
print(f"{f"{f"{f"{f"{f"{1+1}"}"}"}"}"}")

# 3) You can now create an f-string spanning multiple lines and including
# comments.
print(f"My friends: {", ".join([
    "Alice",    # My best friend
    'Bob',      # My second best friend
    'Charlie',  # I don't like him
])}")

# 4) You can now use backslashes in an f-string.
print(f"{"\n".join(["Alice", "Bob", "Charlie"])}")
