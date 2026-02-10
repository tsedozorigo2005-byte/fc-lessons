#include <stdio.h>
//for (int i = 1; i <=10; i++){
// //     printf("%d\n", i);

 // int max = arr[0];
    // for ( int i = 0; i < n; i++){
    //     if (max < arr[i]){ //2 > 
    //         max = arr[i];
    //     }
    // }
    // printf("%d\n", max);
    // return 0;

//     def linear_search(arr, target):
//     for i in range(len(arr)):
//         if arr[i] == target:
//             return i
//     return -1
 
// nums = [4, 2, 7, 1, 9, 3]
// print(linear_search(nums, 7))  # 2
// print(linear_search(nums, 5))  # -1


int linerSearch(int arr[], int arrSize, int target) {
    for(int i = 0; i < arrSize; i++) {
        if (arr[i] == target) {
            return 1;
        }
    }
    return 0;
}

int maximum(int arr[], int arrSize) {
    int max = arr[0];
    for(int i = 1; i < arrSize; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

int secondMax(int arr[], int arrSize, int maxEl) {
    int second = arr[0];
    for(int i = 1; i < arrSize; i++) {
        if (maxEl > arr[i] && arr[i] >= second) {
            second = arr[i];
        }
    }
    return second;
}

void reverse(int arr[], int arrSize){
    for(int i = 0; i < arrSize/ 2; i++){
        int temp = arr[i];
        arr[i] = arr[arrSize- 1 - i];
        arr[arrSize - 1 - i] = temp;
    }
}

int main(){
    int n = 5;
    int arr[n];
    
    printf("array iin elemnt iig oruul:\n");
    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    int ih = maximum(arr, n);
    printf( "maximum: %d\n", ih);

    int second = secondMax(arr, n, ih);
    printf("second max: %d \n", second);

    // reverse(arr, n);
    // printf("[");
    // for(int i = 0; i < n; i++){
    //     printf("%d, ",arr[i]);

    // }
    // printf("]");
}


// int max(int arr[], int arrSize) {

// }

// int main() {
//     int n = 5;
//     int arr[n];
    
//     printf("array iin elemnt iig oruul:\n");
//     for (int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }

//     int findEl = 5;

//     int isFound = linerSearch(arr, n, findEl);

//     if (isFound == 1) {
//         printf("oldson \n");
//     } else {
//         printf("oldoogvi \n");
//     }


// }


    

