//Test code 

#include <stdio.h>
#include <string.h> 
#include "code.h"

int main(){
//destination codes
	char *dest_Tests[] = {NULL, "M","D", "MD", "A", "AM","AD","AMD","END"}; 
	char **dest_ptr = dest_Tests; 
	for(char **i = dest_ptr; i < dest_ptr+sizeof(dest_Tests)/sizeof(dest_Tests[0]); i++){
		if(*i == NULL){
			printf("NULL | %s\n", dest_c(*i));
		}else{
			printf("%s | %s\n", *i, dest_c(*i));
		}
		
	}

//compute codes
	char *comp_Tests[] = {"0","1", "-1", "D", "A","!D","!A","-D","-M","M+1","D-M","D|M","END"}; 
	char **comp_ptr = comp_Tests; 

	for(char **i = comp_ptr; i < comp_ptr+sizeof(comp_Tests)/sizeof(comp_Tests[0]); i++){
		if(*i == NULL){
			printf("NULL | %s\n", comp_c(*i));
		}else{
			printf("%s | %s\n", *i, comp_c(*i));
		}
	}
//jump codes
	char *jump_Tests[] = {NULL, "JGT","JEQ", "JGE", "JLT", "JNE","JNE","JLE","JMP","END"}; 
	char **jump_ptr = jump_Tests; 

	for(char **i = jump_ptr; i < jump_ptr+sizeof(jump_Tests)/sizeof(jump_Tests[0]); i++){
		if(*i == NULL){
			printf("NULL | %s\n", jump_c(*i));
		}else{
			printf("%s | %s\n", *i, jump_c(*i));
		}
	}
}