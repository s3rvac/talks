# Based on https://cs-blog.petrzemek.net/2015-08-09-znakova-sada-vs-kodovani

s = 'Kočička'
print(len(s))   # 7
print(ord('č')) # 269
print(hex(269)) # '0x10d' (U+010D: Latin Small Letter C with Caron)
print('Ko\u010di\u010dka') # Unicode literals

# Encoding:
print(s.encode('latin2'))   # b'Ko\xe8i\xe8ka'
print(s.encode('utf-8'))    # b'Ko\xc4\x8di\xc4\x8dka'
print(s.encode('utf-16le')) # b'K\x00o\x00\r\x01i\x00\r\x01k\x00a\x00'
print(s.encode('utf-16be')) # b'\x00K\x00o\x01\r\x00i\x01\r\x00k\x00a'
print(s.encode('utf-16'))   # b'\xff\xfeK\x00o\x00\r\x01i\x00\r\x01k\x00a\x00'
                            #   ^^^^^^^^ BOM
# Decoding:
print(b'Ko\xc4\x8di\xc4\x8dka'.decode('utf-8'))    # 'Kočička'
print(b'Ko\xc4\x8di\xc4\x8dka'.decode('latin2'))   # 'KoÄ\x8diÄ\x8dka' (nonsense)
print(b'Ko\xc4\x8di\xc4\x8dka'.decode('utf-16le')) # UnicodeDecodeError
