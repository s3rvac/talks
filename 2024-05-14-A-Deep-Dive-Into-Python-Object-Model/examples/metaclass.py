# Metaclasses.

# Here is an example of a metaclass that prevents multiple inheritance.
# Based on https://www.youtube.com/watch?v=sPiWg5jSoZI.

class JavaMeta(type):
    def __new__(cls, name, bases, attrs):
        if len(bases) > 1:
            raise TypeError('No way!')
        return super().__new__(cls, name, bases, attrs)

class Base(metaclass=JavaMeta):
    ...

class A(Base): # OK
    ...

class B(Base): # OK
    ...

class C(A, B): # Raises TypeError('No way!')
    ...
