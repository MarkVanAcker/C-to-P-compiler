int main (){

    int var1 = 5;

    int var2 = 5;

    int * ptr1 = & var1;

    int * ptr2 = & var2;

    while (*ptr2 == *ptr1){

            *ptr1 = 6;
    }


    return 1;

}