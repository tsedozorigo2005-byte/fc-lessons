#include <stdio.h>


// int main() {
    
//     printf("Size of int   : %lu\n", sizeof(int));
//     printf("Size of float : %lu\n", sizeof(float));
//     printf("Size of char  : %lu\n", sizeof(char));

//     return 0;
// }


// int main(){
//     int x = 42;
//     int *ptr = &x;
//     printf("%p\n", &x);
// }

// void sum(int *a, int *b, int *total) {
//     // total = a+b
//     *total = *a + *b;
// }

// int main(){
//     int a = 5;
//     int b = 6;
//     int total = 0;

//     sum(&a, &b, &total);
//     printf("%d", total);

//     return 0;
// }



void max(int a, int b, int c, int*ih){
    if (a > b){
        *ih = a;
    }
    else if (b > c){
        *ih = b;
    }
    else if(c > a){
        *ih = c;
    
    }

}


int main(){
    int x = 5;
    int y = 3;
    int z = 2;
    int total = 0;

    max(x, y, z, &total);

    printf("%d\n", total);
    return 0;
    }