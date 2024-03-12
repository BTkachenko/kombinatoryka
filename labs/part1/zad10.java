import java.math.BigDecimal;

public class zad10 {
    public static Object[] countSequences(int n, double p) {
        BigDecimal[][] dpAaa = new BigDecimal[n + 1][4];
        BigDecimal[][] dpAbb = new BigDecimal[n + 1][4];
        BigDecimal[] occurrencesAaa = new BigDecimal[n + 1];
        double q = 1 - p;

        // Initialize BigDecimal arrays
        for (int i = 0; i <= n; i++) {
            occurrencesAaa[i] = BigDecimal.ZERO;
            for (int j = 0; j < 4; j++) {
                dpAaa[i][j] = BigDecimal.ZERO;
                dpAbb[i][j] = BigDecimal.ZERO;
            }
        }

        // Base cases
        dpAaa[0][0] = BigDecimal.ONE;
        dpAbb[0][0] = BigDecimal.ONE;

        // Main DP loop
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 4; j++) {
                int nextStateA = Math.min(j + 1, 3);
                dpAaa[i][nextStateA] = dpAaa[i][nextStateA].add(dpAaa[i - 1][j].multiply(BigDecimal.valueOf(p)));

                int nextStateB = (j != 3) ? 0 : 3;
                dpAaa[i][nextStateB] = dpAaa[i][nextStateB].add(dpAaa[i - 1][j].multiply(BigDecimal.valueOf(q)));

                occurrencesAaa[i] = occurrencesAaa[i].add((j == 3) ? dpAaa[i - 1][j] : BigDecimal.ZERO);

                // For 'abb'
                nextStateA = (j != 3) ? 1 : 3;
                dpAbb[i][nextStateA] = dpAbb[i][nextStateA].add(dpAbb[i - 1][j].multiply(BigDecimal.valueOf(p)));

                nextStateB = (j != 0) ? Math.min(j + 1, 3) : 0;
                dpAbb[i][nextStateB] = dpAbb[i][nextStateB].add(dpAbb[i - 1][j].multiply(BigDecimal.valueOf(q)));
            }
        }

        // Calculate results
        BigDecimal totalSequences = BigDecimal.valueOf(Math.pow(2, n));
        BigDecimal sequencesWithAaa = totalSequences.subtract(dpAaa[n][0].add(dpAaa[n][1]).add(dpAaa[n][2]));
        BigDecimal sequencesWithAbb = totalSequences.subtract(dpAbb[n][0].add(dpAbb[n][1]).add(dpAbb[n][2]));
        double averageOccurrencesAaa = 0;
        for (BigDecimal occurrences : occurrencesAaa) {
            averageOccurrencesAaa += occurrences.doubleValue();
        }
        averageOccurrencesAaa /= totalSequences.doubleValue();

        return new Object[]{sequencesWithAaa, sequencesWithAbb, averageOccurrencesAaa};
    }

    public static void main(String[] args) {
        int n = 4;
        double p = 0.5;  // Probability of 'a'
        Object[] results = countSequences(n, p);
        System.out.println("Sequences with aaa: " + results[0]);
        System.out.println("Sequences with abb: " + results[1]);
        System.out.println("Average occurrences of aaa: " + results[2]);
    }
}

