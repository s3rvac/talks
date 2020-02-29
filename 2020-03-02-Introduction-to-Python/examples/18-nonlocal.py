def bar1():
    x = 1
    def foo():
        x = 2
    foo()
    print(x)

bar1() # 1

def bar1():
    x = 1
    def foo():
        nonlocal x
        x = 2
    foo()
    print(x)

bar1() # 2
