from pwn import *

#context.log_level = "DEBUG"

#p = process(["python3", "random_trial.py"])
p = remote("localhost", 8000)

p.recvuntil("recvuntil!\n")

for i in range(0, 200000):
    rec = p.recvline()

    if rec.startswith(b"Wait"):
        p.sendline(b"0")
    else:
        p.sendline(b"1")
        break
p.interactive()