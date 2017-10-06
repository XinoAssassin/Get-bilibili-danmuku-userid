import binascii

for i in range(1,100000000):
    if binascii.crc32(str(i).encode("utf-8")) == 0xde3bfc47:
        print(i)