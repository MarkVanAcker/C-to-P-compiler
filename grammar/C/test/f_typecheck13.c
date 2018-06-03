

int main(){

    int  *** array[10];

    int a = 6;
    int  *p = & a;

    return  ***array; // wrong pointer value (pointer depth wrong) should be 4 deref


}
