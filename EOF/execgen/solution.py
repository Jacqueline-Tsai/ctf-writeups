from pwn import *

r = remote('edu-ctf.zoolab.org', 10123)
r.interactive()