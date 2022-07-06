def sortList(n):
    x = []
    y = []
    x[:0] = str(n)
    y[:0] = str(n)
    x.sort(reverse=True)
    y.sort()
    x = "".join(x)
    y = "".join(y)
    return x, y

def tenToB(x, b):
    if (b == 10):
        return x
    inBase = ""
    greatestPower = 0
    while (x > b**greatestPower):
        greatestPower += 1
    for i in range(greatestPower-1, -1, -1):
        inBase = str(inBase) + str(x//(b**i))
        x = x % (b**i)
    return inBase

def bToTen(x, b):
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

def algo(n, b):
    x, y = sortList(n)
    x = bToTen(x, b)
    y = bToTen(y, b)
    z = x - y
    z = tenToB(z, b)
    z = z.zfill(len(str(n)))
    return z

def solution(n, b):
    inputs = [n]
    repeatedInputs = []
    output = algo(n, b)
    while not(output in inputs):
        inputs.append(output)
        output = algo(output, b)
        
    repeatedInputs.append(output)
    nextOutput = algo(output, b)
    
    while (nextOutput != output):
        repeatedInputs.append(nextOutput)
        nextOutput = algo(nextOutput, b)
    
    return len(repeatedInputs)

sol = solution(210022, 3)
print(sol)

#sol = solution(100, 3)
#sol = solution(10201, 3)
  
#print("N: " + str(bToTen(n, b)) + " / " + str(n))
#print("X: " + str(bToTen(x, b)) + " / " + str(x))
#print("Y: " + str(bToTen(y, b)) + " / " + str(y))
#print("Z: " + str(bToTen(z, b)) + " / " + str(z) + "\n")
