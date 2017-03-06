# Arithmetic:
print(10 * 'x') # xxxxxxxxxx
print(5 / 2)    # 2.5
print(5 // 2)   # 2
print(2 ** 8)   # 256

# Indexing:
list = [1, 2, 3, 4, 5]
print(list[0])   # 1
print(list[-1])  # 5
# print(list[99])  # IndexError: list index out of range

# Slicing:
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:4])   # [2, 3, 4]
print(list[1:])    # [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[:3])    # [1, 2, 3]
print(list[1:7:2]) # [2, 4, 6]
print(list[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list[:])     # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Logical:
a = 1
b = 2
print(a == 1 and b == 2) # True
print(1 and 2)           # 2
print(0 or 2)            # 2

# Assignment:
list1 = [1, 2, 3]
list2 = [4, 5]
# Beware that `list1 += list2` modifies the list in-place while `list1 = list1
# + list2` creates a new list:
print(id(list1)) # 140045417168968
list1 += list2
print(id(list1)) # 140045417168968
list1 = list1 + list2
print(id(list1)) # 140654991417864 (oops)

# in:
print(3 in [1, 2, 3, 4]) # True

# is:
a = [1, 2, 3]
a = b
print(a is b) # True

# Caching curiosity (unexpected behavior; run this in an interpreter):
# >>> a = 1
# >>> b = 1
# >>> a is b
# True
# >>> a = 300
# >>> b = 300
# >>> a is b
# False
#
# See http://stackoverflow.com/q/306313/2580955 and
# http://stackoverflow.com/q/15171695/2580955 for more details.
