int main (){

    int a;
    int * p = &a;
    int ** p2 = &a; // wrong pointer value (pointer depth wrong)
    p = *p2;
    return 1;
}