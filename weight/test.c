// Port of generate_data in C

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define _USE_MATH_DEFINES

double generate_data(int lw1, int lw2, int lw3, int sw1, int sw2, int sw3, int max1, int max2, int max3) {
	int i, j, k;
	double x1, x2, x3, w, weight;
    x1 = -1 * lw1 * M_PI / sw1;
    x2 = -1 * lw2 * M_PI / sw2;
    x3 = -1 * lw3 * M_PI / sw3;
    for (i = 0; i < max1; i++) {
    	for (j = 0; j < max2; j++) {
    		for (k = 0; k < max3; k++) {
    			 w = exp(i * x1) * exp(j * x2) * exp(j * x3);
    			 weight = pow(((float)rand()/RAND_MAX), (1/w));
    			 printf("%e %f\n", weight, ((float)rand()/RAND_MAX));
    		}
    	}
    }
}

main() {
	generate_data(10, 20, 30, 1000, 2000, 3000, 10, 10, 10);
}