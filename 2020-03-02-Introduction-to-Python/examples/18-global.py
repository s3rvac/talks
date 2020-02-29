x = 1

def foo1():
    x = 2

foo1()
print(x) # 1

def foo2():
    global x
    x = 2

foo2()
print(x) # 2
