#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define false -1

void extractPattern(char *pattern, char *buffer) {
	int flag = 0;
	int fidx = 0,sidx = 0,tidx = 0,fridx = 0;
	char* bufTemp = (char*)malloc(sizeof(char)*2);	
	for (int i = 0; i < strlen(pattern); i++) {
		if (pattern[i] == 'i') {
				if (fidx == 0)
					fidx = i;
				else 
					sidx = i;
		}
		if (pattern[i] == 'u')
			tidx = i;
		else if (pattern[i] == '@')
			fridx = i;
	}
	bufTemp[0] = pattern[fidx];
	bufTemp[1] = '\0';
	strcat(buffer,bufTemp);

	bufTemp[0] = pattern[sidx];
	bufTemp[1] = '\0';
	strcat(buffer,bufTemp);	

	bufTemp[0] = pattern[tidx];
	bufTemp[1] = '\0';
	strcat(buffer,bufTemp);
	
	bufTemp[0] = pattern[fridx];
	bufTemp[1] = '\0';
	strcat(buffer,bufTemp);

	for (int i = fridx+1; i < strlen(pattern); i++) {
		bufTemp[0] = pattern[i];
		bufTemp[1] = '\0';
		strcat(buffer,bufTemp);
	}

}

int main(void) {
	char* pattern = (char*)malloc(sizeof(char)*2048);
//	char pattern[1024];
	char* buffer = (char*)malloc(sizeof(char)*1024);
	
	printf("Please enter your string here : ");
	scanf("%s",pattern);
	extractPattern(pattern, buffer);

	printf("\n%s\n",buffer);
	return 0;
}
