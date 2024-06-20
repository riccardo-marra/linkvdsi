#include <stdio.h>
#include <stdlib.h>

int fib(int n) {

    int f1;
    int f2;

    if (n <= 2) {
        return 1;
    } else {
        f1 = fib(n-1);
        f2 = fib(n-2);

        return f1+f2;
    }
}

int main(int argc, char **argv) {

    int f = fib(10);

    printf("FIB(10)=%d\n", f);

    return 0;

}