#include <stdio.h>

int faculty(int f){

if(f==2)
    return 2;


return f*faculty(f-1);
}


int main(){

int inp;

printf("Geef hier een getal in waarvan u de faculteit wilt berekenen: ");

scanf("%d",&inp);
int x = faculty(inp);

printf("%d faculteit is %d",inp,x);


}
