// Chained comparisons do not work as expected in C, but do in Python.
//
// $ gcc -o 30-comp 30-comp.c
// $ ./30-comp

#include <stdio.h>

int main() {
	int x = 10;
	if (1 < x < 5) {
		printf("Really?\n");
	}
}
