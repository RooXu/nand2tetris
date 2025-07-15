
import sys
class codeWriter:
    commands = {



    }
    eq_count = 0
    lt_count = 0
    gt_count = 0
    def __init__(self,output_name):
        self.output_name = output_name 
        self.file = open(output_name,'w')
    
    def writeArithmetic(self,c_arithmetic):
        # arguments: string of command (e.g. add, sub, neg)
        # writes the assembly that implements the given arithmetic command 

        #add
        if c_arithmetic == "add":
            print(f"// add",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=D+M",file=self.file)

        #sub
        elif c_arithmetic == "sub":
            print(f"// sub",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=M-D",file=self.file)

        #neg
        elif c_arithmetic == "neg":
            print(f"// neg")
            print("@SP",file=self.file)
            print("A=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=-M",file=self.file)

        #eq
        elif c_arithmetic == "eq":
            print(f"// eq",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=M-D",file=self.file)
            print("D=M",file=self.file)
            print(f"@TRUE.EQ{self.eq_count}",file=self.file)
            print("D;JEQ",file=self.file)
            print(f"@FALSE.EQ{self.eq_count}",file=self.file)
            print("D;JNE",file=self.file)
            print(f"(EQ{self.eq_count}.A)",file=self.file)
            print("@SP",file=self.file)
            print("A=M-1",file=self.file)
            print("M=D",file=self.file)
            print(f"@EQ{self.eq_count}.Z",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(TRUE.EQ{self.eq_count})",file=self.file)
            print("D=-1",file=self.file)
            print(f"@EQ{self.eq_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(FALSE.EQ{self.eq_count})",file=self.file)
            print("D=0",file=self.file)
            print(f"@EQ{self.eq_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(EQ{self.eq_count}.Z)",file=self.file)
            self.eq_count = self.eq_count + 1

        #gt
        elif c_arithmetic == "gt":
            print(f"// gt",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=M-D",file=self.file)
            print("D=M",file=self.file)
            print(f"@TRUE.GT{self.gt_count}",file=self.file)
            print("D;JGT",file=self.file)
            print(f"@FALSE.GT{self.gt_count}",file=self.file)
            print("D;JLE",file=self.file)
            print(f"(GT{self.gt_count}.A)",file=self.file)
            print("@SP",file=self.file)
            print("A=M-1",file=self.file)
            print("M=D",file=self.file)
            print(f"@GT{self.gt_count}.Z",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(TRUE.GT{self.gt_count})",file=self.file)
            print("D=-1",file=self.file)
            print(f"@GT{self.gt_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(FALSE.GT{self.gt_count})",file=self.file)
            print("D=0",file=self.file)
            print(f"@GT{self.gt_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(GT{self.gt_count}.Z)",file=self.file)
            self.gt_count = self.gt_count + 1
        #lt
        elif c_arithmetic == "lt":
            print(f"// lt",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=M-D",file=self.file)
            print("D=M",file=self.file)
            print(f"@TRUE.LT{self.lt_count}",file=self.file)
            print("D;JLT",file=self.file)
            print(f"@FALSE.LT{self.lt_count}",file=self.file)
            print("D;JGE",file=self.file)
            print(f"(LT{self.lt_count}.A)",file=self.file)
            print("@SP",file=self.file)
            print("A=M-1",file=self.file)
            print("M=D",file=self.file)
            print(f"@LT{self.lt_count}.Z",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(TRUE.LT{self.lt_count})",file=self.file)
            print("D=-1",file=self.file)
            print(f"@LT{self.lt_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(FALSE.LT{self.lt_count})",file=self.file)
            print("D=0",file=self.file)
            print(f"@LT{self.lt_count}.A",file=self.file)
            print("0;JMP",file=self.file)
            print(f"(LT{self.lt_count}.Z)",file=self.file)
            self.lt_count = self.lt_count + 1
        #and
        elif c_arithmetic == "and":
            print(f"// and",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=D&M",file=self.file)

        #or
        elif c_arithmetic == "or":
            print(f"// or",file=self.file)
            print("@SP",file=self.file)
            print("M=M-1",file=self.file)
            print("A=M",file=self.file)
            print("D=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=D|M",file=self.file)

        #not
        elif c_arithmetic == "not":
            print(f"// not",file=self.file)
            print("@SP",file=self.file)
            print("A=M",file=self.file)
            print("A=A-1",file=self.file)
            print("M=!M",file=self.file)

    def writePushPop(self,c_pushpop,segment,index):
        # takes push or pop commands, segment(string), index(int) 
        # Writes the assembly code that implements the given command, where command is either C_Push or C_POP 

        # PUSH
        if c_pushpop == 1:
            if segment == "constant":
                print(f"// push {segment} {index}", file = self.file)
                print(f"@{index}",file=self.file)
                print("D=A",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)
            elif segment == "temp":
                jndex = 5 + int(index)
                print(f"// push {segment} {index}", file = self.file)
                print(f"@{jndex}",file=self.file)
                print("D=M",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)

            elif segment == "pointer":
                if int(index) == 0: # push this to stack
                    print(f"// push {segment} {index}", file = self.file)
                    print(f"@3",file=self.file)                             #THIS is assigned to register 3 by convention 
                    print("D=M",file=self.file)
                    print("@SP",file=self.file)
                    print("A=M",file=self.file)
                    print("M=D",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M+1",file=self.file)
                elif int(index) == 1:  #push that to stack
                    print(f"// push {segment} {index}", file = self.file)
                    print(f"@4",file=self.file)                             #THAT is assigned to register 4 by convention 
                    print("D=M",file=self.file)
                    print("@SP",file=self.file)
                    print("A=M",file=self.file)
                    print("M=D",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M+1",file=self.file)
            
            elif segment == "static":
                jndex = 16 + int(index) 
                print(f"// push {segment} {index}", file = self.file)
                print(f"@{jndex}",file=self.file)
                print("D=M",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)

            else:
                print(f"// push {segment} {index}",file=self.file)
                print(f"@{segment}",file=self.file)
                print("D=M",file=self.file)
                print(f"@{index}",file=self.file)
                print("A=D+A",file=self.file)
                print("D=M",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)

        #POP
        elif c_pushpop == 2:
            if segment == "temp":
                jndex = 5 + int(index)
                print(f"// pop {segment} {index}",file=self.file)
                print("@SP",file=self.file)
                print("M=M-1",file=self.file)
                print("A=M",file=self.file)
                print("D=M",file=self.file)
                print(f"@{jndex}",file=self.file)
                print("M=D",file=self.file)

            elif segment == "pointer":
                if int(index) == 0: # pop stack to this
                    print(f"// pop {segment} {index}",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M-1",file=self.file)
                    print("A=M",file=self.file)
                    print("D=M",file=self.file)
                    print(f"@3",file=self.file)                          #THIS is assigned to register 3 by convention 
                    print("M=D",file=self.file)
                elif int(index) == 1: # pop stack to that
                    print(f"// pop {segment} {index}",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M-1",file=self.file)
                    print("A=M",file=self.file)
                    print("D=M",file=self.file)
                    print(f"@4",file=self.file)                          #THAT is assigned to register 4 by convention 
                    print("M=D",file=self.file)
            elif segment == "static":
                jndex = 16 + int(index)
                print(f"// pop {segment} {index}",file=self.file)
                print("@SP",file=self.file)
                print("M=M-1",file=self.file)
                print("A=M",file=self.file)
                print("D=M",file=self.file)
                print(f"@{jndex}",file=self.file)
                print("M=D",file=self.file)
        
            else:    
                print(f"// pop {segment} {index}",file=self.file)
                print(f"@{segment}",file=self.file)
                print("D=M",file=self.file)
                print(f"@{index}",file=self.file)
                print("D=D+A",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M-1",file=self.file)
                print("A=M",file=self.file)
                print("D=M",file=self.file)
                print("A=A+1",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
    


    def close(self):
        self.file.close()

if __name__ == "__main__":
    writing_obj = codeWriter("write_test.txt")
    # 12 == 12
    writing_obj.writePushPop(1,"LCL",0)
    writing_obj.writePushPop(1,"LCL",1) 
    writing_obj.writeArithmetic("eq")
    writing_obj.writePushPop(2,"LCL",2)
    writing_obj.writePushPop(1,"LCL",2)
    writing_obj.writeArithmetic("not")
    writing_obj.writePushPop(2,"LCL",3)
    writing_obj.writePushPop(1,"LCL",3)
    writing_obj.writePushPop(1,"LCL",2)
    writing_obj.writeArithmetic("or")
    writing_obj.writePushPop(2,"LCL",4)
    writing_obj.close()
    # 12 == 12 


    # 84 > 85

    # not(true (-1))

    # not(true AND false)