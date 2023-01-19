"""
    1) Start with a random minion ID n, which is a nonnegative integer of length k in base b
    2) Define x and y as integers of length k.  x has the digits of n in descending order, and y has the digits of n in ascending order
    3) Define z = x - y.  Add leading zeros to z to maintain length k if necessary
    4) Assign n = z to get the next minion ID, and go back to step 2
"""

def decToBase(x, b, power):
    result = ""
    
    for i in range(power, -1, -1):
        quotient = x // b**i
        result += str(quotient)
        x -= quotient * b**i
    return result

def nextID(n, b):
    id = [str(n[i]) for i in range(len(n))]
    x = ("".join(sorted(id, reverse=True)))
    y = ("".join(sorted(id)))
    z = int(x, b) - int(y, b)
    z = decToBase(z, b, len(n)-1).rjust(len(n), '0')
    return z

def solution(n, b):
    cycle = False
    ids = []
    z = n
    cycleStart = 0
    cycleLength = 1

    while not cycle:
        z = nextID(n, b)
        if z in ids:
            if cycleStart == 0:
                cycleStart = z
                cycleLength = 1
            else:
                if z == cycleStart:
                    return cycleLength
                cycleLength += 1
        ids.append(z)
        n = z

print(solution("210022", 3)) #3
print(solution("1211", 10)) #1