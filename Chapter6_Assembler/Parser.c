//Parser Implementation 

#include "parser.h" 
#include <ctype.h>
#include <string.h>
#include <stdio.h>

static FILE *sourceLocal;
static FILE *binaryLocal;
static char currentCommand[50];
static char currentCommandTrim[50];
static char symbol_dat[50];
static char dest_dat[4];
static char comp_dat[4];
static char jump_dat[4];
static char buffer[50];

int construct(FILE *source, FILE *binary){
	sourceLocal = source;
	binaryLocal = binary;
	printf("+++++ CHECKING LOCAL POINTER:START ++++++\n");
	if(sourceLocal == NULL){
		return 1;
	}else{
	//	while(fgets(buffer, 50, sourceLocal)){
	//		fputs(buffer, stdout);
	//	}
	}
	printf("+++++ CHECKING LOCAL POINTER:DONE ++++++\n");
	rewind(sourceLocal);
	if(binaryLocal == NULL){
		return 1;
	}
	return 0;
}

int hasMoreCommands(){
	return !feof(sourceLocal);
}

int advance(){
	memset(currentCommand, 0, sizeof(currentCommand)); 
	memset(currentCommandTrim, 0, sizeof(currentCommandTrim)); 
	fgets(currentCommand, 50, sourceLocal);
	for(int i = 0, j = 0 ; i<50; i++){
		if((currentCommand[i] == '/') && currentCommand[i] == '/'){
		// Senses comments
			break;
		}
		if(!isspace(currentCommand[i])){
			currentCommandTrim[j] = currentCommand[i];
			j++;
		}
	}
	printf("Current Line:\n   %s\n",currentCommandTrim);
	return 0;
}

int commandType(){
// Command Type | ASCII code for letter
// A_command    | 65
// C_command    | 67
// L_command    | 76
// comment      | 0
// other        | -1

	if(currentCommandTrim[0] == '@'){
		return 65;
	}else if((currentCommandTrim[0] == 'D') || (currentCommandTrim[0] == 'M') || (currentCommandTrim[0] == 'A') || (currentCommandTrim[0] == '0')|| (currentCommandTrim[0] == '1')|| (currentCommandTrim[0] == '-')|| (currentCommandTrim[0] == '!')){
		return 67; 
	}else if(currentCommandTrim[0] == '('){
		return 76;
	}else if((currentCommandTrim[0] == '/') && currentCommandTrim[1] == '/'){
		return 0;
	}
	return -1;
}

char *symbol(){
	memset(symbol_dat, 0, sizeof(symbol_dat)); 
	if((commandType() == 65) || (commandType() == 76)){
		for(int i = 1, j = 0; i < 50; i++){
			if((currentCommandTrim[i] == ')') || !(currentCommandTrim[i])){
				break;
			}else{
				symbol_dat[j] = currentCommandTrim[i];
				j++;
			}
		}
		return symbol_dat;
	}
	return NULL; 
}

char *dest(){
	memset(dest_dat, 0, sizeof(dest_dat)); 
	if(commandType() == 67){
		if(strstr(currentCommandTrim,"=") == NULL){
			return NULL;
		}else{
			for(int i = 0, j = 0; i < 5 ; i++, j++){
				if(currentCommandTrim[i] == '='){
					break;
				}else{
					dest_dat[j] = currentCommandTrim[i];
				}
			}
		}
		return dest_dat;
	}
	return NULL; 
}

char *comp(){
	memset(comp_dat, 0, sizeof(comp_dat)); 
	if(commandType() == 67){
		if(strstr(currentCommandTrim,"=") == NULL){
			for(int i = 0; i < 5; i++){
				if(currentCommandTrim[i] == ';'){
					break;
				}else{
					comp_dat[i] = currentCommandTrim[i];
				}
			}
			return comp_dat;
		}else{
			int index = strstr(currentCommandTrim,"=") - currentCommandTrim;
			printf("The equal sign is at index: %d\n", index);
			for(int i = index+1, j = 0; i < 8; i++, j++){
				if(currentCommandTrim[i] == ';'){
					break;
				}else{
					comp_dat[j] = currentCommandTrim[i];
				}
			}
			return comp_dat;
		}
	}
	return NULL;
}

char *jump(){
	memset(jump_dat, 0, sizeof(jump_dat)); 
	if(strstr(currentCommandTrim,";") != NULL){
		int index = strstr(currentCommandTrim,";") - currentCommandTrim;
		for(int i = index+1, j = 0; i<13; i++, j++){
			if(currentCommandTrim[i]){
				jump_dat[j] = currentCommandTrim[i];
			}
		}
		return jump_dat;
	}
	return NULL; 
}