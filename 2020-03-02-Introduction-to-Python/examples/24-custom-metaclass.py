# From "B. Jones, D. Beazley: Python Cookbook, 3rd edition, 2013", section 9.17.

class NoMixedCaseMeta(type):
    def __new__(meta, name, bases, dict):
        for name in dict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name)
        return super().__new__(meta, name, bases, dict)

class Base(metaclass=NoMixedCaseMeta):
    pass

class A(Base):
    def foo_bar(self): # OK
        pass

class B(Base):
    def fooBar(self):  # TypeError
        pass
