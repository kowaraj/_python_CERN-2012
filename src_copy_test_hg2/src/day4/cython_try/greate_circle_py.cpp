#include <math.h>
#include <stdio.h>

#define NUM 500000

int main() {
    int i;
    float x;
    for (i=0; i <= NUM; i++) 
        x = great_circle(-72.345, 34.323, -61.823, 54.826);
    printf("%f", x);
}
