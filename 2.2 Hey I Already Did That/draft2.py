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

def algo(n, b):
    x, y = sortList(n)
    x = int(str(x), b)
    y = int(str(y), b)
    z = x - y
    z = tenToB(z, b)
    z = str(z).zfill(len(str(n)))
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

sol1 = solution(210022, 3)
print(sol1)

sol2 = solution(1211, 10)
print(sol2)