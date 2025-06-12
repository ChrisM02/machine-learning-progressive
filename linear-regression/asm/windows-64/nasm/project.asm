section .data
    msg db "Hello World!", 0x0D, 0x0A
    len equ $ - msg

section .text
    global main
    extern GetStdHandle
    extern WriteFile
    extern ExitProcess

main:
    sub rsp, 40
    mov ecx, -11
    call GetStdHandle

    mov rcx, rax
    
    mov rdx, msg
    mov r8d, len
    lea r9, [rsp+32]
    xor rax, rax
    call WriteFile

    xor ecx, ecx
    call ExitProcess
