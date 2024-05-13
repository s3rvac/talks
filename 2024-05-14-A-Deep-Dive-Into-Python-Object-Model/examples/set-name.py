# An example of using __set_name__. It can be used for descriptors to
# automatically detect the name of the attribute they have been assigned to.

class X:
    def __set_name__(self, owner, name):
        print(f'owner: {owner}, name: {name!r}')

class A:
    a = X() # owner: <class '__main__.A'>, name: 'a'
    b = X() # owner: <class '__main__.A'>, name: 'b'
    c = X() # owner: <class '__main__.A'>, name: 'c'
