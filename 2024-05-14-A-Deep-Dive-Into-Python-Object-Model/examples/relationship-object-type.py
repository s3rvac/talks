# The mysterious relationship between object and type.

# Everything inherits from `object`, including the default metaclass `type`:
print(type.__bases__) # (<class 'object'>,)

# However, the type of `object` is `type` as `type` is the default metaclass:
print(type(object)) # <class 'type'>

# Kind of a chicken-an-egg problem, right? :)
