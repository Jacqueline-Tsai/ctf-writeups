from pwn import *
import warnings
warnings.filterwarnings("ignore")

r = remote('edu-ctf.zoolab.org', 10021)
r.interactive()