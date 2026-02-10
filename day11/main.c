// // Бодлого 1: Тэгш өнцөгтийн талбай ба периметр
// // Тэгш өнцөгтийн урт, өргөнийг асууж:
  
// // Талбай = урт × өргөн
// // Периметр = 2 × (урт + өргөн)
// // ⁨⁨
// // Урт: 10
// // Өргөн: 5
// // Талбай: 50
// // Периметр: 30
// // ⁩⁩ 
// // Бодлого 2: Хоёр тооны арифметик үйлдлүүд
// // Хоёр бүхэл тоо авч, +, -, *, / үйлдлүүдийн үр дүнг хэвлэ. 
// // ⁨
// // a = 17
// // b = 5
// // 17 + 5 = 22
// // 17 - 5 = 12
// // 17 * 5 = 85
// // 17 / 5 = 3.40
// // ⁩⁩⁩
// // Бодлого 3: Цельсийг Фаренгейт руу хөрвүүлэх
// // Томьёо: ⁨F = (C × 9/5) + 32⁩
// // ⁨
// // Цельс: 25
// // Фаренгейт: 77.00
// // ⁩
// // Дунд түвшин (5-7)
// // Бодлого 5: Тэгш/Сондгой тоо шалгах
// // Хэрэглэгчээс тоо авч, тэгш үү, сондгой юу гэдгийг шалга.
// // ⁨
// // Тоо: 7
// // 7 бол сондгой тоо
// // ⁩
// // Бодлого 6: Дүнгийн үнэлгээ (Grade)
// // Оюутны дүнг (0-100) авч, үнэлгээ гарга:
// // 90-100: A
// // 80-89: B
// // 70-79: C
// // 60-69: D
// // 0-59: F
// // ⁨
// // Дүн: 85
// // Үнэлгээ: B
// // ⁩
// // Бодлого 7: Гурван тооны хамгийн их
// // Гурван тоо авч, хамгийн их тоог ол.
// // ⁨
// // a = 15
// // b = 42
// // c = 8
// // Хамгийн их: 42
// // ⁩



// //1 int main() {
// //     int urt = 15;
// //     int urgun = 5;
// //     int p = 2 * (urt + urgun);
// //     int s = urt * urgun; 
// //     printf("Perimetr: %d\n", p);
// //     printf("Talbai:  %d\n", s);
// //     return 0;}

// // 2 int main(){
// //     int a = 17;
// //     int b = 21;
// //     int niilber = a + b;
// //     int ylgavar = a - b;
// //     int urjver = a * b;
// //     int noogdvor = a / b;
// //     printf("%d %d %d %d\n", niilber, ylgavar, urjver, noogdvor);
// //     return 0;
// // }

// //3 int main() {
// //     int celcius = 25;
// //     float farengait = (celcius * 9/5) + 32;
// //     printf("%1.f\n", farengait);
// //     return 0;
// // }

// //5 int main(){
// //     int too;

// //     printf("Toogoo oruulna uu;");
// //     scanf("%d", &too);

// //     if (too % 2 == 0){
// //         printf("%d bol tegsh too\n", too);
// //     }else{
// //         printf("%d bol songdoi too\n", too);
    
// //     return 0;
// //     }


// // }

// // int main(){
// // 6    int grade;
// //     printf("Dungee oruulna uu");
// //     scanf("%d", &grade);

// //     if (90 < &grade == 100){
// //         printf("grade: A\n");
// //     } else if (80< &grade <= 90){
// //         printf("grade: B\n");
// //     } else if (70 < &grade <= 80){
// //         printf("grade : C\n");
// //     } else if (60 < &grade <= 70){
// //         printf("grade: D\n");
// //     } else {
// //         printf("grade: F\n");
// //     }
// // return 0;
// // }

// // int main(){
// //     int a = 9;
// //     int b = 81;
// //     int c = 61;
// //     int max;
// //     if (a < b){
// //         max = b;
// //     }else if (b < c){
// //         max = c;
// //     }else if (c < a){
// //         max = a;
// //     }
// //     printf("%d\n: is max", max);
// //     return 0;
// // }


// // Python : for i in range(1, 11)
// // C:
// // for (int i = 1; i <=10; i++){
// //     printf("%d\n", i);
// // }

// // int main(){
// //     int day;
// //     printf("too oruulna uu: ");
// //     scanf("%d", &day);
// //     switch (day)
// //     {
// //     case 1: printf("davaa"); break;
// //     case 2:
// //         printf("mygmar");
// //         break;
// //     case 3:
// //         printf("lhagva");
// //         break;
// //     case 4:
// //         printf("4dh");
// //         break;
// //     case 5:
// //         printf("5");
// //         break;
// //     case 6:
// //         printf("6");
// //         break;
// //     case 7:
// //         printf("7");
// //         break;
    
// //     default:
// //     printf("buruu");
// //         break;
// //     }
// //     return 0;
// // }

// // int main(){
// //     int niilber = 0;
// //     for(int i = 1; i <= 10; i++){
// //         // printf("%d\n", i);
// //         niilber +=  i;
// //     }
// //     printf("%d \n", niilber);
// //     return 0;
// // }

// // int main(){
// //     int niilber = 0;
// //     int i = 1;
// //     while(i <= 10){
// //         niilber += i;
// //         i++;
// //     }
// //     printf("%d\n", niilber);
// //     return 0;
// // }
// #include <stdio.h>
// #include <stdbool.h>

// int niilber(int a, int b){
//     return(a+b);
// }
// //a[1,2,3,4] b = 7
// //a =1 b =2 target = 3 true butsaana
// bool targetExists(int a, int b, int target){
//     if (a+b== target){
//         return true;
//     }
     
//   return false;
// }

// // int main(){
// //     int a,b,target;
// //     // int arr[n];
// //     printf("Ta niilber utga oruulna uu: ");
// //     scanf("%d", &target);
// //     printf("Ta a, b toog oruulna uu: ");
// //     scanf("%d %d",&b, &a);
// //     // scanf("%d", &b);
// //     if (targetExists(a, b, target)){
// //         printf("unen bna bna");
// //     } else {
// //         printf("false");
// //     }
// // }


// bool chechTwoSum(int arr[], int len, int target) {
//     for (int i = 0; i < len; i++) {//
//         for (int j = 0; j < len; j++) {//
//             if (j == i){
//                 continue;
//             }
//             if (arr[i] + arr[j] == target) {//
//                 return true;//
//             }
//         }
//     }
//     return false;
// }

// bool twoPointer(int arr[], int len, int target) {
//     int left = 0;
//     int right = len - 1;

//     while (left < right) {
//         int sum = arr[left] + arr[right];

//         if (sum == target) {
//             return true;
//         }

//         if (sum < target) {
//             left++;
//         } else {
//             right--; 
//         }
//     }

//     return false;
// }

// int main() {
//     int arr[] = {1,4,5,6,8};
//     int target = 9;
//     int arrSize = sizeof(arr) / sizeof(arr[0]);

//     bool isFind = twoPointer(arr, arrSize, target);
//     printf("IS FIND: %d", isFind);

//     return 0;
// }

// int niilber(int a, int b){
//     return(a+b);
// }
// //a[1,2,3,4] b = 7
// //a =1 b =2 target = 3 true butsaana
// bool targetExists(int a, int b, int target){
//     if (a+b== target){
//         return true;
//     }
     
//   return false;

#include <stdio.h>


int main(){
    int N, sum = 0;

    printf("N toog oruulna uu: ");
    scanf("%d", &N);

    for(int i = 1; i <= N; i++) {
        sum += i;
    }

    printf("%d\n", sum);

    return 0;
}