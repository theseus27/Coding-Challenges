#Recursively
def recurse(n):
    if n == 0: return 1
    if n == 1: return 1
    else:   return recurse(n-1) + recurse(n-2)

class Solution(object):     
    def climbStairs(self, n):
        return recurse(n)

testcase = Solution()
print(testcase.climbStairs(10))

#Dynamic Programming
def climbStairs(n):
    if n == 0: return 0
    if n == 1: return 1

    twoback: int = 1
    oneback: int = 1
    total: int = 0
    
    for _ in range(2, n+1):
        total = twoback + oneback
        twoback, oneback = oneback, total
    return total

print(climbStairs(10))