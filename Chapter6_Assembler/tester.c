//Testing 
/* This C Script is for Testing my routines in my modules. */ 

#include "Parser.h" 

int main(int argc, char *argv[]){
	printf("===== CHECKING ARGUMENTS=====\n");
	printf("There are %d Arguments\n",argc);
	printf("The first argument is: %s \n", argv[0]);
	printf("The second argument is: %s \n", argv[1]);
	printf("The third argument is: %s \n", argv[2]);
	
	FILE *sourceF = fopen(argv[1], "r");
	FILE *binaryF = fopen(argv[2], "w");

	printf("=====Is Source Empty?====\n");
	char buffer[50];
	if(sourceF == NULL){
		printf("FAILED READ");
	}else{
		while(fgets(buffer, 50, sourceF)){
			fputs(buffer, stdout);
		}
	}
	rewind(sourceF);
	printf("======== TESTING PARSE MODULE ==========\n");
	
	int loadStat = construct(sourceF, binaryF); 

	printf("File Open Successfully: %d\n", loadStat);
	int counter = 0; 
	printf("Has More Commands?: %d\n", hasMoreCommands());
	while(hasMoreCommands()){
		printf("======Line %d=======\n",counter);
		counter++;
		printf("Advancing: Status: %d\n",advance()); 
		printf("Return Command Type %d\n",commandType()); 
		
		char *symbolRes = symbol();
		char *destRes = dest();
		char *compRes = comp();
		char *jumpRes = jump(); 

		if(symbolRes != NULL){
			printf("Symbol of Command: %s\n", symbolRes); 
		}else{
			printf("Symbol of Command: NULL\n");
		}
		if(destRes != NULL){
			printf("Destination of Command: %s\n", destRes); 
		}else{
			printf("Destination of Command: NULL\n");
		}
		if(compRes != NULL){
			printf("Computation of Command: %s\n", compRes); 
		}else{
			printf("Computation of Command: NULL\n");
		}
		if(jumpRes != NULL){
			printf("Jump of Command: %s\n", jumpRes); 
		}else{
			printf("Jump of Command: NULL\n");
		}
	}
	
	fclose(sourceF); fclose(binaryF); 
	return 0; 
}