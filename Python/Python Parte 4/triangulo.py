from math import sqrt

a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))

def formula(a, b):
    x = sqrt(a**2 + b**2)
    return x
print ('Hipotenusa: {0:.2f}'.format(formula(a, b)))

#Escreva uma função que tenha os comprimentos
#  dos dois lados mais curtos de um triângulo 
# retângulo como seus parâmetros. 
# Retorne a hipotenusa do triângulo, calculada usando o teorema de Pitágoras,
#  como o resultado da função. Inclua um programa principal 
# que lê os comprimentos dos lados mais curtos de um triângulo
#  retângulo do usuário e use sua função para calcular o
#  comprimento da hipotenusa. Exiba o resultado.