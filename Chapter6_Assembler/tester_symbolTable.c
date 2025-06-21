//SymbolTable Test

#include <stdio.h>
#include <string.h> 
#include "symbolTable.h"

int main(){
	char *testWords[] = {"BOB", "LOOP", "xxx", "aba","ab","ba","PACK","END",NULL};
	construct_table(); 
	printf("Test Contains on Construction: %d\n", contains("i"));
	printf("Adding i: %d\n", addEntry("i",69)); 
	printf("Getting address of i: %d\n", getAddress("i"));

	for (int i = 0; testWords[i] != NULL; i++) {
		printf("TEST %d ====================\n",i);
    		printf("Test Contains on Construction: %d\n", contains(testWords[i]));
		printf("Adding %s: %d\n", testWords[i], addEntry(testWords[i],i)); 
		printf("Getting address of %s: %d\n", testWords[i] ,getAddress(testWords[i]));
	}
	return 0; 
}