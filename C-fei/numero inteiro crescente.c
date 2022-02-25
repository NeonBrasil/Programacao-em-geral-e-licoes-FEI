# include <stdio.h>
#include <stdlib.h>

int main(void){

int num1 , num2;



  scanf("%d", &num1);



  scanf("%d", &num2);


    if (num2>num1)
      printf("%d %d", num1, num2);

    else if (num2<num1)
      printf("%d %d", num2, num1);

    else
      printf("Numeros iguais");
}
