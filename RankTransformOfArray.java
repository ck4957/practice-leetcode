import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/* 1331. Rank Transform of an Array */
public class RankTransformOfArray {
    public static void main(String[] args) {
        int[] arr = new int[]{40, 20, 30, 10};
        int[] result = rankTransform(arr);
        System.out.println(
            Arrays.toString(result)
        );
    }

    public static int[] rankTransform(int[] arr) {

        // Sorted and unique elements
        TreeSet<Integer> ts = new TreeSet<>();
        for (int a: arr) {
            ts.add(a);
        }

        Map<Integer, Integer> map= new HashMap<>();
        int rank = 1;
        for (int num: ts) {
            map.put(num, rank++);
        }

        int[] ranks = new int[arr.length];
        for (int i=0; i < arr.length; i++) {
            ranks[i] = map.get(arr[i]);
        }
        return ranks;

    }
}