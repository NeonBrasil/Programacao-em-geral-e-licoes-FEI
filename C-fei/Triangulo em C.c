#include <stdio.h>
#include<stdlib.h>

//O cod vai verificar se é possivel criar um triangulo com essas medidas
int main() {


    int num1, num2, num3;
    printf("Insira o primeiro valor: \n");
    scanf("%d", &num1);
    printf("Insira o segundo valor: \n");
    scanf("%d", &num2);
    printf("Insira o terceiro valor: \n");
    scanf("%d", &num3);

        if (num1 + num2 > num3 && num1 + num3 > num2 && num2+num3 > num1){


                    printf("É possível");}


        else
            printf("Não é possível");



}
