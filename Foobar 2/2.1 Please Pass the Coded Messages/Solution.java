/*
Input: L, a list of 0 to 9 digits in range 0-9
Goal: Find largest number that can be made from digits that is divisible by 3. If none exist, return 0.
Output: Integer, largest found number divisible by 3

Test Case: 3141 -> 4311

I think numbers that are divisible by 3 add up to something divisible by 3
So first, find the combo of numbers where the sum is div by 3, and that has the greatest sum?
    First, find the LONGEST
    Then, find the one with the biggest sum
Then, order those numbers biggest to smallest and return it
*/

import java.util.*;
public class Solution {
    public static int solution(int[] l) {
        // List<Integer> nums = new ArrayList<Integer>();
        // for (int i : l) {
        //     nums.add(i);
        // }

        int answer = 0;
        int sum = 0;
        for (int i : l) { sum += i; }

        if (sum % 3 == 0) {
            System.out.println("Total sum div by 3");
        }

        //Loop for each length
        for (int i = l.length; i > 0; i--) {
            System.out.println(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] nums = {3, 1, 4, 1};
        System.out.println(solution(nums));
    }
}