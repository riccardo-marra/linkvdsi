# run on socket: socat tcp-listen:8000,reuseaddr,fork 'system:python3 random_trial.py'
from random import randint


print("Welcome to the random trial, try skip this message using recvuntil!")

while True:

    rand = randint(0, 10000)

    if rand == 42:
        print("NOW!")
        n = input()

        if n == "1":
            print("You win!")
            exit()
    else:
        print("Wait")
        n = input()

        if n != "0":
            print("You fail!")
            exit() 

