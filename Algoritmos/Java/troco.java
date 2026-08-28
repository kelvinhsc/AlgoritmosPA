import java.util.Scanner;

public class troco {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor da compra: ");
        double compra = scanner.nextDouble();

        System.out.print("Digite o valor pago: ");
        double pago = scanner.nextDouble();

        double troco = pago - compra;
        System.out.println("O troco é: R$" + troco);

        scanner.close();
    }
}