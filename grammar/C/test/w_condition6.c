int * func(const int );

int * func(const int a){

        return &a;
}


int main(){

    int ret = 0;
    if (*func(4) > 1 ){
          ret = 10;
     }

    return ret;
}