int *** func(const int );

int *** func(const int a){

        int * ptr = &a;
        int ** ptr2 = & ptr1;
        int *** ptr3 = &ptr2;

        return ptr3;
}


int main(){

    int ret = 0;
    if (***func(4) == 1 ){
          ret = 10;
     }

    return ret;
}