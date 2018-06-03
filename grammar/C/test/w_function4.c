int test (const float a, int ** d){ return 1;}

int othertest(const float a, int d, const int c){

    float * fptr  = & a;
    float ** fptr2 = & fptr;

    return 0;

    return 10;
}

int main(){

    int d = 5;
    float list [3];
    int lista [5];
    int ** pointer;
    int result = othertest(list[1],1, test(1.0,pointer));

    return 1;

}