void* GetStdHandle(int);
int WriteConsoleA(void*, const void*, unsigned long, unsigned long*, void*);
void ExitProcess(int);

void main() {
    const char msg[] = "Hello World!\n";
    unsigned long written;

    void* h = GetStdHandle(-11);
    WriteConsoleA(h, msg, sizeof(msg) - 1, &written, 0);
    ExitProcess(0);
}
