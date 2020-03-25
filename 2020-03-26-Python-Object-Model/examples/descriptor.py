# A simple example of a descriptor.

class MyDescriptor:
    def __get__(self, instance, owner=None):
        return f'__get__: {self}, {instance}, {owner}'

class A:
    x = MyDescriptor()

a = A()
print(a.x) # __get__: <__main__.MyDescriptor object>, <__main__.A object>, <class '__main__.A'>
print(A.x) # __get__: <__main__.MyDescriptor object>, None, <class '__main__.A'>
