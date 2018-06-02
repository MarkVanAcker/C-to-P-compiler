
int * fun(int ** );
int * fun(int  ** a){

    int *pttt [5];

    int v = 4;
    int * ptr = &v;
    *ptr = v;
    int alpha = *ptr;
    return ptr;
}




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


}

/* if (*t < 4){
     return 1;
    }

    int * ptr = &t;
    int *ptr2 = ptr;


    int a = *ptr + &ptr + **ptr2 + ptr2;
    */