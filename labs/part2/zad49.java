public class zad49 {
    public static void main(String[] args) {
        int maxN = 100;
        long[] pn = calculatePn(maxN);

        // Wyświetlenie pierwszych 10 wartości dla demonstracji
        for (int i = 1; i <= 100; i++) {
            System.out.println("p(" + i + ") = " + pn[i]);
        }
    }

    private static long[] calculatePn(int maxN) {
        long[] pn = new long[maxN + 1];
        int[] sigmaValues = calculateSigmaUpTo(maxN);

        pn[0] = 1; // p0 = 1 jako przypadek bazowy

        for (int n = 1; n <= maxN; n++) {
            pn[n] = 0;
            for (int j = 1; j <= n; j++) {
                pn[n] += sigmaValues[j] * pn[n - j];
            }
            pn[n] /= n;
        }

        return pn;
    }

    private static int[] calculateSigmaUpTo(int maxN) {
        int[] sigmaValues = new int[maxN + 1];
        for (int n = 1; n <= maxN; n++) {
            for (int i = n; i <= maxN; i += n) {
                sigmaValues[i] += n;
            }
        }
        return sigmaValues;
    }
}
