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
    

#Drafts    
"""
        locked = [False for _ in range(len(s))]
        for i in range(len(s)):
            if int(s[i]) == 0:
                if i > 0 and i < len(s):
                    if locked[i-1] == 1 or locked[i-1] == 2:
                        locked[i] = True
                        locked[i-1] = True
                    else:
                        return 0
                else:
                    return 0

        ways = 1
        for i in range(len(s)-1):
            if not locked[i] and not locked[i+1]:
                curr = int(s[i])
                nxt = int(s[i+1])
                if curr == 1: 
                    print(str(i) + ": break 1")
                    ways += 1
                elif curr == 2:
                    if nxt <= 6: 
                        print(str(i) + ": break 2")
                        ways += 1
                        
        
        return ways
"""