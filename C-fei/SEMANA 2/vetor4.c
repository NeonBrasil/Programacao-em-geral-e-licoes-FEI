/*
Crie um algoritmo em C que receba um vetor de 3 posições e ordene o de maneira
crescente, UTILIZANDO FOR OU OUTRA ESTRUTURA DE LAÇO.
Dicas de lógica:
1. Criem um vetor v1 e dois contadores i e j e uma variável aux.
2. Percorra v1 com contador i
3. Para CADA POSIÇÃO DE v1[i] inicialize v[j],
4. Percorra v[j]
5. Se v[i]>v[j] -> troque os valores utilizando aux





*/



#include <stdio.h>
#include <stdlib.h>
#include <math.h>


int main(){

int ordena(int v[], int lim);

int main (){
 int lim;
 printf("Qual o tamanho do vetor? \n");
 scanf ("%d", &lim);
 int v[lim];

 for(int i=0; i<lim; ++i){
   printf("Digite o valor da posição %d\n",i);
   scanf("%d", &v[i]);
 }

 ordena(v,lim);
}

int ordena(int v[], int lim){
  int i, j, aux;
  for(i=0; i<lim;i++){
    for(j=0; j<lim;j++){
      if(v[i]<v[j]){ //TROCA!!!
        aux=v[i];
        v[i]=v[j];
        v[j]=aux;
      }
    }
  }
 printf("Print do vetor ORDENADO:");
 for(int i=0; i<lim; i++){
    printf("%d, ", v[i]);
 }
 return 0;
}








}
