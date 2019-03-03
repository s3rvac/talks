# Acts like a sequence via the sequence protocol.
class MySequence:
    def __init__(self, content):
        self.content = content

    def __len__(self):
        return len(self.content)

    def __getitem__(self, index):
        return self.content[index]

s = MySequence([1, 2, 3])
for x in s:
    print(x) # Prints 1, 2, 3.
