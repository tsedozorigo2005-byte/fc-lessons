#include <stdio.h>

int main() {  
    int n = 0;
    scanf("%d", &n);
    
    if (n <= 0) {
        return 0;
    }

    int F[n];

    // эхний 2 гишүүн
    F[0] = 0;
    if (n > 1) {
        F[1] = 1;
    }

    // дараагийн гишүүдийг тооцоолох: F(i) = F(i-1) + F(i-2)
    for (int i = 2; i < n; i++) {
        F[i] = F[i-1] + F[i-2];    }

    // массивыг хэвлэх
    for (int i = 0; i < n; i++) {
        printf("%d ", F[i]);
    }
    printf("\n");

    return 0;
}

// int F(int n) {
//     if (n == 0) {
//         return 0;
//     }
//     if (n == 1) {
//         return 1;
//     }
//     return F(n-1) + F(n-2);
// }

// int main() {
//     int n = 5;
//     printf("F(%d) = %d\n", n, F(n));
//     return 0;
// }

    