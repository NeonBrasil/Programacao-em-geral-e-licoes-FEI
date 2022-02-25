#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
  int numero, inverso = 0, temp;



  scanf("%d", &numero);

  // enquanto número for diferente de zero
  while(numero != 0){
    // temp recebe o resto da divisão do número por 10
    temp = numero % 10;
    // e vamos guardando no inverso
    inverso = inverso * 10 + temp;
    // número recebe ele dividido por 10
    numero = numero / 10;
  }

  // e agora mostramos o resultado
  printf("%d", inverso);


}
