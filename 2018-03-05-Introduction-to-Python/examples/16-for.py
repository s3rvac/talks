colors = ['red', 'green', 'blue']

# Good (idiomatic):
for color in colors:
    print(color)

# Bad (unidiomatic, don't do that):
for i in range(len(colors)):
    print(colors[i])
