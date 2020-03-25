# The basics.

import math

class GeometricObject:
    ...

class Circle(GeometricObject):
    """A representation of a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return 2 * self.radius

    @classmethod
    def unit_circle(cls):
        return cls(1)

c1 = Circle(10)
print(c1.radius) # 10
print(c1.area()) # 314.1592653589793
print(c1.diameter) # 20

c2 = Circle.unit_circle()
print(c2.radius) # 1
