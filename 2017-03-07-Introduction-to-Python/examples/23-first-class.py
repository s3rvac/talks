class Point:
    ...

# Python classes are first-class objects. For example, you can assign them to
# variables:

P = Point
print(P()) # <__main__.Point object at 0x7fc1f458c400>

# Pass them to other functions:
def create(cls):
    return cls()

p = create(Point)
print(p) # <__main__.Point object at 0x7fc6b516d4a8>

# Create them during runtime and return them:
def foo():
    class Point2:
        ...

    return Point2

P = foo()
print(P()) # <__main__.foo.<locals>.Point2 object at 0x7f5cf0ae3ac8>
