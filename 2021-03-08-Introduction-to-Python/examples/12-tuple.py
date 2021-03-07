t = ('Cabernet Sauvignon', 1995)
print(t[0])  # Cabernet Sauvignon
t[0] = 'xxx' # TypeError: 'tuple' object does not support item assignment

# A singleton tuple:
x = (1,)
