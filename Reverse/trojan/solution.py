key = "0vCh8RrvqkrbxN9Q7Ydx\0"

with open("test") as fr:
    file = fr.read()
    enc_flag = bytearray(file)
    for i in range(len(enc_flag)):
        enc_flag[i] = enc_flag[i] ^ ord(key[i % len(key)])
    with open('flag') as fw:
        fw.write(enc_flag)