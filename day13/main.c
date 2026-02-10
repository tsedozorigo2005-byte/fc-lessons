#include <stdio.h>
// def bubble_sort(arr):
//     n = len(arr)
//     for i in range(n):
//         for j in range(0, n - i - 1):
//             if arr[j] > arr[j + 1]:
//                 arr[j], arr[j+1] = arr[j+1], arr[j]
//     return arr
 

// int main(){
//     int arr[]= (1, 3, 4, 5, 2);
//     int n = 5;
//     int i, j;
//     for (i = 0; i < n - 1; i++){
//         for (j = 0, j < n - i - 1; j++){
        
//             if (arr[j] > arr[j+1]){
//                 arr[j], arr[j+1] = arr[j+1], arr[j]
//             }
            
//             }
//         }
        
    
//      for(i = 0; i < n; i++) {
//         printf("%d ", arr[i]);
//      }
//      return 0
// }




// int add(int a, int b){
//     return a + b;
// }

// int main(){
//     printf("%d\n", add(5, 3));
//     return 0;
// }

// void greet(char name[]){
//     printf("Sain baina uu, %s!\n", name);
// }

// int add(int a, int b);
// int main(){
//     printf("%d\n", add(5,3));
//     return 0;
// }
// int add(int a, int b){
//     return a + b;
// }

// int array_sum(int arr[], int size){
//     int sum = 0;
//     for (int i = 0; i < size; i++){
//         sum += arr[i];
//     }
//     return sum;
// }

// int main(){
//     int nums[] = {1, 2, 3, 4, 5};
//     printf("niilber: %d\n", array_sum(nums, 5));
//     return 0;
// }





// int main(){
//     int x = 42;
//     printf("utga: %d\n", x);
//     printf("hayg: %p\", &x);
//     return 0
// }




// sizeof()
// printf("char: %lu\n", sizeof(char));
// printf("int: %lu\n", sizeof(int));
// printf("Float: %lu\n", sizeof(float));

// int arr[10];
// printf("int[10]: %lu\n", sizeof(arr));

// int main(){
//     int arr[] = {1, 2 ,3 ,4, 5};
//     int size = sizeof(arr) / sizeof(arr[0]);
//     printf("Size: %d\n", size);
//     return size;
// }


// int main(){
//     int a;
//     printf("toogoo oruulna uu");
//     scanf("%d", &a);


//     printf("%p", &a);
//     return a;
// }


// int main(){
//     char ner[] = "hehe";
//     char size = sizeof(ner) / sizeof(ner[0]);
//     printf("char:%lu\n", sizeof(ner));
//     printf("char %lu\n", sizeof(ner[0]));

// int main() {
//     int arr[] = {5, 1, 4, 2, 8};
//     int n = 5;
//     int i, j;

//     for(i = 0; i < n-1; i++) {
//         for(j = 0; j < n-i-1; j++) {
//             if(arr[j] > arr[j+1]) {
//                 int temp;
//                 temp = arr[j];
//                 arr[j] = arr[j+1];
//                 arr[j+1] = temp;   
//             }
           
//         }
//     }
//     for(i = 0; i <= n-1; i++) {
//      printf("%d\n", arr[i]);
//     }
//     return 0;
// }
