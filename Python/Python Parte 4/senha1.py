senha = int(input("Digite a senha de 4 digítos: "))

#Senha == 2579 significa q a senha tem q ser esse valor, se só tivesse dado um '=' não daria certo.
#se fosse de idade acima de 18 poderia colocar '>=18'
if senha == 2579:
    print("Senha correta!")
else:
    print("Senha incorreta!")