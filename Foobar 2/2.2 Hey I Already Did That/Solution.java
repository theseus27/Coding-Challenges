import java.util.*;

public class Solution {
    public static void main(String[] args) {
        System.out.println(solution("210022", 3)); //3
        System.out.println(solution("1211", 10)); //1
    }

/*
    1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
    2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
    3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
    4) Assign n = z to get the next minion ID, and go back to step 2
*/
    public static int solution(String n, int b) {
        List<Integer> id = new ArrayList<Integer>();
        for (int i = 0; i < n.length(); i++) {
            id.add(Integer.parseInt(n, i, i+1, 10));
        }

        System.out.println(id);

        return 1;
    }
}
