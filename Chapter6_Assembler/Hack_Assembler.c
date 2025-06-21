//The Assembler 
/*This is the C Code written to convert symbolic representation of machine code (Assembly) into binary. The language neutral API for this assembler is described in chapter six of the Nand2Tetris textbook. I am writing this assembler in C to familiarize myself with the C syntax.*/

//NOTES
// - The current hash function works to assemble all testfiles provided by the nand2tetris course (Max, Rect, and Pong). 
// - Because my hash function is so terrible, there is no guarrantee it will work on other programs. Collision is imminent. 
// - IF I every use this code again for actual use (whenever I try to physically build or make a hack computer on a microcontroller), I will need to get a hash utility from somewhere. 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "parser.h"
#include "code.h"
#include "symbolTable.h" 

int main(int argc, char *argv[]) {
	// Check if arguments are correct 
	printf("===== CHECKING ARGUMENTS=====\n");
	printf("There are %d Arguments\n",argc);          // if argc has the correct number. Should be 3 
	printf("The first argument is: %s \n", argv[0]); 
	printf("The second argument is: %s \n", argv[1]); //is .asm file?
	printf("The third argument is: %s \n", argv[2]);  // is .hack file?
	
	FILE *sourceF = fopen(argv[1], "r");
	FILE *binaryF = fopen(argv[2], "w"); 


		// if the second and third arguments have the correct file extension. 
			//First file needs to be .asm
			//second file needs to be .hack 

	printf("=====Is Source Empty?====\n");
	char buffer[50];
	if(sourceF == NULL){
		printf("FAILED READ");
	}else{
	//	while(fgets(buffer, 50, sourceF)){
	//		fputs(buffer, stdout);
	//	}
	}
	rewind(sourceF);
	printf("======== ASSEMBLING ==========\n");

	int loadStat = construct(sourceF, binaryF); 

	printf("File Open Successfully Into Frame: %d\n", loadStat);
	int counter = 0; 
	printf("Has More Commands?: %d\n", hasMoreCommands());

	char binarybuffer[256];
	memset(binarybuffer,0, 256);
	static char *c_command_head = "111"; 

	int comType = 0; 

	char *destBin;
	char *compBin;
	char *jumpBin;
	char *symbolRes = NULL;
	char *symbolProbe;
	char symbolBit[2]; symbolBit[1] = '\0';
	int aDecimal;
	construct_table();
	
	int symbolTally = 16; 
	int address_counter = 0; 

	while(hasMoreCommands()){
		advance();
		comType = commandType();
		symbolRes = symbol();
		if(comType == 76){
			if(symbolRes == NULL){printf("ERROR: symbol() returned NULL");return -1;}
			addEntry(symbol(),address_counter);
		}
		if(comType != 0 && comType != -1 && comType != 76){address_counter++;}; 
	}
	rewind(sourceF); 
	address_counter = 0; 

	while(hasMoreCommands()){
		printf("======First PASS Line %d=======\n",counter);
		advance();
		comType = commandType();
		symbolRes = symbol();
		if(comType == 65 || comType == 76){
			if(symbolRes == NULL){printf("ERROR: symbol() returned NULL");return -1;}
			aDecimal = strtol(symbolRes,&symbolProbe,10);
			if(symbolProbe[0] != '\0'){ 
				printf("BUMBBY\n");
				if((!contains(symbol()))){
					printf(".   CHUMMY\n");
					if((!strcmp(symbol(),"SP") || !strcmp(symbol(),"R0"))){
						printf("---BOOM---");
						addEntry(symbol(),0);
					}else if((!strcmp(symbol(),"LCL") || !strcmp(symbol(),"R1"))){
						addEntry(symbol(),1);
					}else if(!(strcmp(symbol(), "ARG") && strcmp(symbol(),"R2"))){
						addEntry(symbol(),2);
					}else if(!(strcmp(symbol(), "THIS") && strcmp(symbol(),"R3"))){
						addEntry(symbol(),3);
					}else if(!(strcmp(symbol(),"THAT") && strcmp(symbol(),"R4"))){
						addEntry(symbol(),4);
					}else if(!(strcmp(symbol(),"R5"))){
						addEntry(symbol(),5);
					}else if(!(strcmp(symbol(),"R6"))){
						addEntry(symbol(),6);
					}else if(!(strcmp(symbol(),"R7"))){
						addEntry(symbol(),7);
					}else if(!(strcmp(symbol(),"R8"))){
						addEntry(symbol(),8);
					}else if(!(strcmp(symbol(),"R9"))){
						addEntry(symbol(),9);
					}else if(!(strcmp(symbol(),"R10"))){
						addEntry(symbol(),10);
					}else if(!strcmp(symbol(),"R11")){
						addEntry(symbol(),11);
					}else if(!strcmp(symbol(),"R12")){
						addEntry(symbol(),12);
					}else if(!strcmp(symbol(),"R13")){
						addEntry(symbol(),13);
					}else if(!strcmp(symbol(),"R14")){
						addEntry(symbol(),14);
					}else if(!strcmp(symbol(),"R15")){
						printf("-KABOOM-");
						addEntry(symbol(),15);
					}else if(!strcmp(symbol(),"SCREEN")){
						addEntry(symbol(),16384);
					}else if(!strcmp(symbol(),"KBD")){
						addEntry(symbol(),24576);
					}else{
						if(symbolTally == 16384 && comType != 76){
							symbolTally++;
							addEntry(symbol(),symbolTally);
							symbolTally++;
						}else if(symbolTally >= 24576 && comType != 76){
							printf("ERROR: OUT OF SYMBOL MEMORY\n");
							return -1;
						}else if(!contains(symbol()) && comType != 76){
							addEntry(symbol(),symbolTally);
							printf("Address is %d\n",symbolTally);
							symbolTally++;
						}else if(comType == 76){
							addEntry(symbol(), address_counter);
						}
					}
					printf("Address Stored Right? %d\n", getAddress(symbol()));
				}
			}
		}
		if(comType != 0 && comType != -1 && comType != 76){address_counter++;}; 
		
		
	}
	rewind(sourceF);
	counter = 0; 
	while(hasMoreCommands()){
		memset(binarybuffer,0, 256);
		printf("======Line %d=======\n",counter);
		counter++;
		printf("Advancing: Status: %d\n",advance()); 
		
		comType = commandType();
		printf("Return Command Type %d\n", comType); 
		
		if(comType == 67){
			destBin = dest_c(dest());
			compBin = comp_c(comp());
			jumpBin = jump_c(jump()); 
			if(destBin == NULL){
				printf("ERROR: Unexpected Destination Code\n");
				printf("|-dest_c returned NULL\n");
				printf("|--dest() returned: %s\n", dest());
				return -1;			
			}
			if(compBin == NULL){
				printf("ERROR: Unexpected Compute Code\n");
				printf("|- comp_c returned NULL\n");
				printf("|-- comp() returned: %s\n", comp());
				return -1;			
			}
			if(jumpBin == NULL){
				printf("ERROR: Unexpected Jump Code\n");
				printf("|- jump_c returned NULL\n");
				printf("|-- jump() returned: %s\n", jump());
				return -1;		
			}
			strcat(binarybuffer,c_command_head);	
			strcat(binarybuffer,compBin);	
			strcat(binarybuffer,destBin);	
			strcat(binarybuffer,jumpBin);
		}else if(comType == 65){
			symbolRes = symbol();
			if(symbolRes == NULL){printf("ERROR: symbol() returned NULL");return -1;}
			aDecimal = strtol(symbolRes,&symbolProbe,10);
			strcat(binarybuffer,"0");
			if(symbolProbe[0] != '\0'){ 
				if(contains(symbolRes)){
					aDecimal = getAddress(symbolRes);
					printf("Decimal Address of Symbol: %d\n", aDecimal);
				}
			}
			for(int i = 14; i >= 0; i--){
				symbolBit[0] = ((aDecimal >> i) & 1)+'0';
				strcat(binarybuffer, symbolBit);
			}
			printf("Binary of Address: %s\n",binarybuffer);

		}
		strcat(binarybuffer,"\n");
		
		if(binarybuffer[0] != '\n'){
			fputs(binarybuffer,binaryF);
		}
		if(symbolRes != NULL){
			printf("Symbol of Command: %s\n", symbolRes); 
		}else{
			printf("Symbol of Command: NULL\n");
		}
		if((destBin != NULL) && (comType == 67)){
			printf("Destination of Command: %s\n", destBin); 
		}else{
			printf("Destination of Command: NULL\n");
		}
		if((compBin != NULL) && (comType == 67)){
			printf("Computation of Command: %s\n", compBin); 
		}else{
			printf("Computation of Command: NULL\n");
		}
		if((jumpBin != NULL) && (comType == 67)){
			printf("Jump of Command: %s\n", jumpBin); 
		}else{
			printf("Jump of Command: NULL\n");
		}
	}
	
	fclose(sourceF); fclose(binaryF); 

	return 0; 
}
