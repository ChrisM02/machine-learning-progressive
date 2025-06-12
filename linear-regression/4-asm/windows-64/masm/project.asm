.data
    msg db "Hello World!", 0Dh, 0Ah
    len equ ($ - offset msg)

.code
main PROC
    sub rsp, 40

    mov ecx, -11
    call GetStdHandle

    mov rcx, rax
    lea rdx, msg
    mov r8d, len
    lea r9, [rsp + 32]
    xor rax, rax
    call WriteFile

    xor ecx, ecx
    call ExitProcess
main ENDP
END main
