#include <stdio.h>

// int main(){
//     int N, sum = 0;

//     printf("N toog oruulna uu: ");
//     scanf("%d", &N);

//     for(int i = 1; i <= N; i++) {
//         sum += i;
//     }

//     printf("%d\n", sum);

//     return 0;
// }

// int main() {
    

// //     return 0;
// // 
// int main() {
//     int arr[] = {10, 20, 30, 40, 50};
//     int size = 5;
//     int sum = 0;
//     for(int i = 0; i <= size-1; i++) {
//         sum += arr[i];
//     }
//     printf("%d\n", sum);
//     return 0;
// }


// int main(){
//     int n;
//     printf("heden too");
//     scanf("%d", &n);

//     int arr[n];
//     for (int i = 0; i < n; i++) {
//         printf("arrayiin %d dahi element oruul: ", i + 1);
//         scanf("%d", &arr[i]);
//         printf("\n");
//     }

//     int a = 1;
//     for (int i = 1; i <= n; i++){
//         a *= i;
//     }
//     printf("%d\n", a);
//     return 0;
// }


    // int max = arr[0];
    // for ( int i = 0; i < n; i++){
    //     if (max < arr[i]){ //2 > 
    //         max = arr[i];
    //     }
    // }
    // printf("%d\n", max);
    // return 0;
//}

// int main(){
//     int arr[] = {1, 2, 3, 4, 5};
//     int n = 5;
//     for (int i = 0; i < n/2; i++){
//     int temp = arr[i];
//     arr[i] = arr[n-1-i];
//     arr [n-1-i] = temp;
// }
// }


// int main(){
//     int arr[]= {1, 2, 3, 4, 5};
//     int n = 5;
//     for (int i = n; i > 0; i--){
//         printf("%d\n", arr[i-1]);
//     }
//     return 0;

// }

// def bubble_sort(arr):
//     n = len(arr)
//     for i in range(n):
//         for j in range(0, n - i - 1):
//             if arr[j] > arr[j + 1]:
//                 arr[j], arr[j+1] = arr[j+1], arr[j]
//     return arr
 

int main() {
    int arr[] = {5, 1, 4, 2, 8};
    int n = 5;
    int i, j;

    for(i = 0; i < n-1; i++) {
        for(j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                int temp;
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

    return 0;
}
