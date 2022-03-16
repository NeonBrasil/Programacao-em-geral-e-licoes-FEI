#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){

    int n, i;

    double soma = 0;



    printf("Digite o numero de vetores e escreva eles ate o limite");

    scanf("%d", &n);
    float vetor[n];


    for (i=0; i<n; i++){


        scanf("%f", &vetor[i]);


    }

    for (i=0;i<n;i++){

        soma += vetor[i];


    }
    printf("%lf", soma);

}
