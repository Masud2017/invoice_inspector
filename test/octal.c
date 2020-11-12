#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int digitCount(int input) {
	int count = 0;
	while (input > 0) {
		input /= 10;
		count++;
	}
	return count;
}


int *digitSeperator(int input) {
	int *buffer = (int*)malloc(sizeof(int)*digitCount(input));
	int i = 0;
	while (input > 0) {
		buffer[i] = input % 10;
		input /= 10;
		i++;
	}
	return buffer;
}

int convertToDecimal(int input) {
	int temp = input;
	int j = 0, sum = 0;
	int *buffer = (int*)malloc(sizeof(int)*digitCount(input));
	buffer = digitSeperator(input);
	for (int i = 0 ; i < digitCount(input); i++) {
		sum += (buffer[i]*(int)pow(8,j));
		j++;
	}
	return sum;
}

int main()  {
	int input;
	printf("Enter your input :  ");
	scanf ( "%d",&input);
	printf("\nAnswer : %d\n",convertToDecimal(input));
	return 0;
}
