import java.util.Random;
import java.util.Arrays;

public class zad9 {
    public static void main(String[] args) {
        int n = 10;
        int trials = 1000;

        float avgNoFixed = averageNoFixedPoints(n, trials);
        float avgOneFixed = averageOneFixedPoint(n, trials);
        float avgCycles = averageCycles(n, trials);

        System.out.println("Średnia liczba permutacji bez stałych punktów: " + avgNoFixed);
        System.out.println("Średnia liczba permutacji z jednym punktem stałym: " + avgOneFixed);
        System.out.println("Średnia liczba cykli: " + avgCycles);
    }

    public static int[] fisherYatesShuffle(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i + 1;
        }

        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            int j = i + rand.nextInt(n - i);
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }

        return arr;
    }

    public static int countFixedPoints(int[] arr) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == i + 1) {
                count++;
            }
        }
        return count;
    }

    public static float averageNoFixedPoints(int n, int trials) {
        int count = 0;
        for (int i = 0; i < trials; i++) {
            int[] perm = fisherYatesShuffle(n);
            if (countFixedPoints(perm) == 0) {
                count++;
            }
        }
        return (float) count / trials;
    }

    public static float averageOneFixedPoint(int n, int trials) {
        int count = 0;
        for (int i = 0; i < trials; i++) {
            int[] perm = fisherYatesShuffle(n);
            if (countFixedPoints(perm) == 1) {
                count++;
            }
        }
        return (float) count / trials;
    }

    public static float averageCycles(int n, int trials) {
        int totalCycles = 0;
        for (int i = 0; i < trials; i++) {
            int[] perm = fisherYatesShuffle(n);
            totalCycles += countCycles(perm);
        }
        return (float) totalCycles / trials;
    }

    public static int countCycles(int[] arr) {
        boolean[] visited = new boolean[arr.length];
        int cycles = 0;

        for (int i = 0; i < arr.length; i++) {
            if (visited[i]) {
                continue;
            }

            int j = i;
            while (!visited[j]) {
                visited[j] = true;
                j = arr[j] - 1;
            }
            cycles++;
        }

        return cycles;
    }
}
