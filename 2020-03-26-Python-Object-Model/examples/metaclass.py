# Metaclasses.

# Here is an example of a metaclass that prevents multiple inheritance.
# Based on https://www.youtube.com/watch?v=sPiWg5jSoZI.

class Java(type):
    def __new__(cls, name, bases, dict):
        if len(bases) > 1:
            raise TypeError('No way!')
        return super().__new__(cls, name, bases, dict)

class Base(metaclass=Java):
    ...

class A(Base): # OK
    ...

class B(Base): # OK
    ...

class C(A, B): # Raises TypeError('No way!')
    ...
