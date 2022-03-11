import java.util.Scanner;

public class ComparadorDeNumeros {
    

    public static void main(String [] args){

        //programa que vai
        //comparar dois numeros
        //colocados pelo usuário

// o "scanner" é o nome
        Scanner scanner = new Scanner(System.in);
        
        int numero1, numero2;
        // tbm poderia ser int num1
        //int num2 mas ja q significa a mesma coisa
        //pode meter assim

        System.out.print("Entre o primeiro numero: ");
        numero1 = scanner.nextInt(); 


        System.out.print("Entre o segundo número: ");
        numero2 = scanner.nextInt();
        // lembrar sempre de fechar o scanner
        scanner.close();
        // agora é a parte de comparar os numeros

        if (numero1 > numero2){

            System.out.print("O primeiro número é maior");

        }
        else if (numero2 > numero1){

            System.out.print("O segundo número é maior");


        }
        else{
            System.out.print("É o mesmo número");
        }





    }



}
