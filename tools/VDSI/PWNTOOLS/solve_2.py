from pwn import *

#context.log_level = "DEBUG"

SCRIPT_PATH = "/mnt/hgfs/shared_rev/VDSI/PWNTOOLS/"
session = ssh("user", "192.168.208.210", 22, "user")

p =  session.process(["python3", SCRIPT_PATH+"random_trial.py"])
#p = process(["python3", "random_trial.py"])
#p = remote("127.0.0.1", 8000)

p.recvuntil(b" recvuntil!\n")

for i in range(0, 20000):

    rec = p.recvline()

    # print("rec:", rec)

    if rec.startswith(b"Wait"):
        p.sendline(b"0")
    else:
        p.sendline(b"1")
        break

p.interactive()