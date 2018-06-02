const int ** func();


const int ** func(){

    int var = 5;
    int * ptr = &var;
    int ** ptr2 = & ptr;

    return ptr2;

}


int main(){
    return 1;
}