#include 'stdio.h'


int main(){

    float var = 10.1;
    float * var2 = &var;

    char mc = 'd';

    char array [10];

    printf("a %d %f %f %c %s aaa", 4, var, *var2, mc, 'mystring');
    return 1;

}