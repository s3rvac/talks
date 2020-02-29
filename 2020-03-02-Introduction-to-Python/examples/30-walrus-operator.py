# An example of using the "walrus operator" :=.
# Requires Python 3.8 or newer.

def process(block):
    print(len(block))

with open('30-walrus-operator.txt', 'r') as f:
    while block := f.read(256):
        process(block)

# In Python 3.7 or lower, you could write the code as:
#
# 1) This one duplicates the `f.read(256)` call:
print()
with open('30-walrus-operator.txt', 'r') as f:
    block = f.read(256)
    while block:
        process(block)
        block = f.read(256)

# 2) This one uses a `while True` loop:
print()
with open('30-walrus-operator.txt', 'r') as f:
    while True:
        block = f.read(256)
        if not block:
            break
        process(block)
