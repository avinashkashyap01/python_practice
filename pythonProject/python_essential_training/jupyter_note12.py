
# Bytes
a = bytes(4)
print(a)

smileybytes = bytes('🙄','utf-8')
print(smileybytes)

b = smileybytes.decode('utf-8')
print(b)

smileybytes = bytearray('🙄','utf-8')
print(smileybytes)

smileybytes[3] = int('85',16)
c = smileybytes.decode('utf-8')
print(c)
