from Crypto.Cipher import AES
from hashlib import sha256
import os
#token=66
i = [0, 2, 3, 4, 5, 7, 32, 34, 35, 36, 37, 39, 80, 81, 82, 83, 84, 85, 86, 87, 94, 95]
m = [48,49,50,51,52,53,54,55,56,57, 65,66,67,68,69,70, 97,98,99,100,101,102]

for a in i:
    print(a^102,end=' ')

token = os.urandom(8)
iv = os.urandom(16)
key = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
ct = cipher.encrypt(token.hex().encode()).hex()

print('token:',token.hex())
print('iv:',iv.hex())
print('ct:',ct)

ia, ma = [],[]
for i in range(128):
    #print(i)
    iv_mod = iv[:15] + (iv[15] ^ i).to_bytes(1, 'big') + iv[16:]
    #print('iv aft:',iv_mod)

    cipher = AES.new(key, AES.MODE_CBC, iv=iv_mod)
    m = cipher.decrypt(bytes.fromhex(ct)).decode()
    try:
        m = bytes.fromhex(m)
        ia.append(i)
        ma.append(m[-1])
    except:
        pass

print(ia)
print(sorted(ma))
print(sorted([ma[i]^ia[i] for i in range(len(ma))]))
print(sorted([i^token[-1] for i in ia]))
