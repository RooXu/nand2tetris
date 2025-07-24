            //Output Name: BasicLoop.asm
            //BootStrapping: False
        //Main code body below
            // push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
            // pop LCL 0
@LCL
D=M
@0
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
A=A+1
A=M
M=D
(.LOOP)
            // push ARG 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
            // push LCL 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
            // pop LCL 0
@LCL
D=M
@0
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
A=A+1
A=M
M=D
            // push ARG 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
            // push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
A=A-1
M=M-D
            // pop ARG 0
@ARG
D=M
@0
D=D+A
@SP
A=M
M=D
@SP
M=M-1
A=M
D=M
A=A+1
A=M
M=D
            // push ARG 0
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
            //IF-GOTO LOOP
@SP
AM=M-1
D=M
@.LOOP
D;JNE
            // push LCL 0
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
