/* Compile with symbols: gcc vuln.c -o vuln */
/* Compile without symbols: gcc -s vuln.c -o vuln */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


void hello() {

    puts("Hi");

}
void vuln(){
    char buffer[100];
    printf("Enter your name:\n");
    fgets(buffer, 100, stdin);
    //read(1, buffer, 100);
    printf("Hi: ");
    printf(buffer);
    printf("\n");


    unsigned long to_save, where_save;
    printf("Enter the number to save: \n");
    scanf("%lu", &to_save);
    //printf("%lx\n", to_save);
    printf("Tell me where to save it: \n");
    scanf("%lu", &where_save);
    //printf("%lx\n", where_save);
    *((unsigned long*)where_save) = to_save;

    asm("xor %rsi,%rsi; xor %rdx,%rdx"); //nothing to see here
}

void main() {

    hello();
    vuln();

}