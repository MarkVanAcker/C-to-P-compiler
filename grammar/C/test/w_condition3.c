int func(){

    float c = 10.0;
    float d = 9.0;

    if(3 < 4){

        return 1;
    }else{
         d = d + 0.3;
        if (c > d){
            return 1;
        }else
        {
            return 10;
        }
        return 3;
    }


    return  1;

}


int main(){

    int b = func();
    return 1;
}