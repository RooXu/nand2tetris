
import sys
class codeWriter:
    functions = {}
    eq_count = 0
    lt_count = 0
    gt_count = 0
    filename = ''
    filename_no_ext = '' 
    def __init__(self, output_name, isBootstrap):
        
        self.output_name = output_name 
        self.file = open(output_name,'w')

        print(f'            //Output Name: {self.output_name}',file=self.file)
        print(f'            //BootStrapping: {isBootstrap}', file=self.file) 

        self.currentFunction = ''
        if isBootstrap == True:
            self.currentFunction = '_BOOTSRAP'
            self.writeInit()
        
        print(f'        //Main code body below', file=self.file)
        
        

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
                print(f"            // push {segment} {index}", file = self.file)
                print(f"@{index}",file=self.file)
                print("D=A",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)
            elif segment == "temp":
                jndex = 5 + int(index)
                print(f"            // push {segment} {index}", file = self.file)
                print(f"@{jndex}",file=self.file)
                print("D=M",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)

            elif segment == "pointer":
                if int(index) == 0: # push this to stack
                    print(f"            // push {segment} {index}", file = self.file)
                    print(f"@3",file=self.file)                             #THIS is assigned to register 3 by convention 
                    print("D=M",file=self.file)
                    print("@SP",file=self.file)
                    print("A=M",file=self.file)
                    print("M=D",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M+1",file=self.file)
                elif int(index) == 1:  #push that to stack
                    print(f"            // push {segment} {index}", file = self.file)
                    print(f"@4",file=self.file)                             #THAT is assigned to register 4 by convention 
                    print("D=M",file=self.file)
                    print("@SP",file=self.file)
                    print("A=M",file=self.file)
                    print("M=D",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M+1",file=self.file)
            
            elif segment == "static":
                # jndex = 16 + int(index) 
                # print(f"// push {segment} {index}", file = self.file)
                # print(f"@{jndex}",file=self.file)
                # print("D=M",file=self.file)
                # print("@SP",file=self.file)
                # print("A=M",file=self.file)
                # print("M=D",file=self.file)
                # print("@SP",file=self.file)
                # print("M=M+1",file=self.file)
                print(f"            // push {segment} {index}", file = self.file)
                print(f"@{self.filename_no_ext}.{index}",file=self.file)
                print("D=M",file=self.file)
                print("@SP",file=self.file)
                print("A=M",file=self.file)
                print("M=D",file=self.file)
                print("@SP",file=self.file)
                print("M=M+1",file=self.file)

            else:
                print(f"            // push {segment} {index}",file=self.file)
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
                print(f"            // pop {segment} {index}",file=self.file)
                print("@SP",file=self.file)
                print("M=M-1",file=self.file)
                print("A=M",file=self.file)
                print("D=M",file=self.file)
                print(f"@{jndex}",file=self.file)
                print("M=D",file=self.file)

            elif segment == "pointer":
                if int(index) == 0: # pop stack to this
                    print(f"            // pop {segment} {index}",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M-1",file=self.file)
                    print("A=M",file=self.file)
                    print("D=M",file=self.file)
                    print(f"@3",file=self.file)                          #THIS is assigned to register 3 by convention 
                    print("M=D",file=self.file)
                elif int(index) == 1: # pop stack to that
                    print(f"            // pop {segment} {index}",file=self.file)
                    print("@SP",file=self.file)
                    print("M=M-1",file=self.file)
                    print("A=M",file=self.file)
                    print("D=M",file=self.file)
                    print(f"@4",file=self.file)                          #THAT is assigned to register 4 by convention 
                    print("M=D",file=self.file)
            elif segment == "static":
                # jndex = 16 + int(index)
                # print(f"// pop {segment} {index}",file=self.file)
                # print("@SP",file=self.file)
                # print("M=M-1",file=self.file)
                # print("A=M",file=self.file)
                # print("D=M",file=self.file)
                # print(f"@{jndex}",file=self.file)
                # print("M=D",file=self.file)

                print(f"            // pop {segment} {index}",file=self.file)
                print("@SP",file=self.file)
                print("AM=M-1",file=self.file)
                print("D=M",file=self.file)
                print(f"@{self.filename_no_ext}.{index}",file=self.file)
                print("M=D",file=self.file)
        
            else:    
                print(f"            // pop {segment} {index}",file=self.file)
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
    
    def setFileName(self,fileName):
        #Informs the codeWriter that translation of a new VM File has begun 
        self.filename = fileName
        dot_index = self.filename.find('.')
        self.filename_no_ext = fileName[0:dot_index]
    
    def writeInit(self):
        # wirtes the assembly instructions that effect the bootstrap code that initializes the VM. 
        print(f'            //Bootstrapping',file=self.file)
        print(f"@256",file=self.file) 
        print(f'D=A',file=self.file)
        print(f"@SP",file=self.file) 
        print(f'M=D',file=self.file)

        print(f"@1",file=self.file) 
        print(f'D=A',file=self.file)
        print(f'@LCL',file=self.file)
        print(f'M=D',file=self.file)
       
        print(f"@2",file=self.file) 
        print(f'D=A',file=self.file)
        print(f'@ARG',file=self.file)
        print(f'M=D',file=self.file)
        
        print(f"@3",file=self.file) 
        print(f'D=A',file=self.file)
        print(f'@THIS',file=self.file)
        print(f'M=D',file=self.file)
        
        print(f"@4",file=self.file) 
        print(f'D=A',file=self.file)
        print(f'@THAT',file=self.file)
        print(f'M=D',file=self.file)

        self.writeCall('Sys.init', 0) 
          
    def writeLabel(self, label):
        print(f'({self.currentFunction}.{label})', file =self.file)
    
    def writeGoto(self, label):
        print(f'            //goto')
        print(f'@{self.currentFunction}.{label}\n0;JMP',file=self.file)
    
    def writeIf(self, label):
        print(f'            //IF-GOTO {label}',file=self.file)
        print(f'@SP',file=self.file)        
        print(f'AM=M-1',file=self.file)      #go to the previous reg. referred by the SP
        print(f'D=M',file=self.file)        #load data in to D reg.
        print(f'@{self.currentFunction}.{label}',file=self.file)   #set jump address -- the label
        print(f'D;JNE',file=self.file)      #if data in D reg. is not equal to zero (should be -1) jump to address
    
    def writeFunction(self,functionName,numVars):
        funcName = functionName
        if(funcName.find(self.filename_no_ext)) == -1:
            #print(f'({filename_no_ext}.{funcName})',file=self.file)
            print(self.filename_no_ext)
            print(funcName)
            print('//WARNING: Unconventional function name in VM Code. Risks collisions')
            raise
        else:
            print(f'         //Function {functionName}',file=self.file)
            print(f'({functionName})',file=self.file)
        self.currentFunction = functionName
        if int(numVars) >= 1:                        #If there are nonzero LCL variables, initialize numVar number of LCL segment of this frame to 0. 
            for i in range(int(numVars)):
                print(f'@0',file=self.file)     #Get 0
                print(f'D=A',file=self.file)    #Put 0 in D reg.
                print(f'@SP',file=self.file)    #Go to Stack Pointer Reg.
                print(f'A=M',file=self.file)    #Go to the pointer referred by SP
                print(f'M=D',file=self.file)    #Set the memory of the referenced register to 0
                print(f'@SP',file=self.file)    
                print(f'M=M+1',file=self.file)  #Increment the stack pointer

    def writeCall(self, functionName, numArgs): 

        caller = self.currentFunction
        callee = functionName
        if self.functions.get(caller) == None:
            self.functions[caller] = 0 
        else:
            self.functions[caller] = self.functions[caller] + 1

        print(f'            //Call {functionName} provoding {numArgs} arguments',file=self.file)
        print(f'@{caller}$ret.{self.functions[caller]}',file=self.file)  #get return address
        print(f'D=A',file=self.file)    #Put return address in D reg.
        print(f'@SP',file=self.file) 
        print(f'A=M',file=self.file)    #Go to the pointer referred by SP
        print(f'M=D',file=self.file)    #Set the memory of the referenced register to return address 

        print(f'@SP',file=self.file)    
        print(f'M=M+1',file=self.file)  #Increment the stack pointer

        print(f'@LCL',file=self.file) 
        print(f'D=M',file=self.file)
        print(f'@SP',file=self.file)
        print(f'A=M',file=self.file)    #Go to the pointer referred by SP
        print(f'M=D',file=self.file)    #Set the memory of the referenced register to the base address of LCL

        print(f'@SP',file=self.file)    
        print(f'M=M+1',file=self.file)  #Increment the stack pointer

        print(f'@ARG',file=self.file) 
        print(f'D=M',file=self.file)
        print(f'@SP',file=self.file)
        print(f'A=M',file=self.file)    #Go to the pointer referred by SP
        print(f'M=D',file=self.file)    #Set the memory of the referenced register to the base address of ARG

        print(f'@SP',file=self.file)    
        print(f'M=M+1',file=self.file)  #Increment the stack pointer

        print(f'@THIS',file=self.file) 
        print(f'D=M',file=self.file)
        print(f'@SP',file=self.file)
        print(f'A=M',file=self.file)    #Go to the pointer referred by SP
        print(f'M=D',file=self.file)    #Set the memory of the referenced register to the base address of THIS

        print(f'@SP',file=self.file)    
        print(f'M=M+1',file=self.file)  #Increment the stack pointer

        print(f'@THAT',file=self.file) 
        print(f'D=M',file=self.file)
        print(f'@SP',file=self.file)
        print(f'A=M',file=self.file)    #Go to the pointer referred by SP
        print(f'M=D',file=self.file)    #Set the memory of the referenced register to the base address of THAT

        print(f'@SP',file=self.file)    
        print(f'M=M+1',file=self.file)  #Increment the stack pointer

        print(f'@SP',file=self.file)            #get address in current stack 
        print(f'D=M',file=self.file)            # store in D Reg.
        print(f'@{5+int(numArgs)}',file=self.file)   #get the relative distance of ARG 0
        print(f'D=D-A',file=self.file)          #subtract relative distance from current stack address
        print(f'@ARG',file=self.file)           
        print(f'M=D',file=self.file)          #store reult in ARG

        print(f"@SP",file=self.file)
        print(f'D=M',file=self.file)
        print(f'@LCL',file=self.file) 
        print(f'M=D',file=self.file)    #Set the memory of the LCL to the current location in stack 

        print(f'@{callee}',file=self.file)
        print(f'0;JMP',file=self.file)
        print(f'({caller}$ret.{self.functions[caller]})',file=self.file)

    def writeReturn(self):
        print('         // Return',file=self.file)
        #get endFrame and store in R13 
        
        print(f'@LCL',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@R13',file=self.file)
        print(f'M=D',file=self.file)    #Set the memory of R13 to the endFrame

        #get return address and store in R14
        print(f'@5',file=self.file)
        print(f'A=D-A',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@R14',file=self.file)
        print(f'M=D',file=self.file)    #Set the memory of R14 to value at endFrame - 5

        #put return value at ARG 0 
        print(f"@SP",file=self.file)
        print(f'A=M-1',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@ARG',file=self.file)
        print(f'A=M',file=self.file)
        print(f'M=D',file=self.file)

        #reposition SP to after ARG 0 
        print(f'@ARG',file=self.file)
        print(f'D=M+1',file=self.file)
        print(f"@SP",file=self.file)
        print(f'M=D',file=self.file)

        #restore THAT 
        print(f'@R13',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@1',file=self.file)
        print(f'A=D-A',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@THAT',file=self.file)
        print(f'M=D',file=self.file)

        #restore THIS 
        print(f'@R13',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@2',file=self.file)
        print(f'A=D-A',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@THIS',file=self.file)
        print(f'M=D',file=self.file)

        #restore ARG 
        print(f'@R13',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@3',file=self.file)
        print(f'A=D-A',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@ARG',file=self.file)
        print(f'M=D',file=self.file)

        #restore LCL 
        print(f'@R13',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@4',file=self.file)
        print(f'A=D-A',file=self.file)
        print(f'D=M',file=self.file)
        print(f'@LCL',file=self.file)
        print(f'M=D',file=self.file)

        #earase temp values and jump to return address 
        print(f'@R13',file=self.file)
        print(f'M=0',file=self.file)
        print(f'@R14',file=self.file)
        print(f'D=M',file=self.file)
        print(f'M=0',file=self.file)
        print(f'A=D',file=self.file)
        print(f'0;JMP',file=self.file)

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