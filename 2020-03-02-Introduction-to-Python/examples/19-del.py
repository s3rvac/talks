x = 1
print(x) # 1
del x
print(x) # NameError: name 'x' is not defined

a = [1, 2, 3]
b = a
del a
print(b) # OK: [1, 2, 3]
del b
print(b) # NameError: name 'b' is not defined
