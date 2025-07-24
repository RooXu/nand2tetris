import sys 

class VMParser:
    command_types = {
        'add' : 0,
        'sub' : 0,
        'neg' : 0,
        'eq'  : 0,
        'gt'  : 0,
        'lt'  : 0,
        'and' : 0,
        'or'  : 0,
        'not' : 0,
        'pop' : 2,
        'push': 1,
        'label':3,
        'goto':4,
        'if-goto':5,
        'function':6,
        'return':7,
        'call':8,
        '': -1 }
    segment_type = {
        "local" : "LCL",
        "this"  : "THIS",
        "that"  : "THAT",
        "argument":"ARG",
        "static" : "static",
        "pointer" : "pointer",
        "temp" : "temp",
        "constant" : "constant"
    }
    stream_loc = -1
    def __init__(self,vm_file):
        self.current_path = vm_file
        slash_index = vm_file.find("/")+1
        self.current_file = vm_file[slash_index:]
        self.file = open(vm_file)
        self.current_command = '\n'
        self.args = []
    
    def hasMoreCommands(self):
        #print("Previous Loc:" + str(self.stream_loc))
        #print("Current Loc:" + str(self.file.tell()))
        if self.stream_loc != self.file.tell():
            return True
        else:
            return False
 
    
    def advance(self):
        #print('advancing\n')
        if not(self.hasMoreCommands()):
            raise Exception("No More Commands Left")
        self.stream_loc = self.file.tell()
        self.current_command = self.file.readline().lstrip()
        
    
        #print("file read\n")
        if (self.current_command.isspace() or self.current_command == ''):
            self.current_command = '//'
        
        has_comment = self.current_command.find('//')
        if has_comment == -1:
            self.args = self.current_command.split()
        elif has_comment == 0:
            self.args = ['']
        else:
            self.args = self.current_command[0:has_comment].split()
        
       
        # Reads Next command from input and makes it the current command. Should be called only if hasMore Commands() is True. Initially, there is no current command

    def commandType(self):
        # Returns 0 = C_ARITHMETIC
        # Returns 1 = C_PUSH
        # Returns 2 = C_POP
        # Returns 3 = C_LABEL
        # Returns 4 = C_GOTO
        # Returns 5 = C_IF
        # Returns 6 = C_FUNCTION
        # Returns 7 = C_RETURN
        # Returns 8 = C_CALL
        # Returns -1 = White space or Comment
        return self.command_types[self.args[0]]

    def arg1(self):
        # Returns a string
        # Returns first argument of current command
        if self.commandType() == 0:
            return self.args[0]
        elif self.commandType() == 7:
            raise Exception("This function cannot be used for RETURN commands") # Raise Exception 
        elif self.commandType() == -1:
            raise Exception("Cannot return args for comments")
        else:
            try:
                return self.segment_type[self.args[1]]
            except IndexError as err:
                raise IndexError(f"Expected second argument for this command type: {self.args[0]}") from err
            except KeyError:
                return self.args[1]
                

    def arg2(self):
        # Returns int
        # Returns the second argument of current command. 
        # Only for POP,PUSH,FUNCTION,CALL 
        if self.commandType() == 1 or self.commandType() == 2 or self.commandType() ==6 or self.commandType() == 8:
            return self.args[2]
        else:
            raise Exception("This function is reserved only for POP, PUSH, FUNCTION, and CALL commands")
        
    def closefile(self):
        self.file.close()

if __name__ == "__main__": 
    parsing_obj = VMParser(sys.argv[1])
    print('current_command: ',parsing_obj.current_command,'\n')
    parsing_obj.advance()
    counter = 0
    while parsing_obj.hasMoreCommands():
        print('===== Line ', counter, ' =======\n')
        print('current_command: ',parsing_obj.current_command,'\n')
        print('args: ', parsing_obj.args,'\n')
        print(' Has More Commands? ', parsing_obj.hasMoreCommands(),'\n')
        print(' command type: ', parsing_obj.commandType(),'\n')
        if parsing_obj.commandType() > -1:
            if parsing_obj.commandType() != 7:
                print(' arg1: ', parsing_obj.arg1(),'\n')
            if parsing_obj.commandType() == 1 or parsing_obj.commandType() == 2 or parsing_obj.commandType() ==6 or parsing_obj.commandType() == 8:
                print(' arg2: ', parsing_obj.arg2(),'\n')
        parsing_obj.advance()
        counter= counter + 1
    parsing_obj.closefile()
