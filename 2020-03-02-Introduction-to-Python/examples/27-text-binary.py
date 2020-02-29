# Binary mode:
with open('26-text-binary.txt', 'rb') as f:
    data = f.read()

print(data)                 # b'Ko\xc4\x8di\xc4\x8dka\r\n'
print(len(data))            # 11
print(data.decode('utf-8')) # Kočička

# Text mode:
with open('26-text-binary.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(text)                 # Kočička
print(len(text))            # 8
print(text.encode('utf-8')) # b'Ko\xc4\x8di\xc4\x8dka\n'
