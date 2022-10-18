import java.util.*;

public class CodeSignalPractice {
}

class Palindrome {
    String solution(String s) {
        boolean hasPalindrome = true;
        
        while (hasPalindrome) {
            System.out.println(s);
            hasPalindrome = false;
            for(int i = s.length()-1; i > 0; i--) {
                //Check for palindrome
                if (isPalindrome(s, i)) {
                    hasPalindrome = true;
                    s = s.substring(i+1);
                    i = -1;
                }
            }
        }  
        return s;
    }
    
    boolean isPalindrome(String s, int end) {
        for (int i = 0; i < end/2+1; i++) {
            if (s.charAt(i) != s.charAt(end-i)) {
                return false;
            }
        }
        return true;
    }
}

class ZigZag {
    int[] solution(int[] numbers) {
        int[] result = new int[numbers.length -2];
        for (int i = 0; i < numbers.length-2; i++) {
            if ((numbers[i] < numbers[i+1] && numbers[i+1] > numbers[i+2]) || (numbers[i] > numbers[i+1] && numbers[i+1] < numbers[i+2])) {
                result[i] = 1;
            }
            else {
                result[i] = 0; 
            }
        }
        return result;
    }
}

class Words {
    String solution(String[] arr) {
        List<Integer> lengths = new ArrayList<Integer>();
        for (String s : arr) {
            lengths.add(s.length());
        }
        int longest = Collections.max(lengths);
    
        String answer = "";
        for (int i = 0; i < longest; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (i < arr[j].length()) {
                    answer += Character.toString(arr[j].charAt(i));
                }
            }
        }
        return answer;
    }
}

//Errored out on 2/11 tests...not sure why
class SumPairs {
    long solution(int[] a, int k) {   
        long answer = 0;
        int[] offset = new int[k];
        for (int w = 0; w < k; w++) { offset[w] = 0; }
        
        //Set list of offsets
        for (int y = 0; y < a.length-1; y++) {
            offset[(a[a.length-1] + a[y]) % k] += 1;
        }
        
        answer += offset[0];
        
        for (int i = a.length-2; i >= 0; i--) {
            int diff = (((a[a.length-1] % k) - (a[i] % k)) + k) % k;
            offset[(a[a.length-1] + (a[i])) % k] -= 1;
            answer += offset[diff];
        }
        
        return answer;
    }    
}
