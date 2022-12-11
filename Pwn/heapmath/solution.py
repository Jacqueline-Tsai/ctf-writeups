from pwn import *
import math

context.arch = "amd64"
context.terminal = ['tmux', 'splitw', '-h']
r = remote("edu-ctf.zoolab.org", "10006")

# ----------- ** tcache chall ** -----------
r.recvline() 

tcache_size, tcache_free_order = [], []
for i in range(7):
    msg = int(str(r.recvline()).split('(')[2].split(')')[0], 16)
    size = math.ceil((msg + 0x10 - 0x08) / 0x10) * 0x10
    tcache_size.append(size)

for i in range(7):
    msg = str(r.recvline()).split('(')[1].split(')')[0]
    tcache_free_order.append(ord(msg) - ord('A'))

ans_0x30, ans_0x40 = ['NULL'], ['NULL']
for tcache in tcache_free_order:
    if tcache_size[tcache] == 0x30:
        ans_0x30 = [chr(tcache + ord('A'))] + ans_0x30
    if  tcache_size[tcache] == 0x40:
        ans_0x40 = [chr(tcache + ord('A'))] + ans_0x40

# send answer
for i in range(3): r.recvline()
r.sendline(' --> '.join(ans_0x30))
for i in range(2): r.recvline()
r.sendline(' --> '.join(ans_0x40))
for i in range(2): r.recvline()

# ----------- ** address chall ** -----------
r.recvline()

msg = str(r.recvline())

target1, address1 = ord(msg.split(' ')[1]) - ord('A'), int(msg.split(' ')[3], 16)
target2 = ord(str(r.recvline()).split(' ')[0].split("'")[1]) - ord('A')
address2 = address1 + sum(tcache_size[target1:target2])
r.sendline(hex(address2))

for i in range(2): r.recvline()

# ----------- ** index chall ** -----------
r.recvline()

chunk_size = int(r.recvline().decode("ascii").split('(')[2].split(')')[0], 16) + 0x10
r.recvline()
secret_idx = int(r.recvline().decode("ascii").split("[")[1].split("]")[0])
r.recvline()
r.sendline(str(int(chunk_size / 0x8) + secret_idx))

for i in range(2): r.recvline()

# ----------- ** tcache fd chall ** -----------
for i in range(3): r.recvline()

y_address = int(r.recvline().decode("ascii").split('== ')[1].split(' ')[0], 16)
y_fd = y_address - chunk_size
r.sendline(str(hex(y_fd)))

for i in range(3): r.recvline()

# ----------- ** fastbin fd chall (final) ** -----------
for i in range(11): r.recvline()

y_fd = y_fd - 0x10
r.sendline(hex(y_fd).split('x')[1])

print(r.recvline())
print(r.recvline()) # FLAG