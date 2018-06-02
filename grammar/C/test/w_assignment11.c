float ** func(int * pointer);

float ** func(int * pointer){

    float var = 5.0;
    float * ptr = & var;
    float ** ptr2;
    ptr2 = & ptr;

    return ptr2;

}

int main(){

    int* p;
    float ** returnvalue = func(p);

    return 1;

}