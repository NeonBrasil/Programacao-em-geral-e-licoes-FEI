//definir tamanho do vetor

#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){

    int n, i;





    printf("Digite o numero de vetores e escreva eles ate o limite");

    scanf("%d", &n);
    float vetor[n];


    for (i=0; i<n; i++){


        scanf("%f", &vetor[i]);
        printf("%f\n", vetor[i]);
    }

    printf("%f", vetor);



}
