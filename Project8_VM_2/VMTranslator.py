import sys
import os
import glob
import VMparser
import codeWriter

if __name__ == "__main__": 
    parsing_objs = []
    isBootstrap = False
    #Check if file or directory 
    if os.path.isfile(sys.argv[1]):
        parsing_objs.append(VMparser.VMParser(sys.argv[1]))
        #Parse this way if single file
        dot_index = sys.argv[1].find(".")
        out_file = sys.argv[1][0:dot_index] + ".asm"
    else:
        vm_files = glob.glob(sys.argv[1] + '/*.vm')
        for vm_file in vm_files: 
            print(vm_file)                                      #PROBLEM HERE. SHOULDNT RETURN THE ENTIRE PATHNAME
            parsing_objs.append(VMparser.VMParser(vm_file))
        #dot_index = sys.argv[1].find("/")
        out_file = sys.argv[1]+ "/" + sys.argv[1] + ".asm"
        isBootstrap = True

    
    coding_obj = codeWriter.codeWriter(out_file,isBootstrap) 

    for parsing_obj in parsing_objs:
        print(f'current file: {parsing_obj.current_file}\n')
        print('current_command: ',parsing_obj.current_command,'\n')
        parsing_obj.advance()
        coding_obj.setFileName(parsing_obj.current_file)
        counter = 0
        while parsing_obj.hasMoreCommands():
            print(f"======= Line {counter} =======\n")
            print('current_command: ',parsing_obj.current_command,'\n')
            print(f"command type is {parsing_obj.commandType()}\n")

            commandType = parsing_obj.commandType()

            if commandType == 0: #if command type is 0
                # feed arg1 into coding_obj.writeArithmetic
                coding_obj.writeArithmetic(parsing_obj.arg1())
            elif commandType == 1:
                # feed arg1 and arg2 into coding_obj.writePushPop 
                coding_obj.writePushPop(parsing_obj.commandType(),parsing_obj.arg1(),parsing_obj.arg2())
            elif commandType == 2:
                coding_obj.writePushPop(parsing_obj.commandType(),parsing_obj.arg1(),parsing_obj.arg2())
            elif commandType == 3: #C_LABEL
                coding_obj.writeLabel(parsing_obj.arg1())
            elif commandType == 4: #C_GOTO 
                coding_obj.writeGoto(parsing_obj.arg1()) 
            elif commandType == 5: #C_IF-GOTO
                coding_obj.writeIf(parsing_obj.arg1())
            elif commandType == 6: #C_FUNCTION 
                print("Printing Functions")
                coding_obj.writeFunction(parsing_obj.arg1(),parsing_obj.arg2()) 
            elif commandType == 7: #C_RETURN 
                coding_obj.writeReturn() 
            elif commandType ==8: #C_CALL
                coding_obj.writeCall(parsing_obj.arg1(),parsing_obj.arg2())
            counter = counter + 1
            parsing_obj.advance()
            #advance parsing
        parsing_obj.closefile() 

    coding_obj.close()
   