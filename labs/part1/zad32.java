import java.util.function.Function;
import java.util.Arrays;

public class zad32 {
  
    public static double[] findFormalInverse(Function<Integer, Double> f, int n) {
        double[] b = new double[n];
        double a0 = f.apply(0);
        
        if (a0 == 0) {
            throw new IllegalArgumentException("f(0) must be non-zero");
        }
        
        b[0] = 1 / a0;
        
        for (int i = 1; i < n; i++) {
            double sum = 0;
            for (int j = 1; j <= i; j++) {
                sum += f.apply(j) * b[i - j];
            }
            b[i] = -sum / a0;
        }
        
        return b;
    }
  
    public static void main(String[] args) {
        int n = 10;
        
        Function<Integer, Double> f1 = (Integer n1) -> 1.0;
        Function<Integer, Double> f2 = (Integer n1) -> Math.pow(2, n1);
        Function<Integer, Double> f3 = (Integer n1) -> {
            double fact = 1;
            for (int i = 1; i <= n1; i++) {
                fact *= i;
            }
            return fact;
        };
        Function<Integer, Double> f4 = (Integer n1) -> {
            double fact = 1;
            for (int i = 1; i <= n1; i++) {
                fact *= i;
            }
            return 1 / fact;
        };
        
        System.out.println("f(n) = 1: " + Arrays.toString(findFormalInverse(f1, n)));
        System.out.println("f(n) = 2^n: " + Arrays.toString(findFormalInverse(f2, n)));
        System.out.println("f(n) = n!: " + Arrays.toString(findFormalInverse(f3, n)));
        System.out.println("f(n) = 1/n!: " + Arrays.toString(findFormalInverse(f4, n)));
    }
}
