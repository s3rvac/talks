class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <= 0:
            raise ValueError('age has to be positive')
        self._age = new_age


p = Person('John', 30)
print(p.age)
p.age = -1 # Raises ValueError.
