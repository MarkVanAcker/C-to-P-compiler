#include <stdio.h>


void main(){

    int y = 4;

    int * z;
    int ** x;
    z= &y;

    x = &z;

    y = **x;
}
