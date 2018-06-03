float return5(){

    return 5.01;
}


int main(){

    int ret = 0;

    float val = 10.5;
    float *ptr = &val ;
    if (val == (1.99)*3.0 ){
          ret = 12;
     }

     if (*ptr  == val  ){
          return 1;
     }

     if (*ptr > return5() ){
          ret = 10;
     }


    return ret;
}