#include 'stdio.h'


int main(){

    float var = 10.1;
    float * var2 = &var;

    char mc = 'd';

    printf("a %d %f %f %c aaa", 4, var, *var2, mc);
    return 1;

}