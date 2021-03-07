# Based on https://en.wikipedia.org/wiki/Duck_typing#In_Python

class Duck:
    def quack(self):
        print("quack quack")

class Person:
    def quack(self):
        print("faked quack quack")

def in_forest(duck):
    duck.quack()

in_forest(Duck())   # prints "quack quack"
in_forest(Person()) # prints "faked quack quack"
