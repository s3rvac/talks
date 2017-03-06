# Note: This script is just an illustration. It contains a very simple solution
# to the problem, which is far from perfect.

import sys

if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
    print(f'usage: {sys.argv[0]} FILE')
    sys.exit(0)

lines = 0
words = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        lines += 1
        for word in line.split(' '):
            if word.strip():
                words += 1
print(lines, words)
