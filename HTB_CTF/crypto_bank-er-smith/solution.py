from pwn import *

r = remote("134.209.22.155","32082")
r.interactive()
"""
print(r.recvline())


# welcome
for i in range(9): print(r.recvline())

def instruction():
    print('ins')
    for i in range(5): r.recvline()

instruction()

r.sendline('1')
r.recvline()
r.recvline()
n = int(r.recvline().decode('ascii'))
e = int(r.recvline().decode('ascii'))
r.recvline()

instruction()

r.recvline()
r.sendline('2')
r.recvline()
p0 = int(r.recvline().decode('ascii'))
r.recvline()


"""