def bToTen(x, b):
    print(x, b)
    x = str(x).lstrip('0')
    sum = 0
    xArray = []
    xArray[:0] = str(x)
    length = len(x) - 1
    
    for index, value in enumerate(xArray):
        power = pow(b, (length-index))
        add = int(value) * int(power)
        sum += add
    return sum

#answer = bToTen(10201, 3)
#print(answer)

def tenToB(x, b):
    if (b == 10):
        return x
    inBase = ""
    greatestPower = 0
    while (x > b**greatestPower):
        greatestPower += 1
    for i in range(greatestPower-1, -1, -1):
        print(i)
        inBase = str(inBase) + str(x//(b**i))
        x = x % (b**i)
    return inBase

answer = tenToB(100, 3)
print(answer)
