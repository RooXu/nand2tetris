            //Output Name: FibonacciSeries.asm
            //BootStrapping: False
        //Main code body below
            // push ARG 1
@ARG
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
            // pop pointer 1
@SP
M=M-1
A=M
D=M
@4
M=D
            // push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
            // pop THAT 0
@THAT
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
            // push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
            // pop THAT 1
@THAT
D=M
@1
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
            // push constant 2
@2
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
            //IF-GOTO COMPUTE_ELEMENT
@SP
AM=M-1
D=M
@.COMPUTE_ELEMENT
D;JNE
@.END
0;JMP
(.COMPUTE_ELEMENT)
            // push THAT 0
@THAT
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
            // push THAT 1
@THAT
D=M
@1
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
            // pop THAT 2
@THAT
D=M
@2
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
            // push pointer 1
@4
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
// add
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M
            // pop pointer 1
@SP
M=M-1
A=M
D=M
@4
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
@.LOOP
0;JMP
(.END)
