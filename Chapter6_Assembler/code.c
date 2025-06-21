//Code Module
/* This module returns the binary code for the assembly mnemonic entered*/ 

#include "code.h"
#include <stdio.h>
#include <string.h>

char* dest_c(char *mnemonic){
	
	if(mnemonic == NULL){
		return "000";
	}else if(!strcmp(mnemonic,"M")){
		return "001";
	}else if(!strcmp(mnemonic,"D")){
		return "010";
	}else if(!strcmp(mnemonic,"MD")){
		return "011";
	}else if(!strcmp(mnemonic,"A")){
		return "100";
	}else if(!strcmp(mnemonic,"AM")){
		return "101";
	}else if(!strcmp(mnemonic,"AD")){
		return "110";
	}else if(!strcmp(mnemonic,"AMD")){
		return "111";
	}else{
		return NULL;
	}
	return "-1";
}

char* comp_c(char *mnemonic){
	
	if(!strcmp(mnemonic,"0")){
		return "0101010";
	}else if(!strcmp(mnemonic,"1")){
		return "0111111";
	}else if(!strcmp(mnemonic,"-1")){
		return "0111010";
	}else if(!strcmp(mnemonic,"D")){
		return "0001100";
	}else if(!strcmp(mnemonic,"A")){
		return "0110000";
	}else if(!strcmp(mnemonic,"M")){
		return "1110000";
	}else if(!strcmp(mnemonic,"!D")){
		return "0001101";
	}else if(!strcmp(mnemonic,"!A")){
		return "0110001";
	}else if(!strcmp(mnemonic,"!M")){
		return "1110001";
	}else if(!strcmp(mnemonic,"-D")){
		return "0001111";
	}else if(!strcmp(mnemonic,"-A")){
		return "0110011";
	}else if(!strcmp(mnemonic,"-M")){
		return "1110011";
	}else if(!strcmp(mnemonic,"D+1")){
		return "0011111";
	}else if(!strcmp(mnemonic,"A+1")){
		return "0110111";
	}else if(!strcmp(mnemonic,"M+1")){
		return "1110111";
	}else if(!strcmp(mnemonic,"D-1")){
		return "0001110";
	}else if(!strcmp(mnemonic,"A-1")){
		return "0110010";
	}else if(!strcmp(mnemonic,"M-1")){
		return "1110010";
	}else if(!strcmp(mnemonic,"D+A")){
		return "0000010";
	}else if(!strcmp(mnemonic,"D+M")){
		return "1000010";
	}else if(!strcmp(mnemonic,"D-A")){
		return "0010011";
	}else if(!strcmp(mnemonic,"D-M")){
		return "1010011";
	}else if(!strcmp(mnemonic,"A-D")){
		return "0000111";
	}else if(!strcmp(mnemonic,"M-D")){
		return "1000111";
	}else if(!strcmp(mnemonic,"D&A")){
		return "0000000";
	}else if(!strcmp(mnemonic,"D&M")){
		return "1000000";
	}else if(!strcmp(mnemonic,"D|A")){
		return "0010101";
	}else if(!strcmp(mnemonic,"D|M")){
		return "1010101";
	}else{
		return NULL;
	}
	return "-1";
}
char* jump_c(char *mnemonic){
	if(mnemonic == NULL){
		return "000";
	}else if(!strcmp(mnemonic,"JGT")){
		return "001";
	}else if(!strcmp(mnemonic,"JEQ")){
		return "010";
	}else if(!strcmp(mnemonic,"JGE")){
		return "011";
	}else if(!strcmp(mnemonic,"JLT")){
		return "100";
	}else if(!strcmp(mnemonic,"JNE")){
		return "101";
	}else if(!strcmp(mnemonic,"JLE")){
		return "110";
	}else if(!strcmp(mnemonic,"JMP")){
		return "111";
	}else{
		return NULL;
	}
	return "-1";
}