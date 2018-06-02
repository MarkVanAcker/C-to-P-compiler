float func ();

float func(){

    return 10.0;

}


int main (){

    float var = 0.0;

    while (var < func()){

            var = var + 1.0;
    }


    return 1;

}