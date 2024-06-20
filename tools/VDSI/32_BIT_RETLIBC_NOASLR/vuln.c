/* Compile with symbols: gcc -fno-stack-protector -no-pie -m32 vuln.c -o vuln */
/* Disable ASLR: echo 0 > /proc/sys/kernel/randomize_va_space */ 
#include <stdio.h>

int vuln() {
    char buf[80];
    int r;
    r = read(0, buf, 400);
    printf("\nRead %d bytes. buf is %s\n", r, buf);
    puts("No shell for you :(");
    return 0;
}

int main(int argc, char *argv[]) {
    printf("Try to exec /bin/sh");
    vuln();
    return 0;
}
