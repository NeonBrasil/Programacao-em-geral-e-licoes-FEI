#include <stdio.h>
#include <stdlib.h>

int main(){


//Elaborar um programa para exibir os múltiplos de um número compreendidos entre dois valores dados.
    int num1,num2,num3,h;
    printf("Insira o divisivel: \n");
    scanf("%d", &num1);
    printf("Insira o inicio: \n");
    scanf("%d", &num2);
    printf("Insira o final: \n");
    scanf("%d", &num3);




    for (h = num2; h<=num3; h++){
        if (h%num1==0)
            printf("%d ", h);

    }




}
