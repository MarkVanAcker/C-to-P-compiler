int testmain (const float);


int test (const float a, int ** d){ return 1;}

float othertest(const float a, int d){

    int *var = &d;
    if ( 0 == 0 ){
        return 2.0 ;
    }
    else if ( 3 < 4 ) {
        return 1.0;
    }else{
        return 0.3;
    }

    return 1.0;}

int main(){

    int d = 5;
    float list [3];
    int lista [5];

    int result = test(list[1],1);

    return 1;

}