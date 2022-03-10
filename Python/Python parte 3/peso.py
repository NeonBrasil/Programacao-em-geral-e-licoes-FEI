planeta = input('Digite o o nome do planeta desejado: ')
peso = float(input('Digite o peso da pessoa na Terra em kg: '))


def pesoPessoa(planeta, peso):
    if planeta == 'Mercúrio':
        pesoPlaneta = peso * 0.37
    elif planeta == 'Vênus':
        pesoPlaneta = peso * 0.88
    elif planeta == 'Marte':
        pesoPlaneta = peso * 0.38
    elif planeta == 'Júpiter':
        pesoPlaneta = peso * 2.64
    elif planeta == 'Saturno':
        pesoPlaneta = peso * 1.15
    elif planeta == 'Urano':
        pesoPlaneta = peso * 1.17
    elif planeta == 'Netuno':
        pesoPlaneta = peso * 1.18
    return pesoPlaneta


print('Peso em {0}: {1:.2f}' .format(planeta, pesoPessoa(planeta, peso)))

#Crie uma função para calcular e retornar o peso 
# de uma pessoa nos outros planetas do Sistema Solar. 
# A função deve ter dois parâmetros: 
# o planeta desejado e o peso em Kg da pessoa na Terra.
#  O programa principal deve receber o 
# peso da pessoa na Terra (em Kg) e o planeta desejado.

#Relação de pesos: 1 Kg na Terra equivale a: 
# 0.37 Kg em Mercúrio; 0.88 Kg em Vênus; 0.38 Kg em Marte;
#  2.64 Kg em Júpiter; 1.15 Kg em Saturno;
#  1.17 Kg em Urano; e 1.18 Kg em Netuno.  