# Note: This script is just an illustration. It contains a very simple solution
# to the problem, which is far from perfect.

import sys
import re

emails = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        for email in re.findall(r'[\w.-]+@[\w.-]+', line):
            emails.append(email.rstrip('.'))
print(emails)
