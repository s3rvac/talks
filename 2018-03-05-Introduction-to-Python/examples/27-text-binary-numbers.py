# Text mode:
with open('25.txt', 'w') as f:
    print(f.write(str(25))) # 2 bytes written

with open('25.txt', 'r') as f:
    print(f.read()) # 25

# Binary mode:
import struct
with open('25.bin', 'wb') as f:
    print(f.write(struct.pack('i', 25))) # 4 bytes written (32b int, native endianness)

with open('25.bin', 'rb') as f:
    print(f.read()) # b'\x19\x00\x00\x00'  # 0x19 == 25
