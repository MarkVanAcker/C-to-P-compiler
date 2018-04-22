#include <stdio.h>


float function(float b){
    return 2*b;
}

int main()
{
    int integerType;
    float floatType = 1.0;
    char charType;

    int a = 0;
    for(a=2;a<10;a=a+1){

        // Sizeof operator is used to evaluate the size of a variable
        printf('Size of int: %ld bytes\n',sizeof(integerType));
        printf("Size of float: %ld bytes\n",sizeof(floatType));
        printf("Size of double: %ld bytes\n",sizeof(doubleType));
        printf("Size of char: %ld byte\n",sizeof(charType));
        
        f(1.0);
    }

    return 0;
}
