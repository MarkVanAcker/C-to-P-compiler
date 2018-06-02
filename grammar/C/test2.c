

int a(int);

float xx = 7.0;

float x = 2.0 + 4.0 + xx;

int main(){

    int y = a(7) + 9;

    if (y < a(9)){
        int z = 8;
    }else if(y < a(9)){
        int z = 9;
        int p = 10;
        int q = p + z;
    }

    float zz  = 0.1;


    return 0;


}



int a(int b){
    int z = b+5;
    return z;
}