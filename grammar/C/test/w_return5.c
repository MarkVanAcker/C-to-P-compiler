const int ** func();


const int ** func(){

    int var = 5;
    int * ptr = &var;
    int ** ptr2 = & ptr;
    int ** ptr3 = &ptr2;

    return *ptr3;

}


int main(){
    return 1;
}