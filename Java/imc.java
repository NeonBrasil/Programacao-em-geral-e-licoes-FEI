import java.util.Scanner;

public class imc {
    public static void main (String[] args){

      
       

       System.out.println("Por favor, entre seu peso: ");
        //pegar o que o usuario escrever
        Scanner scanner = new Scanner(System.in);

        float peso = scanner.nextFloat();
        

       System.out.println("Por favor, entre sua altura: ");

       float altura = scanner.nextFloat();

            scanner.close();
       float imc = peso/(altura*altura);

        System.out.print("IMC = " +imc);

    }
}
