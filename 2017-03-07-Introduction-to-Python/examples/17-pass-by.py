def foo(x):
    x = 4

a = 1
foo(a)
print(a)  # 1

def bar(list):
    list.append(4)

b = [1, 2, 3]
bar(b)
print(b)  # [1, 2, 3, 4]
