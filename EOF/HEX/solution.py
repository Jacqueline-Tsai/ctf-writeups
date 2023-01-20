from pwn import *
import warnings
warnings.filterwarnings("ignore")

# one element in arr1 ^ one element in arr2 = specific number, return specific number
def xor_match(arr1, arr2):
    tmp = []
    for a in arr1:
        for b in arr2:
            tmp.append(a^b)
    for i in tmp:
        if tmp.count(i)==22:
            return chr(i)
    return -1

r = remote('eof.ais3.org', 10050)
tmp = str(r.readline())[2:-3]
iv, token_ct = tmp[:32], tmp[32:]
token_sha256 = r.readline()

# those characters that will return "Well received"
well_print = [48,49,50,51,52,53,54,55,56,57, 65,66,67,68,69,70, 97,98,99,100,101,102]

token = ''
for byte_i in range(15, -1, -1):
    well_xor = []
    for test_val in range(128):
        iv_mod = iv[:byte_i*2] + format(int(iv[byte_i*2:(byte_i+1)*2],16) ^ test_val, '02x') + iv[(byte_i+1)*2:]
        #print(iv_mod)
        for i in range(3): r.readline()
        r.sendline('1')
        r.sendline(iv_mod + token_ct)
        res = r.readline()
        if res == b'Message(hex): Well received\n':
            well_xor.append(test_val)
    token = xor_match(well_xor, well_print) + token
    print(token)

for i in range(3): r.readline()
r.sendline('2')
r.sendline(token)
print(r.readline())