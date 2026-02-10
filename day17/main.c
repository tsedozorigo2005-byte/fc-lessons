#include <stdio.h>
int main(){
    int n = 345678;
    int z = 0;
    int m = 0;
    while(n>0){
        z = n % 10;
        m = m * 10 +z;
        n =n /10;
        
        // printf("%d\n", z);
        // printf("%d\n", n);
        // printf("%d", z);
        // n =n /10;
    }

    printf("%d", m);
}