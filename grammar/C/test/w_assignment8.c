int main(){

    int  t = 1;

    int * v1= &t;
    int ** v2 = &v1;

    if (**v2 < 4){
     return **v2;
    }

    int * ptr = &t;
    int **ptr2 = &ptr;


    int a = *ptr + 6 + **ptr2 + *ptr;


    return a;


}