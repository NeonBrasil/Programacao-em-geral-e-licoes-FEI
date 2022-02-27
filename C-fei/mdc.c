#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    int n1, n2, resto;
    scanf("%d %d", &n1, &n2);
    if (n1 == 1){
        printf("MDC = %d", n2);
    }
    else if (n2 == 1){
        printf("MDC = %d", n1);
    }
    else
        while (n2 != 0){
            resto = n1 % n2;
            n1 = n2;
            n2 = resto;
        }printf("MDC = %d", n1);
}
