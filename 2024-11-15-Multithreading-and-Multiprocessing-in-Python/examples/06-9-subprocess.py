import subprocess


p = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True,
)
print(p.stdout)
print(p.returncode)
