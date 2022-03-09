import os #Serve para fazer ações do sistema operacional como apagar um arquivo.
from datetime import datetime #Serve para colocar o dia, mes, ano e hora exato no arquivo.
def main():
    while True:#Serve para dar looping, ou seja, quando terminar de fazer uma dessas operações, o programa
        #não fecha, a menos que o usuário selecione "0 - Sair".
        print()#Pula uma linha para facilitar a visualização e embelezamento do código.
        print("""-----Menu-----""") #Menu de opções do programa.
        print("1 - Criar nova conta")#Opção de criação de uma nova conta.
        print("2 - Apagar uma conta")#Opção de apagar uma conta existente.
        print("3 - Debita")#Opção de sacar dinheiro de uma conta existente.
        print("4 - Deposito")#Opção de depositar dinheiro em uma conta existente.
        print("5 - Saldo")#Opção de ver o saldo de uma conta existente.
        print("6 - Extrato")#Opção de ver o extrato de uma conta existente.
        print("0 - Sair")#Opção de sair do programa.
        opcao = input("Escolha uma das opções: ") #Aqui o usuário digitará sua escolha
    #Cada 'if' representa uma escolha.
        if opcao =="1":
             criarNovo() #Selecionando '1' o usuário será direcionado para a função 'criarNovo' que tem o objetivo de criar uma nova conta.
        elif opcao =="2":
            apagarConta() #Selecionando '2' o usuário será direcionado para a função 'apagarConta' que tem o objetivo de apagar uma conta.
        elif opcao =="3":
            debitaEpic() #Selecionando '3' o usuário será direcionado para a função 'debitaEpic' que tem o objetivo de debitar de uma conta.    
        elif opcao =="4":
            depositoEpico() #Selecionando '4' o usuário será direcionado para a função 'depositoEpico' que tem o objetivo de depositar em uma conta.
        elif opcao =="5":
            saldo() #Selecionando '5' o usuário será direcionado para a função 'saldo' que tem o objetivo de ver o saldo de uma conta.
        elif opcao =="6":
            extrato() #Selecionando '6' o usuário será direcionado para a função 'extrato' que tem o objetivo de ver o histórico de uma conta.
        elif opcao =="0":
            break #Selecionando '0' o usuário será direcionado para a função 'break' que tem o objetivo de finalizar o programa.
        else:
            print("Opção inválida! Selecione uma opção válida!!") #Selecionando qualquer outra tecla além das anteriores, o programa exibira uma mensagem dizendo para selecionar uma opção válida.
            


def criarNovo():#funcão de criar nova conta.
    data = datetime.now()#variável da hora.
    hora = data.strftime("%d\%m\%Y %H:%M")
    
    nome = input("Digite o nome: ") #variável que recebe o nome.
    cpf = input("Digite o CPF: ")#variável que recebe o CPF.
    if os.path.isfile(cpf+".txt"):#condição que vai verificar se já existe um arquivo com o mesmo CPF.
        print("CPF já registrado!")#imprimir a mensagem que o CPF já está registrado caso o programa encontre um arquivo com um mesmo CPF.
    else:#condição caso não exista uma outra conta com o mesmo CPF.
        print("-----Tipo de Conta-----") #print mensagem que mostrará ao usuário as três tipos de contas disponíveis para escolha.
        print("1 - Conta salario")#Conta que cobra taxa de 5% a cada débito realizado e não permite débitos que deixem a conta com saldo negativo.
        print("2 - Conta comum")#Conta que cobra taxa de 3% a cada débito realizado e permite débitos que deixem a conta com saldo negativo de até 500 reais.
        print("3 - Conta plus")#Conta que cobra taxa de 1% a cada débito realizado e permite débitos que deixem a conta com saldo negativo de até 5000 reais.
        conta = input("Digite o tipo de conta: ")#variável para digitar o tipo de conta.
        if conta == "1":#condição caso o usuário digite o número '1'
            conta = "salario"
        elif conta =="2":#condição caso o usuário digite o número '2'
            conta = "comum"
        elif conta == "3":#condição caso o usuário digite o número '3'
            conta = "plus"
        else:#Caso o usuário digite qualquer valor além do esperado, uma mensagem aparecerá.
            print()
            print("Digite uma opção válida!")#Mensagem caso o usuário digite um valor não esperado.
        valor = float(input("Digite o valor inicial da sua conta: "))#Recebe float, ou seja, o valor da conta.
        senha = input("Digite sua senha: ")#Variável que recebe a senha da conta.
        arquivo = open(cpf+".txt","w")#O arquivo será criado com o nome do CPF que o usuário escolheu.
        arquivo.write("%s\n" % nome)#Pulando uma linha, será digitado o nome do usuário.
        arquivo.write("%s\n" % cpf)#Pulando outra linha será digitado o CPF do usuário.
        arquivo.write("%s\n" % conta)#Pulando outra linha será digitado o tipo de conta do usuário.
        arquivo.write("%s\n" % senha)#Pulando outra linha será digitado a senha do usuário.
        arquivo.write("Data: %s + %.2f Tarifa: 0.00 Saldo: %.2f\n" %(hora,valor,valor))#Pulando outra linha será digitado a data, hora, valor recebido uqe nesse caso será o mesmo do saldo e a tarifa que será 0.
        arquivo.close()#O arquivo será fechado e ficará salvo.

def apagarConta():#Função de apagar uma conta já existente.
    confi = []#Lista que será utilizada para encontrar elementos no arquivo como a senha.
    cpf = input("Digite o CPF: ")#variável do CPF.
    senha2 = input("Digite sua senha: ")#Variável que recebe a senha da conta.
    if os.path.isfile(cpf+".txt"):#condição que vai verificar se existe um arquivo com o CPF digitado.
        arquivo = open (cpf+".txt","r")#Caso um arquivo com o CPF selecionado existir, o arquivo será aberto no modo leitura.      
        for i in arquivo.readlines(): 
            confi.append(i.split())       
        arquivo.close()
        if confi[3][0]==senha2:#O programa vai ler todas as linhas do arquivo em busca da coluna "3", ou seja, onde a senha está.
            os.remove(cpf + ".txt")#O programa vai apagar o arquivo.
            print("Conta deletada!")#Essa mensagem será mostrada para o usuário.
        else:#Caso não exista um arquivo com a senha selecionada, essa mensagem será mostrada para o usuário.
            print("Senha incorreta!")
    else:#Caso não exista um arquivo com o CPF selecionado, essa mensagem será mostrada para o usuário.
        print("CPF errada!")

def debitaEpic():#Função de debitar de uma conta já existente.
    data = datetime.now()#variável da hora.
    hora = data.strftime("%d\%m\%Y %H:%M")
    confi = []#Lista que será utilizada para encontrar elementos no arquivo como a senha.
    cpf = input("Digite o CPF: ")#variável do CPF.
    senha2 = input("Digite sua senha: ")#Variável que recebe a senha da conta.
    
    if os.path.isfile(cpf+".txt"): #condição que vai verificar se existe um arquivo com o CPF digitado.


        arquivo = open (cpf+".txt","r")#Caso um arquivo com o CPF selecionado existir, o arquivo será aberto no modo leitura.
        for i in arquivo.readlines(): 
            confi.append(i.split())
        
        arquivo.close()

        arquivo = open (cpf+".txt","a") #O arquivo com o CPF correto será aberto em modo 'adição'.
        if confi[3][0]==senha2:#O programa vai ler todas as linhas do arquivo em busca da coluna "3", ou seja, onde a senha está.
            posiSaldo = float(confi[-1][8])#O programa vai procurar a posição onde está o saldo atual para poder modificar (nesse caso, diminuir)
            saque = float(input("Digite o valor do saque: "))#Variável para escrever quanto dinheiro o usuário decidi debitar.
            if confi[2][0] == "salario":#Condição em relação ao tipo de conta, nesse caso, conta Salário.
                tarifa = 0.05*saque#Além do dinheiro debitado, será adcionado uma tarifa de 5%.
                sobras = ((posiSaldo - tarifa) - saque)#Variável sobras, que será o valor que sobrou na conta, que condiz o antigo valor - tarifa - o quando o usuário quer sacar.
                if sobras >= 0:#Caso o valor que sobrar de reais na conta for de 0 ou mais reais, o arquivo será aberto e efetuará o codigo.
                    arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(hora,saque,tarifa,sobras))
                else:#Caso o valor da conta ficar negativo, essa mensagem será exibida.
                    print("Não foi possível continuar a operação, pois a mesma deixaria a conta negativa!")
            elif confi[2][0] == "comum":#Condição em relação ao tipo de conta, nesse caso, conta Comum.
                tarifa = 0.03*saque#Além do dinheiro debitado, será adcionado uma tarifa de 3%.
                sobras = ((posiSaldo - tarifa) - saque)#Variável sobras, que será o valor que sobrou na conta, que condiz o antigo valor - tarifa - o quando o usuário quer sacar.
                if sobras>=-500:#Caso o valor que sobrar de reais na conta for de 500 negativo ou mais reais, o arquivo será aberto e efetuará o codigo.
                     arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(hora,saque,tarifa,sobras))
                else:#Caso o valor da conta ficar inferior de -500, essa mensagem será exibida.
                     print("Não é possivel deixar uma conta comum com saldo inderior a 500!")
            elif confi[2][0] == "plus":#Condição em relação ao tipo de conta, nesse caso, conta Plus.
                tarifa = 0.01*saque#Além do dinheiro debitado, será adcionado uma tarifa de 1%.
                sobras = ((posiSaldo - tarifa) - saque)#Variável sobras, que será o valor que sobrou na conta, que condiz o antigo valor - tarifa - o quando o usuário quer sacar.
                if sobras>=-5000:#Caso o valor que sobrar de reais na conta for de 5000 negativo ou mais reais, o arquivo será aberto e efetuará o codigo.
                    arquivo.write("Data: %s - %.2f Tarifa: %.2f Saldo: %.2f\n" %(hora,saque,tarifa,sobras))
                else:#Caso o valor da conta ficar inferior de -5000, essa mensagem será exibida.
                    print("Não é possivel deixar uma conta plus com saldo inderior a 5000!")
        else:#Caso não exista um arquivo com a senha selecionada, essa mensagem será mostrada para o usuário.
            print("Senha errada!")   
    else: #Caso não exista um arquivo com o CPF selecionado, essa mensagem será mostrada para o usuário.
        print("CPF errado!")
          

            


def depositoEpico():#Função de depositar para uma conta já existente.
    data = datetime.now()#variável da hora.
    hora = data.strftime("%d\%m\%Y %H:%M")
    confi = []#Lista que será utilizada para encontrar elementos no arquivo como a senha.
    cpf = input("Digite o CPF: ")#variável do CPF.
    senha2 = input("Digite sua senha: ")#Variável que recebe a senha da conta.
    
    if os.path.isfile(cpf+".txt"):#condição que vai verificar se existe um arquivo com o CPF digitado.


        arquivo = open (cpf+".txt","r")#Caso um arquivo com o CPF selecionado existir, o arquivo será aberto no modo leitura.
        for i in arquivo.readlines(): 
            confi.append(i.split())
        
        arquivo.close()

        arquivo = open (cpf+".txt","a")#O arquivo com o CPF correto será aberto em modo 'adição'.
        if confi[3][0]==senha2:#O programa vai ler todas as linhas do arquivo em busca da coluna "3", ou seja, onde a senha está.
            posiSaldo = float(confi[-1][8])#O programa vai procurar a posição onde está o saldo atual para poder modificar (nesse caso, diminuir)
            deposito = float(input("Digite o valor do depósito: "))#Variável para escrever quanto dinheiro o usuário decidi depositar.
            if confi[2][0] == "salario":#Condição em relação ao tipo de conta, nesse caso, conta Salário.
                sobras = ((posiSaldo) + deposito)#O dinheiro que sobrará na conta será o valor atual comando com o deposito.
                
                arquivo.write("Data: %s - %.2f Tarifa: R$ 0.00 Saldo: %.2f\n" %(hora,deposito,sobras))#O programa vai escrever escrever a data, hora, deposito e dinheiro que sobrou.
                
            elif confi[2][0] == "comum":#Condição em relação ao tipo de conta, nesse caso, conta Comum.
                
                sobras = ((posiSaldo) + deposito)#O dinheiro que sobrará na conta será o valor atual comando com o deposito.
                
                arquivo.write("Data: %s - %.2f Tarifa: 0.00 Saldo: %.2f\n" %(hora,deposito,sobras))#O programa vai escrever escrever a data, hora, deposito e dinheiro que sobrou.
            elif confi[2][0] == "plus":#Condição em relação ao tipo de conta, nesse caso, conta Plus.
               
                sobras = ((posiSaldo) + deposito)#O dinheiro que sobrará na conta será o valor atual comando com o deposito.
                
                arquivo.write("Data: %s - %.2f Tarifa: 0.00 Saldo: %.2f\n" %(hora,deposito,sobras))#O programa vai escrever escrever a data, hora, deposito e dinheiro que sobrou.
        else:#Caso não exista um arquivo com a senha selecionada, essa mensagem será mostrada para o usuário.
            print("Senha errada!")   
    else: #Caso não exista um arquivo com o CPF selecionado, essa mensagem será mostrada para o usuário.
        print("CPF errado!")




def saldo():#Função de verificar o saldo de uma conta já existente.
    confi = []#Lista que será utilizada para encontrar elementos no arquivo como a senha.
    
    cpf = input("Digite o CPF: ")#variável do CPF.
    senha2 = input("Digite sua senha: ")#Variável que recebe a senha da conta.
    if os.path.isfile(cpf+".txt"):#condição que vai verificar se existe um arquivo com o CPF digitado.


        arquivo = open (cpf+".txt","r")#Caso um arquivo com o CPF selecionado existir, o arquivo será aberto no modo leitura.
        for i in arquivo.readlines(): 
            confi.append(i.split())
        
        arquivo.close()

       
        if confi[3][0]==senha2:#O programa vai ler todas as linhas do arquivo em busca da coluna "3", ou seja, onde a senha está.
            print(confi[-1][8])#Programa vai printar o saldo atual.
        else:#Caso a senha selecionada não condizer com a do arquivo, essa mensagem será mostrada para o usuário.
            print("Senha errada!")    

    else:#Caso não exista um arquivo com o CPF selecionado, essa mensagem será mostrada para o usuário.
        print("CPF errado!")        

def extrato():#Função de mostrar o extrato uma conta já existente.
    confi = []#Lista que será utilizada para encontrar elementos no arquivo como a senha.
    
    cpf = input("Digite o CPF: ")#variável do CPF.
    senha2 = input("Digite sua senha: ")#Variável que recebe a senha da conta.
    if os.path.isfile(cpf+".txt"):#condição que vai verificar se existe um arquivo com o CPF digitado.


        arquivo = open (cpf+".txt","r")#Caso um arquivo com o CPF selecionado existir, o arquivo será aberto no modo leitura.
        for i in arquivo.readlines(): 
            confi.append(i.split())
        
        arquivo.close()

       
        if confi[3][0]==senha2:#O programa vai ler todas as linhas do arquivo em busca da coluna "3", ou seja, onde a senha está.
            confi.pop(3)#o programa vai printar todo o arquivo com excessão da senha.
            for linha in range(len(confi)):
                for coluna in range(len(confi[linha])):
                    print(confi[linha][coluna], end=" ")
                    print()
        else:#Caso não exista um arquivo com a senha selecionada, essa mensagem será mostrada para o usuário.
            print("Senha errada!")    

    else:#Caso não exista um arquivo com o CPF selecionado, essa mensagem será mostrada para o usuário.
        print("CPF errado!")        


main()