x=int(input("escreva: "))
def test_prime(x):
    mult=0
    for count in range(2,x):
        if (x % count == 0):
            mult += 1
    if(mult==0):
        print("true")
    else:
        print("false")

#Escreva uma função, test_prime() que recebe um
#número e verifica se ele é primo ou não. A função
#retorna True ou False. 
# Não é necessário desenvolver o programa principal.