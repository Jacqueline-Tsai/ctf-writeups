from pwn import *
from base64 import b64encode, b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes
import warnings, math, time
warnings.filterwarnings("ignore")

r = remote('eof.ais3.org', 10051)
n, e, flag_ct = [], [], []
for i in range(10):
    n.append(bytes_to_long(b64decode(r.readline())))
    e.append(bytes_to_long(b64decode(r.readline())))
    flag_ct.append(bytes_to_long(b64decode(r.readline())))
print(n,flag_ct)

def test():
    for i in range(2): r.readline()
    r.sendline('1')
    r.sendline('0')
    r.sendline(b64encode(long_to_bytes(flag_ct[0])))
    cur_bit = int(str(r.readline())[15:-3])

    for i in range(2): r.readline()
    r.sendline('1')
    r.sendline('0')
    r.sendline(b64encode(long_to_bytes((flag_ct[0]*pow(3, -e[0], n[0])) %n[0])))
    bit = int(str(r.readline())[15:-3])

print(cur_bit,bit)

