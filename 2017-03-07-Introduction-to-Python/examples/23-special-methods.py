class MyList(list):
    def __setitem__(self, index, value):
        raise RuntimeError('cannot be indexed')

list = MyList([1, 2, 3])
print(list[0]) # 1
# list[0] = 2    # RuntimeError: cannot be indexed

class HasAll:
    def __getattr__(self, attr):
        print(str(attr))

x = HasAll()
x.foo # foo
x.bar # bar
