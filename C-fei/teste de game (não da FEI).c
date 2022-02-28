#include <stdio.h>
#include <stdlib.h>
#include<time.h>

int main (){



    char nome [30];
    int idade, c, d, resp;

    printf("Carregando...\n");

    for (c = 1; c <= 32767; c++)
       for (d = 1; d <= 32767; d++)
       {}
    printf("Bem vindo ao Celer2000 ©\n\n");

    printf("Voce deseja instalar os pacotes iniciais?\n");
    printf("1 - sim; 2 - nao\n");

    scanf("%d",&resp );
    if (resp == 1){
        printf("instalando pacotes de atualizaçao...\n");
        printf("Pacote 1 instalado...\n");
        printf("Pacote 2 instalado...\n");
        printf("Pacote 3 instalado...\n");
        printf("Pacote 4 instalado...\n");
        printf("Pacote 5 instalado...\n");
        for (c = 1; c <= 32767; c++)
       for (d = 1; d <= 32767; d++)
       {}
        printf("Pacote 6 instalado...\n");
        for (c = 1; c <= 32767; c++)
       for (d = 1; d <= 32767; d++)
       {}
        printf("Pacote 7 instalado...\n");
    }
    else if (resp == 2){
        printf("Ok, mantendo sistema antigo\n");
    }
    else{
        printf("valor errado, nao instalando pacotes...\n");
    }


    printf("Por favor, insira seu nome: \n");
    scanf("%s", &nome);

    printf("Ola, %s", nome);

    printf("Quantos anos você teria?; \n");

    scanf("%d", &idade);






}
