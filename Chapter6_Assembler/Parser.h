//Parser Header
#include <stdio.h>
#ifndef PARSER 
#define PARSER

int construct(FILE *source, FILE *binary);
int hasMoreCommands();
int advance();
int commandType(); 
char *symbol(); 
char *dest(); 
char *comp(); 
char *jump(); 

#endif 
	   
