from math import *

def dist(latA, latB, longA, longB):
    return (6371.01*acos(sin(latA)*sin(latB)+cos(latA)*cos(latB)*cos(longA-longB)))
    
def main():
    latA = radians(float(input('Digite a latitude A: ')))
    longA = radians(float(input('Digite a longitude A: ')))
    latB = radians(float(input('Digite a latitude B: ')))
    longB = radians(float(input('Digite a longitude B: ')))
    
    print('A distância é %.2fkm.' % dist(latA, latB, longA, longB))
    
main()
#Escreva uma função que recebe a latitude e a 
# longitude de dois pontos (latitude e longitude 
# do ponto A, latitude e longitude do ponto B) como 
# valores float.  Essa função deve calcular e imprimir 
# a distância em km entre os dois pontos. Utilize os métodos 
# radians, sin, cos e acos do módulo math para auxiliar nos cálculos. 
# A distância é calculada conforma equação: 

#dist=6371.01∗acos(sin(latitude1)∗sin(latitude2)+cos(latitude1)∗cos(latitude2)∗cos(longitude1−longitude2))

#Faça o programa principal que recebe os valores das duas latitudes e das duas longitudes e chama a função.