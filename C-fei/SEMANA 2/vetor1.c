#include <stdio.h>
#include <stdlib.h>
#include <math.h>


//PROGRAMA DE MÉDIA

//<tipo do vetor> nome_dele [<tamanho>]

/*
void main()
int v[10];
int i;
for(i=0;i<10;i++) vai do 0 ao 9
    v[i] = 0


*/

int main(){

    double nota [4];
    double media;
    int i;

    for(i=0; i<4; i++){
        scanf("%lf", &nota[i]);

    }

    media = (nota[0] + nota[1] + nota[2] + nota[3])/4;
    printf("%lf", media);

}
