/* Compile with symbols: gcc -m32 -fno-stack-protector vuln.c -o vuln */
/* Compile without symbols: gcc -s -m32 -fno-stack-protector -nolibc -static vuln.c -o vuln */

char str[] = "/bin/sh";
void func() {
    // It's dangerous to go alone! Take this.
    asm ( ".intel_syntax noprefix;"
    "mov eax, 0xc358;"
    "pop ebx; ret;"
    "pop ecx; ret;"
    "pop edx; ret;"
    ".att_syntax;"
    :
    :); 
}

int vuln() {
    char buf[80];
    // read(0, buf, 400);
    asm ( ".intel_syntax noprefix;" 
    "mov ebx, 0;"
    "mov ecx, %0;"
    "mov edx, 400;"
    "mov eax, 3;"
    "int 0x80;"
    ".att_syntax;"
    :
    : "r" (&buf));
    return 0;
}

__attribute__((force_align_arg_pointer))
void _start() {
    
    vuln();
    __builtin_unreachable();
}