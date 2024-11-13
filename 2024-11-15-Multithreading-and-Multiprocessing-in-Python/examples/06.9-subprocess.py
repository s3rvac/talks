#
# An example of using the subprocess module.
#

import subprocess


p = subprocess.run(
    ["ls", "-l"],
    # We want to capture the output so that we can print it ourselves.
    capture_output=True,
    # Automatically decode the output from bytes to a string.
    text=True,
)
print(p.stdout)
print(p.returncode)
