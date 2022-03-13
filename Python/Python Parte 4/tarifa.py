Km = float(input("Digite a quantidade de quilômetros: "))
def tarifa(Km):
    return 10.00 + (0.5 * (Km/0.125))
print("Tarifa %.2f" % tarifa(Km))

#Em uma determinada jurisdição, as tarifas de táxi 
#consistem em uma tarifa básica de R$ 10.00, mais 
#R$ 0.50 para cada 125 metros percorridos. Escreva 
#uma função que considere a distância percorrida 
#(em quilômetros inteiros) como seu único parâmetro 
#e retorne a tarifa total como seu único resultado. 
#Escreva um programa principal em que a quantidade de 
#km será digitada e onde a função será chamada.