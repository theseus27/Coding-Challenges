def checkString(substring, string):
    occurences = 0
    used = []
    for i in range(0, len(string)-len(substring)+1):
        if ((i not in used) and (string[i:i+len(substring)] == substring)):
            occurences += 1
            used.extend(range(i, i+len(substring)))
    return occurences

def solution(s):
    maxOccurences = 0
    minLeftover = len(s)
    for subLen in range(1, len(s)+1):
        for start in range(0, len(s)-subLen+1):
            substring = s[start:start + subLen]
            occurences = checkString(substring, s)
            leftover = len(s)-occurences*subLen
            if (leftover < minLeftover):
                maxOccurences = occurences
                minLeftover = leftover
            elif (leftover == minLeftover):
                if (occurences > maxOccurences):
                    maxOccurences = occurences
    return maxOccurences
