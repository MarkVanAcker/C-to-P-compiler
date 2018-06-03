int main (){

    int a;
    int * p = &a;
    int ** p2 = &a;
    p = *p2;
    return 1;;
}