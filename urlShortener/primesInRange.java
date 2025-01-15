import java.util.Scanner;
public class primesInRange{
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        for(int i=1; i<=num; i++) {
            if(isPrime(i)) {
                System.out.println(i);
            }
        }
    }
    public static boolean isPrime(int num) {
        if(num == 2) {
            return true;
        }
        for(int i=2; i<=num; i++) {
            if(num % i == 0) return false;
        }
        return true;
    }
}