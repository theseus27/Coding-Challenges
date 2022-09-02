class Solution:
    def numDecodings(self, s: str) -> int:
        ways = [0 for _ in range(len(s)+1)]
        ways[0] = 1
        
        #Base Case
        ways[1] = 0 if int(s[0]) == 0 else 1
        
        #Recursive Case
        for i in range(1, len(s)):
            if int(s[i]) != 0: ways[i+1] += ways[i]
            if int(s[i-1] + s[i]) in range(10, 27):
                ways[i+1] += ways[i-1]
            
        return ways[-1]