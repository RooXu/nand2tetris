//The Assembler 
/*This is the C Code written to convert symbolic representation of machine code (Assembly) into binary. The language neutral API for this assembler is described in chapter six of the Nand2Tetris textbook. I am writing this assembler in C to familiarize myself with the C syntax.*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	// Check if arguments are correct 
		// if argc has the correct number. Should be 3 
		// if the second and third arguments have the correct file extension. 
			//First file needs to be .asm
			//second file needs to be .hack 
	
	FILE *sourceF = fopen(*argv[1], "r");

	
	return 0; 
}
