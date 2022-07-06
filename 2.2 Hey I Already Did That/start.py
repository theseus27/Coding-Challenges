#n = ID
#b = base
#k = ID length
#x = ID in descending order
#y = ID in ascending order
#z = x - y
# to get next ID, n = z

# Any given digit in n must be between (0, b-1)
# Bases range from (2, 10)
# Lengths range from (2, 9)
# Looking for something such that the numbers in n are the same as the numbers 
#   in z

"""
Depending on the values of n, k(derived from n), and b, at some point the algorithm reaches a cycle, such as by reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of values[210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no matter how many times it iterates.
"""

def descend(n, b):
    originalString = str(n)
    newString = ""
    
    for targetNum in range(0, b-1):
        for strNum in originalString:
            if (int(strNum) == targetNum):
                newString = str(newString) + str(targetNum)
    
    if (len(originalString) != len(newString)):
        exit("Descend: failed to copy")
        
    return str(newString)
    
    

def solution(n, b):
    x = descend(n, b)
    y = ascend(n, b)
    
    return x

sol = solution(351, 10)
print("Solution: " + str(sol))

"""
>> from array import array
>> a = ['a', 'b', 'c', 'd']
>> array('B', map(ord, a)).tostring()
'abcd'

def convertFrom10(x, b):
    if (b == 10):
        return x
    
    baseX = ""
    exp = 0
    while x > 0:
        remainder = x % b
        baseX += str(remainder)
        x -= remainder * b**exp
        exp += 1
    return int(baseX)
"""

Convert from base 10 to base 3
100
100 - 81*1 - 27*0 - 9*2 - 3*0 - 1*1
10201

append(n//b**exp)
n = b**exp%n 

def tenToB(x, b):
    print("Running tenToB with " + str(x) + ", " + str(b))
    if (b == 10):
        return x
    baseX = ""
    
    greatestPower = 0
    while (x > b**greatestPower):
        greatestPower += 1
    
    for i in range(greatestPower, 0, -1):
        baseX = str(baseX) + str(x//(b**i))
        x = x%(b**i)
        print("BaseX: " + str(baseX))
        print("x: " + str(x))
    return baseX

def bToTen(x, b):
    sum = 0
    length = len(x)-1
    for index, value in enumerate(x):
        sum = int(sum) +  int(value * (b**(length-index)))
    return sum