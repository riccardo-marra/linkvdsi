/* Compile with symbols: gcc vuln.c -o vuln */
/* Compile without symbols: gcc -s vuln.c -o vuln */
#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {

    puts("Echoing...\n");
    if (argc == 2) {
        printf(argv[1]);
    }

}