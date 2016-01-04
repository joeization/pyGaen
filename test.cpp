#include <bits/stdc++.h>
using namespace std;
int main(){
    for(int i=0;i<100000;i++){
        printf("dialog %d\n", i+9);
        puts("STOP");
        puts("0 main main");
        puts("-1");
        puts("1");
        puts("NONE");
        puts("test");
        puts("end");
    }
}
/*
dialog 
    #sfx
    STOP
    #branch
    0 main main
    #choice
    -1
    #position
    1
    #img
    NONE
    #content
    test
end
*/