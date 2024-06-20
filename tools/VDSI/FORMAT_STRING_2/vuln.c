/* Compile with symbols: gcc -no-pie -m32 vuln.c -o vuln */
/* Compile without symbols: gcc -s -no-pie -m32 vuln.c -o vuln */
#include <stdio.h>
#include <stdlib.h>

int flag;

int main(int argc, char *argv[]) {

    getchar();
    if (argc < 2) {
        printf("Please, enter your name\n");
        return -1;
    }

    printf(argv[1]);
    
    if (flag) {
        printf("You win!\n");
    } else {
        printf("Try again\n");
    }

}