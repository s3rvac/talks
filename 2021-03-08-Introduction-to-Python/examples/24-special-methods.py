# A list that disallows assignments:
class MyList(list):
    def __setitem__(self, index, value):
        raise RuntimeError('assignment is not supported')

list = MyList([1, 2, 3])
print(list[0]) # 1
# list[0] = 2    # RuntimeError: assignment is not supported
