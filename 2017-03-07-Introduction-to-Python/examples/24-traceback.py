def foo(x, i):
    def bar():
        return x[i]
    return bar()

print(foo([1, 2, 3], 4))
# Traceback (most recent call last):
#   File "24-traceback.py", line 6, in <module>
#     print(foo([1, 2, 3], 4))
#   File "24-traceback.py", line 4, in foo
#     return bar()
#   File "24-traceback.py", line 3, in bar
#     return x[i]
# IndexError: list index out of range
