public class operadores {
    public static void main (String[] args)
    {
        //expresões
        // oepradores = +'mais' - 'menos'
        // * 'multiplicação' / 'divisão'

        int x =5;
        int y = 10;
        int z = y * x / y; // z = y + x é igual a 5 + 10
        //printar a operação
        float w = (float)x / y;

        // x / y na teoria daria 0.5, porém
        // o Java vai dar como resposta, 0
        //para atingir o 0.5, é necessário usar
        //o Float e dps usar o (float)
        //para o programa reconhecer.
        //Ou seja, divisão sempre em float
        //
        //Para dar o mesmo resultado
        //poderia ter feito
        //
        //float x =5;
        //float y = 10;
        //
        //float z = x/y;
        //
        System.out.println(z);
        System.out.println(w);
        
        // '()' funcionam igual na matematica
        float g = (2+6) + (4*4) + 2;

        System.out.println(g);

        // 11 % 5 = resto da divisão de 11/5 que é 1
        // % = modulo

    }
}
