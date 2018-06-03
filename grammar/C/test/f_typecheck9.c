int main (){

    int a;
    int * p = &a;
    int ** p2 = &p;
    **p2 = p;
    return 1;
}