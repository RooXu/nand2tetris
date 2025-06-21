//Symbol Table Header

#include <stdio.h>
#include <string.h> 
#ifndef SYMBOLTABLE 
#define SYMBOLTABLE

void construct_table();
int addEntry(char *symbol, int address);
int contains(char *symbol);
int getAddress(char *symbol);
#endif