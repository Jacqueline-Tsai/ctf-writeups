
xor_list = [0x75, 0x1C, 0xD7, 0x87, 0x83, 0x40, 0x87, 0x98, 0x8A, 0x39, 0x30, 0x93, 0xA6, 0xE6, 0x21, 0x68, 0x44, 0x6F, 0x89, 0x8D, 0x3E, 0xB9, 0x63, 0xAF, 0x1F, 0x6B, 0xF6, 0x86, 0x31, 0x37, 0x3D, 0x46, 0x59, 0x0C, 0x13, 0x23, 0xDC, 0x16, 0xBD, 0x38, 0xC1, 0xEE, 0xB1, 0xFB, 0xDF, 0x8D, 0x2C, 0x85, 0x76, 0x0A, 0x0A, 0x68, 0xCB, 0xD9, 0xA5, 0x44, 0xF5, 0x6B, 0x0E, 0x82, 0xF5, 0xB8, 0xB5, 0x46, 0xE3, 0x69, 0x30, 0x8E, 0x34, 0xD0, 0x83, 0x2F, 0xD5, 0xFD, 0x66, 0xCA, 0x6B, 0x45, 0x41, 0x70, 0xFE, 0xA8, 0x65, 0xD7, 0x4B, 0x32, 0xEA, 0xA7, 0xBD, 0xD0, 0x56, 0xF0, 0x94, 0x4C, 0xDF, 0xEE, 0x56, 0x69, 0xDE, 0x61, 0x3C, 0x70, 0xB9, 0xD6, 0xF3, 0xD6, 0xF7, 0xB3, 0x0F, 0xF0, 0x99, 0x6B, 0x1B, 0xB7, 0xB1, 0xB5, 0x15, 0x1B, 0x23, 0xB0, 0x62, 0x59, 0xE3, 0x64, 0x82, 0x2F, 0x29, 0x20, 0x01, 0xF4, 0xC7, 0x28, 0x29, 0x4D, 0xDE, 0xAC, 0x3A, 0xD8, 0x30, 0x29, 0x04, 0x23, 0x8C, 0xD6, 0x0C, 0x1B, 0x4A, 0x5E, 0x79, 0xF4, 0xE5, 0x72, 0x75, 0xFC, 0xEF, 0xB1, 0x9F, 0xD5, 0x5C, 0xB4, 0x19, 0xB4, 0xE9, 0xD4, 0x51, 0x51, 0xC1, 0x16, 0xEF, 0x47, 0x78, 0xFF, 0x68, 0x29, 0x0D, 0xE7, 0x27, 0xFB, 0x60, 0x39, 0x4E, 0xB4, 0x9F, 0xF3, 0x86, 0x2E, 0x71, 0x75, 0xC9, 0xC6, 0x27, 0x2D, 0x0B, 0xCB, 0xE9, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x41, 0x92, 0x41, 0x47, 0xEF, 0xBC, 0x65, 0x8B, 0xF2, 0x6F, 0x75, 0x5F, 0x6D, 0x75, 0xDF, 0x9A, 0x5F, 0xB3, 0x8F, 0x61, 0x89, 0x31, 0x61, 0xF5, 0x3F, 0x5D, 0x61, 0x69, 0x8F, 0x21, 0x9D, 0x96, 0xA7, 0x61, 0x5C, 0xEC, 0x03, 0x5F, 0x70, 0x3C, 0xC0, 0xDC, 0x79, 0x56, 0x6E, 0x25, 0x6F, 0x5F, 0xBD, 0xDD, 0x72, 0xFF, 0x73, 0x34, 0x69, 0xB5, 0x6D, 0x58, 0x5F, 0x0C, 0x49, 0x40, 0x72, 0xC8, 0x5D]
enc_flag = [0x41, 0x92, 0x41, 0x47, 0x0EF, 0x0BC, 0x65, 0x8B, 0x0F2, 0x6F, 0x75, 0x5F, 0x6D, 0x75, 0x0DF, 0x9A, 0x5F, 0x0B3, 0x8F, 0x61, 0x89, 0x31, 0x61, 0x0F5, 0x3F, 0x5D, 0x61, 0x69, 0x8F, 0x21, 0x9D, 0x96, 0xA7, 0x61, 0x5C, 0xEC, 0x03, 0x5F, 0x70, 0x3C, 0xC0, 0xDC, 0x79, 0x56, 0x6E, 0x25, 0x6F, 0x5F, 0x0BD, 0x0DD, 0x72, 0xFF, 0x73, 0x34, 0x69, 0x0B5, 0x6D, 0x58, 0x5F, 0x0C, 0x49, 0x40, 0x72, 0xC8, 0x5D]

i, index = 0, 0
while True:
    if 3 * i + 2 >= len(xor_list) or not xor_list[3 * i]: break
    lobyte = xor_list[3 * i] & 1
    for j in range(xor_list[3 * i + 1]):
        if lobyte: index = (index + 1) % 65
        else: index = (index + 64) % 65
    enc_flag[index] ^= xor_list[3 * i + 2]
    i += 1

for c in enc_flag:
    print(chr(c), end='')