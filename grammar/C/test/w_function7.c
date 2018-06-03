int test (const float a, int ** d, char array []){ return 1;}


int othertest(const float, int d, const int );

int main(){

    int d = 5;
    float list [3];
    int lista [5];
    int ** pointer;
    char array [20];
    int result = othertest(list[1],1,**pointer);

    return 1;

}

int othertest(const float a, int d, const int c){

    float * fptr  = & a;
    float ** fptr2 = & fptr;

    return 1;
}
