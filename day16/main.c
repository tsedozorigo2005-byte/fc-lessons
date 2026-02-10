#include <stdio.h>
#include <math.h>
// int linerSearch(int arr[], int arrSize, int target) {
//     int counter = 0;

//     for(int i = 0; i < arrSize; i++) {
//         if (arr[i] == target) {
//             counter++;
//         }
//     }
//     return counter;

// }
// int main() {
//     int n = 5;
//     int arr[n];
    
//     printf("array iin elemnt iig oruul:\n");
//     for (int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }
//     int target = 3;
//     int hed = (linerSearch(arr, n, target ));
//     printf("too:%d", hed);
// }


// int main(){
//     int year ;
//     printf("jilee oruulna uu? \n");
//     scanf("%d", &year);

//     if(year % 4 == 0){
//         printf("davhar jil");
//     }
//     else{
//         printf("bish baina");
//     }

// }

// int main(){
//     // n = 4 -> 1234
//     // n = 3 -> 123
//     int n = 5; //100+20+3
//     int result = 0;
//     for (int i = 0; i <= n; i++){
//         result *= 10; //0 0 10 120
//         result += i;//0 1 12 123 
//     }
//     printf("%d\n",result);
// }

// reverse(arr, n);
//     printf("[");
//     for(int i = 0; i < n; i++){
//         printf("%d, ",arr[i]);

//     }
//     printf("]");

int main(){
    int n = 123456;
    int z = 0;
    int m = 0;
    while(n>0){
        z = n % 10;
        m = z * 10;
        
        
        // printf("%d\n", z);
        // printf("%d\n", n);
        // printf("%d", z);
        n =n /10;
        // n =n /10;
    }

    printf("%d", m);
}