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

%macro print 2 
    pushd
    mov rax, 1
    mov rdi, 1
    mov rdx, %1
    mov rsi, %2
    syscall
    popd
%endmacro
%macro print1 1
    pushd
    push rdi
    mov rdi, format
    mov rsi, %1
    call printf
    pop rdi
    popd
%endmacro


section   .text
    global    main

extern printf


main:   
    mov ecx, [len]
    xor edx, edx
arr:
    mov eax, [x+ecx*4-4]
    mov ebx, [y+ecx*4-4]
    sub eax, ebx
    
    add edx, eax
    mov [sum], edx
    ;print1 rdx

    dec ecx
    ;print1 rcx
    test ecx, ecx
    jnz arr

end:
    xor rax, rax
    xor rcx, rcx

    mov eax, [sum]
    mov ecx, [len]
    xor edx, edx
    ;print1 rax ;сумма элементов полученного массива
    ;print1 rcx ;
    cdq
    idiv ecx
    ;print1 rax
    mov [result], eax
    ;print1 rdx

    print1 [result] ;результат

    mov eax, 60                   
    xor edi, edi                  
    syscall


section   .data
    format db "%d", 10, 0;

    x dd 5, 3, 2, 6, 1, 7, 4
    y dd 0, 10, 1, 9, 2, 8, 5
    len dd 7
    sum dd 0


section .bss
    result resd 1
    ;sum resw 1
