# Bad:
f = open('file.txt', 'r')
contents = f.read()
f.close()

# Better:
f = open('file.txt', 'r')
try:
    contents = f.read()
finally:
    f.close()

# The best:
with open('file.txt', 'r') as f:
    contents = f.read()
