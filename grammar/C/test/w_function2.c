int testmain (const float);

int testmain(float a){

    return 1;
}


int test (const float a, int ** d){ return 1;}

float othertest(const float a, int d){



    return 1.0;}

int main(){

    int d = 5;
    float list [3];
    int lista [5];

    int * p = & d;
    int ** pointer = & p;

    int result = test(list[1],pointer);

    return 1;

}