def foo1():
    x = 1
    print(x)

foo1() # 1

def foo2():
    print(x)

x = 2
foo2() # 2

def bar():
    x = 3
    def foo3():
        print(x)
    foo3()

bar() # 3

def foo4():
    print(id)

foo4() # <built-in function id>

# if, for, etc. do not introduce a new scope:
def foo5(i):
    if i > 2:
        x = 5
    print(x)

foo5(4) # 5
# foo5(2) # UnboundLocalError: local variable 'x' referenced before assignment

# This can lead to unexpected behavior:
def foo6():
    for k in [1, 2, 3]:
        ...
    print(k)

foo6() # 3
