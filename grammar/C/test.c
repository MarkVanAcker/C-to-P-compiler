int faculty(int f){

if(f==2)
    return 2;


return f*faculty(f-1);
}


int main(){

int x = faculty(10);


}