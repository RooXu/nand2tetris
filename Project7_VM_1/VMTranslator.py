import sys
import VMparser
import codeWriter

if __name__ == "__main__": 

    parsing_obj = VMparser.VMParser(sys.argv[1])
    dot_index = sys.argv[1].find(".")
    out_file = sys.argv[1][0:dot_index] + ".asm"
    
    coding_obj = codeWriter.codeWriter(out_file)

    print('current_command: ',parsing_obj.current_command,'\n')
    parsing_obj.advance()
    counter = 0
    while parsing_obj.hasMoreCommands():
        print(f"======= Line {counter} =======\n")
        print('current_command: ',parsing_obj.current_command,'\n')
        print(f"command type is {parsing_obj.commandType()}\n")
        if parsing_obj.commandType() == 0: #if command type is 0
            # feed arg1 into coding_obj.writeArithmetic
            coding_obj.writeArithmetic(parsing_obj.arg1())
        elif parsing_obj.commandType() == 1:
            # feed arg1 and arg2 into coding_obj.writePushPop 
            coding_obj.writePushPop(parsing_obj.commandType(),parsing_obj.arg1(),parsing_obj.arg2())
        elif parsing_obj.commandType() == 2:
            coding_obj.writePushPop(parsing_obj.commandType(),parsing_obj.arg1(),parsing_obj.arg2())
        counter = counter + 1
        parsing_obj.advance()
        #advance parsing
    coding_obj.close()
