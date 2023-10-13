# EASY
# Runtime: 38 ms (Beat 53.8%)
# Memory: 14.2 MB (Beat 94.9%)

""" QUESTION
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

def isHappy(self, n: int) -> bool:
    nums = []

    if (n < 0):
        return False

    while (n != 1):
        new_n = 0
        for i in range(len(str(n))):
            new_n += int(str(n)[i])**2
        n = new_n
        if n in nums:
            return False
        nums.append(n)
    
    return True