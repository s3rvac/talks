class A:
    def __init__(self):
        print('__init__')

    def __del__(self):
        print('__del__')

x = A() # __init__
y = x
del x
print('x deleted')
del y   # __del__
