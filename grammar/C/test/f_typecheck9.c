
int main (){

    int a;
    int * p = &a;
    int ** p2 = &p;
    **p2 = p; // wrong pointer value (pointer depth wrong)
    return 1;
}