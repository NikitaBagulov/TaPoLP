;nasm -felf64 main.asm && gcc -no-pie -fno-pie main.o && ./a.out

%macro pushd 0
    push rax
    push rbx
    push rcx
    push rdx
%endmacro

%macro popd 0
    pop rdx
    pop rcx
    pop rbx
    pop rax
%endmacro

%macro print 1
    pushd
    push rdi
    mov rdi, format
    mov rsi, %1
    call printf
    pop rdi
    popd
%endmacro

%macro sqrt1 0
    mov rax, [num]
    mov rbx, 2
    xor rdx, rdx
    div rbx

    mov [x1], rax
    xor rdx, rdx
    xor rax, rax

    mov rax, [num]
    mov rcx, [x1]
    div rcx ;num/x1
    xor rdx, rdx
    add rax, rcx

    div rbx
    mov [x2], rax


    .loop_arr:
        mov rsi, [x1]
        sub rsi, [x2]

        mov rax, [x2]
        mov [x1], rax
        mov rax, [num]
        mov rcx, [x1]
        div rcx ;num/x1
        xor rdx, rdx
        add rax, rcx

        div rbx
        xor rdx, rdx
        mov [x2], rax

        cmp rsi, 1
        jge .loop_arr


    print [x2]
%endmacro

section .text
    global main

extern printf

main:
    sqrt1

    mov       rax, 60
    xor       rdi, rdi
    syscall



section .data
    num dq 144
    format db "%d", 10, 0 


section .bss
    x1 resq 1
    x2 resq 1

