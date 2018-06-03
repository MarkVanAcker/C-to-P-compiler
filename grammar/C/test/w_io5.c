#include 'stdio.h'


int main(){

    float var = 10.1;
    float * var2 = &var;


    printf("a %d %f %f aaa", 4, var, *var2);
    return 1;

}