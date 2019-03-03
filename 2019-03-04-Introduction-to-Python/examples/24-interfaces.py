# Compare this with 24-protocols.py.

import collections.abc

class MySequence(collections.abc.Sequence):
    def __init__(self, content):
        self.content = content

    # Try commenting-out the following method to see what the program prints.
    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        return self.content[index]

s = MySequence([1, 2, 3])
for x in s:
    print(x) # Prints 1, 2, 3.
