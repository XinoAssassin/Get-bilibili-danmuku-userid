import binascii
crc32 = input("Please input user CRC32:")
hex_str = "0x" + crc32
hex_int = int(hex_str,16)
for i in range(1, 100000000):
    if binascii.crc32(str(i).encode("utf-8")) == hex_int:
        print(i)
