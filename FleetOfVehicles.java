// Fleet of Vehicles
/*
If the number is not a multiple of 2 then number of ways is 0. 
if it is, then the problems is to find the number of multiples of 4 in the range 
( for building 4 wheelers ) + 1 for choosing all the vehicles to be 2 wheelers. 
Because number of ways depends like moving a pointer from the range choosing one part to be 2 wheelers 
and the other part to be 4 wheelers.

Time Complexity : O(N)
Space Complexity : O(1)

*/
import java.io.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class FleetOfVehicles {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] wheels = new int[]{0,1,2,3,4,5,6,7,8};
            System.out.println(
                IntStream.of(solution.findWays(wheels)).boxed().collect(Collectors.toList())
            );
    }
}

class Solution {
    public int[] findWays(int[] wheels) {
        for (int i=0; i < wheels.length; i++) {
            wheels[i] = wheels[i]%2 != 0 ? 0 : (wheels[i]/4 + 1);
        }
        return wheels;
    }
}