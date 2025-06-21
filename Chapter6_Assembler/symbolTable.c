//Symbol Table
/* This module describes a frame that handles any user defined symbols in the hack assembly languages. For any new symbol it is fed, it stores in its static variable, assigns an address to that symbol in decimal, and returns its decimal address upon request.*/ 

#include <stdio.h>
#include "symbolTable.h" 
#include <string.h> 
#include <stdlib.h>

typedef struct {
	char *letters; 
	int addr;
} SYMBOL;

static unsigned int max; 
static unsigned int hash(char *symbol){
	unsigned int sum_a = 0; 
	unsigned int sum_b = 0;
	unsigned int power = 1; 
	
	//Hash 1; discards left 28 bits

	//Hash 2 ; discards right 28 bits 

	//combine two hashes & multiply by final char

	
	for(int i = 0; symbol[i] != '\0'; i++){
		sum_a = 57 * sum_a + symbol[i] % 191453;
		sum_b = 251 * sum_b + symbol[i] % 1000000007;
	}
	if(sum_a >= max){
		max = sum_a; printf("--------------------MAX preHASH %u\n",max);
	}
	return (sum_b) % 159544; 
}

static unsigned int hash_gpt(char *symbol){
//sdbm
	unsigned long hash = 0;
    	int c;

    	while((c = *symbol++)){
        	hash = c + (hash << 7) + (hash << 33) - hash;
	}
    	return hash % 2017;  // or any prime ≥ 200
}


static SYMBOL **table = NULL; 

void construct_table(){
	table = malloc(191453 * sizeof(SYMBOL *)); 
	for(int i = 0; i <191453; i++){
		table[i]=malloc(sizeof(SYMBOL));
		table[i] -> letters = NULL;
		table[i] -> addr = -1;
	}
	max = 0;
}

int addEntry(char *symbol, int address){
	int index = hash(symbol); 
	table[index] -> letters = symbol;
	table[index] -> addr = address;
	return 0; 
}

int contains(char *symbol){
	int index = hash(symbol);
	printf("Hash Res: %d\n",index);
	if((table[index] -> letters) != NULL){
		return 1; 
	}
	return 0;	
}

int getAddress(char *symbol){
	int index = hash(symbol);
	printf("getAddress::index of hash is: %d\n",index);
	if(contains(symbol)){
		return table[index] -> addr;
	}else{
		return -1;
	}
}

